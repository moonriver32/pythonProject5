rating = [1, 2, 3, 4]
number = int(input("Введите номер любого натурального числа"))
rating.append(number)
list.sort(rating)
print(rating[::-1])
