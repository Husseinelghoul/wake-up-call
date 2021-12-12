'''
The purpose of this program is to initiate a series of non-ending calls from and to given number(s)
the calls wont stop until the receiving end responds to the call (either answer or decline)
'''
import logging
from time import sleep

from twilio.rest import Client

from utils.constants import FROM, TO, LOG_LEVEL

logging.basicConfig(
    level='WARN',
    format='[%(asctime)s] | %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S',
)

logger = logging.getLogger(__name__)
logger.warning('initializing program')
# pylint: disable=redefined-outer-name
client = Client()
call = client.calls.create(from_=FROM,to=TO,url='http://demo.twilio.com/docs/voice.xml')

logger.warning('initiating a call from %s to %s',call.from_formatted ,call.to_formatted)
logger.warning('call number 1')

def main(call,count=1):
    
    '''this is the main function of the program, it's a recurcive function'''
    if call.update().status in {'busy' , 'in-progress' ,'completed'}:
        logger.warning('call status: busy')
        logger.warning('this event has costed %f %s', call.price or 0.00 , call.price_unit)
        return
    if call.update().status in {'no-answer' , 'failed', 'canceled'}:
        logger.warning('call status: %s',call.update().status)
        logger.warning('call number %d', count+1)
        new_call = client.calls.create(from_=FROM,to=TO,url='http://demo.twilio.com/docs/voice.xml')
        main(new_call,count+1)
    else:
        sleep(5)
        logger.warning('call status: %s',call.update().status)
        main(call,count)

main(call)
logger.warning('program finished running')
