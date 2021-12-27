# APPROACH & ANALYSIS
=====================

- My Approach to the problem set is using **Test Driven Development**

Definition of Test Driven Development or TDD
--------------------------------------------
- Software development process where requirements are synthesised through a lens of test cases before software is developed
- Process is iterative and allows for scaling as new features are rendered as tests, developed and integrated into the codebase ensuring greater code coverage
- **NOTE: It is not a catch all, as this approach is slower, requires significant effort to maintain (as products are dependent on emerging business needs, time to market velocity etc.)**
- Further Reading: https://en.wikipedia.org/wiki/Test-driven_development


PROBLEM SET
===========
- Break down problem into different sections, (1)Inputs, (2)Outputs (3)Assumptions (4)Constraints 

1. INPUTS & OUTPUTS
- The inputs are strings of characters ranging from `a-z/A-Z` - in the problem set test case, the input string was capitalized
- The output is an array with three elements, the palindrome string itself, its starting position (as index) in the input string, and its length
- Outputs are dependent on the palindromes detected in the input string, so the outputs are a variable number of arrays



2. ASSUMPTIONS
- The input string is assumed to be alphabet characters only - any special characters or numbers are not to be used
- Mixed uppercase and lowercase letters are assumed to be valid as palindromes are based on words, not character types
- The length of the input string is n size - assumption is the program should run the same whether `n=1` or `n=1*10^6`
- Validation logic should be utilized to catch invalid inputs and return information to the user for expected input
- Validation logic may include: strings that are too short, contain numbers only, contain special chars only
- Time complexity should ideally be in the range of linear complexity (O(n)), ideally logarithmic (O(n log n)) or constant time (O(1))
- Space complexity due to data structure used in sorting, recursion should be observed and optimized to reduce CPU/RAM - see time complexity



3. CONSTRAINTS
- Fron reviewing the problem set, valid palindromes are at least two adjacent characters so `2 < n` where n is length of input string
- As maximum length constraints were not given, in this scenario max length of input string = 100
- Constraints are: `2 < n < 100` where in is length of input string
- Given the approach of TDD and the assumptions highlighted above, the input string will require cleansing of any invalid characters - 
- From reviewing the test cases, the outputs are sorted by length first then by size of the output string
