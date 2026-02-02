# backend Dockerfile
FROM python:3.11-alpine


RUN apk add --no-cache curl


# Set working directory
WORKDIR /app


# Copy Python script
COPY app.py /app/
# COPY requirements.txt /app/
COPY requirements.txt /app/

#EXPOSE 5057

# Install ddtrace for APM, Flask, and other dependencies in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install ddtrace

# Run the script with ddtrace
CMD ["ddtrace-run", "python", "/app/app.py"]
#CMD ["python", "python-test.py"]