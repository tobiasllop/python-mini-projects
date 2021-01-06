import time

#Write the text as a typewriter
def writer(string):
  for char in string:
    print(char, end="", flush=True)
    time.sleep(.10)
  time.sleep(.20)

string = 'Hi there! \n'
writer(string)
string = "This is a binnary sumation calculator. You must insert two decimal numbers and I will return the result in binary.\n"
writer(string)
string = "Did you understand? "
writer(string)
yes_no = input()
string = "Okay here we go!\n"
writer(string)
string = "Insert the first number: " 
writer(string)
a=int(input())
string = "Insert the second number: "
writer(string)
b=int(input())

#Sum the two decimal numbers and print the result in binary
def add_binary(a,b):
    number = a+b
    binary = bin(number)
    binary = binary.replace("b", "")
    string = (f"The result is: {binary}")
    writer(string)

add_binary(a, b) #Call the function