#!/usr/bin/env python
'''
====================================================================================================================
Complutense University Of Madrid
Astrophysics Department
PhD's Project: To Statistically Study the Seasonal Night Sky Brightness and Color Evolution in Madrid.
Directors: - Ph.D. Jaime Zamorano
           - Ph.D. Sergio Pascual
Script Developed By: Jose Robles, Ph.D. student  email: josrob01@ucm.es

ASTMON Script tasks: 1_Call a .sh file 
                     2_Run executable .sh file to download URL via wget -r --no-parent URL
                     3_Download dynamic content locally
                     4_Upload info to Google Drive via R-Clone


====================================================================================================================
'''

import subprocess
from subprocess import call


# Call .sh file 
subprocess.call(['PATH TO THE .sh FILE'])
