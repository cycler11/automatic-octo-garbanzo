FROM python:3.11
WORKDIR /app
COPY requirements.txt .
COPY app/ ./app/
COPY entrypoint.sh .
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
