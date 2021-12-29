
class Palindrome:
    INVALID_LENGTH = 1

    def __init__(self, valid_input: str):
        self._valid_input = valid_input
        

    def __str__(self):
        return f"{self._valid_input}"
    
    
    def find_palindromes(self):
        """
        @Desc: Finds raw palindromes within string input (includes single char values)
        @Args: N/A as class method
        @Returns: list(str): array of found palindromes

        """
        raw_palindromes = []
        pivot = 0.0
        while (pivot < len(self._valid_input)):
            radius = pivot - int(pivot)

            while((pivot + radius) < len(self._valid_input) and
            (pivot - radius) >= 0 and 
                    self._valid_input[int(pivot - radius)] == self._valid_input[int(pivot + radius)]):
                
                raw_palindromes.append(
                    self._valid_input[int(pivot - radius): int(pivot + radius + 1)])
                radius += 1
            
            pivot += 0.5
            
        return raw_palindromes 


    def strip_invalid_palindromes(self):
        """
        @Desc: Detects invalid palindrome strings and discards from list
        @Args: N/A as class method
        @Returns: list(str): array of valid palindromes

        """
        found_palindromes = self.find_palindromes()
        return [element for element in found_palindromes if len(element) > self.INVALID_LENGTH]
        


    def return_palindromes(self):
        """
        @Desc: Returns valid palindromes back to user
        @Args: N/A as class method
        @Returns: list(str): sorted by length array of palindromes

        """
        found_palindromes = self.strip_invalid_palindromes()
        if not found_palindromes:
            return "\nNo palindromes found"
        return sorted(found_palindromes, key=len, reverse=True)
