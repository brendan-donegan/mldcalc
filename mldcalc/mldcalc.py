import argparse
import sys

import calc


def num_ints(path):
    return str(calc.num_ints_from_file(path))

def longest_line(path):
    return str(calc.longest_line_from_file(path))

def mean(path):
    return str(calc.mean_from_file(path))

def most_common(path):
    return str(calc.most_common_from_file(path))

def main():
    parser = argparse.ArgumentParser("Calculate statistics about integers.")
    subparsers = parser.add_subparsers()
    parser.add_argument('path', help='Path to a CSV file containing integers.')
    num_parser = subparsers.add_parser('num', help='Number of integers.')
    num_parser.set_defaults(function=num_ints)

    longest_parser = subparsers.add_parser('longest', help='Longest line.')
    longest_parser.set_defaults(function=longest_line)

    mean_parser = subparsers.add_parser('mean', help='Mean of integers.')
    mean_parser.set_defaults(function=mean)
    
    most_common_parser = subparsers.add_parser(
        'common',
        help='Most common integers.'
    )
    most_common_parser.set_defaults(function=most_common)
    args = parser.parse_args()
    print(args.function(args.path))

if __name__ == "__main__":
    sys.exit(main())
