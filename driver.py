# this is the driver file for the project. it calls all the other python files with the correct arguments
import os
from tkinter import OUTSIDE

'''
py main.py --f PWR --s 10 --cmd 'https://www.google.com/'

runs the main script for every framework and page
passes along the runtime and repeat parameters to the main script

'''
runtime = 30

repeat = 5

OUTDIR = ("out")
# If folder doesn't exist, then create it.
if not os.path.isdir(OUTDIR):
    os.makedirs(OUTDIR)
    print("INFO: created out directory")
else :
 print("INFO: out directory already created")

# array containing pairs of: framework , sites
pages = [ ("Vue" 
          , [ ("9gag","https://9gag.com/")
            , ("gitlab","https://docs.gitlab.com/ee/user/project/issues/")
            , ("nintendo","https://www.nintendo.co.uk/")
            , ("euronews","https://www.euronews.com/")
            , ("torneo","https://www.torneo.ca/") ])
        , ("Angular" 
          , [ ("db","https://www.db.com/index?language_id=1&kid=sl.redirect-en.shortcut")
            , ("forbes","https://www.forbes.com/")
            , ("paypal","https://www.paypal.com/nl/home/")
            , ("upwork","https://www.upwork.com/")
            , ("google","https://www.google.nl/") ])
        , ("React" 
          , [ ("airbnb","https://www.airbnb.com/")
            , ("nytimes","https://www.nytimes.com/")
            , ("codecademy","https://www.codecademy.com/")
            , ("atlassian","https://www.atlassian.com/")
            , ("scribd","https://www.scribd.com/") ])
        , ("Svelte" 
          , [ ("spotify","https://www.spotify.com/nl/about-us/contact/")
            , ("note","https://note.com/")
            , ("squareup","https://squareup.com/us/en/")
            , ("templatemonster","https://www.templatemonster.com/")
            , ("sentry","https://sentry.io/welcome/") ])]

for framework in pages:
    name = framework[0]
    # for every framework and every page belonging to that framework call the main.py script.
    for page in framework[1]: 
     cmd = "py main.py --f " + name+"_"+page[0] + " --n "+ str(repeat) +" " +  " --s " + str(runtime) + " --cmd " + page[1]
     print("DEBUG: "+cmd)
     os.system(cmd)