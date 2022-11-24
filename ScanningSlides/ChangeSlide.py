# class that interacts with the USB Serial Relay.
# Sends commands to relay and it will energy to close the NO circuit to advance the projector carousel

# https://www.amazon.com/Buying-Dual-Channel-Microcontroller-Intelligent-Overcurrent/dp/B0B64TNS2C/
# (See reviews for better control scheme)

# ✮Instructions for use:
# 1. Connect the USB relay module to the computer, and install the driver for the CH340 USB to the serial port chip.
# 2. Open the serial port debugging software such as STC-ISP and SSCOM32, select the baud
# rate of 9600, and send A0 01 01 A2 and AO 02 01 A3 in hexadecimal (hex) format to open the first and second channels
# respectively. relay; send AO 01 00 A1 and AO 02 00 A2 in hexadecimal (hex) form to close the first and second
# relays respectively.
# ✮3. Relay status query: send FF in hexadecimal (hex) format to query, the data width returned by the serial port is 20 bytes (10 bytes for each channel), if the first channel is open, the second channel When it is off, querying the relay status will return: "CH1: ON IrInCH2: OFF In
# ✮LCS-2 type dual-channel 2-channel USB relay module: send in hexadecimal (hex) form, you can choose to send manually or automatically. Packing List: 2PCS Dual USB Relay Module

# Commands for relay operation (in HEX):

# Open 1st channel USB: A0 01 01 A2
# Close 1st channel USB: A0 01 00 A1
# Open 2nd channel USB: A0 02 01 A3
# Close 2nd channel USB: A0 02 00 A2

import time
import serial

# Serial takes these two parameters: serial device and baudrate. Check Device Manager for COM port#
ser = serial.Serial("COM4", 9600)

OUT_MSG_ON = b"\xA0\x01\x01\xA2"
OUT_MSG_OFF = b"\xA0\x01\x00\xA1"


def push_button_down() -> None:
    """Send to relay set of commands to advance the projector."""
    ser.write(OUT_MSG_ON)


def push_button_up() -> None:
    """Send to relay set of commands to advance the projector."""
    ser.write(OUT_MSG_OFF)
