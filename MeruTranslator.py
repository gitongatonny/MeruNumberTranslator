import csv
import re

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

# Load the dataset from CSV
dataset = load_dataset('MeruNumbers.csv')

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
    return number, grammar, dataset[number][2]

def run_meru_number_analyzer():
    while True:
        # Get user input
        print("Choose an option:")
        print("1. Translate a number to Meru")
        print("2. Translate a Meru number to a number")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            input_number = int(input("Enter a number: \n"))

            # Analyze the Meru number
            meru_number, grammar, morphemes = analyze_meru_number(input_number, dataset)
            print(f"The Meru number for {input_number} is: {meru_number} ({grammar}) \n")
            print(f"Morphemes: {', '.join(morphemes)} \n")

        elif choice == "2":
            input_meru_number = input("Enter a MeruNumber: \n")

            # Analyze the MeruNumber
            number, grammar = analyze_meru_number(input_meru_number, dataset)
            print(f"The NumberEquivalent for {input_meru_number} is: {number} ({grammar}) \n")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again. \n")

run_meru_number_analyzer()
