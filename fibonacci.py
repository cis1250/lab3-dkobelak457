#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.


while True:
  try:
    n = int(input("How many Fibonacci Sequence intergers do you want: "))
    if n > 0
      break
    else: 
      print("Please choose a positive integer.")
  except ValueError:
    print("Please enter a positive integer. ")
a, b = 0, 1
result = []
for _ in range(n):
    result.append(a)
    a, b = b, a + b
print(" ".join(map(str, result)))
    
    
