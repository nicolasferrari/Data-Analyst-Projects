import read
df = read.load_data()
import string 
import collections

head_line = df['headline'].tolist()

# Found which word appear often in the headlines. First I iterate to join the headlines into a longer string and then split them by the separate space
string = ''
for item in head_line:
    string += (str(item) + ' ')
# Split the whole string into sperate words
list_words = string.split()

# convert all the words in list_words into lowercase. For this I use list comprehension
list_words = [word.lower() for word in list_words]

# Count up how many times each word occurs in the list
count_words = collections.Counter(list_words)
for key,value in count_words.items():
    print(key,":",value)

# print the 100 words that occur the most times    
print(count_words.most_common(100))  
