import requests
import logging
import subprocess
import time
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

logger.info('starting the server')
with subprocess.Popen(['python', '-m', 'http.server']) as p:
    logger.info('server has started')

    logger.info('sleeping for one second')
    time.sleep(1)

    logger.info('requesting index.html')
    try:
        response = requests.get('http://localhost:8000/index.html')
    except:
        logger.exception('something went wrong with the request')

    logger.info('\nresponse: {}'.format(response.status_code))

    logger.info('shutting down')
    p.terminate()
