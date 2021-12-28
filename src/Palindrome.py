class Palindrome:
    def __init__(self, valid_input: str):
        self._valid_input = valid_input

    
    def __str__(self):
        return f"{self._valid_input}"
    
    
    def get_palindromes(self):
        # Find the palindromes
        
        palindrome_set = set()
        pivot = 0.0
        while (pivot < len(self._valid_input)):
            radius = pivot - int(pivot)

            while((pivot + radius) < len(self._valid_input) and
            (pivot - radius) >= 0 and 
                    self._valid_input[int(pivot - radius)] == self._valid_input[int(pivot + radius)]):
                
                palindrome_set.add(
                    self._valid_input[int(pivot - radius): int(pivot + radius + 1)])
                radius += 1
            
            pivot += 0.5
        return palindrome_set














        # Store them in a map - of arrays, arranged by length desc order
        # Print the map sorted by length



        #Sorting by Length and start index (Java)
        """
        The trick is to use variables for length and start index instead of start and end index.
        String input = 'funny'
        for (int length=input.length(); length > 0; --length)
            for (int start=0; start + length <= input.length() ++start)
                System.out.println(input.substring(start, start + length))
            System.out.println("")
        If we would write length >= 0 then the empty string "" would be printed input.length() times. But since the empty string "" is a substring of every string we cheat and print it only once by hand.
        """
