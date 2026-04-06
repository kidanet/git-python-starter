# Git + Python Starter

Small real Python programs you can run while practicing Git basics.

## Setup

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

## Run examples
python apps/cli_todo.py add "learn git"
python apps/cli_todo.py list
python apps/wordcount.py data/sample.txt
pytest -q
