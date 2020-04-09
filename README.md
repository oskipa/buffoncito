# Bufoncito: the Petite Motley Fool News Site 

A small website that serves investment news.

## Installation

### Preparation
The instructions assume a unix-like environment like Linux or MacOS. Adapt the instructions if you are using Windows. If using Windows, you can use cygwin or the Windows Linux shell.

It is assumed that you have git and python3 installed.


### Give execute permission to the scripts

If you are running the script in a unix-like environment, you may need to run the following commands to the scripts to give them execution permissions.

    chmod u+x install_and_run.sh

Then execute the script.

    ./install_and_run.sh

### Some notes 

The first thing that I would do is to improve the validation for comments. I would also go around polishing details to that the site would look more polished. Especially the comment area.

I would also run it on postgres. I chose not to do it because I thought it would make it harder to run once you received it.

Some of of the things that I added were the ability to change the slug in the admin area. Also the number of cards or links that appear in the main page and the article page. 
