FROM python:3.8.2-alpine3.11
EXPOSE 5000
WORKDIR /root

RUN pip install flask
RUN pip install datetime

COPY tiny.py .
COPY today.html .

CMD ["python", "tiny.py"]