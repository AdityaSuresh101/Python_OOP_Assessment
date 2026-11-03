# Python OOP Assessment – Vehicle Rental System

## Project Overview

This project is a simple **Vehicle Rental System** developed using Python to demonstrate the fundamental concepts of Object-Oriented Programming (OOP).

The program models different types of vehicles and demonstrates how OOP principles can be used to organise code, manage vehicle availability, and perform basic rental operations.

## OOP Concepts Demonstrated

The project covers the following Object-Oriented Programming concepts:

### 1. Classes and Objects
- Defines a general `Vehicle` class.
- Creates specific vehicle classes such as `Car` and `Motorcycle`.
- Demonstrates object creation and interaction.

### 2. Encapsulation
- Uses a private attribute `__is_available` to manage vehicle availability.
- Controls access to the vehicle's availability through class methods.

### 3. Inheritance
- `Car` and `Motorcycle` inherit properties and methods from the parent `Vehicle` class.
- Promotes code reusability and reduces duplication.

### 4. Polymorphism
- Both `Car` and `Motorcycle` implement their own versions of the `start_engine()` method.
- Demonstrates method overriding, where the same method behaves differently depending on the object.

## Project Structure

```text
Python_OOP_Assessment/
│
├── oop_assignment.py
└── README.md
```

## Features

- Vehicle creation using classes and constructors.
- Vehicle availability management.
- Basic vehicle rental functionality.
- Separate implementations for cars and motorcycles.
- Engine-starting behaviour using method overriding.

## Technologies Used

- **Programming Language:** Python 3
- **Concepts:** Object-Oriented Programming

## How to Run

1. Clone or download this repository.
2. Open the project folder.
3. Make sure Python 3 is installed.
4. Run the Python file:

```bash
python oop_assignment.py
```

## Learning Objectives

The main objective of this project is to understand and apply the fundamental principles of Object-Oriented Programming in Python through a simple, real-world-inspired vehicle rental example.

## Author

Developed as part of a Python Object-Oriented Programming (OOP) assessment.
