import re
import collections


def count_words(path):
    #open file in read mode
    #encoding may be incorrect on the language of the text
    with open(path, 'r', encoding='utf-8') as file:
        all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        all_words = [word.upper() for word in all_words]
        print(f'\nTotal Words: {len(all_words)}')

        word_counts = collections.Counter(all_words)

        print('\nTop 20 Words:')
        for word in word_counts.most_common(20):
            print(f'{word[0]}\t{word[1]}')


# commands used in solution video for reference
if __name__ == '__main__':
    count_words('shakespeare.txt')
def count_words2(path):
    # Open the file in read mode with UTF-8 encoding
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
        
        # Manual word extraction (keeping only alphanumeric characters, hyphens, and apostrophes)
        word = ''
        all_words = []
        
        for char in text:
            if char.isalnum() or char in "-'":  # Keep letters, numbers, hyphens, and apostrophes
                word += char
            else:
                if word:
                    all_words.append(word.upper())
                    word = ''
        
        # Capture the last word if file doesn't end with a non-word character
        if word:
            all_words.append(word.upper())

        # Total words
        print(f'\nTotal Words: {len(all_words)}')

        # Manually count word occurrences using a dictionary
        word_counts = {}
        for word in all_words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

        # Sort words by their count in descending order
        sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)

        # Print top 20 words
        print('\nTop 20 Words:')
        for word, count in sorted_word_counts[:20]:
            print(f'{word}\t{count}')


# commands used in solution video for reference
if __name__ == '__main__':
    count_words2('shakespeare.txt')
