# AirBnB Clone - The Console

AirBnB Clone - The Console is a command-line tool designed to manage and interact with property rental data. This project emulates the basic functionality of Airbnb, allowing you to create, manage, and search for property listings through a user-friendly command-line interface.
# Table of Contents

    Installation
    Usage
    Commands
    Examples
    Contributing
    License

Installation
Requirements

    Python 3.6 or later

    Clone this repository to your local machine:

bash

git clone https://github.com/bonii254/AirBnB_clone.git

    Navigate to the project directory:

bash

cd AirBnB_clone

    Run the console:

bash

./console.py

Now you're ready to start using the AirBnB clone console!
Usage

The console provides a simple, yet powerful, interface for managing property listings. It allows you to create, update, delete, and search for property listings. You can interact with the console by typing in commands and receiving feedback in real-time.
Commands

Here are some of the basic commands you can use in the AirBnB clone console:

    create <class>: Create a new instance of a specified class.
    show <class> <id>: Display information about an instance.
    destroy <class> <id>: Delete an instance.
    all <class>: Display a list of all instances or all instances of a specified class.
    update <class> <id> <attribute> "<value>": Update an attribute of an instance.

For a full list of available commands and their usage, you can use the help command within the console.
Examples

Here are a few examples of how to use the console:

    Create a new user:

sql

(hbnb) create User

    Show details of a user:

sql

(hbnb) show User <user_id>

    List all available users:

scss

(hbnb) all User

    Update a user's information:

sql

(hbnb) update User <user_id> first_name "John"

    Delete a user:

php

(hbnb) destroy User <user_id>

More Info
Execution

works in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

Contributing

We welcome contributions from the community! If you find a bug, have an idea for an improvement, or would like to add new features, please feel free to open an issue or submit a pull request.
License

This project is licensed under the MIT License - see the LICENSE file for details.

Enjoy using the AirBnB Clone - The Console, and happy property management! If you have any questions or need further assistance, feel free to reach out to the project maintainers.

AUTHORS
# contributors to the repository.

Bonface Murangiri <bonnyrangi95@gmail.com>
Nwali Emmanuel <emmanuelsticx6@gmail.com>
