#!/usr/bin/env python
from pathlib import Path
from nornir import InitNornir
from nornir_scrapli.tasks import get_prompt, send_commands

OUTPUT_DIR = "./output"


def write_output(hostname, command, output, path):
    def _safe_name(unsafe):
        keepcharacters = (" ", ".", "_")
        return "".join(c for c in unsafe if c.isalnum() or c in keepcharacters).rstrip()

    out_file = Path(path) / _safe_name(hostname)

    # Create dir if not exist
    out_file.mkdir(parents=True, exist_ok=True)

    out_file = out_file / f"{_safe_name(hostname)}__{_safe_name(command)}.txt"

    with open(out_file, "w") as f:
        f.write(output)


if __name__ == "__main__":

    with open("commands.txt", "r") as f:
        commands = [x.rstrip() for x in f.readlines()]

    nr = InitNornir(config_file="nornir_data/nornir.conf.yaml")

    commands_results = nr.run(task=send_commands, commands=commands)

    for host, result in commands_results.items():
        if result.failed:
            print(f"ERROR: {result.host} {result.exception}")
        else:
            scrapli_result = result[0].scrapli_response
            for i in scrapli_result.data:
                command = i.channel_input
                output = i.result
                write_output(host, command, output, OUTPUT_DIR)
                print(f"Wrote '{command}' output for '{host}'")
