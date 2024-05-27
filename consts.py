from openai import AzureOpenAI

import os
from dotenv import load_dotenv
load_dotenv()

client = AzureOpenAI(
        azure_endpoint=os.getenv('AZURE_ENDPOINT'),
        api_key=os.getenv('AZURE_API_KEY'),
        api_version="2023-05-15"
    )

input_file_path = 'data/input_data.csv'
output_csv_path = 'data/output_data.csv'

table_name = "products"
