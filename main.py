"""
This script will sort and move each log file to the corresponding
directory that matches the isosec timestamp prefix of each file.

"{timestam}example1.txt" --> "logs_{timestamp}"
"20220522171336_log.txt" --> "logs_20220522171336"
"20220613035530_log.txt" --> "logs_20220613035530"

"""

import os
import shutil
import argparse

# Parse commandline flags
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", type=str, required=True)
args = parser.parse_args()

filenames = []
timestamp = ""

# Creates the log director using the filename timestamp prefix.
def create_log_dir(filename):
    """
    create_log_dir("20220522171336")

    :param filename: str - filename containing the isosec timestamp prefix.
    :return: str - log directory name.
    """
    global timestamp
    timestamp = filename[:14]

    log_dir = "log_" + timestamp

    if os.path.isdir(log_dir):
        print("Directory already exists!")
    else:
        os.mkdir(log_dir)
        print("Creating directory: " + log_dir)
    return log_dir

# Read directory for all files containing the same timestamp as filename.
def read_files(timestamp):
    """
    :param timestamp: str - timestamp to identify related log files.
    """
    global filenames
    for file in os.listdir(os.getcwd()):
        if os.path.isfile(os.path.join(os.getcwd(), file)):
            if timestamp in file:
                filenames.append(file)
                print(filenames)

# Move all files with correct timestamp to log_dir.
def move_log_files(log_dir):
    """
    :param log_dir: str - path to the directory to move logs into.
    """
    global filenames
    for filename in filenames:
       source = os.path.join(os.getcwd(), filename)
       destination = os.path.join(os.getcwd(), log_dir)
       print(f"Moving file: {source} to {destination}")
       shutil.move(source, destination)

# Call functions.
if __name__ == "__main__":
    target_dir = create_log_dir(args.filename)
    read_files(timestamp)
    move_log_files(target_dir)
