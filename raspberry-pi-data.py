#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess, re, locale

locale.setlocale(locale.LC_ALL, "")

def freq():
	"""in Hz"""
	return locale.format(
	"%d", int(
	re.search(r'.*frequency\(\d*\)=(.*)',
	subprocess.check_output(["vcgencmd", "measure_clock", "arm"]).replace("\n", "")).group(1)),
	grouping=True) + " Hz"
		
def temp():
	"""in °C """
	return re.search(r'.*temp=(.*)', subprocess.check_output(["vcgencmd", "measure_temp"]).replace("\n", "")).group(1).replace("'C", "°C")
		
def volt():
	"""in Volt"""
	return re.search(r'.*volt=(.+V)', subprocess.check_output(["vcgencmd", "measure_volts"]).replace("\n", "")).group(1)
