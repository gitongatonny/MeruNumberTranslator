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
    return dataset

# Load the dataset from CSV
dataset = load_dataset('MeruNumbers.csv')

def analyze_meru_number(input_number, dataset):
    if input_number in dataset:
        # Number is in the dataset
        return dataset[input_number]

    if input_number == 100:
        # Special case for 100
        return dataset[100]

    if 100 <= input_number < 200:
        tens = (input_number % 100) // 10
        ones = input_number % 10
        if tens == 0:
            meru_number = f"{dataset[100][0]} {dataset[ones][0]}"
            grammar = f"{dataset[100][1]} {dataset[ones][1]}"
        else:
            meru_number = f"{dataset[100][0]} {dataset[tens * 10][0]} na {dataset[ones][0]}"
            grammar = f"{dataset[100][1]} {dataset[tens * 10][1]} na {dataset[ones][1]}"
        return meru_number, grammar, dataset[100][2] + dataset[tens * 10][2] + dataset[ones][2]

    if input_number < 100:
        # Numbers from 1 to 99
        tens = input_number // 10
        ones = input_number % 10
        meru_number = f"{dataset[tens * 10][0]} {dataset[ones][0]}"
        grammar = f"{dataset[tens * 10][1]} {dataset[ones][1]}"
        return meru_number, grammar, dataset[tens * 10][2] + dataset[ones][2]

    if input_number >= 200:
        hundreds = input_number // 100
        remainder = input_number % 100
        if remainder == 0:
            meru_number = f"{dataset[hundreds][0]} {dataset[100][0]}"
            grammar = f"{dataset[hundreds][1]} {dataset[100][1]}"
        else:
            tens = remainder // 10
            ones = remainder % 10
            if tens == 0:
                meru_number = f"{dataset[hundreds][0]} {dataset[100][0]} {dataset[ones][0]}"
                grammar = f"{dataset[hundreds][1]} {dataset[100][1]} {dataset[ones][1]}"
            else:
                meru_number = f"{dataset[hundreds][0]} {dataset[100][0]} {dataset[tens * 10][0]} na {dataset[ones][0]}"
                grammar = f"{dataset[hundreds][1]} {dataset[100][1]} {dataset[tens * 10][1]} na {dataset[ones][1]}"
        return meru_number, grammar, dataset[hundreds][2] + dataset[100][2] + dataset[tens * 10][2] + dataset[ones][2]

def run_meru_number_analyzer():
    # Get user input
    input_number = int(input("Enter a number: "))

    # Analyze the Meru number
    meru_number, grammar, morphemes = analyze_meru_number(input_number, dataset)
    print(f"The Meru number for {input_number} is: {meru_number} ({grammar})")
    print(f"Morphemes: {', '.join(morphemes)}")

run_meru_number_analyzer()