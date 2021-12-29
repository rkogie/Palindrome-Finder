# NOTICE FOR VISITORS
- Please read `Approach-Analysis` first before proceeding to install and run the application


# GENERAL NOTES

PROGRAM FEATURES
----------------
- Program encapsulated as a mini console application with game logic and basic user interface/screen prompts
- Built with validation logic to capture edge and corner cases (please follow instructions under `RUN IN YOUR ENVIRONMENT` to view/run tests)


SOFTWARE DESIGN PATTERNS
------------------------
- Codebase separated into single responsibility modules that handle specific parts of the application logic (SOLID principles)
- Incorporated OOP and functional programming paradigms where possible
- Some dependency injection for decoupling high and low level modules
- Magic numbers, UI/UX components abstracted to separate `Constants` and `GameAssets` files


INCLUDED FUNCTIONALITY (from Requirements)
------------------------------------------
- Finds palindromes in input string
- Substrings are uppercase on output
- Valid substrings are 2 characters or greater
- Palindromes sorted by length


MISSING FUNCTIONALITY (from Requirements)
-----------------------------------------
- Find start index position of found palindrome



KNOWN BUGS/INEFFICIENCIES 
----------
- In `Palindrome.py`, function `find_palindrome()` ideally should implement condition checks in case the palindrome list is null, but this is only feasible within the `return_palindromes()` scope
- `find_palindrome()` should implicitly strip all invalid palindromes without needing an additional helper function `strip_invalid_palindromes()`, but to maintain lean functions, this functionality was exported to its own function. 


IMPROVEMENTS
------------
- Split source files into separate python modules/packages - could not get it to work due to Python's package path system
- Launch as browser based application utilizing web framework (Django, Flask, React/Vue/Angular)
- General refactoring into decoupled modules, resusable components and algorithm performance optimization


TIME COMPLEXITY ANALYSIS
------------------------
- For the raw palindrome algorithm, it gives a worst case scenario logarithmic O(n log n) runtime due to the nesting of while loops as the `radius` expands outwards on each iteration
- If you include the validation and string cleansing logic, this does increase the application runtime further due to the inbuilt Python methods used, but the trade off is building 
a more robust application to run against invalid user inputs and handle them appropriately



# RUN APP AS DOCKER IMAGE
- Install Docker (OS dependent) - https://docs.docker.com/get-docker/
- Open a terminal shell (OS Dependent - CMD or bash) 
- **Note: Windows users may have additional steps to install WSL2 and Ubuntu from the MS Store App:** 
    Installing WSL2 Update Package: https://docs.microsoft.com/en-us/windows/wsl/install-manual
    Installing Linux distribution => visit the Microsoft Store (recommend Ubuntu 20.04 LTS)
    Configure UNIX user/password
- If Docker is already installed (run `docker --version` to confirm), run `docker search rkogie0308/my-palindrome-app`
- Results should show:
```
NAME: rkogie0308/my-palindrome-app 
DESCRIPTION: Repository for palindrome application
```
- Run `docker pull rkogie0308/my-palindrome-app` if you want a local copy in your local machine. If not, skip this step
- As the application includes user input, please run with - `docker run --interactive --tty rkogie0308/my-palindrome-app`


# RUN IN YOUR ENVIRONMENT (if Docker image fails)
- Fork or clone repo to your local machine
- Install Python - https://www.python.org/downloads/
- Open src files in IDE of choice (**VS Code or PyCharm recommended**)
- Click run application. Ensure script path is set to `Game.py` if prompted
- To run against test cases, navigate to `Tests.py`, copy the test strings labelled under `FAILED_TEST_CASES` dictionary into your console, when prompted with message: `"Please type or paste your inputs to the console:"` during runtime