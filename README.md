# ImageDownloader

A simple tool for synchronous downloading of images stored in a flat list in a text file. 

Usage:

    python run.py --urls=<path/to/file-with-urls> --output=<directory>

A short integration test can be started (prerequisites: Bash, Python 2.X) as follows:

    make integration-test
    
After the test, you should see, that 5 out of 6 files could be downloaded correctly
(one of the input URLs is invalid on purpose). 
You should be able to open the local `target` directory and verify that it contains:

- 4 JPG files
- 1 DAT file (a fallback extension for URLs without a file extension)