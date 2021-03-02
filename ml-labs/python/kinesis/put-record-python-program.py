{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\margl1440\margr1440\vieww28600\viewh17480\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import requests\
import boto3\
import uuid\
import time\
import random\
import json\
\
client = boto3.client('kinesis', region_name='<INSERT_YOUR_REGION>')\
partition_key = str(uuid.uuid4())\
\
# Added 08/2020 since randomuser.me is starting to throttle API calls\
# The following code loads 500 random users into memory\
number_of_results = 500\
r = requests.get('https://randomuser.me/api/?exc=login&results=' + str(number_of_results))\
data = r.json()["results"]\
\
while True:\
        # The following chooses a random user from the 500 random users pulled from the API in a single API call.\
        random_user_index = int(random.uniform(0, (number_of_results - 1)))\
        random_user = data[random_user_index]\
        random_user = json.dumps(data[random_user_index])\
        client.put_record(\
                StreamName='<INSERT_YOUR_STREAM_NAME>',\
                Data=random_user,\
                PartitionKey=partition_key)\
        time.sleep(random.uniform(0, 1))\
}