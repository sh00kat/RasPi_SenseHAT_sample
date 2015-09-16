#!/usr/bin/python
# -*- coding: utf-8 -*-
from sense_hat import SenseHat
import sys
import codecs
import math

sense = SenseHat()
sense.set_rotation(180)
red = (255, 0, 0)
green = (0, 255, 0)

humidity = sense.get_humidity()
temp = sense.get_temperature()
temp_from_humidity = sense.get_temperature_from_humidity()
temp_from_pressure = sense.get_temperature_from_pressure()
pressure = sense.get_pressure()

# LEDに気温を表示
sense.show_message("Temp is " + str(math.floor(temp)) + "C", text_colour=green)

sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
print(u"湿度: %s %%rH" % humidity)
print(u"気温: %s C" % temp)
print(u"気温(湿度センサーから取得): %s C" % temp_from_humidity)
print(u"気温(気圧センターから取得): %s C" % temp_from_pressure)
print(u"気圧: %s Millibars" % pressure)

# こう書いても取得できる
#print(sense.humidity)
#print(sense.temp)
#print(sense.temperature)
#print(sense.pressure)

