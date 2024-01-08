"""
An application for creating a new file from data taken from two seperate files
provided in words/ directory

Practised:
logging
parsing command line argument
reading and writing files
running commands and application from within python script
creating and using builder functions

Its important to use docstrings because it makes it easier for me to explain myself when someone asks....

"""
import random
import sys
import subprocess
import argparse
from make_logs_and_run_tests import TestingFramework


class FrameWork:
    """
    TODO documentation
    """

    def create_new_file(self, num_positive_words, num_negative_words,
                        positive_file="words/positive.txt", negative_file="words/negative.txt"):
        """
        Given file 1 and file 2, this function generates a new file with a mix of words
        """
        try:
            with open(positive_file, "r") as file1:
                content1 = file1.read().split()

            with open(negative_file, "r") as file2:
                content2 = file2.read().split()

            # Shuffle content to get different words each time
            # random.shuffle(content1)
            # random.shuffle(content2)

            # Grabs words from the given files
            positive_words = content1[:num_positive_words]
            negative_words = content2[:num_negative_words]

            # Combines words together
            combined_words = positive_words + negative_words
            random.shuffle(combined_words)
            combined_output = " ".join(combined_words)

            with open("application_output.txt", "w") as output_file:
                output_file.write(combined_output)

            print("Words combined and saved to new file")
        except FileNotFoundError:
            print("An error occurred: file not found")

    def how_many_words(self, file1, file2):

        count = 0

        try:
            with open(file1, "r") as f1:
                content1 = f1.read().split()

            with open(file2, "r") as f2:
                content2 = f2.read().split()

            for word in content2:
                if word in content1:
                    count += 1

            return count

        except FileNotFoundError:
            print("An error occurred: file not found")
            return None

    def search_for_words(self, file, word):
        """
        return True is word is found in specified
        """
        try:
            with open(file, "r", encoding="utf-8") as f:
                for line in f:
                    if word in line:
                        return True
            return False
        except FileNotFoundError:
            return False

    def search_many_words(self, file, *words):
        """
        TOD0
        """
        for word in words:
            if not self.search_for_words(file, word):
                return False
        return True

    def run_command(self, command):
        """
        TOD0
        """
        try:
            result = subprocess.run(
                command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return result.stdout

        except subprocess.CalledProcessError as e:
            return f"Command failed with error: {e}\n{e.stderr}"


def main():
    """
    Main function to handle command line input and call application
    Exits with code that is input from the user under argument one.
    """

    log = TestingFramework()
    log.create_logging()

    parser = argparse.ArgumentParser(description='My application')
    parser.add_argument("-f", "--file", type=str,
                        default="default_parameter.txt",  help="Path to the input file")
    parser.add_argument("-r", "--reverse", action="store_true",
                        help="reverse input order")
    parser.add_argument("-n", "--number", type=int,
                        help="Number argument that becomes app exit code")
    parser.add_argument("-p", "--positive_words", type=int,
                        help="Positive words argument")
    parser.add_argument("-ne", "--negative_words", type=int,
                        help="Negative words argument")

    args = parser.parse_args()

    # If an arg is not given in the cli it will search the default file or the specified '-f' file for the value(s).
    if args.positive_words is None or args.negative_words is None:
        with open(args.file) as file:
            arguments = file.read().split()

        if args.number is None and '-n' in arguments:
            index = arguments.index('-n') + 1
            args.number = int(arguments[index])

        if args.positive_words is None and '-p' in arguments:
            index = arguments.index('-p') + 1
            args.positive_words = int(arguments[index])

        if args.negative_words is None and '-ne' in arguments:
            index = arguments.index('-ne') + 1
            args.negative_words = int(arguments[index])

    # args = parser.parse_args(arguments)
    print(f'Parsed Arguments: {args}')

    # Check if inputs are between 0 and 10
    if not (0 <= int(args.positive_words) <= 10 and 0 <= int(args.negative_words) <= 10):
        print("Inputs must be between 0 and 10. Please try again.")
        log.print_and_log("invalid input")
        print("exiting program")
        exit(11)

    if args.reverse:
        args.number, args.positive_words, args.negative_words = args.number, args.negative_words, args.positive_words
        print("Reverse order mode")

    # Bring in the application framwork in the form of an object.
    frame_work = FrameWork()
    frame_work.create_new_file(args.positive_words, args.negative_words)
    print(f"{args.number} {args.positive_words} {args.negative_words}")
    print(f"Exit code {args.number}")
    log.print_and_log(
        f"{args.positive_words} positive words and {args.negative_words} negative words printed to file")

    sys.exit(args.number)


if __name__ == "__main__":
    main()
