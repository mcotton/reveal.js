from Phidgets.PhidgetException import *
from Phidgets.Events.Events import *
from Phidgets.Devices.InterfaceKit import *

try:
  device = InterfaceKit()
except RuntimeError as e:
  print("Runtime Error: %s" % e.message)

def sensorChanged(e):
  if e.value > 0 and e.value < 301:
    device.setOutputState(0, 1)
    device.setOutputState(1, 0)
    device.setOutputState(2, 0)
  if e.value > 300 and e.value < 601:
    device.setOutputState(0, 0)
    device.setOutputState(1, 1)
    device.setOutputState(2, 0)
  if e.value > 601 and e.value < 999:
    device.setOutputState(0, 0)
    device.setOutputState(1, 0)
    device.setOutputState(2, 1)

try:
  device.openPhidget()
  device.waitForAttach(10000)
except PhidgetException as e:
  print('Phidget Exception')
  exit(1)

def AttachHandler(event):
  attachedDevice = event.device
  serialNumber = attachedDevice.getSerialNum()
  deviceName = attachedDevice.getDeviceName()
  print("Hello to Device " + str(deviceName) + ", Serial Number: " + str(serialNumber))
  device.setOnSensorChangeHandler(sensorChanged)

try:
  device.setOnAttachHandler(AttachHandler)
except PhidgetException as e: 
  pass
