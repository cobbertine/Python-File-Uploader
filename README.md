# PyFiUp - (Py)THON (Fi)LE (Up)LOADER

## Requirements
This was developed with Python 3.8.2; any OS running this version of Python should work.

For Windows users, the .exe is intended to be standalone and should have no pre-requisites.

## Usage

### Launching

Launch parameters:

* --interface (IP) e.g. --interface 192.168.1.100 (default is "0.0.0.0"; all interfaces)
* --port (port number) e.g. --port 10000 (default is "9337")
* --output (output path) e.g. --output /tmp/ (default is ./uploads)

Note: Windows users can probably just use "python", while Linux users will likely need to use "python3" when typing the following commands in a terminal.

Launch examples:

```
python3 PyFiUp.py (Start the server on all interfaces, bound to port 9337, outputting to ./uploads)

python3 PyFiUp.py --interface 192.168.1.100 --port 10000 --output /tmp (Start the server on 192.168.1.100, bound to port 10000, outputting to /tmp/)
```

### Accessing

Once the script is running, open up a browser and access the "/upload" page.

Note: You must determine yourself what IP address your computer has on your LAN.

Example:

```
http://192.168.1.100:10000/upload
```

## Client-side setup

### Python standard
* Open up a terminal and clone the repo
* Change to the repo's folder
* Type "pip install -r requirements.txt"
* Run PyFiUp.py using the information in the **Usage** section

### Python virtual environment
* Open up a terminal and clone the repo
* Change to the repo's folder
* Type "pip install pipenv" (Some users may need to use "pip3" instead of "pip")
* Type "pipenv install --ignore-pipfile"
* After successful installation, type "pipenv shell" (PyFiUp will only work inside a pipenv shell)
* Run PyFiUp.py using the information in the **Usage** section

### Docker
* Install Docker and Docker Compose. Go to the official Docker website for instructions.
* Open up a terminal and clone the repo
* Change to the repo's folder
* **Note: Docker will bind to the port 9337 on the host. If this is not OK, make the necessary changes in Dockerfile & docker-compose.yml**
* Type: "docker-compose up --build -d"
* This will automatically create the "uploads" folder in the PyFiUp directory.
* Access PyFiUp using the information in the **Usage/Accessing** section

### .exe (Windows Only)
Note: This .exe was created by using "nuitka" which compiles python scripts into .exes

* Go to the releases tab on this website and download pyfiup-win.zip
* Open up a file explorer and navigate to the downloaded file
* Unzip the file
* View the unzipped files 
* Hold down shift and right click anywhere in the window
* In the pop-up menu, an item saying "Open Powershell/Command Prompt window here" should be available. Click it.
* Type ".\PyFiUp.exe" followed by the parameters described in the **Usage** section