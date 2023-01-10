import pymysql
import json
import sys
import boto3
from botocore.exceptions import ClientError
ses=boto3.client('ses')
SENDER="ranasaket19110@gmail.com "

def send_emails(name, email):
    try:
       res = ses.send_templated_email(
           Source=SENDER,
           Destination={
           'ToAddresses': [str(email)],
        },
        Template='Keepsl_welcome_Template_new',
        TemplateData="{\"user\":\""+str(name)+"\"}"
    )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
      print("Email sent! Message ID:",res['MessageId']),

    return

def lambda_handler(event, context):
    print("Name:",event['queryStringParameters']['name'])
    print("Email:",event['queryStringParameters']['email'])
    name=event['queryStringParameters']['name']
    email=event['queryStringParameters']['email']
    send_emails(name,email)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully sent mail from AWS Lambda!')
        }
    
