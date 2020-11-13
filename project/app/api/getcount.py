from fastapi import APIRouter, HTTPException
import pandas as pd
import numpy as np
# from .update import backlog_path  # Use this when able to get the backlog.csv filled correctly
from ast import literal_eval
import os
import json
import ast
import app.api.getcounthelper as gch

router = APIRouter()

@router.get('/getcount')
async def getcount():
    '''
    Get jsonified dataset from all_sources_geoed.csv
    '''

    # Path to dataset used in our endpoint
    locs_path = os.path.join(os.path.dirname(
        __file__), '..', '..', 'all_sources_geoed.csv')

    df = pd.read_csv(locs_path)
    # Got rid of unnecessary columns
    columns = ["Unnamed: 0", "src", "state", "city", "desc", "geolocation", "title", "date", "date_text", "id", "lat", "long"]
    df = df.drop(columns=columns)

    # Removes the string type output from columns tags
    for i in range(len(df)):
        df['tags'][i] = ast.literal_eval(df['tags'][i])
    
    force = gch.helper(df)

    """
    Convert data to useable json format
    ### Response
    dateframe: JSON object
    """
    return json.loads(force.to_json(orient="table"))
