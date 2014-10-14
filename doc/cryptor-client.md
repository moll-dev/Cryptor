#Cryptor API Documentation

######This readme file was created for devs to get a good understanding of the objects and their attributes and methods in CryptCastle-II. It's going to be frequently updated! So if you don't know where to look this is probably a good place to start.


#Cryptor Client

######These objects are all related to the Engine.py file and handle pretty much everything relating to the game's inner workings.

##The Engine Object itself
This is THE object that is created by the Gui object (when initialized) and pretty much handles all behind the scenes aspects of the game.

##Engine.initPlayer()
This method creates a Player object and initializes its position and items (see player)
```python
#Player creation example
self.user = Player(self, [5,5],[2,2],None)

#Creates an object with the reference 'user' for example engine.user would be the player object
#the first parameter sets the player's parent, then its region, and room location, along with a list of items
```
##Engine.step()
Steps the engine! This is where all calculations, combat, etc will go.

And it runs the Engine.do() command which is pretty important (see Engine.do())

##Engine.do()
This is it, the meat and potatos of the engine. This method requires no parameters, and relies on the Command object which gets updated within this method.
>Engine.do() takes all the verbs and checks against them to correctly select the action needed and then preforms that on the object.

##Player Object
Needs to be initialized with a parent (usually the engine or self), region x and y, and a room x and y, and then a list of items (as objects not as strings)

##Player.move()
This method simply checks if a player can move by calling the .updateRoom method, and then checking the room's exits to see if the player can actually exit! If the player can exit, the coordinates of the player will be incremented by a vector direction function (still to be written!!)

Example in python:
```python
user.move('north')
```

##Player.warp()
This method does the same exact thing as player.move with the exception of jumping regions although note this has NOT been implimented!!!

##Player.take()
Not finished! but should TAKE the item passed as a parameter

##Player.drop()
Not finished! but should drop an item in the inventory given an item as a parameter


##Player.look()
Not finished, but should return the description of an item in the inventory or room.


Example in python:
```python
user.look('beer')
```

#Gui Objects

######This section contains all the details for working with the current gui setup in CC-II, including the initilization of a new gui object, methods associated with gui, and objects as well.
##gui object
Needs to be initialized with just a parent (which should be a tkinter window).

```python
#Python Example
#Create a new gui object with 'window' as it's parent
game = gui(window)
```
Also when a new gui object is created, it executes the following methods:

>self.e = Engine(self), [gui.initUI()](https://github.com/QuantumFractal/CryptCastle-II/blob/master/docs/Objects%20and%20Methods.md#guiinitui), [gui.initColor()](), engine.loadMap, and engine.initPlayer


##gui.initUI()

Takes no parameters, this method is here simply to setup the buttons and text boxes that make CCII run.
It creates the following objects:

>statText, consoleText, objectText, invText, entryText, and the enterButton

This method is run during the creation of a new gui object.


##gui.initColor()
This method currently isn't being used, but in the future it should add the ability to color text and make cool sequences


##gui.OnPressEnter()
This method does not require any parameters, and it is run when the "Enter" button is pressed. It simply runs the gui.OnButtonPress() method. (It's kind of a loop back method)

##gui.OnButtonPress()
This method does not require any parameters, but it has a very important purpose. It signals the start of a new turn, takes the data from gui.entryText via the get() method and steps the engine. The exact usages are below.
```python
def OnButtonPress(self):
  self.e.commandstr = self.entryText.get()          #Sets the engine's command string as the entry text from the user

  if self.entryText.get() == "exit":                #Checks if the command is to exit, then exits
    self.e.consolePrintln("Good Bye Adventurer!")   #<- With a cheeky exit note :)
    self.parent.quit()

  elif self.e.commandstr.isspace()== True or len(self.entryText.get()) == 0:
    pass                                         #Ignores an all spaces command input
  else:
    self.entryText.delete(0,END)                 #If its normal text, then step the engine (see engine.step)
    self.e.step()
  self.entryText.delete(0,END)                   #Clears the entryText box for the next command!
```
#World Objects:
Note for all lists that need to be inputed with XML use a space character as a delimter
For Example:
the position 2,2 becomes "2 2"
##World
needs to be initialized with a dictionary of values, these include:
name,desc,size NOTE: order of attrs do NOT matter

```python
#Python Example
attributes = {'name': 'World1', 'desc': 'This is a world', 'size':'10 10'}

#Create a new world object with the attributes defined above
world1 = World(attributes)
```
```xml
XML TAG example
<World size = "10 10" name="World1" desc="This is a world">
</World>
```

##Region
needs to be initialized just like World with these values:
loc, size, name, desc.
```python
#Python Example
attributes = {'name': 'Region1', 'desc': 'This is a region', 'size':'10 10', 'loc':'2 2'}

#Create a new world object with the attributes defined above
region1 = region(attributes)
```
```xml
XML TAG example
<Region loc="2 2" size = "10 10" name="Region1" desc="This is a region">
</Region>
```

##Room
needs to be initialized just like World and Region with these values:
loc, name, desc, exits, and items
```python
#Python Example
attributes = {'name': 'Room1', 'desc': 'This is a room, 'loc':'3 4'}

#Create a new world object with the attributes defined above
region1 = region(attributes)
```
```xml
XML TAG example
<Region loc="3 4" name="Room1" desc="This is a room">
</Region>
```
##Room.canExit()
Returns whether a player can or cannot exit a room! (In a certain direction)

