import os

###
'''Separate files into their respective folders by hour '''
###

# Get path to files
def move_files(orig_dir, ends_with, new_dir):

    # TODO add checks for file type 
    files = os.listdir(orig_dir)

    # Find all files to move
    _files = [os.path.join(orig_dir, f) for f in files if f.endswith(ends_with)]
    
    # Create directories if they don't exist
    if not os.path.exists(orig_dir + new_dir):
        os.mkdir(orig_dir + new_dir)

    # Create new destination file names
    _new_dest = [os.path.join(orig_dir, new_dir,f) for f in files if f.endswith(ends_with)]

    for old, new in zip(_files, _new_dest):
        os.rename(old, new)
