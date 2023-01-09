import json
import pymysql
import sys
import json
import boto3
from botocore.exceptions import ClientError
ses=boto3.client('ses')
SENDER=" "
conn = pymysql.connect(
        user="admin",
        password="saketrana",
        host="database-1.ciqfjj2rs3ed.us-east-1.rds.amazonaws.com",
        port=3306,
        database="Person"

    )     
#m=int(input('Enter the order quantity:'))


def lambda_handler(event, context):
    try:
        cur = conn.cursor()
        stmt="SELECT * FROM Customer  WHERE renew_date BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 3 DAY)"
        cur.execute(stmt)
        datas=list(cur.fetchall())
        # print(datas)    
        #  # Get Cursor
        for curs in datas:
            print(curs[1],curs[2],curs[3])

    except ClientError as e:
        print(f"Error connecting to Database Platform: {e}")
        sys.exit(1)


lambda_handler(None,None)

# def send_emails(name, email,date):
#     try:
#        res = ses.send_templated_email(
#            Source=SENDER,
#            Destination={
#            'ToAddresses': [str(email)],
#         },
#         Template='Keepsl_payment_reminder_Template',
#         TemplateData="{\"user\":\""+str(name)+"\", \"date\": \""+str(date)+"\" }"
#     )
#     except ClientError as e:
#         print(e.response['Error']['Message'])
#     else:
#       print("Email sent! Message ID:",res['MessageId']),

#     return
