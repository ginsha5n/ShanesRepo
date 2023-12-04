"""
This class and function set up the logging and run the pytest command on the testcase folder.
Keeping it seperate makes the main app and test file cleaner looking.
"""
import os
import logging
import pytest


class TestingFramework():
    """
    Includes functions for:
    setting up lo files and folder 
    runnning testcases from within the python script
    """

    def create_logging(self, log_file = "Logs.log"):
        # Create log folder
        log_folder = "reports"
        os.makedirs(log_folder, exist_ok=True)

        # Log output file
        log_file = os.path.join(log_folder, log_file)

        # Configure logging to save logs to a file
        logging.basicConfig(
            filename=log_file,
            level=logging.DEBUG,
            filemode='w'
        )

    def run_tests(self, file_name):

        file_path = "test_folder/" + file_name

        status = pytest.main(["-v", "--capture=tee-sys", file_path])
        logging.info("Exiting PyTest with status: %s", str(status))

    def make_and_run(self, file_name):
        """
        Sets up the logging file and folder if it doesnt already exist then runs pytest on the tests.py files
        """
        # check current working directory and change if neccesary
        cwd = os.getcwd()
        if cwd.endswith("myapp"):
            pass
        else:
            parent_dir = os.path.dirname(cwd)
            os.chdir(parent_dir)

        self.create_logging()
        self.run_tests(file_name)

    def print_and_log(self, string):
        print(string)
        logging.info(string)
