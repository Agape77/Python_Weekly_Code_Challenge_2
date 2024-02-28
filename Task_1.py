numbers = input("Enter a list 0f integers separated by spaces: ").split() 
numbers = [int(num) for num in numbers] 
sum_of_numbers = sum(numbers) 
print("The sum of the integers in the list is:", sum_of_numbers)