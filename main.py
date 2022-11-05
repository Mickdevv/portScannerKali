import PortScanner
import sys
from BannerRender import printBanner as br

br.printBanner("Welcome")

PortScanner.portScan(sys.argv[0])
