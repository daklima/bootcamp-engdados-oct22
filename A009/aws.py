import boto3
from botocore.exceptions import ClientError
import logging
from dotenv import load_dotenv
from os import getenv

#%%
load_dotenv('D:\Documentos\.env')

#%%
s3_client  = boto3.client(
    's3',
    aws_access_key_id = getenv('AWS_ID'),
    aws_secret_access_key = getenv('AWS_KEY')
)

# %%
def create_bucket(name):
    try:
        s3_client.create_bucket(Bucket=name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

# %%
create_bucket('dakl-s3-bucket-bootcamp-eng-dados')
# %%
