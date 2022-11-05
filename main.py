import PortScanner
import sys
import BannerRender as br

br.printBanner("Welcome")
print("_" * 50)
PortScanner.portScan(sys.argv[1])
