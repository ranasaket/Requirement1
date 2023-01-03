import json
import boto3
import codecs
from botocore.exceptions import ClientError

ses=boto3.client('ses')
file = codecs.open("html_templates/features_template.html", "r", "utf-8")
z=file.read()

response = ses.create_template(
    Template={
        'TemplateName': 'Keepsl_product_Template',
        'SubjectPart': 'Keepsl_products updates',
        'HtmlPart':str(z),
    }
)

print(response)

