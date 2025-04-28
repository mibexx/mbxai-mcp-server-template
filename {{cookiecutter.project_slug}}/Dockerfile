FROM python:3.12-slim

WORKDIR /app

# Install uv
RUN pip install --no-cache-dir uv

# Copy project files
COPY pyproject.toml .
COPY src/ src/

# Install dependencies
RUN uv pip install -e .

# Expose the port
EXPOSE 5000

# Run the service
CMD ["uv", "run", "service"] 