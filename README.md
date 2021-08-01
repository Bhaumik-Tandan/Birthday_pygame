
# Project Title

Customizable Birthday snake game


## Customisation

You can add and remove audio in the audio folder in the asset directory

>>Add photos that you want to be displayed in snake in the snake_photo folder

>>Add one or more header photos into the birthday_photo folder

>>Add quit/icon photo into quit_photo


## Installation

Download the library dependeny using pip

```bash
  pip install -r requirements.txt
```
You can also directly install pygames
```bash
  pip install pygame
```
Now run the file main.py using gui
or You can do it using terminal 
```bash
  cd [PATH]\\Birthday_pygame
  py main.py
```




    
## Features
>>You can change the settings of the game using settings.json

  
## Controls
>>The user can control the snake using arrow keys and wasd keys

>>The screen of the game is stopped until the user press any of the above keys

>>On pressing escape key the user is routed to the menu screen

>>User can press q to quit the game or c to play the game again


  
## Variables in settings.json
  ### Size
  >>`block width` It denotes the width of the single block of the snake

  >>`block height` It denotes the heigt of the single block of the snake
  ###### Note : All the other variables of sizes will be multiplied by the block variables to find the net value

  >>`window width` It denotes the width of the window of the game

  >>`window height` It denotes the height of the window of the game

  >>`happy birthday banner height` It denotes the height of the header photo


### Score and Message

>>`font size` It denotes font size of the of respective text

>>`color`  It denotes the color of the text

>>`type`  It denotes font family of the text
       

###### Note : Score controls the text "Your Score" and Message controls the message displayed on the second game window
### Other Settings
>>`full screen` Its true value indicates that when the game loads it is opened in full screen and in case of false value it is loaded in minimissed mode

>>`audio`: True value indicates audio "on" and False value indicates audio "off"

>>`background color` It indicates the background color of the screen
    
>>`speed` It indicates the initial speed of the snake

>>`speed increment` It indicates the increment in speed of the snake on eating the food

## FAQ

#### Does the name of my image or audio matters?

No you can insert the files in the assets folder by any name.

#### Does the name of json and py file matters?

Yes it is not recomended to change the name of the name of py and json file except main.py

#### Can images be of any type like jpg, png, etc.?

Yes you can insert image of any type

#### Can we change the name or location of the folders?

No the location\name of the folder must not be changed

#### Can we change the structure or names in the json file?

No it is not recomended





  
## 🛠 Skills
Python, pygames, os, json...

  
