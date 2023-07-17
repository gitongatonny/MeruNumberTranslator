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
            dataset[meru_number] = (number, grammar, morphemes)
    return dataset

dataset = load_dataset('MeruNumbers.csv')

# Analyze a MeruNumber
def analyze_meru_number_recursive(input_number, dataset, cache=None):
    if cache is None:
        cache = {}

    if input_number in cache:
        return cache[input_number]

    if input_number in dataset:
        # Number is in the dataset
        result = dataset[input_number]
    elif input_number in dataset.values():
        for number, (meru_number, grammar, morphemes) in dataset.items():
            if input_number == meru_number:
                result = number, grammar, morphemes
                break
        else:
            result = None
    elif 'na' in input_number:
        parts = input_number.split('na')
        if len(parts) == 2:
            hundreds = analyze_meru_number_recursive(parts[0].strip(), dataset, cache)[0]
            tens = analyze_meru_number_recursive(parts[1].strip(), dataset, cache)[0]
            corresponding_number = hundreds + tens
            result = corresponding_number, '', dataset[hundreds][2] + dataset[tens][2]
        else:
            result = None
    else:
        parts = input_number.split()
        number = 0
        grammar = ''
        morphemes = []
        for part in parts:
            part = part.strip()
            if part in dataset:
                part_number, part_grammar, part_morphemes = analyze_meru_number_recursive(part, dataset, cache)
                number += part_number
                grammar += part_grammar + ' '
                morphemes.extend(part_morphemes)
        grammar = grammar.strip()
        result = number, grammar, [m for m in morphemes if m != 'na']  # Filter out 'na' from morphemes

    cache[input_number] = result
    return result

def analyze_meru_number(input_number, dataset):
    return analyze_meru_number_recursive(input_number, dataset)

def convert_to_meru_number_recursive(input_number, dataset, cache=None):
    if cache is None:
        cache = {}

    if input_number in cache:
        return cache[input_number]

    if input_number in dataset:
        # Number is in the dataset
        result = dataset[input_number]
    elif input_number >= 200:
        hundreds = input_number // 100
        remainder = input_number % 100
        if remainder == 0:
            meru_number = f"{convert_to_meru_number_recursive(hundreds, dataset, cache)} {dataset[100][0]}"
            grammar = f"{dataset[hundreds][1]} {dataset[100][1]}"
            morphemes = dataset[hundreds][2] + dataset[100][2]
        else:
            tens = remainder // 10
            ones = input_number % 10
            if tens == 0:
                meru_number = f"{convert_to_meru_number_recursive(hundreds, dataset, cache)} {dataset[100][0]} {convert_to_meru_number_recursive(ones, dataset, cache)}"
                grammar = f"{dataset[hundreds][1]} {dataset[100][1]} {dataset[ones][1]}"
                morphemes = dataset[hundreds][2] + dataset[100][2] + dataset[ones][2]
            else:
                meru_number = f"{convert_to_meru_number_recursive(hundreds, dataset, cache)} {dataset[100][0]} {convert_to_meru_number_recursive(tens * 10, dataset, cache)} na {convert_to_meru_number_recursive(ones, dataset, cache)}"
                grammar = f"{dataset[hundreds][1]} {dataset[100][1]} {dataset[tens * 10][1]} na {dataset[ones][1]}"
                morphemes = dataset[hundreds][2] + dataset[100][2] + dataset[tens * 10][2] + dataset[ones][2]
        result = meru_number, grammar, morphemes
    elif input_number < 100:
        tens = input_number // 10
        ones = input_number % 10
        meru_number = f"{convert_to_meru_number_recursive(tens * 10, dataset, cache)} {convert_to_meru_number_recursive(ones, dataset, cache)}"
        grammar = f"{dataset[tens * 10][1]} {dataset[ones][1]}"
        morphemes = dataset[tens * 10][2] + dataset[ones][2]
        result = meru_number, grammar, morphemes
    elif 100 <= input_number < 200:
        tens = (input_number % 100) // 10
        ones = input_number % 10
        if tens == 0:
            meru_number = f"{convert_to_meru_number_recursive(100, dataset, cache)} {convert_to_meru_number_recursive(ones, dataset, cache)}"
            grammar = f"{dataset[100][1]} {dataset[ones][1]}"
            morphemes = dataset[100][2] + dataset[ones][2]
        else:
            meru_number = f"{convert_to_meru_number_recursive(100, dataset, cache)} {convert_to_meru_number_recursive(tens * 10, dataset, cache)} na {convert_to_meru_number_recursive(ones, dataset, cache)}"
            grammar = f"{dataset[100][1]} {dataset[tens * 10][1]} na {dataset[ones][1]}"
            morphemes = dataset[100][2] + dataset[tens * 10][2] + dataset[ones][2]
        result = meru_number, grammar, morphemes

    cache[input_number] = result
    return result

def convert_to_meru_number(input_number, dataset):
    return convert_to_meru_number_recursive(input_number, dataset)

print()
print("Welcome to the Meru Number Converter!🎉")
print()

def run_program():
    print("Choose an option:")
    print("1. Convert a digit to its MeruNumber")
    print("2. Convert a MeruNumber to its digit")
    print("3. Quit")

    choice = input("Enter your choice: ")
    print()

    if choice == '1':
        input_number = int(input("Enter a number: "))
        meru_number, grammar, morphemes = convert_to_meru_number(input_number, dataset)
        meru_number_phrase = ' '.join([str(item) for item in meru_number if not isinstance(item, tuple) and item != 'na'])
        grammar_phrase = ' '.join([str(item) for item in grammar.split(' ') if item != 'na'])
        morphemes_list = [m for m in morphemes if m != 'na']
        print(f"The MeruNumber for {input_number} is: {meru_number_phrase}")
        print(f"Grammar: {grammar_phrase}")
        print(f"Morphemes: {', '.join(morphemes_list)}")
        print()
        run_program()

    elif choice == '2':
        input_meru_number = input("Enter a MeruNumber: ")
        number, grammar, morphemes = analyze_meru_number(input_meru_number, dataset)
        print(f"The Digit Equivalent for {input_meru_number} is: {number}")
        print(f"Grammar: {grammar}")
        print(f"Morphemes: {', '.join(morphemes)}")
        print()
        run_program()

    elif choice == '3':
        print("Thank you for using Meru Number Translator!💯")
        print("Exiting...")

    else:
        print("Invalid choice. Please try again.")
        print()
        run_program()

# Run the program
run_program()

