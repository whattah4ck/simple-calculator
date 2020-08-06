# simple calculator
print ("Welcome to The Simple Calculator")
print ("write 2 numbers")
# we take 2 numbers
number=input("number 1:")
number2=input("number 2:")
floatnumber=float(number)
floatnumber2=float(number2)

print ("choose the process")
print (" addition = +\n subtract = -\n multiply = *\n divide   = /")
işlem = input("process:")

if işlem == "+":
    output=floatnumber+floatnumber2
if işlem == "-":
    output=floatnumber-floatnumber2
if işlem == "*":
    output=floatnumber*floatnumber2
if işlem == "/":
    output=floatnumber/floatnumber2
print ("that's it: "+str(output))    
