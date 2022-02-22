"""Script that runs the power gadget tool and records results."""
import os
import argparse

parser = argparse.ArgumentParser(description='Power usage test tool.')
parser.add_argument('--p', '-path', type=str, help='Path to the Power Log executable',
                    default='C:\Program Files\Intel\Power Gadget 3.6')
parser.add_argument('--f', '-file', type=str, help='File path for saving the results (csv file)',
                    default='PWR.csv')
parser.add_argument('--s', '-seconds', type=int, help='Number of seconds to run power gadget tool',
                    default=10)


args = vars(parser.parse_args())


cmd_to_run = f'"{args.get("p")}\PowerLog3.0.exe" -duration {args.get("s")} -file {args.get("f")}'
print("Running:", cmd_to_run, "...")

os.system(cmd_to_run)
print("DONE")
