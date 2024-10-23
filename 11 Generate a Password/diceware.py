import random
import secrets

def generate_passphrase(num_words, wordlist_path='diceware.wordlist.asc'):
    with open(wordlist_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()[2:7778]
        word_list = [line.split()[1] for line in lines]
    #secrets is better than normal random because it is cryptographically secure and harder to predict the next number generated by it 
    words = [secrets.choice(word_list) for i in range(num_words)]
    return ' '.join(words)


def simulate_dice_roll():
    return ''.join(str(random.randint(1, 6)) for _ in range(5))
def generate_passphrase2(dice_rolls, wordlist_path='diceware.wordlist.asc'):
    # Read the wordlist and create a mapping of dice rolls to words
    with open(wordlist_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()[2:7778]  # Adjust this based on your actual file structure
        word_list = {line.split()[0]: line.split()[1] for line in lines}  # Mapping of dice rolls to words

    # Retrieve words based on provided dice rolls
    words = [word_list.get(roll, 'UNKNOWN') for roll in dice_rolls]  # Use 'UNKNOWN' if roll is not found
    return ' '.join(words)
def genpassphrase2(num_words):
    # Generate a list of dice rolls
    dice_rolls = [simulate_dice_roll() for _ in range(num_words)]

    # Generate a passphrase based on the dice rolls
    return generate_passphrase2(dice_rolls)
# commands used in solution video for reference
if __name__ == '__main__':
    print(generate_passphrase(7))
    print(genpassphrase2(7))
