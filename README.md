# Airbnb Clone Project

## Description

This project aims to create an Airbnb clone with a command-line interface for managing Airbnb objects. The command interpreter allows users to create new objects, retrieve objects from files or databases, perform operations on objects, update object attributes, and destroy objects.

## Command Interpreter

### How to Start

To start the command interpreter, run the following command:

```bash
./console.py
How to Use
The command interpreter supports various commands for managing Airbnb objects. Some of the basic commands include:

create: Create a new object.
show: Retrieve an object.
update: Update attributes of an object.
destroy: Destroy an object.
all: Show all objects or objects of a specific class.
quit: Exit the command interpreter.

Examples
$ ./console.py
(hbnb) create User
2b3e8ac5-7d18-4f20-8b10-17d5e67b01d2
(hbnb) show User 2b3e8ac5-7d18-4f20-8b10-17d5e67b01d2
[User] (2b3e8ac5-7d18-4f20-8b10-17d5e67b01d2) {'id': '2b3e8ac5-7d18-4f20-8b10-17d5e67b01d2', 'created_at': '2023-11-24T12:00:00', 'updated_at': '2023-11-24T12:00:00'}
(hbnb) quit
$

