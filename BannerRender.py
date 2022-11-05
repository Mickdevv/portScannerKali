from pyfiglet import Figlet

def printBanner(banner):
    fonts = ['roman', 'doh', 'banner4', 'char3___', 'banner3', 'clb8x10', 'colossal', 'univers', 'starwars']
    # Print banner
    f = Figlet(font=fonts[-3])
    print(f.renderText(banner))