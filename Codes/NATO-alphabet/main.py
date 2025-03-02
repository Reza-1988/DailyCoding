import pandas as pd


df = pd.read_csv('nato_phonetic_alphabet.csv')

# Create a dictionary from csv file
nato_phonetic_dict = {row.letter:row.code for (index, row) in df.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
user_word = input('Enter a word: ').upper()
output_list = [nato_phonetic_dict[letter] for letter in user_word if letter in nato_phonetic_dict.keys()]
print(output_list)

