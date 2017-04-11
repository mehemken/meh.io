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
    """Run a python http.server in the files directory."""

    args = ['python', '-m', 'http.server', '8001']
    p = subprocess.Popen(args)
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


def test_index(httpd):
    response = requests.get('http://localhost:8001/files/index.html')
    logger.info('asserting response is 200')
    assert response.status_code == 200

def test_resume_page(httpd):
    response = requests.get('http://localhost:8001/files/resume/')
    logger.info('asserting response is 200')
    assert response.status_code == 200

def test_resume_pdf(httpd):
    response = requests.get('http://localhost:8001/files/static/resume/resume.pdf')
    logger.info('asserting response is 200')
    assert response.status_code == 200
