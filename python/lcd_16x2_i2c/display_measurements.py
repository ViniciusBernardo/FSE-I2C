# requires RPi_I2C_driver.py
import RPi_I2C_driver
from time import *
import smbus2
import bme280

porta_i2c = 1
endereco = 0x76
bus = smbus2.SMBus(porta_i2c)

calibracao_paramentros = bme280.load_calibration_params(bus, endereco)

mylcd = RPi_I2C_driver.lcd()
mylcd.lcd_clear()
while True:
    dado = bme280.sample(bus, endereco, calibracao_paramentros)

    temperature = round(dado.temperature, 2)
    humidity = round(dado.humidity, 2)
    pressure = round(dado.pressure, 2)

    mylcd.lcd_display_string(f"P: {pressure} hPa", 1)
    mylcd.lcd_display_string(f"U{humidity}% T{temperature}C", 2)

    sleep(1) # 1 sec delay
