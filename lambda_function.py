import json
import os
import sys
import subprocess
import boto3
from hdbcli import dbapi

#####instance info########
region = 'cn-northwest-1'
instances = ['instanceid']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
        
    conn = dbapi.connect(
        address="hana-privateip/overlayip", 
        port=30015, 
#           user="lambdahanauser", 
        user="SAPHANADB", 
        password="*********"
    )
    cursor = conn.cursor()
    sql_command = "select count(*) from SAPHANADB.USR41"
    cursor.execute(sql_command)
    (number_of_rows,)=cursor.fetchone()
    
#####check instance status########
#####n=user session########    
    if (number_of_rows) >'n':
#####start new instance########
 #       def lambda_handler(event, context):
        ec2.start_instances(InstanceIds=instances)
        print('started your instances: ' + str(instances))
    elif (number_of_rows) <'m':
#####m=user session########    
#        def lambda_handler(event, context):
        ec2.stop_instances(InstanceIds=instances)
        print('stop your instances: ' + str(instances))    
    cursor.close()
    conn.close()