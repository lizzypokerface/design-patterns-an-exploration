# A Collection of Design Patterns in Python

This repository contains implementations of all 23 GoF (Gang of Four) Design Patterns in Python. You can find the source [here](https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25231942#overview).

## Design Patterns

### Creational Design Patterns
Creational design patterns deal with object creation mechanisms, aiming to create objects in a manner suitable to the situation. They help manage the instantiation process, providing flexibility and efficiency in object creation.

* [Factory Pattern](https://sbcode.net/python/factory/)
    - The Factory pattern is useful when a class cannot anticipate the class of objects it must create, requiring the creation of objects without specifying the exact class of object that will be created.
* [Abstract Factory Pattern](https://sbcode.net/python/abstract_factory/)
    - The Abstract Factory pattern is useful when you need to create groups of related objects without knowing their exact types in advance, unlike the Factory pattern, which focuses on creating a single object type.
* [Builder Pattern](https://sbcode.net/python/builder/)
    - The Builder pattern is useful when an object needs to be created in a step-by-step manner, allowing for the construction of complex objects with a clear separation of concerns.
* [Prototype Pattern](https://sbcode.net/python/prototype/)
    - The Prototype pattern is useful when you need to create new objects by copying existing ones, ensuring efficient object creation.
* [Singleton Pattern](https://sbcode.net/python/singleton/)
    - The Singleton pattern is useful when you need to ensure a class has only one instance and provide a global access point to it.

### Structural Design Patterns
Structural design patterns focus on the composition of classes and objects, allowing them to work together while ensuring that they remain flexible and efficient. They help define clear relationships and simplify complex structures.

* [Decorator Pattern](https://sbcode.net/python/decorator/)
    - The Decorator pattern is useful when you want to add responsibilities to objects dynamically and transparently without altering their structure.
* [Adapter Pattern](https://sbcode.net/python/adapter/)
    - The Adapter pattern is useful when you need to make incompatible interfaces work together without changing their existing code.
* [Facade Pattern](https://sbcode.net/python/facade/)
    - The Facade pattern simplifies complex systems by providing a unified interface, making it easier for clients to interact with the subsystems without needing to understand their intricacies.
* [Bridge Pattern](https://sbcode.net/python/bridge/)
    - The Bridge pattern connects an interface with its implementation, letting you change both independently. This makes it easier to add new features without affecting existing code.
* [Composite Pattern](https://sbcode.net/python/composite/)
    - The Composite pattern allows you to treat individual objects and groups of objects uniformly. This makes it easy to work with complex tree structures, as you can use the same interface for both single items and collections.
* [Flyweight Pattern](https://sbcode.net/python/flyweight/)
    - The Flyweight pattern minimizes memory usage by sharing common data among multiple objects. It’s useful when you have a large number of similar objects, allowing you to store shared state externally and keep individual object sizes small.
* [Proxy Pattern](https://sbcode.net/python/proxy/)
    - The Proxy pattern provides a surrogate or placeholder for another object to control access to it. This is useful for managing resource-intensive objects, adding security, or implementing lazy loading without changing the original object's interface.
* [Mediator Pattern](https://sbcode.net/python/mediator/)
    - The Proxy pattern provides a surrogate or placeholder for another object to control access to it. This is useful for managing resource-intensive objects, adding security, or implementing lazy loading without changing the original object's interface.

### Behavioural Design Patterns
Behavioral design patterns emphasize the interaction and responsibility between objects. They define how objects communicate and collaborate, promoting effective communication and reducing dependencies in a system.

* [Command Pattern](https://sbcode.net/python/command/)
    - The Command pattern encapsulates a request as an object, allowing you to parameterize clients with queues, requests, or operations. This enables features like undo/redo functionality and supports logging or queuing of commands without changing the objects that execute them.
* [Chain of Responsibility Pattern](https://sbcode.net/python/chain_of_responsibility/)
    - The Chain of Responsibility pattern passes a request along a chain of handlers, allowing multiple objects to process it without knowing which object will handle it. This promotes loose coupling and flexibility in handling requests, as you can add or change handlers easily.
* [Observer Pattern](https://sbcode.net/python/observer/)
    - The Observer pattern allows one object (the subject) to notify multiple dependent objects (observers) about changes in its state. This promotes a loose coupling between the subject and observers, making it easy to add or remove observers without affecting the subject.
* [Interpreter Pattern](https://sbcode.net/python/interpreter/)
    - The Interpreter pattern defines a representation for a language's grammar and provides an interpreter to evaluate sentences in that language. It’s useful for designing domain-specific languages, allowing for easy parsing and execution of expressions based on the defined grammar.
* [Iterator Pattern](https://sbcode.net/python/iterator/)
    - The Iterator pattern provides a way to access elements of a collection sequentially without exposing its underlying structure. This allows for easier traversal of complex data structures, promoting flexibility and encapsulation.
* [Mediator Pattern](https://sbcode.net/python/mediator/)
    - The Mediator pattern centralizes communication between objects, reducing their dependencies on one another. This simplifies interactions and promotes loose coupling, making it easier to manage complex relationships in a system.
* [Memento Pattern](https://sbcode.net/python/memento/)
    - The Memento pattern captures and stores an object's state without exposing its internal structure, allowing you to restore the object to a previous state later. This is useful for implementing undo functionality or saving snapshots of an object's state.
* [State Pattern](https://sbcode.net/python/state/)
    - The State pattern allows an object to alter its behavior when its internal state changes, enabling it to appear as if it has changed its class. This promotes cleaner code by encapsulating state-specific behavior and making it easier to manage complex state transitions.
* [Strategy Pattern](https://sbcode.net/python/strategy/)
    - The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. This allows clients to choose an algorithm at runtime, promoting flexibility and the ability to change behavior without modifying the context in which the algorithm is used.

## Requirements

* Python 3.x

## Setup

Navigate to the design_patterns_python directory.

### Conda Environment

1. Create a Conda environment with Python 3.x:

```bash
    conda create --name py3x python=3.x
```

2. Activate the Conda environment:

```bash
    conda activate py3x
```

### Virtual Environment

1. Navigate to the project directory:

```bash
    cd python/
```

2. Create a virtual environment:

```bash
    python -m venv venv
```

3. Activate the virtual environment:

```bash
    source venv/bin/activate
```

## Installation

Install the project dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Code Quality

### Pre-commit

This project uses pre-commit for static code analysis and formatting.

1. Install pre-commit hooks:

```bash
    pre-commit install
    pre-commit installed at .git/hooks/pre-commit
    ```

2. To run pre-commit on all files:

```bash
    pre-commit run --all-files
    ```

Feel free to contribute or report any issues you encounter. Happy coding!
