## Setup Enviornment
`python -m venv venv`
`source venv/bin/activate`
`pip install .`

This will set up and the requirements

## Working
In terminal type the following commands

<b> Add task </b> <br></br>

`python main.py add "task name" -d "desciption" --due "25 Nov, 2025"`

<b> Remove task </b> <br></br>

`python main.py remove {id}`

<b> Complete task </b> <br></br>

`python main.py complete {id}`

<b> List task </b> <br></br>
For short list format

`python main.py list`

For detailed list format

`python main.py list --all`