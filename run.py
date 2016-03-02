import argparse
import sys
import os
import downloader

# parse all command line arguments
parser = argparse.ArgumentParser(description='Downloads images stored in a text file as a flat list of URLs.')
parser.add_argument('--urls', help='path to the text file with URLs', required=True)
parser.add_argument('--output', help='directory where downloaded images should be stored', required=True)
args = vars(parser.parse_args())

outputDirectory = args['output']

# are we allowed to run?
if (not os.path.isdir(outputDirectory) or not os.path.exists(outputDirectory)):
    print(outputDirectory + " does not exists or is not a directory")
    sys.exit(1)

instance = downloader.Downloader(args['urls'], outputDirectory)

(fetched, attempts) = instance.downloadSync()

print
print("Successfully fetched {0} files from {1}".format(fetched, attempts))