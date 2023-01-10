import json
import boto3
from botocore.exceptions import ClientError
ses=boto3.client('ses')

dels = ses.delete_template(
    TemplateName='Keepsl_welcome_Template'
)
