from typing import Optional

from ophyd import Arming, Component, Device, EpicsSignal, Signal
from ophyd.status import SubscriptionStatus

from dodal.devices.detector import DetectorParams
from dodal.devices.status import await_value
from dodal.log import LOGGER


class Attenuator(Device):
    def set(self, value, *, timeout=None, settle_time=None, **kwargs):
        return self.set_transmission(value)

    # Could make a separate class for these, but that's potentially pointless as this is the only PV for it
    pv_calulated_filter_state_0: EpicsSignal = Component(EpicsSignal, ":DEC_TO_BIN.B0")
    pv_calulated_filter_state_1: EpicsSignal = Component(EpicsSignal, ":DEC_TO_BIN.B1")
    pv_calulated_filter_state_2: EpicsSignal = Component(EpicsSignal, ":DEC_TO_BIN.B2")
    pv_calulated_filter_state_3: EpicsSignal = Component(EpicsSignal, ":DEC_TO_BIN.B3")
    pv_calulated_filter_state_4: EpicsSignal = Component(EpicsSignal, ":DEC_TO_BIN.B4")
    pv_calulated_filter_state_5: EpicsSignal = Component(EpicsSignal, ":DEC_TO_BIN.B5")
    pv_calulated_filter_state_6: EpicsSignal = Component(EpicsSignal, ":DEC_TO_BIN.B6")
    pv_calulated_filter_state_7: EpicsSignal = Component(EpicsSignal, ":DEC_TO_BIN.B7")
    pv_calulated_filter_state_8: EpicsSignal = Component(EpicsSignal, ":DEC_TO_BIN.B8")
    pv_calulated_filter_state_9: EpicsSignal = Component(EpicsSignal, ":DEC_TO_BIN.B9")
    pv_calulated_filter_state_10: EpicsSignal = Component(EpicsSignal, ":DEC_TO_BIN.BA")
    pv_calulated_filter_state_11: EpicsSignal = Component(EpicsSignal, ":DEC_TO_BIN.BB")
    pv_calulated_filter_state_12: EpicsSignal = Component(EpicsSignal, ":DEC_TO_BIN.BC")
    pv_calulated_filter_state_13: EpicsSignal = Component(EpicsSignal, ":DEC_TO_BIN.BD")
    pv_calulated_filter_state_14: EpicsSignal = Component(EpicsSignal, ":DEC_TO_BIN.BE")
    pv_calulated_filter_state_15: EpicsSignal = Component(EpicsSignal, ":DEC_TO_BIN.BF")

    # Could also make another class for this - but again it's the only PV used
    pv_actual_filter_state_1: EpicsSignal = Component(EpicsSignal, ":FILTER1:INLIM")
    pv_actual_filter_state_2: EpicsSignal = Component(EpicsSignal, ":FILTER2:INLIM")
    pv_actual_filter_state_3: EpicsSignal = Component(EpicsSignal, ":FILTER3:INLIM")
    pv_actual_filter_state_4: EpicsSignal = Component(EpicsSignal, ":FILTER4:INLIM")
    pv_actual_filter_state_5: EpicsSignal = Component(EpicsSignal, ":FILTER5:INLIM")
    pv_actual_filter_state_6: EpicsSignal = Component(EpicsSignal, ":FILTER6:INLIM")
    pv_actual_filter_state_7: EpicsSignal = Component(EpicsSignal, ":FILTER7:INLIM")
    pv_actual_filter_state_8: EpicsSignal = Component(EpicsSignal, ":FILTER8:INLIM")
    pv_actual_filter_state_9: EpicsSignal = Component(EpicsSignal, ":FILTER9:INLIM")
    pv_actual_filter_state_10: EpicsSignal = Component(EpicsSignal, ":FILTER10:INLIM")
    pv_actual_filter_state_11: EpicsSignal = Component(EpicsSignal, ":FILTER11:INLIM")
    pv_actual_filter_state_12: EpicsSignal = Component(EpicsSignal, ":FILTER12:INLIM")
    pv_actual_filter_state_13: EpicsSignal = Component(EpicsSignal, ":FILTER13:INLIM")
    pv_actual_filter_state_14: EpicsSignal = Component(EpicsSignal, ":FILTER14:INLIM")
    pv_actual_filter_state_15: EpicsSignal = Component(EpicsSignal, ":FILTER15:INLIM")
    pv_actual_filter_state_16: EpicsSignal = Component(EpicsSignal, ":FILTER16:INLIM")

    pv_desired_transmission: EpicsSignal = Component(EpicsSignal, ":T2A:SETVAL1")
    pv_use_current_energy: EpicsSignal = Component(
        EpicsSignal, ":E2WL:USECURRENTENERGY.PROC"
    )
    pv_change: EpicsSignal = Component(EpicsSignal, ":FANOUT")
    pv_actual_transmission: EpicsSignal = Component(EpicsSignal, ":MATCH")

    detector_params: Optional[DetectorParams] = None

    def get_calculated_filter_state_list(self) -> list[EpicsSignal]:
        return [
            self.pv_calulated_filter_state_0,
            self.pv_calulated_filter_state_1,
            self.pv_calulated_filter_state_2,
            self.pv_calulated_filter_state_3,
            self.pv_calulated_filter_state_4,
            self.pv_calulated_filter_state_5,
            self.pv_calulated_filter_state_6,
            self.pv_calulated_filter_state_7,
            self.pv_calulated_filter_state_8,
            self.pv_calulated_filter_state_9,
            self.pv_calulated_filter_state_10,
            self.pv_calulated_filter_state_11,
            self.pv_calulated_filter_state_12,
            self.pv_calulated_filter_state_13,
            self.pv_calulated_filter_state_14,
            self.pv_calulated_filter_state_15,
        ]

    def get_actual_filter_state_list(self) -> list[EpicsSignal]:
        return [
            self.pv_actual_filter_state_1,
            self.pv_actual_filter_state_2,
            self.pv_actual_filter_state_3,
            self.pv_actual_filter_state_4,
            self.pv_actual_filter_state_5,
            self.pv_actual_filter_state_6,
            self.pv_actual_filter_state_7,
            self.pv_actual_filter_state_8,
            self.pv_actual_filter_state_9,
            self.pv_actual_filter_state_10,
            self.pv_actual_filter_state_11,
            self.pv_actual_filter_state_12,
            self.pv_actual_filter_state_13,
            self.pv_actual_filter_state_14,
            self.pv_actual_filter_state_15,
            self.pv_actual_filter_state_16,
        ]

    def set_transmission(self, transmission) -> SubscriptionStatus:
        """Get desired states and calculated states, return a status which is complete once they are equal"""
        # put this in try block?

        LOGGER.info("Using current energy")
        self.pv_use_current_energy.put(1)
        LOGGER.info(f"Setting desired transmission to {transmission}")
        self.pv_desired_transmission.put(transmission)
        LOGGER.info("Sending change filter command")
        self.pv_change.put(1)

        # Get desired filter positions (16phase)

        desired_states = []

        # Get the boolean desired state of each of the 16 filters
        # TODO: put in a try catch block since the get might timeout
        for calculated_state in self.get_calculated_filter_state_list():
            value = int(calculated_state.get(timeout=10))
            desired_states.append(value == 1)

        actual_states = []

        # Get the boolean actual state of each of the 16 filters
        for actual_state in self.get_actual_filter_state_list():
            value = actual_state.get(timeout=10)
            actual_states.append(value == "in")

        return await_value(actual_states, desired_states, timeout=30)

        # If all the actual states are equal to the desired state, we can move on

        # and check if atteunator is ready
        # Get actual positions (get filter positions() from 16 phase)
