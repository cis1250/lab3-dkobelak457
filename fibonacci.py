#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.


while True:
  try:
    n = int(input("How many Fibonacci Sequence intergers do you want: "))
    if n > 0:
      break
    else: 
      print("Please choose a positive integer.")
# try and value error used to check if the input is a integer 
  except ValueError:
    print("Please enter a positive integer. ")


a, b = 0, 1

result = []
#values are held in the result string and printed later
for _ in range(n):
    result.append(a)
    a, b = b, a + b

#all lines are converted to a string and printed out in a single line in the terminal
print(" ".join(map(str, result)))
    
    
