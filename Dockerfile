FROM python:3.10

EXPOSE 80
WORKDIR /app
COPY test.py /app/test.py

# RUN pip install pystrich

CMD [ "python3", "./test.py" ]