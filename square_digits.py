import time
def main():
  def square_digits(num):
    num = str(num)
    my_list = []
    for i in range(0, len(num)):
      square = int(num[i]) * int(num[i])
      my_list.append(str(square))
    x = "" 
    print(x.join(my_list))  

  num = input("Insert a number with 2 or more digits: ")
  if len(num) < 2:
    print("Try again")
    time.sleep(1)
    return main()
  else:
    square_digits(num)

main()
