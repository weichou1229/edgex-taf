import os

# Service for testing
SERVICE_NAME = "device-virtual"

SECURITY_SERVICE_NEEDED = os.getenv("SECURITY_SERVICE_NEEDED")
if SECURITY_SERVICE_NEEDED == 'true':
    SERVICE_PORT = "8443/devicevirtual"
else:
    SERVICE_PORT = 49990

SUPPORTED_DATA_TYPES = [
    #     Boolean
    {"dataType": "BOOL", "commandName": "GenerateDeviceValue_Boolean_RW", "readingName": "DeviceValue_Boolean_RW", "readWrite": "RW"},
    {"dataType": "BOOL", "commandName": "GenerateDeviceValue_Boolean_R", "readingName": "DeviceValue_Boolean_R", "readWrite": "R"},
    {"dataType": "BOOL", "commandName": "GenerateDeviceValue_Boolean_W", "readingName": "DeviceValue_Boolean_W", "readWrite": "W"},
    #     String
    {"dataType": "STRING", "commandName": "GenerateDeviceValue_String_RW", "readingName": "DeviceValue_String_RW", "readWrite": "RW"},
    {"dataType": "STRING", "commandName": "GenerateDeviceValue_String_R", "readingName": "DeviceValue_String_R", "readWrite": "R"},
    {"dataType": "STRING", "commandName": "GenerateDeviceValue_String_W", "readingName": "DeviceValue_String_W", "readWrite": "W"},
    #     Float
    {"dataType": "FLOAT32", "commandName": "GenerateDeviceValue_FLOAT32_RW", "readingName": "DeviceValue_FLOAT32_RW", "readWrite": "RW"},
    {"dataType": "FLOAT32", "commandName": "GenerateDeviceValue_FLOAT32_R", "readingName": "DeviceValue_FLOAT32_R", "readWrite": "R"},
    {"dataType": "FLOAT32", "commandName": "GenerateDeviceValue_FLOAT32_W", "readingName": "DeviceValue_FLOAT32_W", "readWrite": "W"},
    {"dataType": "FLOAT64", "commandName": "GenerateDeviceValue_FLOAT64_RW", "readingName": "DeviceValue_FLOAT64_RW", "readWrite": "RW"},
    {"dataType": "FLOAT64", "commandName": "GenerateDeviceValue_FLOAT64_R", "readingName": "DeviceValue_FLOAT64_R", "readWrite": "R"},
    {"dataType": "FLOAT64", "commandName": "GenerateDeviceValue_FLOAT64_W", "readingName": "DeviceValue_FLOAT64_W", "readWrite": "W"},
    #     Integer
    {"dataType": "INT8", "commandName": "GenerateDeviceValue_INT8_RW", "readingName": "DeviceValue_INT8_RW", "readWrite": "RW"},
    {"dataType": "INT8", "commandName": "GenerateDeviceValue_INT8_R", "readingName": "DeviceValue_INT8_R", "readWrite": "R"},
    {"dataType": "INT8", "commandName": "GenerateDeviceValue_INT8_W", "readingName": "DeviceValue_INT8_W", "readWrite": "W"},
    {"dataType": "INT16", "commandName": "GenerateDeviceValue_INT16_RW", "readingName": "DeviceValue_INT16_RW", "readWrite": "RW"},
    {"dataType": "INT16", "commandName": "GenerateDeviceValue_INT16_R", "readingName": "DeviceValue_INT16_R", "readWrite": "R"},
    {"dataType": "INT16", "commandName": "GenerateDeviceValue_INT16_W", "readingName": "DeviceValue_INT16_W", "readWrite": "W"},
    {"dataType": "INT32", "commandName": "GenerateDeviceValue_INT32_RW", "readingName": "DeviceValue_INT32_RW", "readWrite": "RW"},
    {"dataType": "INT32", "commandName": "GenerateDeviceValue_INT32_R", "readingName": "DeviceValue_INT32_R", "readWrite": "R"},
    {"dataType": "INT32", "commandName": "GenerateDeviceValue_INT32_W", "readingName": "DeviceValue_INT32_W", "readWrite": "W"},
    {"dataType": "INT64", "commandName": "GenerateDeviceValue_INT64_RW", "readingName": "DeviceValue_INT64_RW", "readWrite": "RW"},
    {"dataType": "INT64", "commandName": "GenerateDeviceValue_INT64_R", "readingName": "DeviceValue_INT64_R", "readWrite": "R"},
    {"dataType": "INT64", "commandName": "GenerateDeviceValue_INT64_W", "readingName": "DeviceValue_INT64_W", "readWrite": "W"},
    #     Unsigned Integer
    {"dataType": "UINT8", "commandName": "GenerateDeviceValue_UINT8_RW", "readingName": "DeviceValue_UINT8_RW", "readWrite": "RW"},
    {"dataType": "UINT8", "commandName": "GenerateDeviceValue_UINT8_R", "readingName": "DeviceValue_UINT8_R", "readWrite": "R"},
    {"dataType": "UINT8", "commandName": "GenerateDeviceValue_UINT8_W", "readingName": "DeviceValue_UINT8_W", "readWrite": "W"},
    {"dataType": "UINT16", "commandName": "GenerateDeviceValue_UINT16_RW", "readingName": "DeviceValue_UINT16_RW", "readWrite": "RW"},
    {"dataType": "UINT16", "commandName": "GenerateDeviceValue_UINT16_R", "readingName": "DeviceValue_UINT16_R", "readWrite": "R"},
    {"dataType": "UINT16", "commandName": "GenerateDeviceValue_UINT16_W", "readingName": "DeviceValue_UINT16_W", "readWrite": "W"},
    {"dataType": "UINT32", "commandName": "GenerateDeviceValue_UINT32_RW", "readingName": "DeviceValue_UINT32_RW", "readWrite": "RW"},
    {"dataType": "UINT32", "commandName": "GenerateDeviceValue_UINT32_R", "readingName": "DeviceValue_UINT32_R", "readWrite": "R"},
    {"dataType": "UINT32", "commandName": "GenerateDeviceValue_UINT32_W", "readingName": "DeviceValue_UINT32_W", "readWrite": "W"},
    {"dataType": "UINT64", "commandName": "GenerateDeviceValue_UINT64_RW", "readingName": "DeviceValue_UINT64_RW", "readWrite": "RW"},
    {"dataType": "UINT64", "commandName": "GenerateDeviceValue_UINT64_R", "readingName": "DeviceValue_UINT64_R", "readWrite": "R"},
    {"dataType": "UINT64", "commandName": "GenerateDeviceValue_UINT64_W", "readingName": "DeviceValue_UINT64_W", "readWrite": "W"},
]
