a = ['SHannu', 'vAibhav', 'shridhar', 'heamaNNthU']
l = [ch for word in a for ch in word if ch.isupper()]
print(l) 

# Create a list of all uppercase words from a given list.
words = ['HELLO', 'World', 'PYTHON', 'is', 'FUN']
uppercase_words = [word for word in words if word.isupper()]
print(uppercase_words) # ['HELLO', 'PYTHON', 'FUN']

# Given a list of words create a list with words that starts with a vowel.
words = ['apple', 'banana', 'Orange', 'grape', 'umbrella', 'Egg']
vowel_words = [word for word in words if word[0].lower() in 'aeiou']
print(vowel_words) # ['apple', 'Orange', 'umbrella', 'Egg']

# Given a list of strings create a new list that contains the string and its length.
words = ['apple', 'banana', 'cherry', 'kiwi']
word_lengths = [(word, len(word)) for word in words]
print(word_lengths) # [('apple', 5), ('banana', 6), ('cherry', 6), ('kiwi', 4)]
