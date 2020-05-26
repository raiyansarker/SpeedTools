from time import sleep
import sys
import time
from answer import a, t, d, u, v

# Logo
print("███████ ██████  ███████ ███████ ██████      ████████  ██████   ██████  ██      ███████ ")
print("██      ██   ██ ██      ██      ██   ██        ██    ██    ██ ██    ██ ██      ██      ")
print("███████ ██████  █████   █████   ██   ██        ██    ██    ██ ██    ██ ██      ███████ ")
print("     ██ ██      ██      ██      ██   ██        ██    ██    ██ ██    ██ ██           ██ ")
print("███████ ██      ███████ ███████ ██████         ██     ██████   ██████  ███████ ███████ ")
print(".......................................................................................")

# Welcome message
message = "\033[1;31;49mThe tool is starting!.............." + "\n"
for char in message:
    sleep(0.2)
    sys.stdout.write(char)
    sys.stdout.flush()

# Array to get desired query
options = ["(1) Acceleration", "(2) Time", "(3) Distance", "(4) First Momentum", "(5) Last Momentum"]

for x in options:
    time.sleep(0.3)
    print("\033[1;34;49m"+x)

# Break
print("\n")

try:
    # Guery
    query = float(input("\033[1;31;49mWhat you want to know? - "))

    # Get the program
    if query == 1:
        print("\033[1;34;49mThe acceleration is " + str(a()) + "m/s\u00b2")
    elif query == 2:
        print("\033[1;34;49mThe time is " + str(t()) + "s")
    elif query == 3:
        print("\033[1;34;49mThe distance is " + str(d()) + "m")
    elif query == 4:
        print("\033[1;34;49mThe first momentum is " + str(u()) + "m/s")
    elif query == 4:
        print("\033[1;34;49mThe last momentum is " + str(v()) + "m/s")
    else:
        print("Something went wrong")
except ValueError:
    print("Select a number")