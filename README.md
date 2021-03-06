# energy-comsumption-project

Energy consumption project for Frontend JavaScript frameworks (React, Vue, Angular, Svelte).

## Set up on your machine
1. Make sure you have python and pip installed (and download [Power Gadget 3.6](https://www.intel.com/content/www/us/en/developer/articles/tool/power-gadget.html)).
```bash
python3 -m pip install --user --upgrade pip
python3 -m pip --version
python3 -m pip install --user virtualenv
```
2. Create and activate virtual environment (preferably in Git Bash).

```bash
python3 -m venv venv
source venv/Scripts/activate
```

OR

```bash
python3 -m venv venv
.\venv\Scripts\activate
```


3. Install all packages in ```requirements.txt``` with pip. If you need to use a python package, put it there.
```bash
pip install -r requirements.txt
```
4. Download the necessary selenium webdrivers (make sure you also have "chrome", "firefox", "ie", "edge" and "opera" browsers downloaded on your machine).
```bash
python drivers/driver_downloader.py
```
5. Create a ```configurations.ini``` and copy the following configurations (of course replace the place holder ```__your_path__``` with your actual paths to the downloaded drivers):
```python
[DRIVER_PATHS]
EDGE_EXE_PATH=__your_path__\\.wdm\\drivers\\edgedriver\\win64\\98.0.1108.62\\msedgedriver.exe
OPERA_EXE_PATH=__your_path__\\.wdm\\drivers\\operadriver\\win64\\v.98.0.4758.82\\operadriver_win64\\operadriver.exe
CHROME_EXE_PATH=__your_path__\\.wdm\\drivers\\chromedriver\\win32\\98.0.4758.102\\chromedriver.exe
FIREFOX_EXE_PATH=__your_path__\\.wdm\\drivers\\geckodriver\\win64\\v0.30.0\\geckodriver.exe
IE_EXE_PATH=__your_path__\\.wdm\\drivers\\IEDriverServer\\win64\\4.0.0\\IEDriverServer.exe
```
6. To run the experiments run scripts:
```bash
python experiment_run.py
```

7. To get parsed csv files within new generated directory ```out``` and get results for each framework and website run:
```bash
python parsers/parse.py
```

8. Once you have finished working within the virtual environment, you can deactivate it.
```bash
deactivate
```
