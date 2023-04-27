# File: main.py
import commands

commands.load()

while True:
  masukan = input(">>> ")
  commands.run(masukan)
  