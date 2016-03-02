import argparse
import sys
import os
import downloader

# parse all command line arguments
parser = argparse.ArgumentParser(description='Downloads images stored in a text file as a flat list of URLs.')
parser.add_argument('--urls', help='path to the text file with URLs', required=True)
parser.add_argument('--output', help='directory where downloaded images should be stored', required=True)
args = vars(parser.parse_args())

output_directory = args['output']

# are we allowed to run?
if (not os.path.isdir(output_directory) or not os.path.exists(output_directory)):
    print(output_directory + " does not exists or is not a directory")
    sys.exit(1)

instance = downloader.Downloader(args['urls'], output_directory)

(fetched, attempts) = instance.download()

print
print("Successfully fetched {0} files from {1}".format(fetched, attempts))