f = open("words.txt", "r")

# Initialize variables. words is initialized to 1 to account for the first word.
words = 1
chars = 0

# Add flag to make sure that variable lengths of spacing is accounted for.
triggered = False

# Enter read loop. Stream every character in individually and do logic.
while True:
    # Read character and break if end of file is reached.
    char = f.read(1)
    if len(char) == 0: break

    # If character is a space, newline, or tab, trigger the space status.
    if char == " " or char == "\n" or char == "\t":
        if triggered: continue
        triggered = True
        continue
    # Make sure carriage returns don't count as characters.
    if (char == "\r"): continue

    # If character is normal character, add 1 to character count.
    chars += 1
    # If the normal character is the beginning of a word, increment the word count and reset flag.
    if triggered:
        words += 1
        triggered = False

# Output.
print("Number of words: " + str(words))
print("Number of characters: " + str(chars))