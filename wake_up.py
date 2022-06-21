"""
The purpose of this program is to initiate a series of non-ending calls from and to given number(s)
the calls wont stop until the receiving end responds to the call (either answer or decline)
"""
import logging
import sys
from time import sleep

from twilio.rest import Client

from utils.constants import FROM, LOG_LEVEL, TO

logging.basicConfig(
    level=LOG_LEVEL,
    format="[%(asctime)s] | %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
)
logging.getLogger("twilio").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)
logger.info("initializing program")

if len(sys.argv) > 1:
    logger.info("trying to use sys.argv parameters")
    if len(sys.argv) == 3:
        FROM = "+961" + str(sys.argv[1])
        TO = "+961" + str(sys.argv[2])
    if len(sys.argv) == 2:
        TO = "+961" + str(sys.argv[1])

# pylint: disable=redefined-outer-name
client = Client()
call = client.calls.create(
    from_=FROM, to=TO, url="http://demo.twilio.com/docs/voice.xml"
)
logger.info("initiating a call from %s to %s", call.from_formatted, call.to_formatted)
logger.info("call number %d", 1)


def main(call, latest_status: str = "", count=1):
    """
    this is the main function of the program, it's a recurcive function
    """
    status = call.update().status
    if status != latest_status:
        logger.info("call status: %s", status)
    if status in {"busy", "in-progress", "completed"}:
        logger.info("this event has costed %f %s", call.price or 0.00, call.price_unit)
        return
    if status in {"no-answer", "failed", "canceled"}:
        logger.info("call number %d", count + 1)
        new_call = client.calls.create(
            from_=FROM, to=TO, url="http://demo.twilio.com/docs/voice.xml"
        )
        main(new_call, status, count + 1)
    else:
        sleep(10)
        main(call, status, count)


main(call)
logger.info("program finished running")
