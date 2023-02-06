from UI import Terminal,GUI,UI
from sys import argv

def usage():   
    print(f"""
Usage: {argv[0]} [g | t]
g : play with the GUI
t : play with the Terminal""")
    x =input()
    if x =='g':
        ui = GUI()
        ui.run()
    elif x =='t':
        ui = Terminal()
        ui.run()
    else:
        raise ValueError("Input should be either 'g' or 't'")


usage()