### 1. Encapsulation 
 Explanation: Hiding internal data and requiring all interactions to go through strict public interfaces. 
This prevents external code from corrupting your object's internal state.
Python Implementation: Python doesn't have true private keywords like Java. We use underscores to flag access.
**rules**:
1. _variable:
     Protected (A warning to other devs: Leave this alone unless you are a subclass).
2. __variable:
     Private (Triggers Name Mangling where Python renames it behind the scenes to_ClassName__variable to prevent accidental overwrites).

### 2. Inheritance
 Explanation:
 Creating a hierarchy where child classes inherit attributes and code from a parent class to maximize reuse and maintainability.
 Best Practice: Don't build massive inheritance chains.

 If a child class only needs a part of the parent's logic, use Composition (making an instance of one class an attribute of another) instead of inheritance.

 ### 3. Polymorphism
  Explanation: "Many forms."
   It allows different classes to share the same method names but implement their own distinct logic underneath.
  - Method Overriding: When a child class redefines a method that it inherited from a parent class to specialize its behavior (e.g., Dog overriding Animal.speak()).
  
 ### 4. Abstraction
   Explanation: Hiding complex execution details and only showing essential features. 
    In Python, we enforce this using the abc (Abstract Base Classes) module.
    You cannot create an instance of an abstract class;
    it acts strictly as a mandatory blueprint for child classes.



What is OOP?
A programming paradigm that models real-world software components as "objects" combining data (attributes) and behavior (methods).

What is a class vs. an object?
A Class is the blueprint or data type definition (e.g., class Car). An Object is a live instance allocated in memory built from that template (e.g., my_tesla = Car()).

What is the difference between Abstract Classes and Interfaces?
Python doesn't have an explicit interface keyword. We simulate an interface by creating an Abstract Base Class where all methods are marked with @abstractmethod and contain no functional code.
