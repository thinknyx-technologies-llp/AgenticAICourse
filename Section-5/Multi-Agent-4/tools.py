import os
import boto3
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta
from google.cloud import compute_v1
from crewai.tools import tool
from dotenv import load_dotenv

load_dotenv()

class CloudTools:

    @tool("Get AWS EC2 and Cost Data")
    def get_aws_data():
        """Fetches active EC2 instances and estimated monthly cost from AWS."""
        try:
            # 1. Get EC2 Instances
            ec2 = boto3.client(
                'ec2',
                aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                region_name=os.getenv('AWS_REGION_NAME')
            )
            
            response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
            instances = []
            for reservation in response['Reservations']:
                for instance in reservation['Instances']:
                    instances.append({
                        'id': instance['InstanceId'],
                        'type': instance['InstanceType'],
                        'launch_time': str(instance['LaunchTime'])
                    })

            # 2. Get Cost Estimates (Last 30 days)
            ce = boto3.client(
                'ce',
                aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                region_name=os.getenv('AWS_REGION_NAME')
            )
            
            end = datetime.now().date()
            start = end - timedelta(days=30)
            
            cost_response = ce.get_cost_and_usage(
                TimePeriod={'Start': str(start), 'End': str(end)},
                Granularity='MONTHLY',
                Metrics=['UnblendedCost']
            )
            
            total_cost = cost_response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount']
            
            return f"AWS Report:\nRunning EC2 Instances: {len(instances)}\nDetails: {instances}\nEst. Cost (Last 30 Days): ${total_cost}"
            
        except Exception as e:
            return f"Error fetching AWS data: {str(e)}"

    @tool("Get GCP Instance Data")
    def get_gcp_data():
        """Fetches active GCP Compute Engine instances."""
        try:
            # Ensure GOOGLE_APPLICATION_CREDENTIALS is set in .env
            project_id = os.getenv('GCP_PROJECT_ID')
            zone = "us-central1-a" # Default zone, or iterate over zones if needed
            
            instance_client = compute_v1.InstancesClient()
            request = compute_v1.ListInstancesRequest(project=project_id, zone=zone)
            
            instances = []
            for instance in instance_client.list(request=request):
                if instance.status == "RUNNING":
                    instances.append({
                        'name': instance.name,
                        'type': instance.machine_type.split('/')[-1],
                        'status': instance.status
                    })
            
            # Note: Real-time GCP Cost API is complex (requires BigQuery). 
            # We will return instance data and let the Analyst estimate based on standard rates.
            return f"GCP Report:\nRunning Instances: {len(instances)}\nDetails: {instances}\n(Cost requires BigQuery export, please estimate based on machine type standard rates)"

        except Exception as e:
            return f"Error fetching GCP data: {str(e)}"

    @tool("Send Email Report")
    def send_email(report_content: str):
        """Sends the final HTML report via email to the manager."""
        try:
            # Note the 'html' argument here
            msg = MIMEText(report_content, 'html')
            msg['Subject'] = f"Multi-Cloud Infrastructure Report - {datetime.now().date()}"
            msg['From'] = os.getenv('SENDER_EMAIL')
            msg['To'] = os.getenv('RECIPIENT_EMAIL')

            with smtplib.SMTP(os.getenv('SMTP_SERVER'), int(os.getenv('SMTP_PORT'))) as server:
                server.starttls()
                server.login(os.getenv('SENDER_EMAIL'), os.getenv('SENDER_PASSWORD'))
                server.send_message(msg)
            
            return "Email sent successfully."
        except Exception as e:
            return f"Failed to send email: {str(e)}"