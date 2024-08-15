from enum import Enum

# Function Code Definitions
class FunctionCode(Enum):
    READ_COILS = 0x01
    READ_DISCRETE_INPUTS = 0x02
    READ_HOLDING_REGISTERS = 0x03
    READ_INPUT_REGISTERS = 0x04
    WRITE_SINGLE_COIL = 0x05
    WRITE_SINGLE_REGISTER = 0x06
    READ_EXCEPTION_STATUS = 0x07
    DIAGNOSTICS = 0x08
    GET_COMM_EVENT_COUNTER = 0x0B
    GET_COMM_EVENT_LOG = 0x0C
    WRITE_MULTIPLE_COILS = 0x0F
    WRITE_MULTIPLE_REGISTERS = 0x10
    REPORT_SLAVE_ID = 0x11
    READ_FILE_RECORD = 0x14
    WRITE_FILE_RECORD = 0x15
    MASK_WRITE_REGISTER = 0x16
    READ_WRITE_MULTIPLE_REGISTERS = 0x17
    READ_FIFO_QUEUE = 0x18
    ENCAPSULATED_INTERFACE_TRANSPORT = 0x2B
    CAN_OPEN_GENERAL_REFERENCE = 0x2B
    READ_DEVICE_IDENTIFICATION = 0x2B