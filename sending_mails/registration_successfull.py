import pymysql
import sys
import boto3
from botocore.exceptions import ClientError
ses=boto3.client('ses')
SENDER=" "
conn = pymysql.connect(
        user="root",
        password="",
        host=" ",
        port=3306 ,
        database=""

    )     
def send_emails(name, email):
    try:
       res = ses.send_templated_email(
           Source=SENDER,
           Destination={
           'ToAddresses': [str(email)],
        },
        Template='Keepsl_welcome_Template',
        TemplateData="{\"user\":\""+str(name)+"\"}"
    )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
      print("Email sent! Message ID:",res['MessageId']),

    return


def lambda_handler(event, context):
    try:
        cur = conn.cursor()
        cur.execute('select * from customer')
        datas=list(cur.fetchall())

        for curs in datas:
            send_emails(curs[1],curs[2])
    except ClientError as e:
        print(f"Error connecting to Database Platform: {e}")
        sys.exit(1)

# lambda_handler(None,None)