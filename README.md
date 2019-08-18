# TIGr-Python-Parser
Made for the 2019 Ara Advanced Programming (In Python) Class

## Added By Tom S
Made some changes in few files
1. Parser.py
![alt text](https://github.com/jok0436/TIGr-Python-Parser/blob/ATeamJoMaTo/image/change1.JPG)
Adding try & except bits for self.data = row[1] as if given data in txt is U or P
for pen up and down, will give out of index error without this

2. PyGameDrawer.py
<img src="immage/change2.jpg" alt="change2" class="inline"/>
Adding array called penlist to get value to call from self.colours dictionary
Modified select_pen method so we can choose the colour based on int value e.g. 1,2,3

3. TKDrawer.py
<img src="immage/change3.jpg" alt="change3" class="inline"/>
Again, adding penlist that can be called inside select_pen method as given value will be an integer.

4. draw_line method for most drawer
<img src="immage/change4.jpg" alt="change4" class="inline"/>
Moved where newCoords variable is, it used to be after if statement but that case, if pen is not down, self.x & self.y still needs to be changed without drawing but newcoords variable will only be created if pen is down.


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
