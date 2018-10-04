import pickle

from google.cloud import bigquery
from google.cloud.bigquery import Dataset,LoadJobConfig


client = bigquery.Client()
source_dataset = bigquery.DatasetReference( 'bigquery-public-data', 'samples')
dataset_id = 'dataset_name'
source_table_ref = source_dataset.table('shakespeare')
dest_table_ref = client.dataset(dataset_id).table('destination_table')
job = client.copy_table( source_table_ref, dest_table_ref, location='US')

x = pickle.dumps( job._properties )





client = bigquery.Client()
source_dataset = bigquery.DatasetReference( 'bigquery-public-data', 'samples')
dataset_id = 'dataset_name'
source_table_ref = source_dataset.table('shakespeare')
dest_table_ref = client.dataset(dataset_id).table('destination_table')

y = pickle.loads( x )
j = bigquery.job.CopyJob.from_api_repr( y , client)

print( j )