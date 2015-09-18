## eHealth

In order to use this sketch there is need to install additional libraries to Arduino. This libraries can be found in [this guide](https://www.cooking-hacks.com/documentation/tutorials/ehealth-biometric-sensor-platform-arduino-raspberry-pi-medical) (or use the [direct download link](https://www.cooking-hacks.com/media/cooking/images/documentation/e_health_v2/eHealth_arduino_v2.4.zip)). Go to the "Using the library with Arduino" section in the guide for installing instructions.

Trying compiling the sketch will cause an error so there is need to do [one more step](https://ainiazmi88.wordpress.com/2015/03/19/error-compiling-ehealthdisplay-library/) ->

Add to the beginning of the eHealthDisplay.h file inside the arduino eHealth library (in the Mac the path is /Users/USERNAME/Documents/Arduino/libraries/eHealth):

```c
#ifndef prog_uint8_t
#define prog_uint8_t const uint8_t
#endif
```

Now, just open `eHealth.ino` in Arduino IDE, upload it to the Arduino and the eHealth sensors' data will be sent in JSON format (with checksum) on the serial port.

## Sensirion

Run `./sensirion.py` and sensors' data will be printed