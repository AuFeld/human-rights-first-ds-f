from fastapi import APIRouter
import pandas as pd
import os
import json

router = APIRouter()

@router.get('/get_timeline')
async def get_timeline():
    '''
    Get jsonified dataset from timeline_tags.csv
    '''

    # Path to dataset used in our endpoint
    locs_path = os.path.join(os.path.dirname(
        __file__), '..', '..', 'timeline_tags.csv')

    df = pd.read_csv(locs_path)

    """
    Convert data to useable json format
    ### Response
    dateframe: JSON object
    """
    # Initial conversion to json
    result = df.to_json(orient="table")
    # Parse the jsonified data
    parsed = json.loads(result)
    return parsed