FROM python:3.6

COPY . /app
WORKDIR /app

RUN apt-get update -y
RUN apt-get install texlive-latex-extra texlive-fonts-recommended dvipng -y

COPY ./assets/fonts/*.ttf /usr/local/share/fonts/

RUN fc-cache -f -v

RUN pip install -r /app/requirements.txt

CMD ["/bin/bash"]