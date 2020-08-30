f = open("words.txt", "r")
text = f.read()

char_list = []
for char in text:
    char_list.append(char)

word_list = []
word = text.split(" ")
numword = str(len(word))

numchar = str(len(char_list))
print("Number of characters: " + numchar)
print("Number of words: " + numword)