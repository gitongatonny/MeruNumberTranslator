import csv

def load_dataset(filename):
    dataset = {}
    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            number = int(row[0])
            meru_number = row[1]
            grammar = row[2]
            dataset[meru_number] = (number, grammar)
    return dataset

# Load the dataset from CSV
dataset = load_dataset('MeruNumbers.csv')

def analyze_meru_number(input_number, dataset):
    # Check if the input MeruNumber is a number word from 1 to 100
    if input_number in dataset:
        return dataset[input_number]

    # Check if the input MeruNumber has "na" keyword
    if 'na' in input_number:
        parts = input_number.split('na')
        if len(parts) == 2:
            hundreds = dataset[parts[0].strip()][0]
            tens = dataset[parts[1].strip()][0]
            corresponding_number = hundreds + tens
            tens_grammar = dataset[f"{tens}"][1]
            return corresponding_number, tens_grammar

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
        elif part.isdigit():
            number += int(part)
    grammar = grammar.strip()

    # Handle numbers above 100 using rule-based approach
    if number > 100:
        hundreds = number // 100
        tens = number % 100
        if tens == 0:
            return f"{hundreds} mia", ''
        else:
            tens_grammar = dataset[f"{tens}"][1]
            return f"{hundreds} mia na {tens}", tens_grammar
    else:
        return number, grammar

def run_meru_number_analyzer():
    # Get user input
    input_meru_number = input("Enter a MeruNumber: ")

    # Analyze the MeruNumber
    number, grammar = analyze_meru_number(input_meru_number, dataset)
    print(f"The NumberEquivalent for {input_meru_number} is: {number} ({grammar})")

run_meru_number_analyzer()