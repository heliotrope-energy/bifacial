# This file is going to experiment with row-to-row spacing from (0.1 to 5.0). More research is required for the upper limit.
# The optimal here is believed to be 1.5

import os 
import threading
from bifacialvf import bifacialvf, readepw, sun, vf, __init__, helper 

os.chdir(os.path.dirname(bifacialvf.__file__))
dir_path = os.path.dirname(os.path.realpath(__file__))
print (dir_path)

beta = 10					# tilt 
C = 1                      # GroundClearance(panel slope lengths)
sazm = 180                  # PV Azimuth(deg)

TMYtoread = "data/724010TYA.csv"   # VA Richmond

# Set optional variables.  These are the default values
rowType = "interior"        # RowType(first interior last single)
transFactor = 0.013         # TransmissionFactor(open area fraction)
cellRows = 6                # CellRows(# hor rows in panel)   This is the number of irradiance values returned along module chord
PVfrontSurface = "glass"    # PVfrontSurface(glass or ARglass)
PVbackSurface = "glass"     # PVbackSurface(glass or ARglass)
albedo = 0.62               # ground albedo beneath system

# 1-axis tracking instructions (optional)
tracking=False
backtrack=True       # backtracking optimization as defined in pvlib

rtr = 0.1                  # row to row spacing in panel lengths. 
    
t2 = threading.Thread(target=helper.threading_helper, args=(1.0, 1.9))
t3 = threading.Thread(target=helper.threading_helper, args=(1.9, 2.9))
t4 = threading.Thread(target=helper.threading_helper, args=(2.9, 3.9))
t5 = threading.Thread(target=helper.threading_helper, args=(3.9, 5.1))


t2.start()
t3.start()
t4.start()
t5.start()


t2.join()
t3.join()
t4.join()
t5.join()
    
print("Done!")






