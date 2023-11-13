FROM python:slim

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Run the application:
COPY mnist_server.py mnist_pb2.py mnist_pb2_grpc.py /
ADD samples /samples

CMD ["python", "mnist_server.py"]
