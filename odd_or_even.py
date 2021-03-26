while True:
  num = int(input("What number are you thinking? "))
  
  # Test for parity
  if num % 2 == 0:
    print("That's an even number!")
  else:
    print("That's an odd number!")
  
  # Deciding whether to continue the program
  question = input("Have another? ")
  if question == 'N' or question == 'n':
    break

# The Greeting
print("Have a lovely day!")
