numbers = [1,1,1,2,3,3,3,4,4,4,4,5,5,5,5,5,6]

number_dict = {}

for number in numbers:
  if number in number_dict:
    number_dict[number] = number_dict[number] + 1 
  else:
    number_dict[number] = 1
print(number_dict)

###############

#{1: 3, 2: 1, 3: 3, 4: 4, 5: 5, 6: 1}
