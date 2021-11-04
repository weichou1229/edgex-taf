*** Settings ***
Documentation  Configrations
Resource     TAF/testCaseModules/keywords/common/commonKeywords.robot
Resource  TAF/testCaseModules/keywords/device-sdk/deviceServiceAPI.robot
Suite Setup  Run Keywords  Setup Suite
...                        AND  Run Keyword if  $SECURITY_SERVICE_NEEDED == 'true'  Get Token
...                        AND  Run Keyword And Ignore Error  Stop Services  scalability-test-mqtt-export  app-service-mqtt-export  # No data received from the both services
Suite Teardown  Run Keywords  Run Teardown Keywords
...             AND  Terminate All Processes  kill=True
Force Tags   MessageQueue=MQTT

*** Variables ***
${SUITE}              Core-Data-Configrations
${DATA_CONSOL_PATH}   /v1/kv/edgex/core/${CONSUL_CONFIG_VERSION}/core-data

*** Test Cases ***
CoreConfig001 - Set core-data MessageQueue.SubscribeEnabled to false
    Start process  python ${WORK_DIR}/TAF/utils/src/setup/mqtt-subscriber.py edgex/events/device/# CorrelationID arg &   # Process for MQTT Subscriber
    ...                shell=True  stdout=${WORK_DIR}/TAF/testArtifacts/logs/mqtt-subscriber.log
    Given Set Test Variable  ${device_name}  messageQueue-mqtt-core-1
    And Set MessageQueue SubscribeEnabled=false For core-data On Consul
    And Create Device For device-virtual With Name ${device_name}
    When Get device data by device ${device_name} and command ${PREFIX}_GenerateDeviceValue_UINT8_RW with ds-pushevent=yes
    Then Should Return Status Code "200" And event
    And Event Has Been Recevied By MQTT Subscriber
    And Event Is Not Pushed To Core Data
    [Teardown]  Run keywords  Delete device by name ${device_name}
                ...           AND  Delete all events by age
                ...           AND  Set MessageQueue SubscribeEnabled=true For core-data On Consul 

CoreConfig002 - Set core-data MessageQueue.SubscribeTopic not match device-virtual PublishTopicPrefix
    Given Start process  python ${WORK_DIR}/TAF/utils/src/setup/mqtt-subscriber.py edgex/events/device/# CorrelationID arg &   # Process for MQTT Subscriber
    ...                shell=True  stdout=${WORK_DIR}/TAF/testArtifacts/logs/mqtt-subscriber.log
    And Set Test Variable  ${device_name}  messagebus-mqtt-core-2
    And Set MessageQueue SubscribeTopic=edgex/events/custom/# For core-data On Consul
    And Create Device For device-virtual With Name ${device_name}
    When Get device data by device ${device_name} and command ${PREFIX}_GenerateDeviceValue_UINT8_RW with ds-pushevent=yes
    Then Should Return Status Code "200" And event
    And Event Has Been Recevied By MQTT Subscriber
    And Event Is Not Pushed To Core Data
    [Teardown]  Run keywords  Delete device by name ${device_name}
                ...           AND  Delete all events by age
                ...           AND  Set MessageQueue SubscribeTopic=edgex/events/device/# For core-data On Consul

CoreConfig003 - Customize core-data MessageQueue.PublishTopicPrefix
    Given Start process  python ${WORK_DIR}/TAF/utils/src/setup/mqtt-subscriber.py eedgex/events/custom/# CorrelationID arg &   # Process for MQTT Subscriber
    ...                shell=True  stdout=${WORK_DIR}/TAF/testArtifacts/logs/mqtt-subscriber.log  
    And Set Test Variable  ${device_name}  messagebus-mqtt-core-3
    And Set MessageQueue PublishTopicPrefix=edgex/events/custom For core-data On Consul
    And Update Service Configuration On Consul  ${DATA_CONSOL_PATH}/Writable/LogLevel  DEBUG
    And Create Device For device-virtual With Name ${device_name}
    When Create An Event With ${device_name} and command ${PREFIX}_GenerateDeviceValue_UINT8_RW
    Then Should Return Status Code "201" And id
    And Event Has Been Recevied By MQTT Subscriber
    [Teardown]  Run keywords  Delete device by name ${device_name}
                ...           AND  Delete all events by age
                ...           AND  Set MessageQueue PublishTopicPrefix=edgex/events/core For core-data On Consul                     

*** Keywords ***
Set MessageQueue ${key}=${value} For core-data On Consul
    ${path}=  Set Variable  ${DATA_CONSOL_PATH}/MessageQueue/${key}
    Update Service Configuration On Consul  ${path}  ${value}
    Sleep  500ms
    Restart Services  data
    ${timestamp}  get current epoch time
    Set Test Variable  ${log_timestamp}  ${timestamp}

Event Has Been Recevied By MQTT Subscriber
    ${logs}  Get Service Logs Since Timestamp  core-data  ${log_timestamp}
    Log  ${logs}
    ${correlation_line}  Get Lines Containing String  ${logs}.encode()  Event * on message queue
    ${correlation_id}  Fetch From Right  ${correlation_line}  Correlation-id:
    ${correlation_id}  Fetch From Left  ${correlation_id.strip()}  "
    ${received_event}  Get file  ${WORK_DIR}/TAF/testArtifacts/logs/mqtt-subscriber.log
    Should Contain  ${received_event}  ${correlation_id}  Event is not received by mqtt subscriber

Create An Event With ${device_name} and command ${command_name}
    Generate Event Sample  Event  ${device_name}  ${PREFIX}-Sample-Profile  ${PREFIX}_GenerateDeviceValue_UINT8_RW  Simple Reading  
    Create Event With ${device_name} And ${PREFIX}-Sample-Profile And ${PREFIX}_GenerateDeviceValue_UINT8_RW
