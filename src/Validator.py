import Constants as c
from WrongInputsError import WrongInputsError
from StringTooShortError import StringTooShortError
from StringCleanser import StringCleanser


class Validator:

    # Check empty inputs
    def is_null(self, s:str):
        return s.isspace()
    
    # Check for Numbers
    def is_all_numbers(self, s: str):
        return s.isdigit()

    # Check input size
    def is_correct_size(self, s: str):
        size = len(s)
        return size >= c.RANGE['min'] and size <= c.RANGE['max']


    # Factory method to validate input before returning string back to main program
    def validate_inputs(self, s: str):

        if (self.is_null(s)):
            raise WrongInputsError("Entered null characters, please try again: ")

        s = StringCleanser.cleanse(s)

        if self.is_correct_size(s):
            return s.upper()

        raise StringTooShortError(
            f"Your input string was too short.\
                nPlease ensure its between {c.RANGE['min']} and {c.RANGE['max']}")




