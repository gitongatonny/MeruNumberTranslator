import csv
import re

# Load the dataset from CSV
def load_dataset(filename):
    dataset = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            number = int(row[0])
            meru_number = row[1]
            grammar = row[2]
            morphemes = re.findall(r'\b\w+\b', meru_number)
            dataset[number] = (meru_number, grammar, morphemes)
            dataset[meru_number] = (number, grammar)
    return dataset

dataset = load_dataset('MeruNumbers.csv')

# Analyze a MeruNumber
def analyze_meru_number(input_number, dataset):
    if input_number in dataset:
        # Number is in the dataset
        return dataset[input_number]

    # Check if the input MeruNumber is a number word from 1 to 10
    if input_number in dataset.values():
        for number, (meru_number, grammar) in dataset.items():
            if input_number == meru_number:
                return number, grammar

    # Check if the input MeruNumber has "na" keyword
    if 'na' in input_number:
        parts = input_number.split('na')
        if len(parts) == 2:
            hundreds = dataset[parts[0].strip()][0]
            tens = dataset[parts[1].strip()][0]
            corresponding_number = hundreds + tens
            return corresponding_number, ''

    # No "na" keyword, analyze MeruNumber
    parts = input_number.split()
    number = 0
    grammar = ''
    for part in parts:
        part = part.strip()
        if part in dataset:
            part_number, part_grammar = dataset[part]
            number += part_number
            grammar += part_grammar + ' '
    grammar = grammar.strip()
    return number, grammar

# Convert a number to its MeruNumber representation
def convert_to_meru_number(input_number, dataset):
    if input_number in dataset:
        # Number is in the dataset
        return dataset[input_number][0]

    if input_number >= 200:
        hundreds = input_number // 100
        remainder = input_number % 100
        if remainder == 0:
            meru_number = f"{dataset[hundreds][0]} {dataset[100][0]}"
        else:
            tens = remainder // 10
            ones = input_number % 10
            if tens == 0:
                meru_number = f"{dataset[hundreds][0]} {dataset[100][0]} {dataset[ones][0]}"
            else:
                meru_number = f"{dataset[hundreds][0]} {dataset[100][0]} {dataset[tens * 10][0]} na {dataset[ones][0]}"
        return meru_number

    if input_number < 100:
        # Numbers from 1 to 99
        tens = input_number // 10
        ones = input_number % 10
        meru_number = f"{dataset[tens * 10][0]} {dataset[ones][0]}"
        return meru_number

    if 100 <= input_number < 200:
        tens = (input_number % 100) // 10
        ones = input_number % 10
        if tens == 0:
            meru_number = f"{dataset[100][0]} {dataset[ones][0]}"
        else:
            meru_number = f"{dataset[100][0]} {dataset[tens * 10][0]} na {dataset[ones][0]}"
        return meru_number

# Run the program
while True:
    print("Welcome to the Meru Number Converter! /n")
    print("Choose an option:")
    print("1. Convert a Digit number to its equivalent MeruNumber Translation")
    print("2. Convert a MeruNumber to its equivalent number in Digits form")
    print("3. Quit")

    choice = input("Enter your choice: ")
    print("\n")  


    if choice == '1':
        input_number = int(input("Enter a number: "))
        meru_number = convert_to_meru_number(input_number, dataset)
        print(f"The MeruNumber for {input_number} is: {meru_number} ({grammar})")
        print("\n")

    elif choice == '2':
        input_meru_number = input("Enter a MeruNumber: ")
        number, grammar = analyze_meru_number(input_meru_number, dataset)
        print(f"The NumberEquivalent for {input_meru_number} is: {number} ({grammar})")
        print("\n")

    elif choice == '3':
        print("Thank you for using Meru Number Translator!💯")
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
        print("\n")
