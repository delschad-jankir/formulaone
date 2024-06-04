# How to get started

## Add a config.yaml File
Add a config.yaml file in the root directory which looks like this:

config should look like this:
aws_access_key_id: 'your_access_key_id'
aws_secret_access_key: 'your_secret_access_key'
region_name: 'eu-west-1'

## Start the program
Go into load_movie.py under the dynamodb folder.
Add your own wished movie here:

```python 
# Get movie
data = get_movie(dynamodb, 2002, "8 Mile")
```

Replace year and title with wished movie
