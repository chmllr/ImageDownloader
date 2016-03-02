# ImageDownloader

A simple synchronous script for downloading of images stored in a flat list in a text file. 

## Usage

Run:

    python run.py --urls=<path/to/file-with-urls> --output=<directory>

## Testing

To execute unit tests install the `mock` package using `pip` (only once):

    pip install -r requirements.txt

 and run:

    python tests.py

A short integration test can be started (prerequisites: Bash, Python 2.X) as follows:

    make integration-test
    
After the test, you should see, that 5 out of 7 URLs could be downloaded correctly
(one line is not a URL and one URLs points to 404 on purpose). 
You should be able to open the local `target` directory and verify that it contains:

- 4 JPG files
- 1 DAT file (a fallback extension for URLs without a file extension)