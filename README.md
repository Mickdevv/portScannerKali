# portScannerKali

This is a port scanner app written in Python that uses Docker for deployment, 
Git for version control, mongoDB as a database, and various libraries to complete its funciton.

Running the Docker file runs the application. It takes 2 arguments : the URL you wish to scan, and the amount of times to perform the scan.
The range of the scan is changeable within the PortScanner.py file at lines 99 and 100.

The progress bar only works when the program is run in the terminal, I'm not sure why. 
Libraries to install foir this to run : pymongo, pyfiglet, tdqm
