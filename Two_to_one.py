def longest(s1, s2):
  string = (s1+s2).lower()
  string1 = "".join(set(string))
  string = sorted(string1)
  string = "".join(string)
  print(string)
longest("Tobias", "Llop")