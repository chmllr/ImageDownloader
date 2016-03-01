from __future__ import print_function
import argparse
import urllib2
import uuid
import sys
import os

# parse all command line arguments
parser = argparse.ArgumentParser(description='Downloads images stored in a text file as a flat list of URLs.')
parser.add_argument('--urls', help='path to the text file with URLs', required=True)
parser.add_argument('--output', help='directory where downloaded images should be stored', required=True)
args = vars(parser.parse_args());

outputDirectory = args['output']

# are we allowed to run?
if (not os.path.isdir(outputDirectory) or not os.path.exists(outputDirectory)):
    print (outputDirectory + " does not exists or is not a directory")
    sys.exit(1)

# read and trim all URLs
with open(args['urls']) as fileHandler:
    urls = map(lambda line: line.strip(), fileHandler.readlines())

# download images
attempt = 0
fetched = 0
for url in urls:
    # note: it would be fatal to extract the file name from the URL and use it as a local file name due to
    # different URLs with the same file name! As no explicit requirement about the file name is known,
    # we generate a GUID string for every local file name.
    extension = url.split(".")[-1]
    # in case if we couldn't guess (!) an extension
    if (len(extension) == 0 or len(extension) > 4): extension = "dat"
    fileName = outputDirectory + "/" + str(uuid.uuid1()) + "." + extension
    # inform user about what's going on
    print ("[" + str(attempt) + "/" + str(len(urls)) + "] Fetching...", end = " ")
    sys.stdout.flush()
    try:
        # try to fetch the URL and stored in case of a success
        response = urllib2.urlopen(url)
        f = open(fileName, 'wb')
        f.write(response.read())
        f.close()
        print ("Stored " + url + " as " + fileName)
        fetched = fetched + 1
    except urllib2.URLError, e:
        print ("Failed with " + url + ": " + str(e))
    attempt = attempt + 1
    
print ("Successfully fetched {0} files from {1}".format(fetched, attempt))