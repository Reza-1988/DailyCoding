import pandas as pd


# Read data from csv file with pandas library
df = pd.read_csv('nato_phonetic_alphabet.csv')

# Create a dictionary from csv file
nato_phonetic_dict = {row.letter:row.code for (index, row) in df.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    try:
        user_word = input('Enter a word: ').upper()
        output_list = [nato_phonetic_dict[letter] for letter in user_word]
    except KeyError:
        print('Sorry, only letters a-z are allowed.')
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()