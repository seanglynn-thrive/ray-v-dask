
from dask_bigquery import read_gbq

# Define the project and dataset
project_id = 'bigquery-public-data'
dataset_id = 'samples'
table_id = 'wikipedia'

# SQL query to
ddf = read_gbq(
    project_id=project_id,
    dataset_id=dataset_id,
    table_id=table_id,
)

# Display Dask DataFrame
print(ddf.head())
