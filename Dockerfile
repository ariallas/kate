FROM python:3.10

EXPOSE 80
WORKDIR /app
COPY server.py /app/server.py

# RUN pip install pystrich

CMD [ "python3", "./server.py" ]