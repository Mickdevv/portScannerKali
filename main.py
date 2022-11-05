import PortScanner
import sys
import BannerRender as br

br.printBanner("Welcome")

PortScanner.portScan(sys.argv[0])
