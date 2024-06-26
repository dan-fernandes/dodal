"""
Module for containing errors in operation of the OAV.
"""
from dodal.log import LOGGER


class OAVError_ZoomLevelNotFound(Exception):
    def __init__(self, errmsg):
        LOGGER.error(errmsg)


class OAVError_BeamPositionNotFound(Exception):
    def __init__(self, errmsg):
        LOGGER.error(errmsg)


class OAVError_WaveformAllZero(Exception):
    def __init__(self, errmsg):
        LOGGER.error(errmsg)


class OAVError_NoRotationsPassValidityTest(Exception):
    def __init__(self, errmsg):
        LOGGER.error(errmsg)


class OAVError_MissingRotations(Exception):
    def __init__(self, errmsg):
        LOGGER.error(errmsg)


class OAVError_TipDistanceExceedsMax(Exception):
    def __init__(self, errmsg):
        LOGGER.error(errmsg)
