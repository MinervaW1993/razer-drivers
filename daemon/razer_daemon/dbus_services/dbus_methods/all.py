"""
DBus methods available for all devices.
"""
from razer_daemon.dbus_services import endpoint

@endpoint('razer.device.misc', 'version', out_sig='s')
def version(self):
    """
    Get the devices driver version

    :return: Get driver version string like 1.0.7
    :rtype: str
    """
    self.logger.debug("DBus call version")

    driver_path = self.get_driver_path('version')

    try:
        with open(driver_path, 'r') as driver_file:
            return driver_file.read().strip()
    except (IOError, OSError):
        return '0.0.0'

@endpoint('razer.device.misc', 'getFirmware', out_sig='s')
def get_firmware(self):
    """
    Get the devices firmware version

    :return: Get firmware string like v1.1
    :rtype: str
    """
    self.logger.debug("DBus call get_firmware")

    driver_path = self.get_driver_path('get_firmware_version')

    with open(driver_path, 'r') as driver_file:
        return driver_file.read().strip()

@endpoint('razer.device.misc', 'getDeviceName', out_sig='s')
def get_device_name(self):
    """
    Get the device's descriptive string

    :return: Device string like 'BlackWidow Ultimate 2013'
    :rtype: str
    """
    self.logger.debug("DBus call get_device_name")

    driver_path = self.get_driver_path('device_type')

    with open(driver_path, 'r') as driver_file:
        return driver_file.read().strip()

# Functions to define a hardware class
@endpoint('razer.device.misc', 'getDeviceType', out_sig='s')
def get_device_type_keyboard(self):
    """
    Get the device's type

    :return: 'keyboard'
    :rtype: str
    """
    self.logger.debug("DBus call get_device_type")
    return 'keyboard'

@endpoint('razer.device.misc', 'getDeviceType', out_sig='s')
def get_device_type_mouse(self):
    """
    Get the device's type

    :return:'mouse'
    :rtype: str
    """
    self.logger.debug("DBus call get_device_type")
    return 'mouse'

@endpoint('razer.device.misc', 'getDeviceType', out_sig='s')
def get_device_type_firefly(self):
    """
    Get the device's type

    :return:'firefly'
    :rtype: str
    """
    self.logger.debug("DBus call get_device_type")
    return 'firefly'

@endpoint('razer.device.misc', 'getDeviceType', out_sig='s')
def get_device_type_tartarus(self):
    """
    Get the device's type

    :return:'tartarus'
    :rtype: str
    """
    self.logger.debug("DBus call get_device_type")
    return 'tartarus'


@endpoint('razer.device.misc', 'hasMatrix', out_sig='b')
def has_matrix(self):
    """
    If the device has an LED matrix
    """
    self.logger.debug("DBus call has_matrix")

    return self.HAS_MATRIX

@endpoint('razer.device.misc', 'getMatrixDimensions', out_sig='ai')
def get_matrix_dims(self):
    """
    If the device has an LED matrix
    """
    self.logger.debug("DBus call has_matrix")

    return list(self.MATRIX_DIMS)

