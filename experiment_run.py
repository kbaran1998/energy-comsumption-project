"""
Runner file for the project. it calls all the other python files with the correct arguments

python main.py --f PWR --s 10 --cmd 'https://www.google.com/'

runs the main script for every framework and page
passes along the runtime and repeat parameters to the main script

"""
import os
from page_list import pages

TEST_RUN_TIME = 30
REPEAT = 5
OUT_DIR = "out"

# If folder doesn't exist, then create it.
if not os.path.isdir(OUT_DIR):
    os.makedirs(OUT_DIR)
    print(f"INFO: created {OUT_DIR} directory")
else :
    print(f"INFO: {OUT_DIR} directory already created")

# array containing pairs of: framework , sites


for framework in pages :
    # for every framework and every page belonging to that framework call the main.py script.
    for page in pages[framework]:
        cmd = f"python main.py --f {framework}_{page[0]} --n {REPEAT} --s {TEST_RUN_TIME} --cmd {page[1]}"
        print("DEBUG: "+cmd)
        os.system(cmd)
