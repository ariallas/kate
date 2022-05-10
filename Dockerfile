FROM python:3.10

EXPOSE 8080
WORKDIR /app
COPY app.py /app/
COPY templates/ /app/templates

RUN pip install flask
RUN pip install pymongo

CMD [ "python3", "./app.py" ]
# CMD [ "flask", "run" ]