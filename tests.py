from mock import patch, mock_open, call
import downloader

def testURLparsing():
    # case 1: trivial
    content1 = """http://host.com/file.png
    http://host.com/file2.png"""
    with patch("__builtin__.open", mock_open(read_data = content1)) as mock_file:
        instance = downloader.Downloader("file.txt", "output")
        assert instance.urls == ["http://host.com/file.png", "http://host.com/file2.png"]
    # case 2: use unix & windows line breaks, unneccessary white space
    content2 = " http://host.com/file.png\nhttp://host.com/file2.png\r\n http://host.com/file3.png        "
    with patch("__builtin__.open", mock_open(read_data = content2)) as mock_file:
        instance = downloader.Downloader("/test/path/file2.txt", "output")
        assert instance.urls == ["http://host.com/file.png", "http://host.com/file2.png", "http://host.com/file3.png"]
    # case 3: test2 + empty line
    content2 = " http://host.com/file.png\n\nhttp://host.com/file2.png\r\n http://host.com/file3.png        "
    with patch("__builtin__.open", mock_open(read_data = content2)) as mock_file:
        instance = downloader.Downloader("/test/path/file3.txt", "output")
        assert instance.urls == ["http://host.com/file.png", "http://host.com/file2.png", "http://host.com/file3.png"]

@patch('downloader.urllib2.urlopen')
def testURLCalling(mocked_urlopen):
    content1 = "http://host.com/file.png\nhttp://host.com/file2.png"
    with patch("__builtin__.open", mock_open(read_data = content1)) as mock_file:
        instance = downloader.Downloader("file.txt", "output")
        instance.downloadSync()
        calls = [call("http://host.com/file.png"), call().read(), call("http://host.com/file2.png"), call().read()]
        mocked_urlopen.assert_has_calls(calls)
        
        
testURLparsing()
testURLCalling()
print
print "All tests executed successfuly"