from ophyd import Component, Device, EpicsSignal, EpicsSignalRO, Movable, Readable

class CAENelsBimorphChannel(Device, Movable, Readable):
    """A class representing a single bimorph mirror channel.

    Attributes:
        voltage_target
        shift
        voltage_out
        voltage_out_readback_value
        status
    """
    voltage_target: EpicsSignal = Component(EpicsSignal, "VTRGT")
    voltage_target_readback_value: EpicsSignalRO
    shift: EpicsSignal = Component(EpicsSignal, "SHIFT")
    voltage_out: EpicsSignal = Component(EpicsSignal, "VOUT")
    voltage_out_readback_value: EpicsSignalRO = Component(EpicsSignalRO, "VOUT_RBV")
    status: EpicsSignalRO = Component(EpicsSignalRO, "STATUS")
