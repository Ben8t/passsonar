FROM python:3.6

COPY . /app
WORKDIR /app

COPY ./assets/fonts/*.otf /usr/local/share/fonts/
RUN fc-cache -f -v

RUN pip install -r /app/requirements.txt

CMD ["/bin/bash"]