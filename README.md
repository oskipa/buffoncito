# Bufoncito: the Petite Motley Fool News Site 

A small website that serves investment news.

## Installation

### Preparation
The instructions assume a unix-like environment like Linux or MacOS. Adapt the instructions if you are using Windows. If using Windows, you can use cygwin or the Windows Linux shell.

It is assumed that you have git and python3 installed.

### Give execute permission to the scripts

If you are running the script in a unix-like environment, you may need to run the following commands to the scripts to give them execution permissions.

    chmod u+x get_dependencies.sh
    chmod u+x run.sh


### Getting code and instaling dependencies

    git clone <repo name>

Enter into the `bufoncito` directory. Now run dependency installation script.

    ./get_dependencies.sh


## Running the server

You can run the server in two ways.

    ./run.sh
 
Or 
    python manage.py runserver

