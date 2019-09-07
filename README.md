# TIGr-Python-Parser
Made for the 2019 Ara Advanced Programming (In Python) Class

## Added By Tom S
Made some changes in few files
1. Parser.py

![Changes made 1](https://github.com/jok0436/TIGr-Python-Parser/blob/ATeamJoMaTo/image/change1.JPG)

Adding try & except bits for self.data = row[1] as if given data in txt is U or P
for pen up and down, will give out of index error without this

2. PyGameDrawer.py

![Changes made 2](https://github.com/jok0436/TIGr-Python-Parser/blob/ATeamJoMaTo/image/change2.JPG)

Adding array called penlist to get value to call from self.colours dictionary
Modified select_pen method so we can choose the colour based on int value e.g. 1,2,3

3. TKDrawer.py

![Changes made 3](https://github.com/jok0436/TIGr-Python-Parser/blob/ATeamJoMaTo/image/change3.JPG)

Again, adding penlist that can be called inside select_pen method as given value will be an integer.

4. draw_line method for most drawer

![Changes made 4](https://github.com/jok0436/TIGr-Python-Parser/blob/ATeamJoMaTo/image/change4.JPG)

Moved where newCoords variable is, it used to be after if statement but that case, if pen is not down, self.x & self.y still needs to be changed without drawing but newcoords variable will only be created if pen is down.

5. TDrawer.py

![Changes made 5](https://github.com/jok0436/TIGr-Python-Parser/blob/ATeamJoMaTo/image/change5.JPG)

* initialize the penlist when its created as unlike TKinter or PyGame, turtle uses with string, but given txt value will be an integer value, so we can select string value out of an array with given integer by index.
* For I & Chris, decided to do go_along & go_down like in photo as we don't want turtle to draw the line while its moving and if you guys want that way, feel free to do so :)


## Working great in both directionwise & drawing tool

1. Draw line with all drawing tool

![Turtle lines](https://github.com/jok0436/TIGr-Python-Parser/blob/ATeamJoMaTo/image/T.JPG)

![TK lines](https://github.com/jok0436/TIGr-Python-Parser/blob/ATeamJoMaTo/image/TK.JPG)

![PyGame lines](https://github.com/jok0436/TIGr-Python-Parser/blob/ATeamJoMaTo/image/P.JPG)

2. Draw shapes with all drawing tools

![Turtle shapes](https://github.com/jok0436/TIGr-Python-Parser/blob/ATeamJoMaTo/image/T1.JPG)

![TK shapes](https://github.com/jok0436/TIGr-Python-Parser/blob/ATeamJoMaTo/image/TK1.JPG)

![PyGame shapes](https://github.com/jok0436/TIGr-Python-Parser/blob/ATeamJoMaTo/image/p1.JPG)



## Josiah and Tom Created Files:

* Parser
* Reader
* TKCMD
* TKDrawer


## Josiah and Marcus Created Files:

* ParserMike
* TDrawer
* LookupArgParser


## Marcus and Tom Created Files:

* PyGameDrawer


## Josiah and Tom Points and Reasoning:

* Interactive Front-End x2

	* More Functional
	* Allows the user to input commands one by one instead of from a text file.
	
* Command Line Switches x2

	* More Functional
	* Allows for multiple outputs at the same time
	
* Outputs with TKinter x2

	* More Functional
	* Even more Functionality with Drawing Shapes
	
* Supports Piping and Scripting x2

	* More Flexible
	* Allows the user to Pipe in a file and Output it to multiple Drawers


## Josiah and Marcus Points and Reasoning:

* Parsed from Configurable Lookup Table x12:
	
	* More Flexible
	* It easier to add new functions to lookup table than adding functions to the class directly
  
* Outputs with turtle x2:

  * More Functional
  * We added more drawing functions to enhance the drawe
  
* Interactive front-end x2:

  * More Functional
  * Users can input commands dynamically instead of inputting a .txt file
  
* Command line switches x2:

  * More Flexible
  * Users can switch between different drawers with command switches
  
* Uses generic parsing engine x2:
  
  * More robust
  * Users can input slightly incorrect commands (e.g. 'C           100' and it will still work)


## Marcus and Tom Points and Reasoning:

* Output with Pygame x2:

	* More functional
	* We add more drawing functions to enhance the drawer


## Files that were worked on by both teams:

* TXTDrawer
* Main
