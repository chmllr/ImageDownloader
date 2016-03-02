from mock import patch, mock_open
import downloader

def testURLparsing():
    # case 1: trivial
    content1 = """http://host.com/file.png
    http://host.com/file2.png"""
    with patch("__builtin__.open", mock_open(read_data = content1)) as mock_file:
        instance = downloader.Downloader("/test/path/file.txt", "output")
        assert instance.urls == ["http://host.com/file.png", "http://host.com/file2.png"]
    # case 2: use unix & windows line breaks, unneccessary white space
    content2 = " http://host.com/file.png\nhttp://host.com/file2.png\r\n http://host.com/file3.png        "
    with patch("__builtin__.open", mock_open(read_data = content2)) as mock_file:
        instance = downloader.Downloader("/test/path/file.txt", "output")
        assert instance.urls == ["http://host.com/file.png", "http://host.com/file2.png", "http://host.com/file3.png"]
    # case 3: test2 + empty line
    content2 = " http://host.com/file.png\n\nhttp://host.com/file2.png\r\n http://host.com/file3.png        "
    with patch("__builtin__.open", mock_open(read_data = content2)) as mock_file:
        instance = downloader.Downloader("/test/path/file.txt", "output")
        assert instance.urls == ["http://host.com/file.png", "http://host.com/file2.png", "http://host.com/file3.png"]
        
testURLparsing()
print
print "All tests executed successfuly"