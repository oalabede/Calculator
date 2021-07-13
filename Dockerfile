FROM python:3.8.7

ADD . .

RUN pip install -r requirements.txt

CMD [ "python", "-m", "unittest", "discover", "-s", "Test" ]