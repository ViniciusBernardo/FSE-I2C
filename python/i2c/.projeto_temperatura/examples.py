# requires RPi_I2C_driver.py
import RPi_I2C_driver
from time import *
import smbus2
import bme280

mylcd = RPi_I2C_driver.lcd()

porta_i2c = 1
endereco = 0x76
bus = smbus2.SMBus(porta_i2c)

calibracao_paramentros = bme280.load_calibration_params(bus, endereco)

arquivo = open("meidcoes.txt", "w+")

contador = 0

while True:

	dado = bme280.sample(bus, endereco, calibracao_paramentros)

	# mylcd.lcd_display_string("Temperatura: ", 1)
	# mylcd.lcd_display_string(str(dado.temperature), 2)

	temperatura = "Temp. " + "{:.2f}".format(dado.temperature)
	umidade = "Umid. " + "{:.2f}".format(dado.humidity)

	mylcd.lcd_display_string(temperatura, 1)
	mylcd.lcd_display_string(umidade, 2)

	sleep(5)

	contador = contador + 1
	if(contador == 12):
		saida = str(dado.timestamp) + ", " +  "{:.2f}".format(dado.temperature) + ", " + "{:.2f}".format(dado.humidity)
		arquivo.write("%s\n" % saida)
		print(saida)
		contador = 0
