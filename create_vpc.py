# By Muzakkir Saifi
# import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError

REGION = input("Please enter the REGION")
Tag=input("Enter the tag name: ")
Tag_Value=input("Enter the tag value: ")

logger_for = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

vpc_resource = boto3.resource("ec2", region_name=REGION)


def vpc(ip_cidr):
# Configration for VPC creation
    try:
        res = vpc_resource.create_vpc(CidrBlock=ip_cidr,
                                           InstanceTenancy='default',
                                           TagSpecifications=[{
                                               'ResourceType':'vpc',
                                               'Tags': [{
                                                   'Key':Tag,
                                                   'Value':Tag_Value
                                               }]
                                           }])

    except ClientError:
        logger_for.exception('Oops sorry, Your VPC can not be created.')
        raise
    else:
        return res


if __name__ == '__main__':
    CIDR = input("Please enter the IP CIDR")
    logger_for.info(f'Please wait !! We are creating a custom VPC...')
    my_vpc = vpc(CIDR)
    logger_for.info(f'Wow!!, Your custom VPC is ready: {my_vpc.id}')