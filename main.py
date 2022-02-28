"""Script that runs the power gadget tool and records results.

Examples of running the scripts:

python main.py --cmd 'https://www.google.com/' - measure the power consumtion of opening and staying on google.com using the scrollthrough python script.

python main.py --s 5 --cmd 'https://www.google.com/' - measure the power consumtion of opening and staying on google.com using the scrollthrough python script for 5 seconds.

py main.py --f PWR --s 10 --cmd 'https://www.google.com/' - measures power usage of running test.py file and save results to PWR_1.csv

"""
import os
import argparse
import time

DEFAULT_POWERLOG = 'C:\\Program Files\\Intel\\Power Gadget 3.6'
parser = argparse.ArgumentParser(description='Power usage test tool.')
parser.add_argument('--p', '-path', type=str,
                    help=f"Path to the Power Log executable (default={DEFAULT_POWERLOG})",
                    default=DEFAULT_POWERLOG)
parser.add_argument('--f', '-file', type=str, help='File path for saving the results to a csv file (default=PWR.csv)',
                    default='PWR')
parser.add_argument('--n', type=int, help='Number of times to run the power gadget tool', default=1)
parser.add_argument('--s', '-seconds', type=int, help='Number of seconds to run power gadget tool')
parser.add_argument('--cmd', '-command', type=str, help='Webpage to collect data from')


args = vars(parser.parse_args())

times_to_run = args.get('n')

if times_to_run < 1 :
    raise Exception('n must be at least 1')

duration_str = f"-duration {args.get('s')}" if args.get("s") is not None else ""
runtime_str = f"--s {args.get('s')}" if args.get("s") is not None else ""
command_str = f"--p {args.get('cmd')}" if args.get("cmd") is not None else ""

print(f"DEBUG: RUN PowerLog3.0 {times_to_run} times...\n")

ZFILL_NUM = len(str(times_to_run))

for i in range(times_to_run):
    SAVEFILE = os.path.join('out', args.get("f")+"_"+ str(i+1) +".csv")
    print("DEBUG: " + SAVEFILE)
    cmd = f'"{args.get("p")}\\PowerLog3.0.exe" {duration_str} -file {SAVEFILE} {"-cmd py scrollthrough.py " + command_str + " " + runtime_str}'
    print("DEBUG: Running:", cmd, "\n")

    os.system(cmd)
    # wait one minute between page executions for system to cooldown.
    time.sleep(60)
