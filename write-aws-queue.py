#UPDATE

import sys
import boto.sqs
import boto.sqs.queue
import urllib2
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError

name = sys.argv[1]
queue_message = sys.argv[2]

response = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
html = response.read().split(':')
access_key_id = html[0]
secret_access_key = html[1]

conn = boto.sqs.connect_to_region('eu-west-1', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

queue = conn.get_queue(name)

try:
	conn.send_message(queue,queue_message)
	print('Message added ' + queue_message)

except Exception, e:
	print(e)


