'''Describe a component from a text-editor GUI and the methods that it encapsulates.'''
'''
File Operations is one of the core components in every text editor. This component encapsulates the methods such as 

1. Opening existing files:
As the name implies, this method opens the existing files by reading its path in the disk and converts the stream of zeros and one's to readable text.

2. Saving files to the disk:
This method takes the path and stores the new document at a specified location by giving it a unique name.

3. Printing the page:
This method reads the text and streams the information such as plain text, indentations, images, properties of text to the printer. 

4. Creating new files:
This method creates a new instance of the file and allots space for the file.

5. Mouse cursor movements and clicks:
This method takes an instance of Action class and calls various methods in that class to perform the mouse actions such as clicks, double clicks, right clicks, etc.'''