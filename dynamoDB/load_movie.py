import json
from DecimalEncoder import DecimalEncoder
from helpers import *

# Start dynamo session
dynamodb = get_config_and_start_dynamo_session()

# Get movie
data = get_movie(dynamodb, 2002, "8 Mile")

raw_data_path = get_raw_data_path()
raw_data_path.mkdir(parents=True, exist_ok=True)

# Load Decimal Encoder class
decimalEncoder = DecimalEncoder()

with open(raw_data_path / 'current.json', 'w') as f:
    json.dump(data, f, cls=DecimalEncoder, indent=4)
