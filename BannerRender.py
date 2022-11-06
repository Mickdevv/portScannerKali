from pyfiglet import Figlet
import random

def printBanner(banner):
    #fonts = ['roman', 'doh', 'banner4', 'char3___', 'banner3', 'clb8x10', 'colossal', 'univers', 'starwars']
    # Print banner
    #f = Figlet(font=fonts[random.randint(0, len(fonts)-1)])
    f = Figlet(font="banner")
    print(f.renderText(banner))
    print("_" * 50)
