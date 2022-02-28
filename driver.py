# this is the driver file for the project. it calls all the other python files with the correct arguments
import os
from tkinter import OUTSIDE


OUTDIR = ("out")
# If folder doesn't exist, then create it.
if not os.path.isdir(OUTDIR):
    os.makedirs(OUTDIR)
    print("created out")
else :
 print("already created")