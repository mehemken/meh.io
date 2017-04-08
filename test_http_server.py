import pytest
import requests
import subprocess
import time
import atexit
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

@pytest.fixture
def httpd(request):
    p = subprocess.Popen(['python', '-m', 'http.server'])
    logger.info('server has started')

    logger.info('sleeping for one second')
    time.sleep(.123)

    def fin():
        logger.info('shutting down')
        def close_subprocess():
            p.kill()
        atexit.register(close_subprocess)

    request.addfinalizer(fin)
    return httpd


def test_server(httpd):
    response = requests.get('http://localhost:8000/index.html')
    logger.info('asserting response is 200')
    assert response.status_code == 200
