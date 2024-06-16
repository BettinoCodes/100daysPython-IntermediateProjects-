student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
user_name = input("What is your name: ")

nato_phonetic = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_dict = {row.letter: row.code for (k, row) in nato_phonetic.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

first_let = [x.upper() for x in user_name]
li = [nato_dict[x] for x in first_let if nato_dict.get(x)]

print(li)
