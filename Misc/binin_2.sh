#!/bin/python3
import pyperclip
def a(a) -> str:
	x = ""
	str(a)
	for i in a:
		x+=i+"\t"
		pyperclip.copy(x)
while True:
	a(input("Enter your bin number to split into tabs for excel: "))
