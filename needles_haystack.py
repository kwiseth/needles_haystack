#!/usr/bin/python3/needles_haystack.py
"""Python version of my stretch exercise based on Google tech writing exercise.

Console application that models finding needles in a haystack. Needles are words
entered by the user, and the haystack is a file containing plain unstuctured
text. User can set the number of words to enter, from 1 to 5.
"""

__author__ = """Kelli Wiseth (kelli@alameda-tech-lab.com)"""

# 25-April-2020 reorganize using main() and functions in place of one long script
#               Refactored code to reduce extraneous list, use dictionary to collect
#               needle input and to count instances of the needle in the haystack


def haystack_builder(filename):
    """ Opens specified file, reads each line, and tokenizes into individual strings.
    Eliminates contractions, punctuation, parenthesis, and so on, and builds a
    list named 'haystack' of each word, in sequence.

    Args:
            filename: The path and name of the text file to use as haystack.
    Returns:
            haystack: A list of each word (in order) in the text file.
    """

    haystack = []

    with open(filename) as textfile:
        lines = textfile.readlines()
        for line in lines:
            nuline = line.strip().split()
            clean_line = [chunk.strip('.,:;?!"()') for chunk in nuline]
            for word in clean_line:
                word = word.lower().strip()
                haystack.append(word)
    return haystack

def find_needles(needles_found, haystack):
    """ Compares each word in the dictionary to each word in the haystack list.
    If the needle matches the word in haystack, increments its counter value.

    Args:
            needles_found: A dictionary comprising each needle and its count.
            haystack: A list containing all 'words' from the text file.
    Returns:
            needles_found: A dictionary of all needles updated with actual counts.
    """

    for needle in needles_found:
        for word in haystack:
            if word == needle.lower().strip():
                needles_found[needle] += 1
    return needles_found

def main():
    """ Handles input for the program and invokes the functions to perform
    the search and prints the results.
    """
    # 1. Welcome info about console program
    print("=" * 50)
    print("This console program accepts up to 5 words ('needles') \nto search for \
    in a textfile ('haystack'). Specify your choices \nafter each prompt below. \
    Include full path if 'filename' \nis not in the same path as this application.")
    print("=" * 50)

    # 2. Prompt for filename to use as haystack.
    filename = input("Enter the filename to use as the haystack: ")

    # 3. Validate input from user. Must be digit from 1 to 5, inclusive.
    valid_entry = False # prime the while loop

    while not valid_entry:
        num_needles = input("How many needles do you want to look for (1 to 5)?: ")
        if num_needles.isdigit() and int(num_needles) >= 1 and int(num_needles) <= 5:
            num_needles = int(num_needles)
            valid_entry = True
        else:
            print("Invalid entry. Please enter a number between 1 and 5. ")

    # 4. Prompt user for each word (needle) to look for in the file (haystack).
    #    Build up dictionary of words and set counter for each to 0.
    needles_found = {}
    counter = 1
    for word in range(0, num_needles):
        print(str(counter), end=". ")
        word = input("Enter the word: ")
        needles_found[word.lower().strip()] = 0
        counter += 1

    # 5. Process file and words
    haystack = haystack_builder(filename)
    needles_found = find_needles(needles_found, haystack)

    # 6. Loop through the updated dictionary and print results in the console.
    print("=" * 50)
    print("Your haystack contains these ", f"{len(needles_found)}", "needles:\n")
    for needle in needles_found:
        print("%-20s %25d" % (needle, needles_found[needle]))

if __name__ == '__main__':
    main()
