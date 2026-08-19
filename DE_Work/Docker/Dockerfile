FROM python:3.12-slim
WORKDIR /app
COPY DataWork.py /app
COPY 03_Library_Systembook.csv .
COPY 03_Library_SystemCustomers.csv .
COPY Requirements.txt .

RUN pip install --no-cache-dir -r Requirements.txt

CMD ["python3", "DataWork.py"]

# docker build -t hellovol .
# docker run -v my-data:/app/data hellovol
# docker build -t hellovol .