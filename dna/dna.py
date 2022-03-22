import csv
import sys


def main():

    # TODO: Check for command-line usage
    if (len(sys.argv) != 3):
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # list for Short Tandem Repeats (STRs)
    STRs = []
    data = []
    # TODO: Read database file into a variable
    with open(sys.argv[1], "r") as database:
        # maps the information in each row to a dict
        reader = csv.DictReader(database)
        # add 1st row item to STR list
        STRs = reader.fieldnames[1:]
        # add data to each row
        for row in reader:
            data.append(row)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as DNAsequence:
        DNA = DNAsequence.read()

    # TODO: Find longest match of each STR in DNA sequence)
    STR_result = []
    for i in range(len(STRs)):
        STR = longest_match(DNA, STRs[i])
        STR_result.append(STR)

    # TODO: Check database for matching profiles
    for row in data:
        # set counter of correctness for each row
        correct = 0
        for i in range(len(STRs)):
            # check if numbers of STR for each person in database match the STR result
            # if match then increase correct 1 point
            if int(row[STRs[i]]) == STR_result[i]:
                correct += 1
                # if all correct then print name of that person
                if correct == len(STRs):
                    print(row["name"])
                    return
    else:
        print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in sequence, return longest run found
    return longest_run


main()
