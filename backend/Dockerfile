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
# Install Gunicorn to run the Flask app in production to enables spans in Datadog APM 
RUN pip install gunicorn  

# Run the script with ddtrace
#CMD ["ddtrace-run", "python", "/app/app.py"]
CMD ["ddtrace-run", "gunicorn", "-b", "0.0.0.0:5000", "app:app"]
#CMD ["python", "python-test.py"]