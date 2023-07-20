from .CAENels_bimorph_mirror_0_channel import CAENelsBimorphMirror0Channel

from ophyd import Component, Device, EpicsSignal, EpicsSignalRO

class CAENelsBimorphMirror7Channel(CAENelsBimorphMirror0Channel):
    """
    Class representing a CAENels 7-Channel Bimorph Mirror.

    Adds 7 channels to 0 inherited.

    """
    channel_1_voltage_target: EpicsSignal = Component(EpicsSignal, "C1:VTRGT")
    channel_2_voltage_target: EpicsSignal = Component(EpicsSignal, "C2:VTRGT")
    channel_3_voltage_target: EpicsSignal = Component(EpicsSignal, "C3:VTRGT")
    channel_4_voltage_target: EpicsSignal = Component(EpicsSignal, "C4:VTRGT")
    channel_5_voltage_target: EpicsSignal = Component(EpicsSignal, "C5:VTRGT")
    channel_6_voltage_target: EpicsSignal = Component(EpicsSignal, "C6:VTRGT")
    channel_7_voltage_target: EpicsSignal = Component(EpicsSignal, "C7:VTRGT")

    channel_1_voltage_target_readback_value: EpicsSignalRO = Component(
        EpicsSignalRO, "C1:VTRGT_RBV"
    )
    channel_2_voltage_target_readback_value: EpicsSignalRO = Component(
        EpicsSignalRO, "C2:VTRGT_RBV"
    )
    channel_3_voltage_target_readback_value: EpicsSignalRO = Component(
        EpicsSignalRO, "C3:VTRGT_RBV"
    )
    channel_4_voltage_target_readback_value: EpicsSignalRO = Component(
        EpicsSignalRO, "C4:VTRGT_RBV"
    )
    channel_5_voltage_target_readback_value: EpicsSignalRO = Component(
        EpicsSignalRO, "C5:VTRGT_RBV"
    )
    channel_6_voltage_target_readback_value: EpicsSignalRO = Component(
        EpicsSignalRO, "C6:VTRGT_RBV"
    )
    channel_7_voltage_target_readback_value: EpicsSignalRO = Component(
        EpicsSignalRO, "C7:VTRGT_RBV"
    )

    channel_1_shift: EpicsSignal = Component(EpicsSignal, "C1:SHIFT")
    channel_2_shift: EpicsSignal = Component(EpicsSignal, "C2:SHIFT")
    channel_3_shift: EpicsSignal = Component(EpicsSignal, "C3:SHIFT")
    channel_4_shift: EpicsSignal = Component(EpicsSignal, "C4:SHIFT")
    channel_5_shift: EpicsSignal = Component(EpicsSignal, "C5:SHIFT")
    channel_6_shift: EpicsSignal = Component(EpicsSignal, "C6:SHIFT")
    channel_7_shift: EpicsSignal = Component(EpicsSignal, "C7:SHIFT")

    channel_1_voltage_out: EpicsSignal = Component(EpicsSignal, "C1:VOUT")
    channel_2_voltage_out: EpicsSignal = Component(EpicsSignal, "C2:VOUT")
    channel_3_voltage_out: EpicsSignal = Component(EpicsSignal, "C3:VOUT")
    channel_4_voltage_out: EpicsSignal = Component(EpicsSignal, "C4:VOUT")
    channel_5_voltage_out: EpicsSignal = Component(EpicsSignal, "C5:VOUT")
    channel_6_voltage_out: EpicsSignal = Component(EpicsSignal, "C6:VOUT")
    channel_7_voltage_out: EpicsSignal = Component(EpicsSignal, "C7:VOUT")

    channel_1_voltage_out_readback_value: EpicsSignalRO = Component(
        EpicsSignalRO, "C1:VOUT_RBV"
    )
    channel_2_voltage_out_readback_value: EpicsSignalRO = Component(
        EpicsSignalRO, "C2:VOUT_RBV"
    )
    channel_3_voltage_out_readback_value: EpicsSignalRO = Component(
        EpicsSignalRO, "C3:VOUT_RBV"
    )
    channel_4_voltage_out_readback_value: EpicsSignalRO = Component(
        EpicsSignalRO, "C4:VOUT_RBV"
    )
    channel_5_voltage_out_readback_value: EpicsSignalRO = Component(
        EpicsSignalRO, "C5:VOUT_RBV"
    )
    channel_6_voltage_out_readback_value: EpicsSignalRO = Component(
        EpicsSignalRO, "C6:VOUT_RBV"
    )
    channel_7_voltage_out_readback_value: EpicsSignalRO = Component(
        EpicsSignalRO, "C7:VOUT_RBV"
    )

    channel_1_status: EpicsSignalRO = Component(EpicsSignalRO, "C1:STATUS")
    channel_2_status: EpicsSignalRO = Component(EpicsSignalRO, "C2:STATUS")
    channel_3_status: EpicsSignalRO = Component(EpicsSignalRO, "C3:STATUS")
    channel_4_status: EpicsSignalRO = Component(EpicsSignalRO, "C4:STATUS")
    channel_5_status: EpicsSignalRO = Component(EpicsSignalRO, "C5:STATUS")
    channel_6_status: EpicsSignalRO = Component(EpicsSignalRO, "C6:STATUS")
    channel_7_status: EpicsSignalRO = Component(EpicsSignalRO, "C7:STATUS")


    # lists of channels for easy access
    # there must be a nicer way to do this:
    _voltage_target_channels = CAENelsBimorphMirror0Channel._voltage_target_channels.copy()
    
    _voltage_target_channels.extend([
        channel_1_voltage_target,
        channel_2_voltage_target,
        channel_3_voltage_target,
        channel_4_voltage_target,
        channel_5_voltage_target,
        channel_6_voltage_target,
        channel_7_voltage_target,
    ])

    _voltage_target_readback_value_channels = CAENelsBimorphMirror0Channel._voltage_target_readback_value_channels.copy()
    
    _voltage_target_readback_value_channels.extend([
        channel_1_voltage_target_readback_value,
        channel_2_voltage_target_readback_value,
        channel_3_voltage_target_readback_value,
        channel_4_voltage_target_readback_value,
        channel_5_voltage_target_readback_value,
        channel_6_voltage_target_readback_value,
        channel_7_voltage_target_readback_value,
    ])

    _shift_channels = CAENelsBimorphMirror0Channel._shift_channels.copy()

    _shift_channels.extend([
        channel_1_shift,
        channel_2_shift,
        channel_3_shift,
        channel_4_shift,
        channel_5_shift,
        channel_6_shift,
        channel_7_shift,
    ])

    _voltage_out_channels = CAENelsBimorphMirror0Channel._voltage_out_channels.copy()

    _voltage_out_channels.extend([
        channel_1_voltage_out,
        channel_2_voltage_out,
        channel_3_voltage_out,
        channel_4_voltage_out,
        channel_5_voltage_out,
        channel_6_voltage_out,
        channel_7_voltage_out,
    ])

    _voltage_out_readback_value_channels = CAENelsBimorphMirror0Channel._voltage_out_readback_value_channels.copy()
    
    _voltage_out_readback_value_channels.extend([
        channel_1_voltage_out_readback_value,
        channel_2_voltage_out_readback_value,
        channel_3_voltage_out_readback_value,
        channel_4_voltage_out_readback_value,
        channel_5_voltage_out_readback_value,
        channel_6_voltage_out_readback_value,
        channel_7_voltage_out_readback_value,
    ])
    _status_channels = CAENelsBimorphMirror0Channel._status_channels
    
    _status_channels.extend([
        channel_1_status,
        channel_2_status,
        channel_3_status,
        channel_4_status,
        channel_5_status,
        channel_6_status,
        channel_7_status,
    ])