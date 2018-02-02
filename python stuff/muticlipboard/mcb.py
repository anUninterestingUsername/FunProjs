#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.


import shelve, pyperclip, sys
mcbShelf = shelve.open('multiClipBoard')

# Save clipboard content.
currentCB = pyperclip.paste()
command = sys.argv[1].lower()
reservedKeys = ["save", "list", "delete", "undo"]
if len(sys.argv) == 3 and command == 'save':
    if sys.argv[2].lower() in reservedKeys:
        print("Sorry but '"+ sys.argv[2] + "' is a reserved keyword")
    else:
        mcbShelf[sys.argv[2]] = pyperclip.paste()
        print("'"+pyperclip.paste() + "' saved under keyword: " + sys.argv[2])
elif len(sys.argv) == 2:
    #List keywords and load content.
    if command == 'help':
        print("save, list, delete and undo are special commands")
    elif command == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print("The following list of keywords are copied to your clipboard:\n" + pyperclip.paste())
        mcbShelf["undo"] = currentCB
    elif command == "delete":
        confirm = input("You sure u wanna clear the multi-clipboard? (type 'y' to confirm)")
        if confirm == "y":
            mcbShelf.clear()
    elif command in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print("'"+mcbShelf[sys.argv[1]] + "' is copied from keyword: "+ command)
        mcbShelf["undo"] = currentCB
    else:
        print("command not recognised")



mcbShelf.close()