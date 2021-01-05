s1 = str(input("Insert one random word: "))
s2 = str(input("Insert another random word: "))
def longest(s1, s2):
  string = (s1+s2).lower()
  string1 = "".join(set(string))
  string = sorted(string1)
  string = "".join(string)
  print(f"Your two to one word is: {string}")

longest(s1, s2)
