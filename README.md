# Python Classes, Inheritance and Polymorphism

This project showcases Object-Oriented Programming (OOP) concepts in Python, including class creation, inheritance, and polymorphism, using examples of a Smartphone class and animal classes.

## Features

* Creation of the `Smartphone` class with attributes and methods.
* Inheritance demonstration with the `GamingSmartphone` subclass.
* Polymorphism example with the `Animal` class and its subclasses (`Dog`, `Bird`, `Fish`).
* Smartphone class includes contact storage, adding, and calling features.

## Getting Started

1.  Clone this repository to your local machine.
2.  Ensure you have Python installed.
3.  Navigate to the project directory in your terminal.
4.  Run the Python files using `python smartphone.py`, `python gamingsmartphone.py`, and `python animal_polymorphism.py`.

## Usage

```python
#Example of Smartphone usage
john_phone = Smartphone("Google", "Pixel 6", 128, 50, 4614, "John Doe")
john_phone.turn_on()
john_phone.add_contact("Alice", "555-1234")
john_phone.call_contact("Alice")

#Example of animal usage
dog = Dog()
dog.move() #output: Running on four legs.

Author
Stephany Winam / @stephwinam
