import json
import pymysql
import sys
import json
import boto3
from botocore.exceptions import ClientError
ses=boto3.client('ses')
SENDER=" "
conn = pymysql.connect(
        user="root",
        password=" ",
        host=" ",
        port=3306,
        database="customerrecords"

    )     

def send_emails(name, email,date):
    try:
       res = ses.send_templated_email(
           Source=SENDER,
           Destination={
           'ToAddresses': [str(email)],
        },
        Template='Keepsl_payment_reminder_Template',
        TemplateData="{\"user\":\""+str(name)+"\", \"date\": \""+str(date)+"\" }"
    )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
      print("Email sent! Message ID:",res['MessageId']),

    return

def lambda_handler(event, context):
    try:
        cur = conn.cursor()
        cur.execute('select * from customer_payment')
        datas=list(cur.fetchall())

         # Get Cursor
        for curs in datas:
            send_emails(curs[1],curs[2],curs[3])
            #print(curs[1],curs[2],curs[3])

    except ClientError as e:
        print(f"Error connecting to Database Platform: {e}")
        sys.exit(1)


#lambda_handler(None,None)