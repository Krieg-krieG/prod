FROM python


WORKDIR /app

COPY ./code/requirements.txt requirements.txt

COPY ./code/ .

RUN pip3 install PyInstaller

RUN pip3 install -r requirements.txt

CMD python3 -m PyInstaller --onefile  *.py





