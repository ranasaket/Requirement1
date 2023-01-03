import pymysql
import sys
import json
import boto3
from botocore.exceptions import ClientError
ses=boto3.client('ses')
SENDER=" "
conn = pymysql.connect(
        user="root",
        password="",
        host=" ",
        port=3306,
        database="customerrecords"

    )     
def send_emails(name, email):
    try:
       res = ses.send_templated_email(
           Source=SENDER,
           Destination={
           'ToAddresses': [str(email)],
        },
        Template='Keepsl_product_Template',
        TemplateData="{\"user\":\""+str(name)+"\"}"
    )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
      print("Email sent! Message ID:",res['MessageId']),

    return

def lambda_handler(event,context):
    try:
        cur = conn.cursor()
        cur.execute('select * from customer')
        datas=list(cur.fetchall())

        # Get Cursor
        for curs in datas:
            send_emails(curs[1],curs[2])
        
    except pymysql.Error as e:
        print(f"Error connecting to Data Platform: {e}")
        sys.exit(1)


#lambda_handler(None,None)