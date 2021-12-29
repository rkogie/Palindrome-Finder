from Validator import Validator
from Palindrome import Palindrome
import time


class Program: 
    def run(self):
        
        validator = Validator()
        test_string = input("Enter your string: ")
        
        def run_palindrome_finder():
            """
            @Desc: Utility function to run the program - find palindromes
            @Args: N/A
            @Returns: None (void) - prints the list of palindromes
            """
            valid_input = validator.validate(test_string)
            palindrome = Palindrome(valid_input)
            print(palindrome.return_palindromes())

        try:

            start = time.time()
            
            run_palindrome_finder()

            end = time.time()
            print(f"\nProgram Runtime: {end - start} seconds")

        except (Exception) as error:
            print(error)
        finally:
            print(f"\n--------End Program--------")
