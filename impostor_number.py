def iq_test(numbers):
  num = numbers.split()
  Odds=0
  Evens=0
  position = 0
  for i in range(0, len(num)):
    if(int(num[i]) % 2 == 0):
      Evens = Evens + 1
    else:
      Odds = Odds + 1
  if (Odds > Evens):
    for i in range(0, len(num)):
      if (int(num[i]) % 2 == 0):
        position = i+1
  else:
    for i in range(0, len(num)):
      if (int(num[i]) % 2 != 0):
        position=i+1
  print(f"The number that differs from the other is the one that is in the {position}° position \n") 

iq_test("1 26 3 27 27 13")
iq_test("1 1 2 1")
iq_test("8 6 0 3 12 28")
