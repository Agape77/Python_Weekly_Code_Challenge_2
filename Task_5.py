word_list = ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Diani Beach", "Malindi", "Eldoret"]

#Use list comprehension to create a new list with words that have an odd number of characters
odd_length_words = [word for word in word_list if len(word) % 2 != 0]

#print new list
print("Words with odd number of characters:", odd_length_words)