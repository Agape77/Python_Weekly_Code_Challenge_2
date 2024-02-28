set1 = set(input("Enter integers for set 1 separated by spaces: ").split()) 
set2 = set(input("Enter integers for set 2 separated by spaces: ").split()) 
 
#Create a new set containing only the elements that are common to both sets
common_elements = set1.intersection(set2)

#print new set
print("Common elements: ",common_elements)