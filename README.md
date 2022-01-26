# Just Do It

This will allow you to run commands against a set of network devices and save the outputs
to files.

![Just do it!](./just-do-it.jpg)

## Installation

1. Requires python 3.6+
2. `cd just-do-it`
3. `python -m venv venv`
4. `source venv/bin/activate`

## Usage

1. Update the `./nornir_data/hosts.yaml` file with your devices.
2. Update the `./commands.txt` file with the commands to run.
3. `source venv/bin/activate`
4. `python justdoit.py`
