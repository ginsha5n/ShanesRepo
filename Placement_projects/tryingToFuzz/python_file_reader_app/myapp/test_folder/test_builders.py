"""
This runs tests on the application using commands put together using builder function 
"""
import sys
import logging
import pytest

sys.path.append("..") # Makes the files from parent directory visible
from app import FrameWork
from builder import SubmitJobBuilder
from make_logs_and_run_tests import TestingFramework


def main():

    run_tests = TestingFramework()
    run_tests.make_and_run("test_builders.py")

class TestBuilderCases(FrameWork):
    """
    A class with functions to set up builder format and run tests that are set up using 
    builder functions to run commands
    """
    @pytest.fixture
    def job_builder(self):
        return SubmitJobBuilder()

    def run_job(self, job_builder, exit_code = "0", positive_count = "1", negative_count = "1"):
        command = job_builder.set_exit_code(exit_code).set_positive_word_count(positive_count)\
            .set_negative_word_count(negative_count).build()

        logging.info("CLI command: %s",' '.join(command))

    # This is a repeat of another test in test.py except this time the application command is built
    # using builder functions.
    @pytest.mark.parametrize("exit_code, positive_count, negative_count", [("1","5","4"),])
    def test_word_in_new_file_v2(self, job_builder, exit_code, positive_count, negative_count):
        self.run_job(job_builder, exit_code, positive_count, negative_count)
        status = self.search_for_words("application_output.txt", "Start")
        assert status is not False

    @pytest.mark.parametrize("exit_code, positive_count, negative_count", [("1","4","10"),])
    def test_invalid_input(self, job_builder, exit_code, positive_count, negative_count):
        negative_count = "10"
        self.run_job(job_builder, exit_code, positive_count, negative_count)
        status = self.search_for_words("reports/Logs.log", "invalid input")
        assert status is True

if __name__ == "__main__":
    main()
