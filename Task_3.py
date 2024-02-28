person_info ={} 
person_info['name'] = input("Enter your name: ") 
person_info['age'] = input("Enter your age: ") 
person_info['favorite_colour'] = input("Enter your favourite colour: ")   
 
print("Information about the person: ")
for key, value in person_info.items(): 
    print(key.capitalize() + ":", value)