"""Script that runs the power gadget tool and records results.

Examples of running the scripts:

python main.py --cmd 'python test.py' - measures power usage of running test.py file

python main.py --s 5 --cmd 'python test.py' - measures power usage of running test.py file for 5 seconds

python main.py --f PWR.csv --cmd 'python test.py' - measures power usage of running test.py file and save results to PWR.csv

"""
import os
import argparse

DEFAULT_POWERLOG = 'C:\\Program Files\\Intel\\Power Gadget 3.6'
parser = argparse.ArgumentParser(description='Power usage test tool.')
parser.add_argument('--p', '-path', type=str,
                    help=f"Path to the Power Log executable (default={DEFAULT_POWERLOG})",
                    default=DEFAULT_POWERLOG)
parser.add_argument('--f', '-file', type=str, help='File path for saving the results to a csv file (default=PWR.csv)',
                    default='PWR.csv')
parser.add_argument('--s', '-seconds', type=int, help='Number of seconds to run power gadget tool')
parser.add_argument('--cmd', '-command', type=str, help='Command to run the tests on')

args = vars(parser.parse_args())

duration_str = f"-duration {args.get('s')}" if args.get("s") is not None else ""
command_str = f"-cmd {args.get('cmd')}" if args.get("cmd") is not None else ""

cmd = f'"{args.get("p")}\\PowerLog3.0.exe" {duration_str} -file {args.get("f")} {command_str}'
print("Running:", cmd, "...")

os.system(cmd)
print("DONE")
