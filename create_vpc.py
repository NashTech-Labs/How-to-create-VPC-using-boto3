# import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError

AWS_REGION = input("Please enter the AWS_REGION")

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

vpc_resource = boto3.resource("ec2", region_name=AWS_REGION)


def vpc(ip_cidr):
# Configration for VPC creation
    try:
        response = vpc_resource.create_vpc(CidrBlock=ip_cidr,
                                           InstanceTenancy='default',
                                           TagSpecifications=[{
                                               'ResourceType':'vpc',
                                               'Tags': [{
                                                   'Key':'Name',
                                                   'Value':'VPC'
                                               }]
                                           }])

    except ClientError:
        logger.exception('Could not create a custom vpc.')
        raise
    else:
        return response


if __name__ == '__main__':
    IP_CIDR = input("Please enter the IP CIDR")
    logger.info(f'Please wait !! We are creating a custom VPC...')
    my_vpc = vpc(IP_CIDR)
    logger.info(f'Wow!!, Your custom VPC is ready: {my_vpc.id}')