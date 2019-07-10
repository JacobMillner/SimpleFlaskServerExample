# SimpleFlaskServerExample
This is a simple example of a Flask server. It responds to GET requests to root with a JSON timestamp in UTC ISO format.

# Instructions
For Linux:
Make sure you have [Python 3](https://docs.python-guide.org/starting/install3/linux/) and [Flask](http://flask.pocoo.org/docs/1.0/installation/) installed.
Tell your terminal which application to work with by exporting the FLASK_APP environment variable.
```
$ export FLASK_APP=time_server.py
```
Run the Flask app!
```
$ flask run
 * Running on http://127.0.0.1:5000/
```

For Windows:
Make sure you have [Python 3](https://www.python.org/downloads/windows/) and [Flask](http://flask.pocoo.org/docs/1.0/installation/) installed.
In PowerShell set the environment variable for FLASK_APP.
```
PS C:\path\to\app> $env:FLASK_APP = "time_server.py"
```
Now run the Flask app!
```
PS C:\path\to\app> python time_server.py
```

After that, just use curl to send a GET request or point your browser to http://127.0.0.1:5000/ and see your timestamp.
