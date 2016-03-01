from __future__ import print_function
import argparse
import urllib2
import uuid

# parse all command line arguments
parser = argparse.ArgumentParser(description='Downloads images stored in a text file as a flat list of URLs.')
parser.add_argument('--urls', help='path to the text file with URLs', required=True)
parser.add_argument('--output', help='directory where downloaded images should be stored', required=True)
args = vars(parser.parse_args());

# read and trim all URLs
with open(args['urls']) as fileHandler:
    urls = map(lambda line: line.strip(), fileHandler.readlines())

# download images
progress = 0
for url in urls:
    # note: it would be fatal to extract the file name from the URL and use it as a local file name due to
    # different URLs with the same file name! As no explicit requirement about the file name is known,
    # we generate a GUID string for every lcoal file name.
    extension = url.split(".")[-1]
    # in case if we couldn't guess (!) an extension
    if (len(extension) != 3): extension = "dat"
    fileName = args['output'] + "/" + str(uuid.uuid1()) + "." + extension
    print ("[" + str(progress) + "/" + str(len(urls)) + "] Storing file...", end = " ")
    try:
        response = urllib2.urlopen(url)
        f = open(fileName, 'wb')
        f.write(response.read())
        f.close()
        print ("Stored " + url + " as " + fileName + " ...")
    except urllib2.URLError, e:
        print ("Failed with " + url + ": " + str(e))
    progress = progress + 1