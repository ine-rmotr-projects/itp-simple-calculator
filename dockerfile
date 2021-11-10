FROM python:3.7

WORKDIR /itp-simple-calculator

COPY . .

RUN apt-get -y update

RUN pip3 install -r requirements.txt

CMD [ "python","./calculator.py"
