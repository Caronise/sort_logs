This is a simple python script which organizes log files based on the isosec
timestamp prefix.

Usage: python3 main.py --filename "20220522171336_server_log"

This would find all the files that have the prefix "20220522171336", create
the directory "logs_20220522171336" and move all files with the corresponding
prefix into the newkly created directory.
