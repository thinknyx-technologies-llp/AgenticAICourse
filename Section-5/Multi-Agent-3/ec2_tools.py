import boto3
import os
from dotenv import load_dotenv
from crewai.tools import tool

load_dotenv()

class EC2Tools:
    @tool("Fetch EC2 Status")
    def fetch_ec2_status():
        """
        Fetches a list of all EC2 instances in the configured AWS region.
        Returns details including Instance ID, Type, State, and Public IP.
        Useful for checking how many machines are running and their types.
        """
        try:
            ec2 = boto3.client(
                'ec2',
                region_name=os.getenv('AWS_REGION_NAME'),
                aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
            )

            response = ec2.describe_instances()
            
            instances = []
            
            for reservation in response['Reservations']:
                for instance in reservation['Instances']:
                    instances.append({
                        "InstanceID": instance['InstanceId'],
                        "Type": instance['InstanceType'],
                        "State": instance['State']['Name'],
                        "PublicIP": instance.get('PublicIpAddress', 'N/A')
                    })

            if not instances:
                return "No EC2 instances found in this region."

            # Format the list as a readable string for the Agent
            result_str = "--- EC2 INSTANCE REPORT ---\n"
            for inst in instances:
                result_str += f"ID: {inst['InstanceID']} | Type: {inst['Type']} | State: {inst['State']} | IP: {inst['PublicIP']}\n"

            return result_str

        except Exception as e:
            return f"Error fetching EC2 data: {str(e)}"