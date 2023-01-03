import codecs
import boto3
from botocore.exceptions import ClientError

ses=boto3.client('ses')
file = codecs.open("html_templates/payement_reminder_template.html", "r", "utf-8")
z=file.read()


response = ses.create_template(
    Template={
        'TemplateName': 'Keepsl_payment_reminder_Template',
        'SubjectPart': 'KEEPSL Payment Reminder',
        'HtmlPart':str(z)
        ,
    }
)

print(response)


