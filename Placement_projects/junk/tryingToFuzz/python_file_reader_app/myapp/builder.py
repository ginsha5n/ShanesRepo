"""
File for setting up builder functions for the program
"""
import logging

class SubmitJobBuilder(object):
    """
    Builder functions for creating cli commands that run the application.
    """

    def __init__(self):
        self.command = ["python3", "app.py"]

    def set_exit_code(self, exit_code):
        self.command.extend(["-n", str(exit_code)])
        return self

    def set_positive_word_count(self, positive_word_count):
        self.command.extend(["-p", str(positive_word_count)])
        return self

    def set_negative_word_count(self, negative_word_count):
        self.command.extend(["-ne", str(negative_word_count)])
        return self

    def build(self):
        logging.info("building job command")
        return self.command
