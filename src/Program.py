from Validator import Validator
from Palindrome import Palindrome

def run():
    
    validator = Validator()
    test_string = '  6!*$)@  4565ABCBAHELLOHOWRACECARAREYOUILOVEUEVOLIIAMAIDOINGGOOD2%@$ @^&$^$ &*#^36796^ @& $           '
    
    try:
        # Validate
        valid_input = validator.validate(test_string)
        
        # Do palindrome 
        palindrome = Palindrome(valid_input)
        print(palindrome.get_palindromes())
    except (Exception) as error:
        print(error)
    finally:
        print(f"--------End Program--------")




if __name__ == "__main__":
    run()
