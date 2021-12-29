import Constants as c
from WrongInputsError import WrongInputsError
from StringOutOfBoundsError import StringOutOfBoundsError
from StringCleanser import StringCleanser


class Validator:

    # Check empty inputs
    def is_null(self, s:str):
       return s is None or s.isspace() or s == ''
             

    # Check input size
    def is_correct_size(self, s: str):
        size = len(s)
        return size >= c.RANGE['min'] and size <= c.RANGE['max']


    
    def validate(self, s: str):
        """
        @Desc: Validates the string inputs against common test cases
        @Args: s(str): raw user input
        @Returns: s(str): formatted string 
        """

        if (self.is_null(s)):
            raise WrongInputsError("No usable value detected in inputs, please try again. ")

        s = StringCleanser.cleanse(s)

        if self.is_correct_size(s):
            return s.upper()

        raise StringOutOfBoundsError(
            f"Your input string was too short."
            f" Please ensure its between" 
            f" {c.RANGE['min']} and {c.RANGE['max']} characters")




