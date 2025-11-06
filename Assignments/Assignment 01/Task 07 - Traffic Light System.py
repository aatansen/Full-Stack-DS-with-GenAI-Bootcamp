"""
### Task 07 - Traffic Light System

- Ask the user to input a color (`red`, `yellow`, or `green`).
Print:
  - "`Stop`" for `red`
  - "`Ready to go`" for `yellow`
  - "`Go`" for `green`
  - "`Invalid color`" otherwise
"""

color = input("Enter color between :`red`, `yellow`, or `green`")

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Ready to go")
elif color == "green":
    print("Go")
else:
    print("Invalid color")
