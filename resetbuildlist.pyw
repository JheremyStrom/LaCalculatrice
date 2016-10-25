__author__ = "Jheremy Strom"
__Version__ = "1.0"  # Comments modified 10/25/2016

import pickle

""" Opens up the buildlist.pickle file and then resets it to a blank dictionary"""
def resetbuildlist(app=False):  # app=False allows buildlist.pickle to be reset through this file alone

    with open("buildlist.pickle", "wb") as file:
        pickle.dump({}, file)

    # If an app is passed into this function (which will be self of Main(), then run buildspecialfolder() so the list of folders can be refreshed)
    if app:
        app.buildspecialfolder()

""" Uncomment to be able to click resetbuildlist.pyw to manually reset buildlist.pickle """
#resetbuildlist()

""" Uncomment if you want to check what is inside of buildlist.pickle """
# with open("buildlist.pickle", "rb") as file:
#    print(pickle.load(file))
