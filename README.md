# Meru Number Translator & Morphological Analyzer Using Recursion

This project converts numbers to its equivalent Meru name and vice versa. The analyzer takes a numerical input and generates its corresponding Meru name. In addition, it outputs the Meru words' morphological grammar.

**Meru** is a native language spoken in Kenya. The Meru people are natively located in the central region of Kenya around Mt.Kenya.

## Features

- Converts numbers to their Meru language equivalent.
- Converts Meru names of numbers to their numerical equivalent.
- Generates and outputs the Morphological Grammar of the Meru name equivalent.

## How it Works
The Meru Number Converter is implemented using a recursive approach in Python. 
It consists of two main functions: "convert_to_meru_number" and "convert_to_digit". 
The program loads the dataset of MeruNumbers from a CSV file containing mappings between the numbers and their MeruNumber equivalents.

The convert_to_meru_number function takes a digit number as input and recursively converts it to its corresponding MeruNumber representation. 
Similarly, the convert_to_digit function takes a MeruNumber as input and recursively converts it to its decimal equivalent.

## Dataset

The Meru Number Converter uses a dataset stored in a CSV file (MeruNumbers.csv). This dataset contains the mapping between numbers and their corresponding MeruNumbers, and grammar. The program loads this dataset at runtime to perform the conversions.

The dataset contains numbers 0 to 100 [and other values] and their corresponding Meru name and morphological grammar.

The other values are:

- 1,000 and 10,000.
- 1,10 and 100 million.
- 1,10 and 100 billion.

These extra values will enable translation of a larger scope of numbers to their Meru name equivalent and vice versa.

## Usage

To use the Meru Number Translator & Morphological Analyzer, follow these steps:

1. Clone the repository to your local machine.

2. Make sure you have Python installed (version 3.6 or above).

3. Open with **Jupyter Notebook** or an equivalent software.

- or You can use **Google Colab**.

## Acknowledgments

This project was inspired by the fascinating Meru numbering system and the rich cultural heritage of the Meru people.
Special thanks to the Meru community for preserving and sharing their unique numerical system.

## Authors
The Meru Number Converter was implemented and completed through collaboration between Tonny and Moses.
