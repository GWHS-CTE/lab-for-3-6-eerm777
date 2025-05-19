my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
temp_list = []

for number in my_list:
    if number not in temp_list:
        temp_list.append(number)
print("The list with unique elements only:")
print(temp_list)

