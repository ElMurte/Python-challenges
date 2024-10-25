#solution proposed in the video
def sort_words(words):
    return ' '.join(sorted(words.split(), key=str.casefold))
#solution with no libraries (using lists)
#lists, sort,case insensitive
#insert properly check where to insert the word
def insert_properly(finalwords, word):
    inserted = False
    for i in range(len(finalwords)):
        if finalwords[i].lower() >= word.lower():
            finalwords.insert(i, word)  # Insert the word in the correct position
            inserted = True
            break
    if not inserted:
        finalwords.append(word)  # If not inserted, append it at the end

def sort_words2(words):
    finalwords = []
    start = None
    for i in range(len(words)):
        if words[i] == ' ':
            if start is not None:
                insert_properly(finalwords, words[start:i])
            start = None  # Reset start after space
        else:
            if start is None:  # Mark the start of a word
                start = i

    # Add the last word (if any) after the loop finishes
    if start is not None:
        insert_properly(finalwords, words[start:])

    return finalwords
# commands used in solution video for reference
if __name__ == '__main__':
    print(sort_words2('banana ORANGE apple'))  # apple banana ORANGE
