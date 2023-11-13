# Installation Instructions

## Requirements

1. Install Python: https://www.python.org/downloads/
2. Clone the repository:
   `git clone https://github.com/jyuter-interviews/mobileye.git`
3. Set up Python Virtual Environment:
   1. Unix
      - `python3 -m venv .venv`
      - `source .venv/bin/activate`
   2. Windows
      - `py -m venv .venv`
      - `.venv\bin\Activate.bat`
4. Install requirements: `pip install -r requirements.txt`

## Running the Server

1. Locally: `python mnist_server.py`
2. In Docker:
   - `docker build -t mnist_server:v1 .`
   - `docker run -p 50051:50051 mnist_server:v1`

## Running the Client

`python mnist_client.py`
