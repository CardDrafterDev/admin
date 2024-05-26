include $(PWD)/.env

PORT=$(SERVER_PORT)
PYTHON=$(VENV)/bin/python3
HOST=$(SERVER_HOST)


uvi-local:
	uvicorn 'main:server' --reload --host $(HOST) --port $(PORT)
