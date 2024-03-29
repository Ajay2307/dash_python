FROM python

EXPOSE 8050

COPY . /app

WORKDIR /app

RUN python -m pip install --upgrade pip

RUN pip install -r /app/requirements.txt

RUN pip install --upgrade google-api-python-client 

#ENTRYPOINT ["python"]

#CMD ["app.py"]

CMD ["python", "/app/app.py"]

