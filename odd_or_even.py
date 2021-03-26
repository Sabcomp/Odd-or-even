# Input
def odd_or_even():
  num = int(input("What number are you thinking?"))
  if num % 2 == 0:
    print("That's an even number!")
  else:
    print("That's an odd number!") 
odd_or_even()
question = input("Have another?")
while question == 'Y' or question != 'y':
  odd_or_even()
else:
  print("Have a good day!)
