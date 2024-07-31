# Simple Calculator Application

This is a simple calculator application written in C. The application takes two integer arguments from the command line and performs basic arithmetic operations: addition, subtraction, multiplication, and division.

## Files

1. *calc.c*: The main file which contains the entry point of the program. It handles the input arguments and calls the arithmetic functions.
2. *functions.c*: Contains the implementations of the arithmetic functions (addition, subtraction, multiplication, and division).
3. *functions.h*: The header file which declares the arithmetic functions.

## How to Use

### Compilation

To compile the program, you need to have a C compiler installed. You can use the following commands to compile the application:

```sh
gcc -o calculator calc.c functions.c
Running the Application
Once the program is compiled, you can run it from the command line by passing two integer arguments:

sh
Copy code
./calculator <integer1> <integer2>
For example:

sh
Copy code
./calculator 10 5
Output
The application will output the number of arguments passed, the first argument, and the results of the arithmetic operations:

less
Copy code
Calculator

number of arguments passed: 3
first argument: ./calculator
The sum of argv[1] and argv[2]: 15
The difference of argv[1] and argv[2]: 5
The product of argv[1] and argv[2]: 50
The quotient of argv[1] and argv[2]: 2
Learnings
This simple calculator application provides several key learnings:

Basic C Programming: Understanding the structure of a C program, including #include directives, function declarations, and implementations.

Command Line Arguments: Learning how to handle command line arguments in a C program using argc and argv.

Modular Programming: Separating the main program logic (calc.c) from the implementation of functions (functions.c), and using a header file (functions.h) to declare those functions.

Arithmetic Operations: Implementing basic arithmetic operations and understanding integer arithmetic in C.

Input Validation: Basic handling of input validation by checking the number of arguments passed to the program.

Future Enhancements
To further enhance this simple calculator, you could consider:

Adding error handling for invalid inputs (e.g., non-integer arguments, division by zero).
Implementing additional arithmetic operations (e.g., modulus, power).
Creating a user-friendly interface for input and output.
Expanding the program to handle floating-point arithmetic.
Conclusion
This simple calculator is a great starting point for learning basic C programming and understanding fundamental concepts such as command line arguments, function declarations, and modular programming. It provides a foundation upon which more complex applications can be built.

css