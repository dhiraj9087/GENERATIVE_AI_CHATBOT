FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV COHERE_API_KEY='xtXzFR7Yzyb3T9vuCQ563oMdRLXm000eQiDgObuv'

CMD ["python", "app.py"]
