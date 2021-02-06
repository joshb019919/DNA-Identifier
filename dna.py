"""Test Short Tandem Repeats to find DNA profiles."""

from sys import argv
import csv


def main():
    """Open files; print results of match()."""

    if args():
        try:
            db = args()[0]
            seq = args()[1]
            
            # Open STR database and DNA sequence.
            with open(db, newline="") as db, open(seq, "r") as sequence:
                print(match(db, sequence))
        except FileNotFoundError:
            print("One or both files do not exist!")
    else:
        print("Usage: python dna.py database.csv sequence.txt")


def args():
    """Collect command line arguments, return db and sequence or None."""

    # From Python documentation.
    if len(argv) == 3:
        db = argv[1]
        sequence = argv[2]
    else:
        return

    return db, sequence


def match(db, sequence):
    """Search db and sequence, return name if match, else 'No match'."""

    # From Python documentation:
    # Sequence read, STR data, and column header names (STR's).
    sequence = sequence.read()
    people = csv.DictReader(db)
    STRs = people.fieldnames[1:]

    for person in people:
        # Number of STRs found.
        found = 0

        # Based on suggestion given by Discord user Кинтана:
        # Assemble each STR string for which to be searched.
        for STR in STRs:
            check_STR = STR * int(person[STR])
            start = sequence.find(check_STR)

            # Create an easy start and stop for slicing.
            if start != -1:
                end = start + len(check_STR) + len(STR)
                start = start + len(check_STR)

            # Make sure sequence contains the proper number of STRs.
            if check_STR in sequence and sequence[start:end] != STR:
                found += 1

        if found == len(STRs):
            return person["name"]

    return "No match"


main()