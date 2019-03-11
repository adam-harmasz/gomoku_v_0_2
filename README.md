# gomoku_v_0_2 

This is an application to store gomoku game records and display them, it allows user to download game from kurnik/playok
or upload game record from a file.

### GETTING STARTED

1. Checking Python version.
    - To be able to use this app you'll need to have Python installed, you can check whether you have it installed or not by typing in terminal:  
`python3 --version`  
or:  
`python --version`  
    - If you don't have Python installed you can go to [Python.org](https://www.python.org/downloads/) to download it.

1. Creating Virtual Environment  
    - To create a virtual environment, decide upon a directory where you want to place it, and run the venv module as a script with the directory path:  
    `python3 -m venv your-env`  
    - Once you’ve created a virtual environment, you may activate it.  
    `source your-env/bin/activate`  
2. Download  
    - You need to clone repository to your local destination  
    `$ cd path/to/your/workspace`  
    `git clone https://github.com/henryy07/gomoku_v_0_2.git`
    - if you have established ssh connection to github you can use this link to clone repo:  
    `git clone git@github.com:henryy07/gomoku_v_0_2.git`  
3. Requirements
    - Once your virtual environment is activated and project is cloned you need to install requirements:  
    `$ pip install -r requirements.txt`  

### USAGE

- To use this application you need to type (if you're in your workspace directory):  
    `python manage.py runserver`  
or  
    `python3 manage.py runserver`  
- After that you need to create an account to start using app, 
if you'll have problems with downloading/uploading games, follow guide in "Help" section.
- Main functionalities:
    - Downloading game record via URL using requests
    - Uploading game in txt format (for now)
    - Extracting data from game record such as: 
        - player nicknames 
        - result 
        - date of game
        - move coordinates
        - information who started game
        - information whether color was changed or not
        - information about the rule variation
    - Displaying game on the board created in JS(jQuery)/SVG
    - User registration/login
    - Updating user profile
    - Password reset/password change
    
- To do:  
    - Filtering list of games
    - Adding comments and alternative moves to the game record
    - Enable downloading games from [piskvorky.net](http://www.piskvorky.net/) (second biggest gomoku website)
    - Uploading game from .bdt type of file
    
- Technologies used:
    - Python 3.6.5  
    - Django 2.1.7
    - Django-Rest-Framework
    - requests
    - Re
    - PostgreSQL
    - JavaScript/jQuery
    - Bootstrap 4
    
### How does it look like: 
 
First example:  
![example 1](https://github.com/henryy07/gomoku_v_0_2/blob/master/samples/img/sample_img1.jpg)  
Second example:  
![example 2](https://github.com/henryy07/gomoku_v_0_2/blob/master/samples/img/sample_img2.jpg)
