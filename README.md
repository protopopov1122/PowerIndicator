# Power Indicator
Simple project used to "share" battery status between Linux host and Windows guest in virtual machine.
Linux host runs simple BatteryService that serves current battery and power status(uses sysfs). Windows runs
applet(uses wxWidgets library) that gets info from host service and shows icon in tray with some
simple notifications.

Project is ultra-simple and written for more convinient Linux-Windows integration.

### Author & License
Author: Jevgenijs Protopopovs

License: MIT License