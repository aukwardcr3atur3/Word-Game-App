import random

# Function to load the wordlist
def load_wordlist():
    # Load your wordlist of one billion words here
    # This could involve reading from a file or a database
    wordlist = []
    # Code to load the wordlist goes here
    return wordlist

# Function to generate a random word from the wordlist
def generate_word(wordlist):
    return random.choice(wordlist)

# Function to calculate word bonus based on length
def calculate_word_bonus(word):
    bonus = len(word) * 10
    return bonus

# Function to play a level
def play_level(level, wordlist):
    word = generate_word(wordlist)
    print(f"Level {level}")
    print("Unscramble the word:", ''.join(random.sample(word, len(word))))
    
    user_word = input("Enter your answer: ").lower()
    
    if user_word == word:
        word_bonus = calculate_word_bonus(word)
        coins = level * 5
        print("Congratulations! You unscrambled the word correctly!")
        print(f"You earned a word bonus of {word_bonus} and {coins} coins.")
    else:
        print("Oops! Incorrect answer. Try again!")

# Main game loop
def main():
    print("Welcome to the Word Game!")
    print("Each level presents a scrambled word to unscramble.")
    print("Earn word bonuses and coins for every correct answer.")
    
    wordlist = load_wordlist()
    
    for level in range(1, 20001):
        play_level(level, wordlist)
        print("--------------------")
    
    print("Game Over!")

# Run the game
main()