# opendataportal
Open data portal access web application for GEOG483 project

# To run server
Ensure you have flask and watson-developer-cloud libararies by installing them via `pip install flask` and `pip install watson-developer-cloud`

After, navigate to your local version of this repository via command line (`cd \path\to\folder\flaskr`). To initiate Flask server:  

  `export FLASK_APP=flaskr` (use `set` instead of `export` on Windows)  
  `export FLASK_DEBUG=true` (use `set` instead of `export` on Windows)  
  `flask run`  
  
If all goes according to plan, you should now be up and running on [http://localhost:5000/](http://localhost:5000/).

# How is it working?
flaskr.py is a Flask app that initiates a server. It can route GET and POST requests from the client. The `templates` folder holds various HTML templates that the Python script can interact with and publish. These HTML templates can be update via Python and [Jinja2](http://jinja.pocoo.org/docs/2.10/). That's how the web application will create content on the fly, such as Leaflet maps. 

The `callWatson` function interacts with the Watson API. Pay particular attention to the `output` part of the returned JSON, which is where we can customize `responses` to the user, and call other Python functions with `actions`. In order to make this work, you will need to place a `keys` module in the top level folder to access the API.
