__author__ = "Jheremy Strom"
__Version__ = "1.0"  # Comments modified 10/25/2016

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
+ Description: This program functions as a basic calculator and also  +
+ as a file management system for urls.                               +
+                                                                     +
+ What it does: Calculator functions and also creates files for       +
+ urls that have strings (url links) attached to them. Once the url   +
+ button is clicked, the link is copied into the clipboard            +
+                                                                     +
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from tkinter import *
import pickle
from resetbuildlist import resetbuildlist

""" Does a multitude of input and output with files """
def filefunc(filetouse, func, obj=None, folder=None, urlname=None):
    # Load in the file right away because all the if statements need a loaded tempbuildlist
    with open(filetouse, "rb") as file:
        tempbuildlist = pickle.load(file)

    if func == "appendfolder":  # If folder needs to be appended
        with open(filetouse, "wb") as file:
            tempbuildlist[folder] = {}
            pickle.dump(tempbuildlist, file)

    elif func == "appendurl":  # If obj needs to be appended
        with open(filetouse, "wb") as file:
            tempbuildlist[folder][urlname] = obj
            pickle.dump(tempbuildlist, file)
    elif func == "deletefolder":  # If a folder needs to be deleted
        del tempbuildlist[folder]
        with open(filetouse, "wb") as file:
            pickle.dump(tempbuildlist, file)
    elif func == "deleteurl":  # If a url needs to be deleted
        del tempbuildlist[folder][urlname]
        with open(filetouse, "wb") as file:
            pickle.dump(tempbuildlist, file)

    elif func == "load":  # Load the filetouse and return what is in it
        return tempbuildlist

""" Checks a given string if it has a digit in it"""
def hasNumber(string):
    return any(num.isdigit() for num in string)

""" The different mathematical calculations and requires a list"""
""" Function is set up to make sure there is always a digit following an operator"""
def calculations(self, numlist):
    result = 0  # The result that is returned at the end of the function
    cycle = 1  # Lets the loop for the calculations run
    subcycle = 0  # Number that keeps track of the loop when assigning values to operatorlist and digitlist
    operatorlist = []  # List of all the operators
    digitlist = []  # List of all the integers

    """ Loop to add operators to a list """
    if numlist != []:
        while subcycle < len(numlist):
                # Looking to see if it is a number in a string or an operator
                if hasNumber(numlist[subcycle]):
                    digitlist.append(float(numlist[subcycle]))  # If it is a number, this will go through and add int to digitlist
                    subcycle += 1
                else:
                    operatorlist.append((numlist[subcycle]))  # Will append the object to operatorlist because that's the only other option
                    subcycle += 1

    """ While loop that checks for different operations inputed into the calculator"""
    while cycle == 1:

        # Break the loop if a number wasn't inputed last
        if numlist[-1] == "" and numlist[0] != "X" and numlist[0] != "/" and numlist[0] != "--" and numlist[0] != "+":
            result = "Error"
            del numlist[:]
            break

        if numlist[0] == "1486":
            result = "1486"
            del digitlist[0]
            self.special()

        # This runs if nothing has been calculated and removes the need to calculate the first and next number in digitlist
        if result == 0:
            result = digitlist[0]
            del digitlist[0]

        # These are the mathematical operations that take place
        if digitlist:
            if operatorlist[0] == "/":
                result = result/digitlist[0]
                del operatorlist[0]
                del digitlist[0]
            elif operatorlist[0] == "X":
                result = result*digitlist[0]
                del operatorlist[0]
                del digitlist[0]
            elif operatorlist[0] == "--":
                result = result-digitlist[0]
                del operatorlist[0]
                del digitlist[0]
            elif operatorlist[0] == "+":
                result = result+digitlist[0]
                del operatorlist[0]
                del digitlist[0]

        # Checks to see if there are any digits left
        if not digitlist:
            cycle = 0

    return result

""" Set up the calculator """
class Main:

    """ Initial Conditions """
    def __init__(self):
        self.root = Tk()
        self.root.title("La Calculatrice")
        self.root.focus_set()
        self.root.grab_set()
        self.numberlist = []  # Keeps track numbers inputed before and after a sign is clicked
        self.grilldecalcul()
        self.buildlist = {}  # Keeps track of all the folder and link information

    """ Function to interact with the entry box """
    def entryhandler(self, number):
        if number == 0 or number == 1 or number == 2 or number == 3 or number == 4 or number == 5 or number == 6 or number == 7 or number == 8 or number == 9:  # Entry handler when a general number button is pressed
            self.entry.config(state=NORMAL)
            self.entry.insert(END, number)
            self.entry.config(state=DISABLED)
        # The clear button clears the entry
        elif number == 16:  # Entry handler for when Clear is pressed
            self.entry.config(state=NORMAL)
            self.entry.delete(0, END)
            self.entry.config(state=DISABLED)
            del self.numberlist[:]
        elif number == "/":  # Entry handler for when "/" is pressed
            self.numberlist.append(self.entry.get())
            self.numberlist.append("/")
            self.entry.config(state=NORMAL)
            self.entry.delete(0, END)
            self.entry.config(state=DISABLED)
        elif number == "+":  # Entry handler for when "+" is pressed
            self.numberlist.append(self.entry.get())
            self.numberlist.append("+")
            self.entry.config(state=NORMAL)
            self.entry.delete(0, END)
            self.entry.config(state=DISABLED)
        elif number == "--":  # Entry handler for when "--" is pressed
            self.numberlist.append(self.entry.get())
            self.numberlist.append("--")
            self.entry.config(state=NORMAL)
            self.entry.delete(0, END)
            self.entry.config(state=DISABLED)
        elif number == "X":  # Entry handler for when "X" is pressed
            self.numberlist.append(self.entry.get())
            self.numberlist.append("X")
            self.entry.config(state=NORMAL)
            self.entry.delete(0, END)
            self.entry.config(state=DISABLED)
        elif number == "=":  # Entry handler for when "=" is pressed
            self.numberlist.append(self.entry.get())
            result = calculations(self, self.numberlist)
            if result != "1486":
                del self.numberlist[:]
                self.entry.config(state=NORMAL)
                self.entry.delete(0, END)
                self.entry.insert(END, result)
                self.entry.config(state=DISABLED)

    """ Handles the buttons, last number in the entryhandler call is what appears """
    """ Requires self and a number """
    def calcbuttonhandler(self, btnum):
        if btnum == 0:
            self.entryhandler(0)
        elif btnum == 4:
            self.entryhandler(1)
        elif btnum == 5:
            self.entryhandler(2)
        elif btnum == 6:
            self.entryhandler(3)
        elif btnum == 8:
            self.entryhandler(4)
        elif btnum == 9:
            self.entryhandler(5)
        elif btnum == 10:
            self.entryhandler(6)
        elif btnum == 12:
            self.entryhandler(7)
        elif btnum == 13:
            self.entryhandler(8)
        elif btnum == 14:
            self.entryhandler(9)
        elif btnum == 15:
            self.entryhandler("/")
        # This elif handles the clear button
        elif btnum == 16:
            self.entryhandler(16)
        elif btnum == 1:
            self.entryhandler("=")
        elif btnum == 3:
            self.entryhandler("+")
        elif btnum == 7:
            self.entryhandler("--")
        elif btnum == 11:
            self.entryhandler("X")

    """ Builds la calculatrice """
    def grilldecalcul(self):
            self.topframe = Frame(self.root)  # Frame that holds the textbox and clear button
            self.topframe.grid(row=0, column=0, columnspan=4, sticky=W+E+N+S)
            self.bottomframe = Frame(self.root)  # Frame that holds the calculator buttons
            self.bottomframe.grid(row=1, column=0, rowspan=4, columnspan=4, sticky=W+E+N+S)
            self.button = []  # A list for all the buttons

            """ This loop creates the buttons """
            for i in range(16):
                self.button.append(Button(self.bottomframe, width=9, height=3, command=lambda i=i: self.calcbuttonhandler(i)))

                """ If loop to place buttons """
                if i <= 3:  # The last row of buttons
                    self.button[i].grid(row=3, column=i, sticky=W+E, padx=5, pady=5)
                    self.button[i].config(text=i)
                    if i == 1:
                        self.button[i].config(text="=")
                    elif i == 2:
                        self.button[i].config(text="-")
                    elif i == 3:
                        self.button[i].config(text="+")
                elif i > 3 and i <= 7:  # Second to the last row of buttons
                    self.button[i].grid(row=2, column=i-4, sticky=W+E, padx=5, pady=5)
                    self.button[i].config(text=i-3)
                    if i == 7:
                        self.button[i].config(text="--")
                elif i > 7 and i <= 11:  # Second row of buttons
                    self.button[i].grid(row=1, column=i-8, sticky=W+E, padx=5, pady=5)
                    self.button[i].config(text=i-4)
                    if i == 11:
                        self.button[i].config(text="X")
                elif i > 11 and i <= 15:  # First row of buttons
                    self.button[i].grid(row=0, column=i-12, sticky=W+E, padx=5, pady=5)
                    self.button[i].config(text=i-5)
                    if i == 15:
                        self.button[i].config(text="/")

            # Clear Button next to text box
            self.button.append(Button(self.topframe, text="Clear", width=9, height=3, command=lambda i=i: self.calcbuttonhandler(16)))
            self.button[16].grid(row=0, column=3, padx=6, pady=5)

            # Entry box to display numbers
            self.entry = Entry(self.topframe, justify=RIGHT, width=26, disabledbackground="white", disabledforeground="black", font=30, state=DISABLED)
            self.entry.grid(row=0, column=0, padx=5, pady=5, ipady=20)

    """ destroyChildren Function: Destroys the children of the popup window """
    def destroyChildren(self, item):
        for child in self.popupwindow.winfo_children():
            child.destroy()
        self.popupwindow.destroy()
        self.popupresult = item

    """ Generic function to create a popup window"""
    def popup(self, popuptype):

        # Creates the popup window
        self.popupresult = False
        self.popupwindow = Toplevel(self.root)
        self.popupwindow.title("La Calculatrice")
        self.popupwindow.focus_set()
        self.popupwindow.grab_set()

        # Creates a popup for the addfolder button
        if popuptype == "addfolder":
            Label(self.popupwindow, text="Folder Name:", width=30, height=2, font=30).grid(row=0, column=0, padx=5, pady=5, columnspan=2)
            self.tempentry = Entry(self.popupwindow, justify=CENTER, width=20, font=30)
            self.tempentry.grid(row=1, column=0, padx=5, pady=5, ipady=5)
            self.popupbutton = Button(self.popupwindow, text="Enter", width=10, height=2, command=lambda: self.destroyChildren(self.tempentry.get())).grid(row=1, column=1, padx=5, pady=5)
        # Creates a popup for the deletefolder button
        elif popuptype == "deletefolder":
            Label(self.popupwindow, text="Folder Name:", width=30, height=2, font=30).grid(row=0, column=0, padx=5, pady=5, columnspan=2)
            self.tempentry = Entry(self.popupwindow, justify=CENTER, width=20, font=30)
            self.tempentry.grid(row=1, column=0, padx=5, pady=5, ipady=5)
            self.popupbutton = Button(self.popupwindow, text="Enter", width=10, height=2, command=lambda: self.destroyChildren(self.tempentry.get())).grid(row=1, column=1, padx=5, pady=5)
        # Creates a popup for the deleteurl button
        elif popuptype == "deleteurl":
            Label(self.popupwindow, text="Url Name:", width=30, height=2, font=30).grid(row=0, column=0, padx=5, pady=5, columnspan=2)
            self.tempentry = Entry(self.popupwindow, justify=CENTER, width=20, font=30)
            self.tempentry.grid(row=1, column=0, padx=5, pady=5, ipady=5)
            self.popupbutton = Button(self.popupwindow, text="Enter", width=10, height=2, command=lambda: self.destroyChildren(self.tempentry.get())).grid(row=1, column=1, padx=5, pady=5)
        # For addurl button
        elif popuptype == "addurl":
            Label(self.popupwindow, text="Url Name:", width=30, height=2, font=30).grid(row=0, column=0, padx=5, pady=5, columnspan=2)
            self.tempentry = Entry(self.popupwindow, justify=CENTER, width=20, font=30)
            self.tempentry.grid(row=1, column=0, padx=5, pady=5, ipady=5)
            self.popupbutton = Button(self.popupwindow, text="Enter", width=10, height=2, command=lambda: self.destroyChildren(self.tempentry.get())).grid(row=1, column=1, padx=5, pady=5)
        # For the actual url thats linked to the button
        elif popuptype == "addurl2":
            Label(self.popupwindow, text="Url Link:", width=30, height=2, font=30).grid(row=0, column=0, padx=5, pady=5, columnspan=2)
            self.tempentry2 = Entry(self.popupwindow, justify=CENTER, width=20, font=30)
            self.tempentry2.grid(row=1, column=0, padx=5, pady=5, ipady=5)
            self.popupbutton = Button(self.popupwindow, text="Enter", width=10, height=2, command=lambda: self.destroyChildren(self.tempentry2.get())).grid(row=1, column=1, padx=5, pady=5)

        self.root.wait_window(self.popupwindow)

    """ Build the special folders """
    def buildspecialfolder(self):
        rowcounter = 1  # Starts at 1 so the resetbutton does not get drawn over by a folder button
        self.buildlist = filefunc("buildlist.pickle", "load")

        # Destroy the children of bottomframe
        for child in self.bottomframe.winfo_children():  # Destroy any children in scrollcanvas
            child.destroy()

        #   Build the buttons for the folders in buildlist
        self.resetbutton = Button(self.bottomframe, text="Reset Folder", width=40, height=3, command=lambda: resetbuildlist(self)).grid(row=0, column=0, padx=5, pady=5)
        for foldername in self.buildlist:
            Button(self.bottomframe, text=foldername, width=40, height=3, command=lambda: self.buildspecialurl(foldername)).grid(row=rowcounter, column=0, padx=5, pady=5)
            rowcounter += 1

    """ Function to copy the url into the clipboard """
    def clipboard(self, urllink):
        # The program has to be kept open in order for the urllink copied to be pasted somewhere else
        self.root.clipboard_clear()
        self.root.clipboard_append(urllink)

    """  Build the special urls """
    def buildspecialurl(self, foldername):
        rowcounter = 1

        # Destroy the children of bottomframe
        for child in self.bottomframe.winfo_children():
            child.destroy()
        self.addfolder.destroy()  # Remove the buttons of the folder screen
        self.deletefolder.destroy()

        # Building the url screen's gui
        self.addurl = Button(self.root, text="Add Url", width=20, height=3, command=lambda: self.specialhandler("addurl", foldername))
        self.deleteurl = Button(self.root, text="Delete Url", width=20, height=3, command=lambda: self.specialhandler("deleteurl", foldername))
        self.backbutton = Button(self.bottomframe, text="Back to Folders", width=40, height=3, command=lambda: self.special()).grid(row=0, column=0, padx=5, pady=5)
        self.addurl.grid(row=1, column=0, padx=5, pady=5)
        self.deleteurl.grid(row=1, column=1, padx=5, pady=5)
        self.folderheader.config(text="Urls")  # Changes the folder header label to fit the url screen

        # This builds the list of buttons for the urls
        self.buildlist = filefunc("buildlist.pickle", "load")
        if self.buildlist[foldername] != {}:
            for urlname in self.buildlist[foldername]:
                Button(self.bottomframe, text=urlname, width=40, height=3, command=lambda: self.clipboard(self.buildlist[foldername][urlname])).grid(row=rowcounter, column=0, padx=5, pady=5)
                rowcounter += 1


    """ Function that handles all of specials events """
    def specialhandler(self, btntype, foldername=None):
        # Each condition does generally the same thing besides is it a folder/url and to add/delete it
        if btntype == "addfolder":
            self.popup("addfolder")  # Call to the popup function that creates a popup to get input from the user
            foldername = self.popupresult
            filefunc("buildlist.pickle", "appendfolder", None, foldername)
            self.buildspecialfolder()  # Resets the list of buttons in the canvas
        elif btntype == "deletefolder":
            self.popup("deletefolder")
            foldername = self.popupresult
            filefunc("buildlist.pickle", "deletefolder", None, foldername)
            self.buildspecialfolder()
        elif btntype == "addurl":
            self.popup("addurl")
            urlname = self.popupresult
            self.popup("addurl2")
            urllink = self.popupresult
            filefunc("buildlist.pickle", "appendurl", urllink, foldername, urlname)
            self.buildspecialurl(foldername)
        elif btntype == "deleteurl":
            self.popup("deleteurl")
            urlname = self.popupresult
            filefunc("buildlist.pickle", "deleteurl", None, foldername, urlname)
            self.buildspecialurl(foldername)

    # Function that handles the area in which the scrollbar scrolls the canvas
    def canvasevent(self, event):
        self.scrollcanvas.configure(scrollregion=self.scrollcanvas.bbox("all"), width=300, height=300)

    """ Special """
    def special(self):
        # Destroys all the children from the calculator program
        for child in self.root.winfo_children():
            child.destroy()

        # Label that heads the section for the folder
        self.folderheader = Label(self.root, text="Folders", width=50, font=30, height=2)
        self.folderheader.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

        # Button that add or delete folders
        self.addfolder = Button(self.root, text="Add Folder", width=20, height=3, command=lambda: self.specialhandler("addfolder"))
        self.deletefolder = Button(self.root, text="Delete Folder", width=20, height=3, command=lambda: self.specialhandler("deletefolder"))
        self.addfolder.grid(row=1, column=0, padx=5, pady=5)
        self.deletefolder.grid(row=1, column=1, padx=5, pady=5)

        # Frame inception to create a scrollable frame
        # Also reuses topframe and bottomframe
        self.topframe = Frame(self.root, relief=GROOVE, width=300, height=200, bd=1)
        self.topframe.grid(row=2, column=0, columnspan=2)
        self.scrollcanvas = Canvas(self.topframe)
        self.bottomframe = Frame(self.scrollcanvas)
        self.canvasscrollbar = Scrollbar(self.topframe, orient="vertical", command=self.scrollcanvas.yview)
        self.canvasscrollbar.pack(side="right", fill="y")
        self.scrollcanvas.config(yscrollcommand=self.canvasscrollbar.set)
        self.scrollcanvas.create_window((0,0), window=self.bottomframe, anchor="nw", tags="self.bottomframe")
        self.bottomframe.bind("<Configure>", self.canvasevent)
        self.scrollcanvas.pack(side="left")

        self.buildspecialfolder()  # Builds the button list for folders and this is the first iteration

""" Create an instance of Main(), load buildlist (not sure if necessary), and start the mainloop of tkinter """
x = Main()
x.buildlist = filefunc("buildlist.pickle", "load")
x.root.mainloop()
