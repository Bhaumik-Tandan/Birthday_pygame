
# Project Title

Customizable Birthday snake game

## Sample Gameplay

https://user-images.githubusercontent.com/62440699/127781384-a48ee7aa-0e45-4850-b72c-c330b1e5ac46.mp4

## Customisation

You can add and remove audio in the audio folder in the asset directory

![image](https://user-images.githubusercontent.com/62440699/127781155-8e52de99-390a-4aa1-b38e-74dcb4c5e112.png)


Add photos that you want to be displayed in snake in the snake_photo folder

![image](https://user-images.githubusercontent.com/62440699/127781173-1f85172d-ab78-4bb9-905d-60a7b3699888.png)


Add one or more header photos into the birthday_photo folder

![image](https://user-images.githubusercontent.com/62440699/127781192-f91b7e75-84cf-4f58-9403-aef497d7f54a.png)

Add quit/icon photo into quit_photo

![image](https://user-images.githubusercontent.com/62440699/127781209-78cdaafe-6779-46d0-b7e2-2681acb46c9d.png)

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
You can change the settings of the game using settings.json

  
## Controls

The user can control the snake using arrow keys and wasd keys

![Tip1](https://user-images.githubusercontent.com/62440699/127781259-50e62480-7b0d-4de7-a684-daed84c49c6e.jpg)


The screen of the game is stopped until the user press any of the above keys

![image](https://user-images.githubusercontent.com/62440699/127781285-62b65309-4ff4-4001-8cc0-08a710706809.png)


On pressing escape key the user is routed to the menu screen

![Escape-key](https://user-images.githubusercontent.com/62440699/127781300-a49191a6-6097-4ecf-a58c-938c8d105047.jpg)


User can press q to quit the game or c to play the game again

![image](https://user-images.githubusercontent.com/62440699/127781311-fde250e5-ee56-4900-a481-06ea2a41550a.png)


  
## Variables in settings.json
  ### Size
  
  
![image](https://user-images.githubusercontent.com/62440699/127781336-8f4c5e65-b484-4e1c-a601-5e4e0cfb444f.png)

`block width` It denotes the width of the single block of the snake

`block height` It denotes the heigt of the single block of the snake
  ###### Note : All the other variables of sizes will be multiplied by the block variables to find the net value

`window width` It denotes the width of the window of the game

`window height` It denotes the height of the window of the game

`happy birthday banner height` It denotes the height of the header photo


### Score and Message
![image](https://user-images.githubusercontent.com/62440699/127781346-3712a0d4-0a26-488b-84da-64b06c45c09f.png)


`font size` It denotes font size of the of respective text

`color`  It denotes the color of the text

`type`  It denotes font family of the text
       

###### Note : Score controls the text "Your Score" and Message controls the message displayed on the second game window
### Other Settings
![image](https://user-images.githubusercontent.com/62440699/127781356-63d3fa44-ac34-4584-b405-82caf47e8e1b.png)

`full screen` Its true value indicates that when the game loads it is opened in full screen and in case of false value it is loaded in minimissed mode

`audio`: True value indicates audio "on" and False value indicates audio "off"

`background color` It indicates the background color of the screen
    
`speed` It indicates the initial speed of the snake

`speed increment` It indicates the increment in speed of the snake on eating the food

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

  
