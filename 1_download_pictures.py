
'''
Purpose

This notebook connects to the remote picamera, finds all of the new pictures
and downloads them to the local machine.

Import the libraries that will be used. I use `paramiko` to create the
connection to the pi camera.
'''

import paramiko
import os
import pandas as pd

# Set the directory
# Skipping this step when called from RMarkdown
# dir = os.path.dirname(os.getcwd())
# os.chdir(dir)

# read in file containing host information
d = pd.read_csv("server_info.csv")

d = dict(zip(list(d.iloc[:, 0]), list(d.iloc[:, 1])))

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# This should really be a txt file that gets read in
ssh_client.connect(
    hostname=d['hostname'],
    username=d['username'],
    password=d['password'],
    port=22)

# Find all of the files in the pictures folder.

stdin, stdout, stderr = ssh_client.exec_command("ls pictures")
pi_files = stdout.readlines()

# Remove the trailing new line characters.

pi_files = [p.strip("\n") for p in pi_files]

# Get a list of the existing pictures that have already been downloaded.
# We don't want to waste time downloading files
# that have already been downloaded.

existing_files = os.listdir('pi_pics/')

new_files = list(set(pi_files) - set(existing_files))

# Iterate over each new file and download to a local folder
ftp_client = ssh_client.open_sftp()

for file in new_files:
    remotepath = str("/home/pi/pictures/" + file)
    localpath = str("pi_pics/" + file)

    ftp_client.get(remotepath, localpath)

ftp_client.close()
