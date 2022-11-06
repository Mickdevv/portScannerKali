import PortScanner
import sys
import BannerRender as br

br.printBanner("Welcome")

if __name__ == "__main__":
    PortScanner.portScanMain(sys.argv[1], int(sys.argv[2]))
