
from Validator import Validator

def main():
    
    validate_inputs = Validator()
    test_string = '      45652%@$@^&$^$Aa&*#^36796^@&$     '
    
    try:
        result = validate_inputs.validate_inputs(test_string)
        print(result)
    except (Exception) as error:
        print(error)




if __name__ == "__main__":
    main()
