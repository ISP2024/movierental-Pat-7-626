## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

## 2. Move price_code Attribute

2.1 what refactoring signs (code smells) suggest this refactoring?
- Inappropriate Intimacy because the class uses the internal fields and methods of another class.
- Feature Envy because the method accesses the data of another object more than its own data.

2.2 what design principle suggests this refactoring? Why?
- Single Responsibility Principle (SRP) because we changed 2 reasons for the class to change (movie data and rental data) into one reason (movie data).

## Rationale

- The `price_code_for_movie` function is implemented as a top-level function in the `pricing module`. This decision is based on an evaluation of the responsibilities of each class and module.
  - Low Coupling: By placing the `price_code_for_movie` function in the `pricing module`, we maintain a clear separation between pricing logic and other parts of the codes.
  - Single Responsibility Principle: By placing the `price_code_for_movie` function in the `pricing module`, we ensure that all pricing-related functionality is kept together, makes it easier to understand the logic without wading through unrelated codes.