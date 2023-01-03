step 1: Install pymysql in your local machine
step 2: Create AWS account to use AWS lambda,AWS RDS and AWS SES service.
Step 3: Sign-in AWS SES account and then run all the code one by one which is in Template_Creation_code folder in your local Machine.
step 4: Create a RDS maria db and then connect it to the MYSQLworkbench tool which you have to download first for your local machine.
step 5: create database schema customerrecordsand two tables customer(id,cust_name,cust_email) and customer_payment(id, cust_name,cust_email,payment_date)
       and insert some data.
step 6: Make 3 AWS Lambda function irrespective for all 3 code which is in sending_mails folder.
step 7: Paste the code one by one in lambda_function file. If you want to run codes in local machine, then remove the last comment of all codes(send_mails) 


Note: for Importing error first install pymysql in a local folder, the zip that folder and add it to the AWS lambda Layer option.
