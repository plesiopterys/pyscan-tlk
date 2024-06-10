from ctypes import (
    POINTER,
    c_bool,
    c_byte,
    c_char,
    c_double,
    c_int,
    c_int16,
    c_int32,
    c_int64,
    c_long,
    c_short,
    c_uint,
    c_ulong,
    c_void_p,
    cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity,
    KMOT_WheelDirectionSense,
    KMOT_WheelMode,
    MOT_JogModes,
    MOT_LimitsSoftwareApproachPolicy,
    MOT_MovementDirections,
    MOT_MovementModes,
    MOT_StopModes,
    MOT_TravelDirection,
    MOT_TravelModes)
from .definitions.structures import (
    KMOT_MMIParams,
    KMOT_TriggerConfig,
    KMOT_TriggerParams,
    MOT_BrushlessCurrentLoopParameters,
    MOT_BrushlessElectricOutputParameters,
    MOT_BrushlessPositionLoopParameters,
    MOT_BrushlessTrackSettleParameters,
    MOT_HomingParameters,
    MOT_JogParameters,
    MOT_StageAxisParameters,
    MOT_VelocityParameters,
    MOT_VelocityProfileParameters,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from .definitions.kinesisexception import KinesisException


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.KCube.BrushlessMotor.dll")

BMC_CanDeviceLockFrontPanel = lib.BMC_CanDeviceLockFrontPanel
BMC_CanDeviceLockFrontPanel.restype = c_bool
BMC_CanDeviceLockFrontPanel.argtypes = [POINTER(c_char)]


def can_device_lock_front_panel(serial_number):
    # Determine if the device front panel can be locked.

    serial_number = POINTER(c_char)

    output = BMC_CanDeviceLockFrontPanel(serial_number)

    return output


BMC_CanHome = lib.BMC_CanHome
BMC_CanHome.restype = c_bool
BMC_CanHome.argtypes = [POINTER(c_char), c_short]


def can_home(serial_number, channel):
    # Can the device perform a Home.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_CanHome(serial_number, channel)

    return output


BMC_CanMoveWithoutHomingFirst = lib.BMC_CanMoveWithoutHomingFirst
BMC_CanMoveWithoutHomingFirst.restype = c_bool
BMC_CanMoveWithoutHomingFirst.argtypes = [POINTER(c_char), c_short]


def can_move_without_homing_first(serial_number, channel):
    # Can this device be moved without Homing.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_CanMoveWithoutHomingFirst(serial_number, channel)

    return output


BMC_CheckConnection = lib.BMC_CheckConnection
BMC_CheckConnection.restype = c_bool
BMC_CheckConnection.argtypes = [POINTER(c_char)]


def check_connection(serial_number):
    # Check connection.

    serial_number = POINTER(c_char)

    output = BMC_CheckConnection(serial_number)

    return output


BMC_ClearMessageQueue = lib.BMC_ClearMessageQueue
BMC_ClearMessageQueue.restype = c_short
BMC_ClearMessageQueue.argtypes = [POINTER(c_char), c_short]


def clear_message_queue(serial_number, channel):
    # Clears the device message queue.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_ClearMessageQueue(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_Close = lib.BMC_Close
BMC_Close.restype = c_short
BMC_Close.argtypes = [POINTER(c_char)]


def close_device(serial_number):
    # Disconnect and close the device.

    serial_number = POINTER(c_char)

    output = BMC_Close(serial_number)
    if output != 0:
        raise KinesisException(output)


BMC_DisableChannel = lib.BMC_DisableChannel
BMC_DisableChannel.restype = c_short
BMC_DisableChannel.argtypes = [POINTER(c_char), c_short]


def disable_channel(serial_number, channel):
    # Disable the channel so that motor can be moved by hand.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_DisableChannel(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_EnableChannel = lib.BMC_EnableChannel
BMC_EnableChannel.restype = c_short
BMC_EnableChannel.argtypes = [POINTER(c_char), c_short]


def enable_channel(serial_number, channel):
    # Enable channel for computer control.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_EnableChannel(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_EnableLastMsgTimer = lib.BMC_EnableLastMsgTimer
BMC_EnableLastMsgTimer.restype = c_void_p
BMC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_short, c_bool, c_int32]


def enable_last_msg_timer(serial_number, channel):
    # Enables the last message monitoring timer.

    serial_number = POINTER(c_char)
    channel = c_short()
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = BMC_EnableLastMsgTimer(serial_number, channel, enable, lastMsgTimeout)
    if output != 0:
        raise KinesisException(output)


BMC_GetBacklash = lib.BMC_GetBacklash
BMC_GetBacklash.restype = c_long
BMC_GetBacklash.argtypes = [POINTER(c_char), c_short]


def get_backlash(serial_number, channel):
    # Get the backlash distance setting (used to control hysteresis).

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_GetBacklash(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_GetCurrentLoopParams = lib.BMC_GetCurrentLoopParams
BMC_GetCurrentLoopParams.restype = c_short
BMC_GetCurrentLoopParams.argtypes = [POINTER(c_char), c_short, MOT_BrushlessCurrentLoopParameters]


def get_current_loop_params(serial_number, channel):
    # Gets the current loop parameters for moving to required position.

    serial_number = POINTER(c_char)
    channel = c_short()
    currentLoopParams = MOT_BrushlessCurrentLoopParameters()

    output = BMC_GetCurrentLoopParams(serial_number, channel, currentLoopParams)
    if output != 0:
        raise KinesisException(output)


BMC_GetDeviceUnitFromRealValue = lib.BMC_GetDeviceUnitFromRealValue
BMC_GetDeviceUnitFromRealValue.restype = c_short
BMC_GetDeviceUnitFromRealValue.argtypes = [POINTER(c_char), c_short, c_double, c_int, c_int]


def get_device_unit_from_real_value(serial_number, channel):
    # Converts a device unit to a real world unit.

    serial_number = POINTER(c_char)
    channel = c_short()
    real_unit = c_double()
    device_unit = c_int()
    unitType = c_int()

    output = BMC_GetDeviceUnitFromRealValue(serial_number, channel, real_unit, device_unit, unitType)
    if output != 0:
        raise KinesisException(output)


BMC_GetDigitalOutputs = lib.BMC_GetDigitalOutputs
BMC_GetDigitalOutputs.restype = c_byte
BMC_GetDigitalOutputs.argtypes = [POINTER(c_char), c_short]


def get_digital_outputs(serial_number, channel):
    # Gets the digital output bits.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_GetDigitalOutputs(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_GetElectricOutputParams = lib.BMC_GetElectricOutputParams
BMC_GetElectricOutputParams.restype = c_short
BMC_GetElectricOutputParams.argtypes = [POINTER(c_char), c_short, MOT_BrushlessElectricOutputParameters]


def get_electric_output_params(serial_number, channel):
    # Gets the electric output parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    electricOutputParams = MOT_BrushlessElectricOutputParameters()

    output = BMC_GetElectricOutputParams(serial_number, channel, electricOutputParams)
    if output != 0:
        raise KinesisException(output)


BMC_GetEncoderCounter = lib.BMC_GetEncoderCounter
BMC_GetEncoderCounter.restype = c_long
BMC_GetEncoderCounter.argtypes = [POINTER(c_char), c_short]


def get_encoder_counter(serial_number, channel):
    # Get the Encoder Counter.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_GetEncoderCounter(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_GetFirmwareVersion = lib.BMC_GetFirmwareVersion
BMC_GetFirmwareVersion.restype = c_ulong
BMC_GetFirmwareVersion.argtypes = [POINTER(c_char), c_short]


def get_firmware_version(serial_number, channel):
    # Gets version number of the device firmware.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_GetFirmwareVersion(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_GetFrontPanelLocked = lib.BMC_GetFrontPanelLocked
BMC_GetFrontPanelLocked.restype = c_bool
BMC_GetFrontPanelLocked.argtypes = [POINTER(c_char)]


def get_front_panel_locked(serial_number):
    # Query if the device front panel locked.

    serial_number = POINTER(c_char)

    output = BMC_GetFrontPanelLocked(serial_number)

    return output


BMC_GetHardwareInfo = lib.BMC_GetHardwareInfo
BMC_GetHardwareInfo.restype = c_short
BMC_GetHardwareInfo.argtypes = [
    POINTER(c_char),
    c_short,
    POINTER(c_char),
    c_ulong,
    c_long,
    c_short,
    POINTER(c_char),
    c_ulong,
    c_ulong,
    c_long,
    c_long]


def get_hardware_info(serial_number, channel):
    # Gets the hardware information from the device.

    serial_number = POINTER(c_char)
    channel = c_short()
    modelNo = POINTER(c_char)
    sizeOfModelNo = c_ulong()
    type = c_long()
    numChannels = c_short()
    notes = POINTER(c_char)
    sizeOfNotes = c_ulong()
    firmwareVersion = c_ulong()
    hardwareVersion = c_long()
    modificationState = c_long()

    output = BMC_GetHardwareInfo(
        serial_number,
        channel,
        modelNo,
        sizeOfModelNo,
        type,
        numChannels,
        notes,
        sizeOfNotes,
        firmwareVersion,
        hardwareVersion,
        modificationState)
    if output != 0:
        raise KinesisException(output)


BMC_GetHardwareInfoBlock = lib.BMC_GetHardwareInfoBlock
BMC_GetHardwareInfoBlock.restype = c_short
BMC_GetHardwareInfoBlock.argtypes = [POINTER(c_char), c_short, TLI_HardwareInformation]


def get_hardware_info_block(serial_number, channel):
    # Gets the hardware information in a block.

    serial_number = POINTER(c_char)
    channel = c_short()
    hardwareInfo = TLI_HardwareInformation()

    output = BMC_GetHardwareInfoBlock(serial_number, channel, hardwareInfo)
    if output != 0:
        raise KinesisException(output)


BMC_GetHomingParamsBlock = lib.BMC_GetHomingParamsBlock
BMC_GetHomingParamsBlock.restype = c_short
BMC_GetHomingParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_HomingParameters]


def get_homing_params_block(serial_number, channel):
    # Get the homing parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    homingParams = MOT_HomingParameters()

    output = BMC_GetHomingParamsBlock(serial_number, channel, homingParams)
    if output != 0:
        raise KinesisException(output)


BMC_GetHomingVelocity = lib.BMC_GetHomingVelocity
BMC_GetHomingVelocity.restype = c_uint
BMC_GetHomingVelocity.argtypes = [POINTER(c_char), c_short]


def get_homing_velocity(serial_number, channel):
    # Gets the homing velocity.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_GetHomingVelocity(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_GetJogMode = lib.BMC_GetJogMode
BMC_GetJogMode.restype = c_short
BMC_GetJogMode.argtypes = [POINTER(c_char), c_short, MOT_JogModes, MOT_StopModes]


def get_jog_mode(serial_number, channel):
    # Gets the jog mode.

    serial_number = POINTER(c_char)
    channel = c_short()
    mode = MOT_JogModes()
    stopMode = MOT_StopModes()

    output = BMC_GetJogMode(serial_number, channel, mode, stopMode)
    if output != 0:
        raise KinesisException(output)


BMC_GetJogParamsBlock = lib.BMC_GetJogParamsBlock
BMC_GetJogParamsBlock.restype = c_short
BMC_GetJogParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_JogParameters]


def get_jog_params_block(serial_number, channel):
    # Get the jog parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    jogParams = MOT_JogParameters()

    output = BMC_GetJogParamsBlock(serial_number, channel, jogParams)
    if output != 0:
        raise KinesisException(output)


BMC_GetJogStepSize = lib.BMC_GetJogStepSize
BMC_GetJogStepSize.restype = c_uint
BMC_GetJogStepSize.argtypes = [POINTER(c_char), c_short]


def get_jog_step_size(serial_number, channel):
    # Gets the distance to move when jogging.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_GetJogStepSize(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_GetJogVelParams = lib.BMC_GetJogVelParams
BMC_GetJogVelParams.restype = c_short
BMC_GetJogVelParams.argtypes = [POINTER(c_char), c_short, c_int, c_int]


def get_jog_vel_params(serial_number, channel):
    # Gets the jog velocity parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    acceleration = c_int()
    maxVelocity = c_int()

    output = BMC_GetJogVelParams(serial_number, channel, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


BMC_GetMMIParams = lib.BMC_GetMMIParams
BMC_GetMMIParams.restype = c_short
BMC_GetMMIParams.argtypes = [
    POINTER(c_char),
    KMOT_WheelMode,
    c_int32,
    c_int32,
    KMOT_WheelDirectionSense,
    c_int32,
    c_int32,
    c_int16]


def get_m_m_i_params(serial_number):
    # Get the MMI Parameters for the KCube Display Interface.

    serial_number = POINTER(c_char)
    wheelMode = KMOT_WheelMode()
    wheelMaxVelocity = c_int32()
    wheelAcceleration = c_int32()
    directionSense = KMOT_WheelDirectionSense()
    presetPosition1 = c_int32()
    presetPosition2 = c_int32()
    displayIntensity = c_int16()

    output = BMC_GetMMIParams(
        serial_number,
        wheelMode,
        wheelMaxVelocity,
        wheelAcceleration,
        directionSense,
        presetPosition1,
        presetPosition2,
        displayIntensity)
    if output != 0:
        raise KinesisException(output)


BMC_GetMMIParamsBlock = lib.BMC_GetMMIParamsBlock
BMC_GetMMIParamsBlock.restype = c_short
BMC_GetMMIParamsBlock.argtypes = [POINTER(c_char), KMOT_MMIParams]


def get_m_m_i_params_block(serial_number):
    # Gets the MMI parameters for the device.

    serial_number = POINTER(c_char)
    mmiParams = KMOT_MMIParams()

    output = BMC_GetMMIParamsBlock(serial_number, mmiParams)
    if output != 0:
        raise KinesisException(output)


BMC_GetMMIParamsExt = lib.BMC_GetMMIParamsExt
BMC_GetMMIParamsExt.restype = c_short
BMC_GetMMIParamsExt.argtypes = [
    POINTER(c_char),
    KMOT_WheelMode,
    c_int32,
    c_int32,
    KMOT_WheelDirectionSense,
    c_int32,
    c_int32,
    c_int16,
    c_int16,
    c_int16]


def get_m_m_i_params_ext(serial_number):
    # Get the MMI Parameters for the KCube Display Interface.

    serial_number = POINTER(c_char)
    wheelMode = KMOT_WheelMode()
    wheelMaxVelocity = c_int32()
    wheelAcceleration = c_int32()
    directionSense = KMOT_WheelDirectionSense()
    presetPosition1 = c_int32()
    presetPosition2 = c_int32()
    displayIntensity = c_int16()
    displayTimeout = c_int16()
    displayDimIntensity = c_int16()

    output = BMC_GetMMIParamsExt(
        serial_number,
        wheelMode,
        wheelMaxVelocity,
        wheelAcceleration,
        directionSense,
        presetPosition1,
        presetPosition2,
        displayIntensity,
        displayTimeout,
        displayDimIntensity)
    if output != 0:
        raise KinesisException(output)


BMC_GetMotorParams = lib.BMC_GetMotorParams
BMC_GetMotorParams.restype = c_short
BMC_GetMotorParams.argtypes = [POINTER(c_char), c_short, c_long]


def get_motor_params(serial_number, channel):
    # Get the motor parameters for the Brushless Votor.

    serial_number = POINTER(c_char)
    channel = c_short()
    countsPerUnit = c_long()

    output = BMC_GetMotorParams(serial_number, channel, countsPerUnit)
    if output != 0:
        raise KinesisException(output)


BMC_GetMotorParamsExt = lib.BMC_GetMotorParamsExt
BMC_GetMotorParamsExt.restype = c_short
BMC_GetMotorParamsExt.argtypes = [POINTER(c_char), c_short, c_double]


def get_motor_params_ext(serial_number, channel):
    # Get the motor parameters for the Brushless Votor.

    serial_number = POINTER(c_char)
    channel = c_short()
    countsPerUnit = c_double()

    output = BMC_GetMotorParamsExt(serial_number, channel, countsPerUnit)
    if output != 0:
        raise KinesisException(output)


BMC_GetMotorTravelLimits = lib.BMC_GetMotorTravelLimits
BMC_GetMotorTravelLimits.restype = c_short
BMC_GetMotorTravelLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]


def get_motor_travel_limits(serial_number, channel):
    # Gets the absolute minimum and maximum travel range constants for the current stage.

    serial_number = POINTER(c_char)
    channel = c_short()
    minPosition = c_double()
    maxPosition = c_double()

    output = BMC_GetMotorTravelLimits(serial_number, channel, minPosition, maxPosition)
    if output != 0:
        raise KinesisException(output)


BMC_GetMotorTravelMode = lib.BMC_GetMotorTravelMode
BMC_GetMotorTravelMode.restype = MOT_TravelModes
BMC_GetMotorTravelMode.argtypes = [POINTER(c_char), c_short]


def get_motor_travel_mode(serial_number, channel):
    # Get motor travel mode.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_GetMotorTravelMode(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_GetMotorVelocityLimits = lib.BMC_GetMotorVelocityLimits
BMC_GetMotorVelocityLimits.restype = c_short
BMC_GetMotorVelocityLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]


def get_motor_velocity_limits(serial_number, channel):
    # Gets the absolute maximum velocity and acceleration constants for the current stage.

    serial_number = POINTER(c_char)
    channel = c_short()
    maxVelocity = c_double()
    maxAcceleration = c_double()

    output = BMC_GetMotorVelocityLimits(serial_number, channel, maxVelocity, maxAcceleration)
    if output != 0:
        raise KinesisException(output)


BMC_GetMoveAbsolutePosition = lib.BMC_GetMoveAbsolutePosition
BMC_GetMoveAbsolutePosition.restype = c_int
BMC_GetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short]


def get_move_absolute_position(serial_number, channel):
    # Gets the move absolute position.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_GetMoveAbsolutePosition(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_GetMoveRelativeDistance = lib.BMC_GetMoveRelativeDistance
BMC_GetMoveRelativeDistance.restype = c_int
BMC_GetMoveRelativeDistance.argtypes = [POINTER(c_char), c_short]


def get_move_relative_distance(serial_number, channel):
    # Gets the move relative distance.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_GetMoveRelativeDistance(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_GetNextMessage = lib.BMC_GetNextMessage
BMC_GetNextMessage.restype = c_bool
BMC_GetNextMessage.argtypes = [POINTER(c_char), c_short, c_long, c_long, c_ulong]


def get_next_message(serial_number, channel):
    # Get the next MessageQueue item.

    serial_number = POINTER(c_char)
    channel = c_short()
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = BMC_GetNextMessage(serial_number, channel, messageType, messageID, messageData)

    return output


BMC_GetNumberPositions = lib.BMC_GetNumberPositions
BMC_GetNumberPositions.restype = c_int
BMC_GetNumberPositions.argtypes = [POINTER(c_char), c_short]


def get_number_positions(serial_number, channel):
    # Get number of positions.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_GetNumberPositions(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_GetPosLoopParams = lib.BMC_GetPosLoopParams
BMC_GetPosLoopParams.restype = c_short
BMC_GetPosLoopParams.argtypes = [POINTER(c_char), c_short, MOT_BrushlessPositionLoopParameters]


def get_pos_loop_params(serial_number, channel):
    # Gets the position feedback loop parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    positionLoopParams = MOT_BrushlessPositionLoopParameters()

    output = BMC_GetPosLoopParams(serial_number, channel, positionLoopParams)
    if output != 0:
        raise KinesisException(output)


BMC_GetPosition = lib.BMC_GetPosition
BMC_GetPosition.restype = c_int
BMC_GetPosition.argtypes = [POINTER(c_char), c_short]


def get_position(serial_number, channel):
    # Get the current position.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_GetPosition(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_GetPositionCounter = lib.BMC_GetPositionCounter
BMC_GetPositionCounter.restype = c_long
BMC_GetPositionCounter.argtypes = [POINTER(c_char), c_short]


def get_position_counter(serial_number, channel):
    # Get the Position Counter.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_GetPositionCounter(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_GetRealValueFromDeviceUnit = lib.BMC_GetRealValueFromDeviceUnit
BMC_GetRealValueFromDeviceUnit.restype = c_short
BMC_GetRealValueFromDeviceUnit.argtypes = [POINTER(c_char), c_short, c_int, c_double, c_int]


def get_real_value_from_device_unit(serial_number, channel):
    # Converts a device unit to a real world unit.

    serial_number = POINTER(c_char)
    channel = c_short()
    device_unit = c_int()
    real_unit = c_double()
    unitType = c_int()

    output = BMC_GetRealValueFromDeviceUnit(serial_number, channel, device_unit, real_unit, unitType)
    if output != 0:
        raise KinesisException(output)


BMC_GetSoftLimitMode = lib.BMC_GetSoftLimitMode
BMC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
BMC_GetSoftLimitMode.argtypes = [POINTER(c_char), c_short]


def get_soft_limit_mode(serial_number, channel):
    # Gets the software limits mode.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_GetSoftLimitMode(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_GetSoftwareVersion = lib.BMC_GetSoftwareVersion
BMC_GetSoftwareVersion.restype = c_ulong
BMC_GetSoftwareVersion.argtypes = [POINTER(c_char)]


def get_software_version(serial_number):
    # Gets version number of the device software.

    serial_number = POINTER(c_char)

    output = BMC_GetSoftwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


BMC_GetStageAxisMaxPos = lib.BMC_GetStageAxisMaxPos
BMC_GetStageAxisMaxPos.restype = c_int
BMC_GetStageAxisMaxPos.argtypes = [POINTER(c_char), c_short]


def get_stage_axis_max_pos(serial_number, channel):
    # Gets the Brushless Motor stage axis maximum position.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_GetStageAxisMaxPos(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_GetStageAxisMinPos = lib.BMC_GetStageAxisMinPos
BMC_GetStageAxisMinPos.restype = c_int
BMC_GetStageAxisMinPos.argtypes = [POINTER(c_char), c_short]


def get_stage_axis_min_pos(serial_number, channel):
    # Gets the Brushless Motor stage axis minimum position.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_GetStageAxisMinPos(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_GetStageAxisParams = lib.BMC_GetStageAxisParams
BMC_GetStageAxisParams.restype = c_short
BMC_GetStageAxisParams.argtypes = [
    POINTER(c_char),
    c_short,
    c_long,
    c_long,
    POINTER(c_char),
    c_ulong,
    c_ulong,
    c_ulong,
    c_int,
    c_int,
    c_int,
    c_int,
    c_int]


def get_stage_axis_params(serial_number, channel):
    # Gets the Brushless Motor stage axis parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    stageID = c_long()
    axisID = c_long()
    partNumber = POINTER(c_char)
    size = c_ulong()
    serialNumber = c_ulong()
    countsPerUnit = c_ulong()
    minPosition = c_int()
    maxPosition = c_int()
    maxAcceleration = c_int()
    maxDecceleration = c_int()
    maxVelocity = c_int()

    output = BMC_GetStageAxisParams(
        serial_number,
        channel,
        stageID,
        axisID,
        partNumber,
        size,
        serialNumber,
        countsPerUnit,
        minPosition,
        maxPosition,
        maxAcceleration,
        maxDecceleration,
        maxVelocity)
    if output != 0:
        raise KinesisException(output)


BMC_GetStageAxisParamsBlock = lib.BMC_GetStageAxisParamsBlock
BMC_GetStageAxisParamsBlock.restype = c_short
BMC_GetStageAxisParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_StageAxisParameters]


def get_stage_axis_params_block(serial_number, channel):
    # Gets the Brushless Motor stage axis parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    stageAxisParams = MOT_StageAxisParameters()

    output = BMC_GetStageAxisParamsBlock(serial_number, channel, stageAxisParams)
    if output != 0:
        raise KinesisException(output)


BMC_GetStatusBits = lib.BMC_GetStatusBits
BMC_GetStatusBits.restype = c_ulong
BMC_GetStatusBits.argtypes = [POINTER(c_char), c_short]


def get_status_bits(serial_number, channel):
    # Get the current status bits.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_GetStatusBits(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_GetTrackSettleParams = lib.BMC_GetTrackSettleParams
BMC_GetTrackSettleParams.restype = c_short
BMC_GetTrackSettleParams.argtypes = [POINTER(c_char), c_short, MOT_BrushlessTrackSettleParameters]


def get_track_settle_params(serial_number, channel):
    # Gets the track settled parameters used to decide when settled at right position.

    serial_number = POINTER(c_char)
    channel = c_short()
    settleParams = MOT_BrushlessTrackSettleParameters()

    output = BMC_GetTrackSettleParams(serial_number, channel, settleParams)
    if output != 0:
        raise KinesisException(output)


BMC_GetTriggerConfigParams = lib.BMC_GetTriggerConfigParams
BMC_GetTriggerConfigParams.restype = c_short
BMC_GetTriggerConfigParams.argtypes = [
    POINTER(c_char),
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity,
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity]


def get_trigger_config_params(serial_number):
    # Get the Trigger Configuration Parameters.

    serial_number = POINTER(c_char)
    trigger1Mode = KMOT_TriggerPortMode()
    trigger1Polarity = KMOT_TriggerPortPolarity()
    trigger2Mode = KMOT_TriggerPortMode()
    trigger2Polarity = KMOT_TriggerPortPolarity()

    output = BMC_GetTriggerConfigParams(serial_number, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity)
    if output != 0:
        raise KinesisException(output)


BMC_GetTriggerConfigParamsBlock = lib.BMC_GetTriggerConfigParamsBlock
BMC_GetTriggerConfigParamsBlock.restype = c_short
BMC_GetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerConfig]


def get_trigger_config_params_block(serial_number):
    # Gets the trigger configuration parameters block.

    serial_number = POINTER(c_char)
    triggerConfigParams = KMOT_TriggerConfig()

    output = BMC_GetTriggerConfigParamsBlock(serial_number, triggerConfigParams)
    if output != 0:
        raise KinesisException(output)


BMC_GetTriggerParamsParams = lib.BMC_GetTriggerParamsParams
BMC_GetTriggerParamsParams.restype = c_short
BMC_GetTriggerParamsParams.argtypes = [
    POINTER(c_char),
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32]


def get_trigger_params_params(serial_number):
    # Get the Trigger Parameters Parameters.

    serial_number = POINTER(c_char)
    triggerStartPositionFwd = c_int32()
    triggerIntervalFwd = c_int32()
    triggerPulseCountFwd = c_int32()
    triggerStartPositionRev = c_int32()
    triggerIntervalRev = c_int32()
    triggerPulseCountRev = c_int32()
    triggerPulseWidth = c_int32()
    cycleCount = c_int32()

    output = BMC_GetTriggerParamsParams(
        serial_number,
        triggerStartPositionFwd,
        triggerIntervalFwd,
        triggerPulseCountFwd,
        triggerStartPositionRev,
        triggerIntervalRev,
        triggerPulseCountRev,
        triggerPulseWidth,
        cycleCount)
    if output != 0:
        raise KinesisException(output)


BMC_GetTriggerParamsParamsBlock = lib.BMC_GetTriggerParamsParamsBlock
BMC_GetTriggerParamsParamsBlock.restype = c_short
BMC_GetTriggerParamsParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerParams]


def get_trigger_params_params_block(serial_number):
    # Gets the trigger parameters block.

    serial_number = POINTER(c_char)
    triggerParamsParams = KMOT_TriggerParams()

    output = BMC_GetTriggerParamsParamsBlock(serial_number, triggerParamsParams)
    if output != 0:
        raise KinesisException(output)


BMC_GetTriggerSwitches = lib.BMC_GetTriggerSwitches
BMC_GetTriggerSwitches.restype = c_byte
BMC_GetTriggerSwitches.argtypes = [POINTER(c_char), c_short]


def get_trigger_switches(serial_number, channel):
    # Gets the trigger switch bits.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_GetTriggerSwitches(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_GetVelParams = lib.BMC_GetVelParams
BMC_GetVelParams.restype = c_short
BMC_GetVelParams.argtypes = [POINTER(c_char), c_short, c_int, c_int]


def get_vel_params(serial_number, channel):
    # Gets the move velocity parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    acceleration = c_int()
    maxVelocity = c_int()

    output = BMC_GetVelParams(serial_number, channel, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


BMC_GetVelParamsBlock = lib.BMC_GetVelParamsBlock
BMC_GetVelParamsBlock.restype = c_short
BMC_GetVelParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_VelocityParameters]


def get_vel_params_block(serial_number, channel):
    # Get the move velocity parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    velocityParams = MOT_VelocityParameters()

    output = BMC_GetVelParamsBlock(serial_number, channel, velocityParams)
    if output != 0:
        raise KinesisException(output)


BMC_GetVelocityProfileParams = lib.BMC_GetVelocityProfileParams
BMC_GetVelocityProfileParams.restype = c_short
BMC_GetVelocityProfileParams.argtypes = [POINTER(c_char), c_short, MOT_VelocityProfileParameters]


def get_velocity_profile_params(serial_number, channel):
    # Gets the velocity profile parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    velocityProfileParams = MOT_VelocityProfileParameters()

    output = BMC_GetVelocityProfileParams(serial_number, channel, velocityProfileParams)
    if output != 0:
        raise KinesisException(output)


BMC_HasLastMsgTimerOverrun = lib.BMC_HasLastMsgTimerOverrun
BMC_HasLastMsgTimerOverrun.restype = c_bool
BMC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char), c_short]


def has_last_msg_timer_overrun(serial_number, channel):
    # Queries if the time since the last message has exceeded the
    # lastMsgTimeout set by BMC_EnableLastMsgTimer(char const * serialNo, bool
    # enable, __int32 lastMsgTimeout ).

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_HasLastMsgTimerOverrun(serial_number, channel)

    return output


BMC_Home = lib.BMC_Home
BMC_Home.restype = c_short
BMC_Home.argtypes = [POINTER(c_char), c_short]


def home(serial_number, channel):
    # Home the device.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_Home(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_Identify = lib.BMC_Identify
BMC_Identify.restype = c_void_p
BMC_Identify.argtypes = [POINTER(c_char)]


def identify(serial_number):
    # Sends a command to the device to make it identify iteself.

    serial_number = POINTER(c_char)

    output = BMC_Identify(serial_number)
    if output != 0:
        raise KinesisException(output)


BMC_LoadNamedSettings = lib.BMC_LoadNamedSettings
BMC_LoadNamedSettings.restype = c_bool
BMC_LoadNamedSettings.argtypes = [POINTER(c_char), c_short, POINTER(c_char)]


def load_named_settings(serial_number, channel):
    # Update device with named settings.

    serial_number = POINTER(c_char)
    channel = c_short()
    settingsName = POINTER(c_char)

    output = BMC_LoadNamedSettings(serial_number, channel, settingsName)

    return output


BMC_LoadSettings = lib.BMC_LoadSettings
BMC_LoadSettings.restype = c_bool
BMC_LoadSettings.argtypes = [POINTER(c_char), c_short]


def load_settings(serial_number, channel):
    # Update device with stored settings.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_LoadSettings(serial_number, channel)

    return output


BMC_MessageQueueSize = lib.BMC_MessageQueueSize
BMC_MessageQueueSize.restype = c_int
BMC_MessageQueueSize.argtypes = [POINTER(c_char), c_short]


def message_queue_size(serial_number, channel):
    # Gets the MessageQueue size.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_MessageQueueSize(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_MoveAbsolute = lib.BMC_MoveAbsolute
BMC_MoveAbsolute.restype = c_short
BMC_MoveAbsolute.argtypes = [POINTER(c_char), c_short]


def move_absolute(serial_number, channel):
    # Moves the device to the position defined in the SetMoveAbsolute command.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_MoveAbsolute(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_MoveAtVelocity = lib.BMC_MoveAtVelocity
BMC_MoveAtVelocity.restype = c_short
BMC_MoveAtVelocity.argtypes = [POINTER(c_char), c_short, MOT_TravelDirection]


def move_at_velocity(serial_number, channel):
    # Start moving at the current velocity in the specified direction.

    serial_number = POINTER(c_char)
    channel = c_short()
    direction = MOT_TravelDirection()

    output = BMC_MoveAtVelocity(serial_number, channel, direction)
    if output != 0:
        raise KinesisException(output)


BMC_MoveJog = lib.BMC_MoveJog
BMC_MoveJog.restype = c_short
BMC_MoveJog.argtypes = [POINTER(c_char), c_short, MOT_TravelDirection]


def move_jog(serial_number, channel):
    # Perform a jog.

    serial_number = POINTER(c_char)
    channel = c_short()
    jogDirection = MOT_TravelDirection()

    output = BMC_MoveJog(serial_number, channel, jogDirection)
    if output != 0:
        raise KinesisException(output)


BMC_MoveRelative = lib.BMC_MoveRelative
BMC_MoveRelative.restype = c_short
BMC_MoveRelative.argtypes = [POINTER(c_char), c_short, c_int]


def move_relative(serial_number, channel):
    # Move the motor by a relative amount.

    serial_number = POINTER(c_char)
    channel = c_short()
    displacement = c_int()

    output = BMC_MoveRelative(serial_number, channel, displacement)
    if output != 0:
        raise KinesisException(output)


BMC_MoveRelativeDistance = lib.BMC_MoveRelativeDistance
BMC_MoveRelativeDistance.restype = c_short
BMC_MoveRelativeDistance.argtypes = [POINTER(c_char), c_short]


def move_relative_distance(serial_number, channel):
    # Moves the device by a relative distancce defined by SetMoveRelativeDistance.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_MoveRelativeDistance(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_MoveToPosition = lib.BMC_MoveToPosition
BMC_MoveToPosition.restype = c_short
BMC_MoveToPosition.argtypes = [POINTER(c_char), c_short, c_int]


def move_to_position(serial_number, channel):
    # Move the device to the specified position (index).

    serial_number = POINTER(c_char)
    channel = c_short()
    index = c_int()

    output = BMC_MoveToPosition(serial_number, channel, index)
    if output != 0:
        raise KinesisException(output)


BMC_NeedsHoming = lib.BMC_NeedsHoming
BMC_NeedsHoming.restype = c_bool
BMC_NeedsHoming.argtypes = [POINTER(c_char), c_short]


def needs_homing(serial_number, channel):
    # Does the device need to be Homed before a move can be performed.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_NeedsHoming(serial_number, channel)

    return output


BMC_Open = lib.BMC_Open
BMC_Open.restype = c_short
BMC_Open.argtypes = [POINTER(c_char)]


def open_device(serial_number):
    # Open the device for communications.

    serial_number = POINTER(c_char)

    output = BMC_Open(serial_number)
    if output != 0:
        raise KinesisException(output)


BMC_OverrideHomeRequirement = lib.BMC_OverrideHomeRequirement
BMC_OverrideHomeRequirement.restype = c_short
BMC_OverrideHomeRequirement.argtypes = [POINTER(c_char), c_short]


def override_home_requirement(serial_number, channel):
    # Set to allow a device to be positioned without prior homing.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_OverrideHomeRequirement(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_PersistSettings = lib.BMC_PersistSettings
BMC_PersistSettings.restype = c_bool
BMC_PersistSettings.argtypes = [POINTER(c_char), c_short]


def persist_settings(serial_number, channel):
    # persist the devices current settings.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_PersistSettings(serial_number, channel)

    return output


BMC_PollingDuration = lib.BMC_PollingDuration
BMC_PollingDuration.restype = c_long
BMC_PollingDuration.argtypes = [POINTER(c_char), c_short]


def polling_duration(serial_number, channel):
    # Gets the polling loop duration.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_PollingDuration(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_RegisterMessageCallback = lib.BMC_RegisterMessageCallback
BMC_RegisterMessageCallback.restype = c_short
BMC_RegisterMessageCallback.argtypes = [POINTER(c_char), c_short, c_void_p]


def register_message_callback(serial_number, channel):
    # Registers a callback on the message queue.

    serial_number = POINTER(c_char)
    channel = c_short()
    void = c_void_p()

    output = BMC_RegisterMessageCallback(serial_number, channel, void)
    if output != 0:
        raise KinesisException(output)


BMC_RequestBacklash = lib.BMC_RequestBacklash
BMC_RequestBacklash.restype = c_short
BMC_RequestBacklash.argtypes = [POINTER(c_char), c_short]


def request_backlash(serial_number, channel):
    # Requests the backlash.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_RequestBacklash(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_RequestCurrentLoopParams = lib.BMC_RequestCurrentLoopParams
BMC_RequestCurrentLoopParams.restype = c_short
BMC_RequestCurrentLoopParams.argtypes = [POINTER(c_char), c_short]


def request_current_loop_params(serial_number, channel):
    # Requests the current loop parameters for moving to required position.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_RequestCurrentLoopParams(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_RequestDigitalOutputs = lib.BMC_RequestDigitalOutputs
BMC_RequestDigitalOutputs.restype = c_short
BMC_RequestDigitalOutputs.argtypes = [POINTER(c_char), c_short]


def request_digital_outputs(serial_number, channel):
    # Requests the digital output bits.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_RequestDigitalOutputs(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_RequestElectricOutputParams = lib.BMC_RequestElectricOutputParams
BMC_RequestElectricOutputParams.restype = c_short
BMC_RequestElectricOutputParams.argtypes = [POINTER(c_char), c_short]


def request_electric_output_params(serial_number, channel):
    # Requests the electric output parameters.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_RequestElectricOutputParams(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_RequestEncoderCounter = lib.BMC_RequestEncoderCounter
BMC_RequestEncoderCounter.restype = c_short
BMC_RequestEncoderCounter.argtypes = [POINTER(c_char), c_short]


def request_encoder_counter(serial_number, channel):
    # Requests the encoder counter.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_RequestEncoderCounter(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_RequestFrontPanelLocked = lib.BMC_RequestFrontPanelLocked
BMC_RequestFrontPanelLocked.restype = c_short
BMC_RequestFrontPanelLocked.argtypes = [POINTER(c_char)]


def request_front_panel_locked(serial_number):
    # Ask the device if its front panel is locked.

    serial_number = POINTER(c_char)

    output = BMC_RequestFrontPanelLocked(serial_number)
    if output != 0:
        raise KinesisException(output)


BMC_RequestHomingParams = lib.BMC_RequestHomingParams
BMC_RequestHomingParams.restype = c_short
BMC_RequestHomingParams.argtypes = [POINTER(c_char), c_short]


def request_homing_params(serial_number, channel):
    # Requests the homing parameters.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_RequestHomingParams(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_RequestJogParams = lib.BMC_RequestJogParams
BMC_RequestJogParams.restype = c_short
BMC_RequestJogParams.argtypes = [POINTER(c_char), c_short]


def request_jog_params(serial_number, channel):
    # Requests the jog parameters.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_RequestJogParams(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_RequestMMIparams = lib.BMC_RequestMMIparams
BMC_RequestMMIparams.restype = c_short
BMC_RequestMMIparams.argtypes = [POINTER(c_char)]


def request_m_m_iparams(serial_number):
    # Requests the MMI Parameters for the KCube Display Interface.

    serial_number = POINTER(c_char)

    output = BMC_RequestMMIparams(serial_number)
    if output != 0:
        raise KinesisException(output)


BMC_RequestMoveAbsolutePosition = lib.BMC_RequestMoveAbsolutePosition
BMC_RequestMoveAbsolutePosition.restype = c_short
BMC_RequestMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short]


def request_move_absolute_position(serial_number, channel):
    # Requests the position of next absolute move.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_RequestMoveAbsolutePosition(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_RequestMoveRelativeDistance = lib.BMC_RequestMoveRelativeDistance
BMC_RequestMoveRelativeDistance.restype = c_short
BMC_RequestMoveRelativeDistance.argtypes = [POINTER(c_char), c_short]


def request_move_relative_distance(serial_number, channel):
    # Requests the relative move distance.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_RequestMoveRelativeDistance(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_RequestPosLoopParams = lib.BMC_RequestPosLoopParams
BMC_RequestPosLoopParams.restype = c_short
BMC_RequestPosLoopParams.argtypes = [POINTER(c_char), c_short]


def request_pos_loop_params(serial_number, channel):
    # Requests the position feedback loop parameters.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_RequestPosLoopParams(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_RequestPosTriggerParams = lib.BMC_RequestPosTriggerParams
BMC_RequestPosTriggerParams.restype = c_short
BMC_RequestPosTriggerParams.argtypes = [POINTER(c_char)]


def request_pos_trigger_params(serial_number):
    # Requests the position trigger parameters.

    serial_number = POINTER(c_char)

    output = BMC_RequestPosTriggerParams(serial_number)
    if output != 0:
        raise KinesisException(output)


BMC_RequestPosition = lib.BMC_RequestPosition
BMC_RequestPosition.restype = c_short
BMC_RequestPosition.argtypes = [POINTER(c_char), c_short]


def request_position(serial_number, channel):
    # Requests the current position.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_RequestPosition(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_RequestSettings = lib.BMC_RequestSettings
BMC_RequestSettings.restype = c_short
BMC_RequestSettings.argtypes = [POINTER(c_char), c_short]


def request_settings(serial_number, channel):
    # Requests that all settings are download from device.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_RequestSettings(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_RequestStageAxisParams = lib.BMC_RequestStageAxisParams
BMC_RequestStageAxisParams.restype = c_short
BMC_RequestStageAxisParams.argtypes = [POINTER(c_char), c_short]


def request_stage_axis_params(serial_number, channel):
    # Requests the stage axis parameters.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_RequestStageAxisParams(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_RequestStatusBits = lib.BMC_RequestStatusBits
BMC_RequestStatusBits.restype = c_short
BMC_RequestStatusBits.argtypes = [POINTER(c_char), c_short]


def request_status_bits(serial_number, channel):
    # Request the status bits which identify the current motor state.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_RequestStatusBits(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_RequestTrackSettleParams = lib.BMC_RequestTrackSettleParams
BMC_RequestTrackSettleParams.restype = c_short
BMC_RequestTrackSettleParams.argtypes = [POINTER(c_char), c_short]


def request_track_settle_params(serial_number, channel):
    # Requests the parameters used to decide when settled at right position.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_RequestTrackSettleParams(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_RequestTriggerConfigParams = lib.BMC_RequestTriggerConfigParams
BMC_RequestTriggerConfigParams.restype = c_short
BMC_RequestTriggerConfigParams.argtypes = [POINTER(c_char)]


def request_trigger_config_params(serial_number):
    # Requests the Trigger Configuration Parameters.

    serial_number = POINTER(c_char)

    output = BMC_RequestTriggerConfigParams(serial_number)
    if output != 0:
        raise KinesisException(output)


BMC_RequestTriggerSwitches = lib.BMC_RequestTriggerSwitches
BMC_RequestTriggerSwitches.restype = c_short
BMC_RequestTriggerSwitches.argtypes = [POINTER(c_char), c_short]


def request_trigger_switches(serial_number, channel):
    # Requests the trigger switch bits.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_RequestTriggerSwitches(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_RequestVelParams = lib.BMC_RequestVelParams
BMC_RequestVelParams.restype = c_short
BMC_RequestVelParams.argtypes = [POINTER(c_char), c_short]


def request_vel_params(serial_number, channel):
    # Requests the velocity parameters.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_RequestVelParams(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_RequestVelocityProfileParams = lib.BMC_RequestVelocityProfileParams
BMC_RequestVelocityProfileParams.restype = c_short
BMC_RequestVelocityProfileParams.argtypes = [POINTER(c_char), c_short]


def request_velocity_profile_params(serial_number, channel):
    # Requests the velocity profile parameters.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_RequestVelocityProfileParams(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_ResetRotationModes = lib.BMC_ResetRotationModes
BMC_ResetRotationModes.restype = c_short
BMC_ResetRotationModes.argtypes = [POINTER(c_char), c_short]


def reset_rotation_modes(serial_number, channel):
    # Reset the rotation modes for a rotational device.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_ResetRotationModes(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_ResetStageToDefaults = lib.BMC_ResetStageToDefaults
BMC_ResetStageToDefaults.restype = c_short
BMC_ResetStageToDefaults.argtypes = [POINTER(c_char), c_short]


def reset_stage_to_defaults(serial_number, channel):
    # Reset the stage settings to defaults.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_ResetStageToDefaults(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_ResumeMoveMessages = lib.BMC_ResumeMoveMessages
BMC_ResumeMoveMessages.restype = c_short
BMC_ResumeMoveMessages.argtypes = [POINTER(c_char), c_short]


def resume_move_messages(serial_number, channel):
    # Resume suspended move messages.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_ResumeMoveMessages(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_SetBacklash = lib.BMC_SetBacklash
BMC_SetBacklash.restype = c_short
BMC_SetBacklash.argtypes = [POINTER(c_char), c_short, c_long]


def set_backlash(serial_number, channel):
    # Sets the backlash distance (used to control hysteresis).

    serial_number = POINTER(c_char)
    channel = c_short()
    distance = c_long()

    output = BMC_SetBacklash(serial_number, channel, distance)
    if output != 0:
        raise KinesisException(output)


BMC_SetCurrentLoopParams = lib.BMC_SetCurrentLoopParams
BMC_SetCurrentLoopParams.restype = c_short
BMC_SetCurrentLoopParams.argtypes = [POINTER(c_char), c_short, MOT_BrushlessCurrentLoopParameters]


def set_current_loop_params(serial_number, channel):
    # Sets the current loop parameters for moving to required position.

    serial_number = POINTER(c_char)
    channel = c_short()
    currentLoopParams = MOT_BrushlessCurrentLoopParameters()

    output = BMC_SetCurrentLoopParams(serial_number, channel, currentLoopParams)
    if output != 0:
        raise KinesisException(output)


BMC_SetDigitalOutputs = lib.BMC_SetDigitalOutputs
BMC_SetDigitalOutputs.restype = c_short
BMC_SetDigitalOutputs.argtypes = [POINTER(c_char), c_short, c_byte]


def set_digital_outputs(serial_number, channel):
    # Sets the digital output bits.

    serial_number = POINTER(c_char)
    channel = c_short()
    outputsBits = c_byte()

    output = BMC_SetDigitalOutputs(serial_number, channel, outputsBits)
    if output != 0:
        raise KinesisException(output)


BMC_SetDirection = lib.BMC_SetDirection
BMC_SetDirection.restype = c_short
BMC_SetDirection.argtypes = [POINTER(c_char), c_short, c_bool]


def set_direction(serial_number, channel):
    # Sets the motor direction sense.

    serial_number = POINTER(c_char)
    channel = c_short()
    reverse = c_bool()

    output = BMC_SetDirection(serial_number, channel, reverse)
    if output != 0:
        raise KinesisException(output)


BMC_SetElectricOutputParams = lib.BMC_SetElectricOutputParams
BMC_SetElectricOutputParams.restype = c_short
BMC_SetElectricOutputParams.argtypes = [POINTER(c_char), c_short, MOT_BrushlessElectricOutputParameters]


def set_electric_output_params(serial_number, channel):
    # Sets the electric output parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    electricOutputParams = MOT_BrushlessElectricOutputParameters()

    output = BMC_SetElectricOutputParams(serial_number, channel, electricOutputParams)
    if output != 0:
        raise KinesisException(output)


BMC_SetEncoderCounter = lib.BMC_SetEncoderCounter
BMC_SetEncoderCounter.restype = c_short
BMC_SetEncoderCounter.argtypes = [POINTER(c_char), c_short, c_long]


def set_encoder_counter(serial_number, channel):
    # Set the Encoder Counter values.

    serial_number = POINTER(c_char)
    channel = c_short()
    count = c_long()

    output = BMC_SetEncoderCounter(serial_number, channel, count)
    if output != 0:
        raise KinesisException(output)


BMC_SetFrontPanelLock = lib.BMC_SetFrontPanelLock
BMC_SetFrontPanelLock.restype = c_short
BMC_SetFrontPanelLock.argtypes = [POINTER(c_char), c_bool]


def set_front_panel_lock(serial_number):
    # Sets the device front panel lock state.

    serial_number = POINTER(c_char)
    locked = c_bool()

    output = BMC_SetFrontPanelLock(serial_number, locked)
    if output != 0:
        raise KinesisException(output)


BMC_SetHomingParamsBlock = lib.BMC_SetHomingParamsBlock
BMC_SetHomingParamsBlock.restype = c_short
BMC_SetHomingParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_HomingParameters]


def set_homing_params_block(serial_number, channel):
    # Set the homing parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    homingParams = MOT_HomingParameters()

    output = BMC_SetHomingParamsBlock(serial_number, channel, homingParams)
    if output != 0:
        raise KinesisException(output)


BMC_SetHomingVelocity = lib.BMC_SetHomingVelocity
BMC_SetHomingVelocity.restype = c_short
BMC_SetHomingVelocity.argtypes = [POINTER(c_char), c_short, c_uint]


def set_homing_velocity(serial_number, channel):
    # Sets the homing velocity.

    serial_number = POINTER(c_char)
    channel = c_short()
    velocity = c_uint()

    output = BMC_SetHomingVelocity(serial_number, channel, velocity)
    if output != 0:
        raise KinesisException(output)


BMC_SetJogMode = lib.BMC_SetJogMode
BMC_SetJogMode.restype = c_short
BMC_SetJogMode.argtypes = [POINTER(c_char), c_short, MOT_JogModes, MOT_StopModes]


def set_jog_mode(serial_number, channel):
    # Sets the jog mode.

    serial_number = POINTER(c_char)
    channel = c_short()
    mode = MOT_JogModes()
    stopMode = MOT_StopModes()

    output = BMC_SetJogMode(serial_number, channel, mode, stopMode)
    if output != 0:
        raise KinesisException(output)


BMC_SetJogParamsBlock = lib.BMC_SetJogParamsBlock
BMC_SetJogParamsBlock.restype = c_short
BMC_SetJogParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_JogParameters]


def set_jog_params_block(serial_number, channel):
    # Set the jog parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    jogParams = MOT_JogParameters()

    output = BMC_SetJogParamsBlock(serial_number, channel, jogParams)
    if output != 0:
        raise KinesisException(output)


BMC_SetJogStepSize = lib.BMC_SetJogStepSize
BMC_SetJogStepSize.restype = c_short
BMC_SetJogStepSize.argtypes = [POINTER(c_char), c_short, c_uint]


def set_jog_step_size(serial_number, channel):
    # Sets the distance to move on jogging.

    serial_number = POINTER(c_char)
    channel = c_short()
    stepSize = c_uint()

    output = BMC_SetJogStepSize(serial_number, channel, stepSize)
    if output != 0:
        raise KinesisException(output)


BMC_SetJogVelParams = lib.BMC_SetJogVelParams
BMC_SetJogVelParams.restype = c_short
BMC_SetJogVelParams.argtypes = [POINTER(c_char), c_short, c_int, c_int]


def set_jog_vel_params(serial_number, channel):
    # Sets jog velocity parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    acceleration = c_int()
    maxVelocity = c_int()

    output = BMC_SetJogVelParams(serial_number, channel, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


BMC_SetLimitsSoftwareApproachPolicy = lib.BMC_SetLimitsSoftwareApproachPolicy
BMC_SetLimitsSoftwareApproachPolicy.restype = c_void_p
BMC_SetLimitsSoftwareApproachPolicy.argtypes = [POINTER(c_char), c_short, MOT_LimitsSoftwareApproachPolicy]


def set_limits_software_approach_policy(serial_number, channel):
    # Sets the software limits mode.

    serial_number = POINTER(c_char)
    channel = c_short()
    limitsSoftwareApproachPolicy = MOT_LimitsSoftwareApproachPolicy()

    output = BMC_SetLimitsSoftwareApproachPolicy(serial_number, channel, limitsSoftwareApproachPolicy)
    if output != 0:
        raise KinesisException(output)


BMC_SetMMIParams = lib.BMC_SetMMIParams
BMC_SetMMIParams.restype = c_short
BMC_SetMMIParams.argtypes = [
    POINTER(c_char),
    KMOT_WheelMode,
    c_int32,
    c_int32,
    KMOT_WheelDirectionSense,
    c_int32,
    c_int32,
    c_int16]


def set_m_m_i_params(serial_number):
    # Set the MMI Parameters for the KCube Display Interface.

    serial_number = POINTER(c_char)
    wheelMode = KMOT_WheelMode()
    wheelMaxVelocity = c_int32()
    wheelAcceleration = c_int32()
    directionSense = KMOT_WheelDirectionSense()
    presetPosition1 = c_int32()
    presetPosition2 = c_int32()
    displayIntensity = c_int16()

    output = BMC_SetMMIParams(
        serial_number,
        wheelMode,
        wheelMaxVelocity,
        wheelAcceleration,
        directionSense,
        presetPosition1,
        presetPosition2,
        displayIntensity)
    if output != 0:
        raise KinesisException(output)


BMC_SetMMIParamsBlock = lib.BMC_SetMMIParamsBlock
BMC_SetMMIParamsBlock.restype = c_short
BMC_SetMMIParamsBlock.argtypes = [POINTER(c_char), KMOT_MMIParams]


def set_m_m_i_params_block(serial_number):
    # Sets the MMI parameters for the device.

    serial_number = POINTER(c_char)
    mmiParams = KMOT_MMIParams()

    output = BMC_SetMMIParamsBlock(serial_number, mmiParams)
    if output != 0:
        raise KinesisException(output)


BMC_SetMMIParamsExt = lib.BMC_SetMMIParamsExt
BMC_SetMMIParamsExt.restype = c_short
BMC_SetMMIParamsExt.argtypes = [
    POINTER(c_char),
    KMOT_WheelMode,
    c_int32,
    c_int32,
    KMOT_WheelDirectionSense,
    c_int32,
    c_int32,
    c_int16,
    c_int16,
    c_int16]


def set_m_m_i_params_ext(serial_number):
    # Set the MMI Parameters for the KCube Display Interface.

    serial_number = POINTER(c_char)
    wheelMode = KMOT_WheelMode()
    wheelMaxVelocity = c_int32()
    wheelAcceleration = c_int32()
    directionSense = KMOT_WheelDirectionSense()
    presetPosition1 = c_int32()
    presetPosition2 = c_int32()
    displayIntensity = c_int16()
    displayTimeout = c_int16()
    displayDimIntensity = c_int16()

    output = BMC_SetMMIParamsExt(
        serial_number,
        wheelMode,
        wheelMaxVelocity,
        wheelAcceleration,
        directionSense,
        presetPosition1,
        presetPosition2,
        displayIntensity,
        displayTimeout,
        displayDimIntensity)
    if output != 0:
        raise KinesisException(output)


BMC_SetMotorParams = lib.BMC_SetMotorParams
BMC_SetMotorParams.restype = c_short
BMC_SetMotorParams.argtypes = [POINTER(c_char), c_short, c_long]


def set_motor_params(serial_number, channel):
    # Set the motor parameters for the Brushless Votor.

    serial_number = POINTER(c_char)
    channel = c_short()
    countsPerUnit = c_long()

    output = BMC_SetMotorParams(serial_number, channel, countsPerUnit)
    if output != 0:
        raise KinesisException(output)


BMC_SetMotorParamsExt = lib.BMC_SetMotorParamsExt
BMC_SetMotorParamsExt.restype = c_short
BMC_SetMotorParamsExt.argtypes = [POINTER(c_char), c_short, c_double]


def set_motor_params_ext(serial_number, channel):
    # Set the motor parameters for the Brushless Votor.

    serial_number = POINTER(c_char)
    channel = c_short()
    countsPerUnit = c_double()

    output = BMC_SetMotorParamsExt(serial_number, channel, countsPerUnit)
    if output != 0:
        raise KinesisException(output)


BMC_SetMotorTravelLimits = lib.BMC_SetMotorTravelLimits
BMC_SetMotorTravelLimits.restype = c_short
BMC_SetMotorTravelLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]


def set_motor_travel_limits(serial_number, channel):
    # Sets the absolute minimum and maximum travel range constants for the current stage.

    serial_number = POINTER(c_char)
    channel = c_short()
    minPosition = c_double()
    maxPosition = c_double()

    output = BMC_SetMotorTravelLimits(serial_number, channel, minPosition, maxPosition)
    if output != 0:
        raise KinesisException(output)


BMC_SetMotorTravelMode = lib.BMC_SetMotorTravelMode
BMC_SetMotorTravelMode.restype = c_short
BMC_SetMotorTravelMode.argtypes = [POINTER(c_char), c_short, MOT_TravelModes]


def set_motor_travel_mode(serial_number, channel):
    # Set the motor travel mode.

    serial_number = POINTER(c_char)
    channel = c_short()
    travelMode = MOT_TravelModes()

    output = BMC_SetMotorTravelMode(serial_number, channel, travelMode)
    if output != 0:
        raise KinesisException(output)


BMC_SetMotorVelocityLimits = lib.BMC_SetMotorVelocityLimits
BMC_SetMotorVelocityLimits.restype = c_short
BMC_SetMotorVelocityLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]


def set_motor_velocity_limits(serial_number, channel):
    # Sets the absolute maximum velocity and acceleration constants for the current stage.

    serial_number = POINTER(c_char)
    channel = c_short()
    maxVelocity = c_double()
    maxAcceleration = c_double()

    output = BMC_SetMotorVelocityLimits(serial_number, channel, maxVelocity, maxAcceleration)
    if output != 0:
        raise KinesisException(output)


BMC_SetMoveAbsolutePosition = lib.BMC_SetMoveAbsolutePosition
BMC_SetMoveAbsolutePosition.restype = c_short
BMC_SetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short, c_int]


def set_move_absolute_position(serial_number, channel):
    # Sets the move absolute position.

    serial_number = POINTER(c_char)
    channel = c_short()
    position = c_int()

    output = BMC_SetMoveAbsolutePosition(serial_number, channel, position)
    if output != 0:
        raise KinesisException(output)


BMC_SetMoveRelativeDistance = lib.BMC_SetMoveRelativeDistance
BMC_SetMoveRelativeDistance.restype = c_short
BMC_SetMoveRelativeDistance.argtypes = [POINTER(c_char), c_short, c_int]


def set_move_relative_distance(serial_number, channel):
    # Sets the move relative distance.

    serial_number = POINTER(c_char)
    channel = c_short()
    distance = c_int()

    output = BMC_SetMoveRelativeDistance(serial_number, channel, distance)
    if output != 0:
        raise KinesisException(output)


BMC_SetPosLoopParams = lib.BMC_SetPosLoopParams
BMC_SetPosLoopParams.restype = c_short
BMC_SetPosLoopParams.argtypes = [POINTER(c_char), c_short, MOT_BrushlessPositionLoopParameters]


def set_pos_loop_params(serial_number, channel):
    # Sets the position feedback loop parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    positionLoopParams = MOT_BrushlessPositionLoopParameters()

    output = BMC_SetPosLoopParams(serial_number, channel, positionLoopParams)
    if output != 0:
        raise KinesisException(output)


BMC_SetPositionCounter = lib.BMC_SetPositionCounter
BMC_SetPositionCounter.restype = c_short
BMC_SetPositionCounter.argtypes = [POINTER(c_char), c_short, c_long]


def set_position_counter(serial_number, channel):
    # Set the Position Counter.

    serial_number = POINTER(c_char)
    channel = c_short()
    count = c_long()

    output = BMC_SetPositionCounter(serial_number, channel, count)
    if output != 0:
        raise KinesisException(output)


BMC_SetRotationModes = lib.BMC_SetRotationModes
BMC_SetRotationModes.restype = c_short
BMC_SetRotationModes.argtypes = [POINTER(c_char), c_short, MOT_MovementModes, MOT_MovementDirections]


def set_rotation_modes(serial_number, channel):
    # Set the rotation modes for a rotational device.

    serial_number = POINTER(c_char)
    channel = c_short()
    mode = MOT_MovementModes()
    direction = MOT_MovementDirections()

    output = BMC_SetRotationModes(serial_number, channel, mode, direction)
    if output != 0:
        raise KinesisException(output)


BMC_SetStageAxisLimits = lib.BMC_SetStageAxisLimits
BMC_SetStageAxisLimits.restype = c_short
BMC_SetStageAxisLimits.argtypes = [POINTER(c_char), c_short, c_int, c_int]


def set_stage_axis_limits(serial_number, channel):
    # Sets the stage axis position limits.

    serial_number = POINTER(c_char)
    channel = c_short()
    minPosition = c_int()
    maxPosition = c_int()

    output = BMC_SetStageAxisLimits(serial_number, channel, minPosition, maxPosition)
    if output != 0:
        raise KinesisException(output)


BMC_SetTrackSettleParams = lib.BMC_SetTrackSettleParams
BMC_SetTrackSettleParams.restype = c_short
BMC_SetTrackSettleParams.argtypes = [POINTER(c_char), c_short, MOT_BrushlessTrackSettleParameters]


def set_track_settle_params(serial_number, channel):
    # Sets the track settled parameters used to decide when settled at right position.

    serial_number = POINTER(c_char)
    channel = c_short()
    settleParams = MOT_BrushlessTrackSettleParameters()

    output = BMC_SetTrackSettleParams(serial_number, channel, settleParams)
    if output != 0:
        raise KinesisException(output)


BMC_SetTriggerConfigParams = lib.BMC_SetTriggerConfigParams
BMC_SetTriggerConfigParams.restype = c_short
BMC_SetTriggerConfigParams.argtypes = [
    POINTER(c_char),
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity,
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity]


def set_trigger_config_params(serial_number):
    # Set the Trigger Configuration Parameters.

    serial_number = POINTER(c_char)
    trigger1Mode = KMOT_TriggerPortMode()
    trigger1Polarity = KMOT_TriggerPortPolarity()
    trigger2Mode = KMOT_TriggerPortMode()
    trigger2Polarity = KMOT_TriggerPortPolarity()

    output = BMC_SetTriggerConfigParams(serial_number, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity)
    if output != 0:
        raise KinesisException(output)


BMC_SetTriggerConfigParamsBlock = lib.BMC_SetTriggerConfigParamsBlock
BMC_SetTriggerConfigParamsBlock.restype = c_short
BMC_SetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerConfig]


def set_trigger_config_params_block(serial_number):
    # Sets the trigger configuration parameters block.

    serial_number = POINTER(c_char)
    triggerConfigParams = KMOT_TriggerConfig()

    output = BMC_SetTriggerConfigParamsBlock(serial_number, triggerConfigParams)
    if output != 0:
        raise KinesisException(output)


BMC_SetTriggerParamsParams = lib.BMC_SetTriggerParamsParams
BMC_SetTriggerParamsParams.restype = c_short
BMC_SetTriggerParamsParams.argtypes = [
    POINTER(c_char),
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32]


def set_trigger_params_params(serial_number):
    # Set the Trigger Parameters Parameters.

    serial_number = POINTER(c_char)
    triggerStartPositionFwd = c_int32()
    triggerIntervalFwd = c_int32()
    triggerPulseCountFwd = c_int32()
    triggerStartPositionRev = c_int32()
    triggerIntervalRev = c_int32()
    triggerPulseCountRev = c_int32()
    triggerPulseWidth = c_int32()
    cycleCount = c_int32()

    output = BMC_SetTriggerParamsParams(
        serial_number,
        triggerStartPositionFwd,
        triggerIntervalFwd,
        triggerPulseCountFwd,
        triggerStartPositionRev,
        triggerIntervalRev,
        triggerPulseCountRev,
        triggerPulseWidth,
        cycleCount)
    if output != 0:
        raise KinesisException(output)


BMC_SetTriggerParamsParamsBlock = lib.BMC_SetTriggerParamsParamsBlock
BMC_SetTriggerParamsParamsBlock.restype = c_short
BMC_SetTriggerParamsParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerParams]


def set_trigger_params_params_block(serial_number):
    # Sets the trigger parameters block.

    serial_number = POINTER(c_char)
    triggerParamsParams = KMOT_TriggerParams()

    output = BMC_SetTriggerParamsParamsBlock(serial_number, triggerParamsParams)
    if output != 0:
        raise KinesisException(output)


BMC_SetTriggerSwitches = lib.BMC_SetTriggerSwitches
BMC_SetTriggerSwitches.restype = c_short
BMC_SetTriggerSwitches.argtypes = [POINTER(c_char), c_short, c_byte]


def set_trigger_switches(serial_number, channel):
    # Sets the trigger switch bits.

    serial_number = POINTER(c_char)
    channel = c_short()
    indicatorBits = c_byte()

    output = BMC_SetTriggerSwitches(serial_number, channel, indicatorBits)
    if output != 0:
        raise KinesisException(output)


BMC_SetVelParams = lib.BMC_SetVelParams
BMC_SetVelParams.restype = c_short
BMC_SetVelParams.argtypes = [POINTER(c_char), c_short, c_int, c_int]


def set_vel_params(serial_number, channel):
    # Sets the move velocity parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    acceleration = c_int()
    maxVelocity = c_int()

    output = BMC_SetVelParams(serial_number, channel, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


BMC_SetVelParamsBlock = lib.BMC_SetVelParamsBlock
BMC_SetVelParamsBlock.restype = c_short
BMC_SetVelParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_VelocityParameters]


def set_vel_params_block(serial_number, channel):
    # Set the move velocity parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    velocityParams = MOT_VelocityParameters()

    output = BMC_SetVelParamsBlock(serial_number, channel, velocityParams)
    if output != 0:
        raise KinesisException(output)


BMC_SetVelocityProfileParams = lib.BMC_SetVelocityProfileParams
BMC_SetVelocityProfileParams.restype = c_short
BMC_SetVelocityProfileParams.argtypes = [POINTER(c_char), c_short, MOT_VelocityProfileParameters]


def set_velocity_profile_params(serial_number, channel):
    # Sets the velocity profile parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    velocityProfileParams = MOT_VelocityProfileParameters()

    output = BMC_SetVelocityProfileParams(serial_number, channel, velocityProfileParams)
    if output != 0:
        raise KinesisException(output)


BMC_StartPolling = lib.BMC_StartPolling
BMC_StartPolling.restype = c_bool
BMC_StartPolling.argtypes = [POINTER(c_char), c_short, c_int]


def start_polling(serial_number, channel):
    # Starts the internal polling loop which continuously requests position and status.

    serial_number = POINTER(c_char)
    channel = c_short()
    milliseconds = c_int()

    output = BMC_StartPolling(serial_number, channel, milliseconds)

    return output


BMC_StopImmediate = lib.BMC_StopImmediate
BMC_StopImmediate.restype = c_short
BMC_StopImmediate.argtypes = [POINTER(c_char), c_short]


def stop_immediate(serial_number, channel):
    # Stop the current move immediately (with risk of losing track of position).

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_StopImmediate(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_StopPolling = lib.BMC_StopPolling
BMC_StopPolling.restype = c_void_p
BMC_StopPolling.argtypes = [POINTER(c_char), c_short]


def stop_polling(serial_number, channel):
    # Stops the internal polling loop.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_StopPolling(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_StopProfiled = lib.BMC_StopProfiled
BMC_StopProfiled.restype = c_short
BMC_StopProfiled.argtypes = [POINTER(c_char), c_short]


def stop_profiled(serial_number, channel):
    # Stop the current move using the current velocity profile.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_StopProfiled(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_SuspendMoveMessages = lib.BMC_SuspendMoveMessages
BMC_SuspendMoveMessages.restype = c_short
BMC_SuspendMoveMessages.argtypes = [POINTER(c_char), c_short]


def suspend_move_messages(serial_number, channel):
    # Suspend automatic messages at ends of moves.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BMC_SuspendMoveMessages(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BMC_TimeSinceLastMsgReceived = lib.BMC_TimeSinceLastMsgReceived
BMC_TimeSinceLastMsgReceived.restype = c_bool
BMC_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char), c_short, c_int64]


def time_since_last_msg_received(serial_number, channel):
    # Gets the time in milliseconds since tha last message was received from the device.

    serial_number = POINTER(c_char)
    channel = c_short()
    lastUpdateTimeMS = c_int64()

    output = BMC_TimeSinceLastMsgReceived(serial_number, channel, lastUpdateTimeMS)

    return output


BMC_WaitForMessage = lib.BMC_WaitForMessage
BMC_WaitForMessage.restype = c_bool
BMC_WaitForMessage.argtypes = [POINTER(c_char), c_short, c_long, c_long, c_ulong]


def wait_for_message(serial_number, channel):
    # Wait for next MessageQueue item.

    serial_number = POINTER(c_char)
    channel = c_short()
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = BMC_WaitForMessage(serial_number, channel, messageType, messageID, messageData)

    return output


TLI_BuildDeviceList = lib.TLI_BuildDeviceList
TLI_BuildDeviceList.restype = c_short
TLI_BuildDeviceList.argtypes = [c_void_p]


def build_device_list():
    # Build the DeviceList.

    output = TLI_BuildDeviceList()
    if output != 0:
        raise KinesisException(output)


TLI_GetDeviceInfo = lib.TLI_GetDeviceInfo
TLI_GetDeviceInfo.restype = c_short
TLI_GetDeviceInfo.argtypes = [POINTER(c_char), POINTER(c_char), TLI_DeviceInfo]


def get_device_info(serial_number):
    # Get the device information from the USB port.

    serial_number = POINTER(c_char)
    serialNumber = POINTER(c_char)
    info = TLI_DeviceInfo()

    output = TLI_GetDeviceInfo(serial_number, serialNumber, info)
    if output != 0:
        raise KinesisException(output)


TLI_GetDeviceList = lib.TLI_GetDeviceList
TLI_GetDeviceList.restype = c_short
TLI_GetDeviceList.argtypes = [SafeArray]


def get_device_list():
    # Get the entire contents of the device list.

    output = TLI_GetDeviceList()
    if output != 0:
        raise KinesisException(output)


TLI_GetDeviceListByType = lib.TLI_GetDeviceListByType
TLI_GetDeviceListByType.restype = c_short
TLI_GetDeviceListByType.argtypes = [SafeArray, c_int]


def get_device_list_by_type():
    # Get the contents of the device list which match the supplied typeID.

    output = TLI_GetDeviceListByType()
    if output != 0:
        raise KinesisException(output)


TLI_GetDeviceListByTypeExt = lib.TLI_GetDeviceListByTypeExt
TLI_GetDeviceListByTypeExt.restype = c_short
TLI_GetDeviceListByTypeExt.argtypes = [POINTER(c_char), c_ulong, c_int]


def get_device_list_by_type_ext():
    # Get the contents of the device list which match the supplied typeID.

    output = TLI_GetDeviceListByTypeExt()
    if output != 0:
        raise KinesisException(output)


TLI_GetDeviceListByTypes = lib.TLI_GetDeviceListByTypes
TLI_GetDeviceListByTypes.restype = c_short
TLI_GetDeviceListByTypes.argtypes = [SafeArray, c_int, c_int]


def get_device_list_by_types():
    # Get the contents of the device list which match the supplied typeIDs.

    output = TLI_GetDeviceListByTypes()
    if output != 0:
        raise KinesisException(output)


TLI_GetDeviceListByTypesExt = lib.TLI_GetDeviceListByTypesExt
TLI_GetDeviceListByTypesExt.restype = c_short
TLI_GetDeviceListByTypesExt.argtypes = [POINTER(c_char), c_ulong, c_int, c_int]


def get_device_list_by_types_ext():
    # Get the contents of the device list which match the supplied typeIDs.

    output = TLI_GetDeviceListByTypesExt()
    if output != 0:
        raise KinesisException(output)


TLI_GetDeviceListExt = lib.TLI_GetDeviceListExt
TLI_GetDeviceListExt.restype = c_short
TLI_GetDeviceListExt.argtypes = [POINTER(c_char), c_ulong]


def get_device_list_ext():
    # Get the entire contents of the device list.

    output = TLI_GetDeviceListExt()
    if output != 0:
        raise KinesisException(output)


TLI_GetDeviceListSize = lib.TLI_GetDeviceListSize
TLI_GetDeviceListSize.restype = c_short


def get_device_list_size():
    # Gets the device list size.

    output = TLI_GetDeviceListSize()
    if output != 0:
        raise KinesisException(output)


TLI_InitializeSimulations = lib.TLI_InitializeSimulations
TLI_InitializeSimulations.restype = c_void_p


def initialize_simulations():
    # Initialize a connection to the Simulation Manager, which must already be running.

    output = TLI_InitializeSimulations()
    if output != 0:
        raise KinesisException(output)
