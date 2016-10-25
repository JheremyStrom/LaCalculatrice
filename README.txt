Author: Jheremy Strom
E-mail: jheremys@usc.edu
Version: 1.0 (December 26 2014)
Some comment changes and extremely minor code changes happened on 10/25/2016, no functionality was changed.

Description: This program functions as a basic calculator and also
as a file management system for urls.

What it does: Calculator functions and also creates files for
urls that have strings (url links) attached to them. Once the url
button is clicked, the link is copied into the clipboard

The author of this program is Jheremy Strom. It was built as a minor project in order to increase the skills of the author. With that being said, there are multiple issues with this product.
1. DO NOT use the negative (-) sign on the calculator
This will cause the program to freeze
2. The answer returned by the calculator will always be float point
3. The password to the special functions is hard coded and thus can only be changed if the file is opened and the password is changed manually
'1486' has to be entered and then the '=' sign pressed to get to the folder/url functionality of the program
4. The folder and url buttons are not arranged in alphabetical order
5. There may be other issues that arise

Q: What is buildlist.pickle?
A: It is the file that contains the information for the files and urls. The program uses the python library 'pickle' and it saves pickled objects to a file with the extension '.pickle'