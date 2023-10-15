#!/bin/bash

Airbnb Clone Project

This is the Airbnb clone project, an application using Python that simulates the functionality of the popular platform Airbnb. It enables users to create, manage, and interact with property listings. The README.md offers an illustration of the project and shows how to utilize a command interpreter.
Command Interpreter
It is the project's main component since it gives a command-line interface for interacting with the clone, allowing users to do different things correlated to property bookings and listings. 
How to start it
The first step is to clone the project repository into the local machine.
Navigate to the Airbnb directory. 
Run the command interpreter by executing $ ./console.py

Using it
The command interpreter offers both interactive and non-interactive modes for interacting with the clone
Interactive Mode
One can directly enter commands and receive immediate response/feedback. The prompt (hbnb) will be shown.
To begin the interactive mode, one runs (hbnb) help.
This will show a list of available commands. 
Non-Interactive Mode
One can also use the command interpreter in non-interactive mode by piping commands. This helps in automation and scripting. For example, to execute a single command in non-interactive mode, one needs to key in $ echo "help" | ./console.py

This will execute the "help" command and display the output without entering the interactive mode. 
Examples
Listing available commands. 
(hbnb) help

Quitting command interpreter:
(hbnb) quit

Non-interactive mode (execute the "help" command without entering interactive mode):
$ echo "help" | ./console.py

