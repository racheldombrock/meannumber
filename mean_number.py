n_numbers = input("How many numbers will be given? ")
while not n_numbers.isnumeric():
    n_numbers = input("That's not a number! Try again: ")
n_numbers = int(n_numbers)

sum = 0
counter = 0

while counter<n_numbers:
  current_number = input("Provide a number:")
  while not current_number.isnumeric():
    current_number=input("That's not a number! Try again: ")
  sum=int(current_number)+sum
  counter+=1

print("The mean of the numbers you provided is ",(sum/counter),".")