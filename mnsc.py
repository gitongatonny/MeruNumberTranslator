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

# Convert a MeruNumber to a digit
def convert_to_digit_recursive(input_number, dataset, cache=None):
    if cache is None:
        cache = {}

    if input_number in cache:
        return cache[input_number]

    if input_number in dataset:
        # Number is in the dataset
        result = dataset[input_number][0]
    elif input_number in dataset.values():
        for number, (meru_number, grammar, morphemes) in dataset.items():
            if input_number == meru_number:
                result = number
                break
        else:
            result = None
    elif 'na' in input_number:
        parts = input_number.split('na')
        if len(parts) == 2:
            hundreds = convert_to_digit_recursive(parts[0].strip(), dataset, cache)
            tens = convert_to_digit_recursive(parts[1].strip(), dataset, cache)
            corresponding_number = hundreds + tens
            result = corresponding_number
        else:
            result = None
    else:
        parts = input_number.split()
        number = 0
        for part in parts:
            part = part.strip()
            if part in dataset:
                part_number = convert_to_digit_recursive(part, dataset, cache)
                number += part_number
        result = number

    cache[input_number] = result
    return result

def convert_to_digit(input_number, dataset):
    return convert_to_digit_recursive(input_number, dataset)

def convert_to_meru_number_recursive(input_number, dataset, cache=None):
    if cache is None:
        cache = {}

    if input_number in cache:
        return cache[input_number]

    if input_number in dataset:
        # Number is in the dataset
        result = dataset[input_number]
    elif input_number >= 100:
        hundreds = input_number // 100
        remainder = input_number % 100
        if remainder == 0:
            meru_number = f"{dataset[hundreds][0]} {dataset[100][0]}"
            grammar = f"{dataset[hundreds][1]} {dataset[100][1]}"
            morphemes = dataset[hundreds][2] + dataset[100][2]
        else:
            meru_number = f"{dataset[hundreds][0]} {dataset[100][0]} na {convert_to_meru_number_recursive(remainder, dataset, cache)[0]}"
            grammar = f"{dataset[hundreds][1]} {dataset[100][1]} na {convert_to_meru_number_recursive(remainder, dataset, cache)[1]}"
            morphemes = dataset[hundreds][2] + dataset[100][2] + convert_to_meru_number_recursive(remainder, dataset, cache)[2]
        result = meru_number, grammar, morphemes
    else:
        tens = input_number // 10
        ones = input_number % 10
        meru_number = f"{dataset[tens*10][0]} {dataset[ones][0]}"
        grammar = f"{dataset[tens*10][1]} {dataset[ones][1]}"
        morphemes = dataset[tens*10][2] + dataset[ones][2]
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
        number = convert_to_digit(input_meru_number, dataset)
        print(f"The Digit Equivalent for {input_meru_number} is: {number}")
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