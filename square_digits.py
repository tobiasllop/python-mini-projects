import time
def main():
  #Square every digit of he number
  def square_digits(num):
    num = str(num)
    my_list = []
    for i in range(0, len(num)):
      square = int(num[i]) * int(num[i])
      #Create a list with the result of the squared digits
      my_list.append(str(square))
    #Join and print the list
    x = "" 
    print(x.join(my_list))  

  num = input("Insert a number with 2 or more digits: ")
  if len(num) < 2:
    print("Try again")
    time.sleep(1)
    #Go back
    return main()
  else:
    square_digits(num)

main()
