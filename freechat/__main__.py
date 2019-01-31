from udpinput import UDPInput
import sys

print("Starting freechat")

if len(sys.argv) != 2:
	port = 1189
else:
	port = sys.argv[1]

listener = UDPInput(port)

while True:
	message = listener.getMsg()
	parsed_message = f"{message[0]}: {message[1]}"
	print(parsed_message)