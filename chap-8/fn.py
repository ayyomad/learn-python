'''
Learning Functions in Python: Essential Concepts

1. Syntax of Function Definition:
    - Define a function using the def keyword.
      Example:
      def add(a, b):
          return a + b

2. How to Use (Call) Functions:
    - Call a function by its name and pass required arguments.
      Example: result = add(5, 3)

3. Passing Arguments:
    - By Value: Arguments are passed by assignment (object reference).
      - Immutable types (int, str, tuple) cannot be changed inside the function.
      - Mutable types (list, dict) can be modified inside the function.
      Example:
      def update(lst):
          lst.append(10)

4. Return Types:
    - Functions can return any data type or None (no return value).
    - Multiple values can be returned as a tuple.
      Example:
      def get_values():
          return 1, 2

5. Conditions and Edge Cases:
    - Mismatched number of arguments causes runtime errors.
    - Not returning a value from a function returns None.
    - Recursion: Functions can call themselves, but must have a base case to avoid infinite loops.

6. Beginner Mistakes:
    - Forgetting to use def to define a function.
    - Not matching parameter names and number of arguments.
    - Modifying immutable arguments expecting changes outside the function.
    - Using global variables without the global keyword.

7. Important Things to Know:
    - Scope: Variables declared inside a function are local.
    - Lifetime: Local variables exist only during function execution.
    - Functions can be nested in Python.
    - Functions can be defined in modules for modularity.

8. Best Practices:
    - Keep functions small and focused on one task.
    - Use meaningful names.
    - Document parameters and return values (use docstrings).
    - Avoid global variables unless necessary.

Summary:
- Understand function definition and calling.
- Know how arguments are passed and how scope works.
- Be careful with mutable and immutable types.
- Practice writing and using functions for modular, readable code.
'''