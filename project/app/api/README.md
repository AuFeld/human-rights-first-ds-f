# api

This directory contains all directories and files used in the creation of the DS API and its connections with the main DS app.

## Contents

*• viz.py* —— API endpoint instance created by labs 25 to send a choropleth visualization to the web team. Labs 27 didn't use or explore this much.

*• update.py* —— API endpoint instance created by labs 25 to update the backlog.csv file in the projects directory. Labs 27 didn't use or explore this much.

*• predict.py* —— API endpoint instance created by labs 25 and slightly modified by labs 27 that allows the use of the predictive model as an endpoint.

*• getdata.py* —— API endpoint instance created by labs 25 and recreated with modifications by labs 27 that creates a jsonified version of the all_sources_geoed.csv file as a get endpoint.

*• getcounthelper.py* —— Function created by labs 28 that creates a pandas dataframe of the number of times each type of force was used in all_sources_geoed.csv file.

*• getcount.py* —— API endpoint instance created by labs 28 that creates a jsonified version of the pandas dataframe created by getcounthelper.py as a get endpoint.

*• get_timeline.py* —— API endpoint instance created by labs 28 that creates a jsonified version of the relevant data to the timeline created by the frontend web developers as a get endpoint.

*• __init__.py* —— File that initializes the API and ties in all the modules found within the api directory.