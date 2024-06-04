from pathlib import Path
import yaml
import os
import boto3


def get_path_to_data():
    """Return path to data."""
    # Your functionality here
    return Path('Data/')


def get_raw_data_path():
    """Return path to raw data."""
    # Your functionality here 
    return get_path_to_data() / 'RawData'


def get_tidy_data_path():
    """Return path to tidy data."""
    # Your functionality here
    return get_path_to_data() / 'TidyData'

import yaml
import os
import boto3

import yaml
import os
import boto3

def get_config_and_start_dynamo_session():
    """
    Reads the configuration file, checks the required fields, and starts a DynamoDB session.

    """
    config_file = Path(__file__).parent / 'config.yaml'

    # Check if config exists
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"The configuration file was not found: {config_file}")

    # Read the config
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)

    # Check fields
    required_fields = ['aws_access_key_id', 'aws_secret_access_key', 'region_name']
    for field in required_fields:
        if field not in config:
            raise KeyError(f"The required field '{field}' is missing.")
        if not config[field]:
            raise ValueError(f"The required field '{field}' is empty.")

    # Start Dynamo session
    session = boto3.Session(
        aws_access_key_id=config['aws_access_key_id'],
        aws_secret_access_key=config['aws_secret_access_key']
    )

    dynamo_resource = session.resource(
        'dynamodb',
        region_name=config['region_name']
    )

    return dynamo_resource

def get_all_tables (dynamo_resource):
    tables = []
    for table in dynamo_resource.tables.all():
        print(table.name)
        tables.append(table.name)
    return tables

def get_movie(dynamo_resource, year, title):
    movies = dynamo_resource.Table('doc-example-table-movies')
    movie = movies.get_item(Key={'year': year, 'title': title})
    return movie