from __future__ import print_function
import urllib2
import uuid
import sys

class Downloader():

    def __init__(self, fileName, outputDirectory):
        self.outputDirectory = outputDirectory        
        # read URLs, trim, skip empty strings
        with open(fileName) as fileHandler:
            self.urls = map(lambda line: line.strip(), fileHandler.readlines())
            self.urls = filter(None, self.urls)

    def downloadSync(self):
        # download images
        attempts = 0
        fetched = 0
        for url in self.urls:
            attempts = attempts + 1
            # note: it would be fatal to extract the file name from the URL and use it as a local file name due to
            # different URLs with the same file name! As no explicit requirement about the file name is known,
            # we generate a GUID string for every local file name.
            extension = url.split(".")[-1]
            # in case if we couldn't guess (!) an extension
            if (len(extension) == 0 or len(extension) > 4): extension = "dat"
            fileName = self.outputDirectory + "/" + str(uuid.uuid1()) + "." + extension
            # inform user about what's going on
            print("[" + str(attempts) + "/" + str(len(self.urls)) + "] Fetching...", end = " ")
            sys.stdout.flush()
            try:
                # try to fetch the URL and store it in case of a success
                response = urllib2.urlopen(url)
                f = open(fileName, 'wb')
                f.write(response.read())
                f.close()
                print("Stored " + url + " as " + fileName)
                fetched = fetched + 1
            except Exception as e:
                print("Failed to fetch " + url + ": " + str(e))
        return (fetched, attempts)