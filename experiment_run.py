"""
Runner file for the project. it calls all the other python files with the correct arguments

python main.py --f PWR --s 10 --cmd 'https://www.google.com/'

runs the main script for every framework and page
passes along the runtime and repeat parameters to the main script

"""
import os

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
pages = {
  "Vue" : [
    ("9gag", "https://9gag.com/"),
    ("gitlab", "https://docs.gitlab.com/ee/user/project/issues/"),
    ("nintendo", "https://www.nintendo.co.uk/"),
    ("euronews", "https://www.euronews.com/"),
    ("torneo", "https://www.torneo.ca/")
  ],
  "Angular" : [
    ("db", "https://www.db.com/index?language_id=1&kid=sl.redirect-en.shortcut"),
    ("forbes", "https://www.forbes.com/"),
    ("paypal", "https://www.paypal.com/nl/home/"),
    ("upwork", "https://www.upwork.com/"),
    ("google", "https://www.google.nl/")
  ],
  "React" : [
    ("airbnb", "https://www.airbnb.com/"),
    ("nytimes", "https://www.nytimes.com/"),
    ("codecademy", "https://www.codecademy.com/"),
    ("atlassian", "https://www.atlassian.com/"),
    ("scribd", "https://www.scribd.com/")
  ],
  "Svelte" : [
    ("spotify", "https://www.spotify.com/nl/about-us/contact/"),
    ("note", "https://note.com/"),
    ("squareup", "https://squareup.com/us/en/"),
    ("templatemonster", "https://www.templatemonster.com/"),
    ("sentry", "https://sentry.io/welcome/")
  ]
}

for framework in pages :
    # for every framework and every page belonging to that framework call the main.py script.
    for page in pages[framework]:
        cmd = f"python main.py --f {framework}_{page[0]} --n {REPEAT} --s {TEST_RUN_TIME} --cmd {page[1]}"
        print("DEBUG: "+cmd)
        os.system(cmd)
