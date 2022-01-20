# Seting the python env from IBM image
FROM python:slim AS base
RUN apt-get update && apt-get clean
RUN apt-get update \
    && apt-get install -y wget\
    && apt-get install -y curl \
    && apt-get install -y gnupg \
    && apt-get install -yqq unzip\
    && rm -rf /var/lib/apt/lists/*

# Install Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get -y install google-chrome-stable

# install chromedriver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin

# Seting up scraper env
COPY ./requirements.txt /action/requirements.txt

# Installing python libs
RUN pip install -r /action/requirements.txt

# Add the project scripts
RUN mkdir /scrape
Copy . /action/
WORKDIR /action

###########START NEW IMAGE : DEBUGGER ###################
FROM base as debug
RUN pip install ptvsd

# run debugger
CMD python -b -m ptvsd --host 0.0.0.0 --port 5678 --wait .

###########START NEW IMAGE: PRODUCTION ###################
FROM base as prod

CMD python .