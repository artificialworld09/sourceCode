while True:
  inp = input("Enter your word: ").lower()
  if inp == "exit":
    break
  elif "hello" in inp:
    print("\tHello sir, how are you?")
  elif "hi" in inp:
    print("\tHello sir, how are you?")
  elif "your name" in inp:
    print("\tMy name is Alexa")
  elif "how are you" in inp:
    print("\tI'm doing well")
  elif "who are you" in inp:
    print("\tI'm a Python program, my name is Alexa")
  elif "how old are you" in inp:
    print("\tI'm 12 years old")
  elif "m fine" in inp:
    pass
  elif inp == "fine":
    pass
  else:
    print("\tinvalid input")