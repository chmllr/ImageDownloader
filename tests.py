from mock import patch, mock_open, call
import downloader

def test_URL_parsing():
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

# we don't want to unit test the urllib2 as it's the task of the lib developers,
# but we want to ensure, the urllib2.urlopen is called on the expected inputs!
@patch('downloader.urllib2.urlopen')
def test_URL_calling(mocked_urlopen):
    content1 = "http://host.com/file.png\nhttp://another-host.org/file2.jpg"
    with patch("__builtin__.open", mock_open(read_data = content1)) as mock_file:
        instance = downloader.Downloader("file.txt", "output")
        instance.download()
        calls = [call("http://host.com/file.png"), call().read(), call("http://another-host.org/file2.jpg"), call().read()]
        mocked_urlopen.assert_has_calls(calls)
        
test_URL_parsing()
test_URL_calling()

print
print "All tests executed successfully"