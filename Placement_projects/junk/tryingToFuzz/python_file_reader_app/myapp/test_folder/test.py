"""
File contaning testcases for app.py
"""
import sys
import logging
import subprocess

sys.path.append("..")  # Makes the files from parent directory visible
from make_logs_and_run_tests import TestingFramework
from app import FrameWork

def main():

    run_tests = TestingFramework()
    run_tests.make_and_run("test.py")


class TestCase(FrameWork):
    """
    A class containing test cases
    """

    def test_word_in_file(self):
        """
        Given a file and a word, 
        return true if the word is present in the file.
        Return False otherwise
        """
        expected_word = "resink"
        file = "words/randomWords.txt"
        is_word_in_list = self.search_for_words(file, expected_word)
        assert is_word_in_list is True
        logging.info("Expected word: %s", expected_word)
        logging.info("Word in file?: %s", is_word_in_list)

    def test_word_not_in_file(self):
        """
        Given a file and a word, 
        return true if the word is present in the file.
        Return False otherwise
        """
        expected_word = "battle"
        file = "words/randomWords.txt"
        is_word_in_list = self.search_for_words(file, expected_word)
        assert is_word_in_list is False

    def test_search_many_words_pass(self):
        file = "words/randomWords.txt"
        do_words_exist = self.search_many_words(
            file, "resink", "dogwatch", "nope")
        assert do_words_exist is True

    def test_search_many_words_fail(self):
        file = "words/randomWords.txt"
        do_words_exist = self.search_many_words(
            file, "resink", "dogwatch", "battle")
        assert do_words_exist is False

    def test_word_in_new_file(self):
        self.run_command(["python3", "app.py", "-n", "2","-p", "3", "-ne", "4"])
        status = self.search_for_words("application_output.txt", "Start")
        assert status is not False

    def test_word_not_in_new_file(self):
        python_version = "python3"
        self.run_command([python_version, "app.py", "2", "3", "4"])
        status = self.search_for_words("application_output.txt", "NotHere")
        assert status is False

    def test_how_many_positve_words(self):
        self.run_command(["python3", "app.py", "-n", "2","-p", "5", "-ne", "4"])
        word_count = self.how_many_words(
            "words/positive.txt", "application_output.txt")
        assert word_count == 5

    def test_how_many_negative_words(self):
        self.run_command(["python3", "app.py", "-n", "2","-p", "3", "-ne", "4"])
        word_count = self.how_many_words(
            "words/negative.txt", "application_output.txt")
        assert word_count == 4

    def test_exit_code(self):
        command = ["python3", "app.py", "-n", "2","-p", "3", "-ne", "4"]
        process = subprocess.Popen(
            command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        exit_code = process.wait()
        assert exit_code == 2

    def test_input_over_limits(self):
        """
        Giving an invalid input to the application cli.
        Expected outcome: invalid command entered in logs and exits program.
        Tests that 'invalid input' is in log file
        """
        self.run_command(["python3", "app.py", "-n", "2","-p", "3", "-ne", "4"])
        status = self.search_for_words("reports/Logs.log", "invalid input")
        assert status is True


if __name__ == "__main__":
    main()
