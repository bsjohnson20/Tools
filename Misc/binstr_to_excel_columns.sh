#!/bin/python3
import sys
arguments = sys.argv
import pyperclip
def a(a) -> str:
	x = ""
	str(a)
	for i in a:
		x+=i+"\t"
		pyperclip.copy(x)
if len(arguments)==0:
	a(arguments[1])
else:
	while True:
		a(input("INPUT BIN: "))
