import bifacialvf, __init__, readepw, sun, vf 
import os

os.chdir(os.path.dirname(bifacialvf.__file__))
dir_path = os.path.dirname(os.path.realpath(__file__))
print (dir_path)

beta = 10
C = 1                      # GroundClearance(panel slope lengths)
sazm = 180				   # PV Azimuth(deg)

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

rtr = 1.0                  # row to row spacing in panel lengths. The min turned out to be  

while rtr < 5.1: 
    writefiletitle = "Output/rtr" + str(rtr) 
    bifacialvf.simulate(TMYtoread, writefiletitle, beta, sazm, 
                C=C, rtr = rtr, rowType=rowType, transFactor=transFactor, cellRows=cellRows,
                PVfrontSurface=PVfrontSurface, PVbackSurface=PVbackSurface, albedo=albedo, 
                tracking=tracking, backtrack=backtrack, )
    rtr = rtr+0.1