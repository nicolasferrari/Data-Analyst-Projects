import read
df = read.load_data()
import string 
import collections

head_line = df['headline'].tolist()

# In the next step, I will find which word appear more often in the headlines. First I iterate to join the headlines columns into a longer string and then split them by the separate space

string = ''
for item in head_line:
    string += (str(item) + ' ')
# Split the whole string into sperate words. This will end up with a list of words.
list_words = string.split()

# The string list_words is a long string with all the headlines together. Use list comprehension to convert all the words in list_words into lowercase. 

list_words = [word.lower() for word in list_words]

# Count up how many times each word occurs in the list. For this I use the Counter class.
count_words = collections.Counter(list_words)

# Print the 100 words that occur the most times    
print(count_words.most_common(100))  
# This will return a list of tuples with two items in each tuple. The first is the word, and the second the number of times that word appear in headline.
