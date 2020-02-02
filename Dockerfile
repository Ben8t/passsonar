FROM python:3.6

RUN apt-get update -y && \
    apt-get install texlive-latex-extra texlive-fonts-recommended dvipng -y

COPY . /app
COPY ./assets/fonts/*.ttf /usr/local/share/fonts/

WORKDIR /app

RUN fc-cache -f -v

RUN pip install -r /app/requirements.txt

CMD ["/bin/bash"]