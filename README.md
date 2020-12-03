# Web plant

## Requirements

- Python 3 with pip and venv installed

## Installation

1. Download
2. Mount project folder in `CMD / Bash`
3. Create venv `python -m venv venvlib`
4. Activate venv
5. `pip install -r requirements.txt`

## Activating venv

See <https://docs.python.org/3/tutorial/venv.html> further refrences.

- Windows

  1. `cd {project folder}/venvlib/Scripts/`
  2. `activate`

- Linux / Mac

  1. `cd {project folder}/venvlib//bin/`
  2. `source activate`

- Deactivating

  1. Type `deactivate` in shell

## Running the project

Either run `app.py` or `flask run`.  
`app.py` will run on defined `localhost:port` while `flask run` will run on `127.0.0.1:5000`

## Projects Structures

- {venv library}/
- src/
  - /templates/ --> HTML file location
  - /static/ --> css file location
  - /app.py --> The main python file

## Project Refrences and Tutorials

- <https://create.arduino.cc/projecthub/murthysiddhant/plant-monitor-sensor-to-front-end-c1f715>
- <https://www.youtube.com/playlist?list=PLC86yC9XtBxqpbY-3SYs9IahAC9bBE4PY>
- <https://www.youtube.com/watch?time_continue=393&v=tXpFERibRaU&feature=emb_title>
