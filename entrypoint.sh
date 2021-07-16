#!/bin/bash

# uvicorn fastemplate:app --host 0.0.0.0 --port 8000 --reload
gunicorn -w 3 -b :8000 -k uvicorn.workers.UvicornWorker -t 90 --preload --max-requests=500 fastemplate:app
