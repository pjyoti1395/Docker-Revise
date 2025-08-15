FROM python:3.11-slim

WORKDIR /app

# Set environment variable
ENV APP_ENV=production

# Install Flask without requirements.txt
RUN pip install flask

# Copy application code
COPY app.py .

# Expose port
EXPOSE 5000

# Health check endpoint
HEALTHCHECK --interval=30s --timeout=5s \
    CMD curl --fail http://localhost:5000 || exit 1

# Default command
ENTRYPOINT ["python"]

CMD ["app.py"]
