import paramiko
import os
import pandas as pd
from PIL import Image

"""
Purpose

This notebook connects to the remote picamera, finds all of the new pictures
and downloads them to the local machine.

Import the libraries that will be used. I use `paramiko` to create the
connection to the pi camera.

remove metadata from downloaded images by saving
a new copy.
"""


def dl_pictures(server_info, output_path):
    # read in file containing host information
    d = pd.read_csv(server_info)

    # Create dictionary from csv server information
    d = dict(zip(d.attr, d.value))

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # This should really be a txt file that gets read in
    ssh_client.connect(
        hostname=d["hostname"],
        username=d["username"],
        password=d["password"],
        # port=22,
        allow_agent=False,
    )

    # Find all of the files in the pictures folder.
    stdin, stdout, stderr = ssh_client.exec_command("ls pictures")
    pi_files = stdout.readlines()

    # Remove the trailing new line characters.
    pi_files = [p.strip("\n") for p in pi_files]

    # Get a list of the existing pictures that have already been downloaded.
    existing_files = os.listdir(output_path)
    new_files = list(set(pi_files) - set(existing_files))

    # Iterate over each new file and download to a local folder
    ftp_client = ssh_client.open_sftp()

    for file in new_files:
        remotepath = str("/home/pi/pictures/" + file)
        localpath = os.path.join(output_path, file)

        ftp_client.get(remotepath, localpath)

    ftp_client.close()


# Currenlt not being used
def clean_metadata(root_dir):
    # find all files
    new_files = os.listdir(root_dir)

    # remove any file that does not end with .jpg
    nf = [x for x in new_files if x.endswith(".jpg")]

    # remove existing files that have already been cleaned
    existing_files = os.listdir(root_dir + "clean/")
    ef = [x.strip("cl") for x in existing_files]
    nf = list(set(nf) - set(ef))

    # Open and resave each file
    # This scrubs the metadata from each image
    for n in nf:
        img = Image.open(root_dir + n)
        img.save(root_dir + "clean/cl" + n)
