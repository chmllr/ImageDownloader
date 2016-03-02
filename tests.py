from mock import patch, mock_open
import downloader

def testURLparsing():
    content = """http://host.com/file.png
    http://host.com/file2.png"""
    with patch("__builtin__.open", mock_open(read_data = content)) as mock_file:
        instance = downloader.Downloader("/test/path/file.txt", "output")
        assert instance.urls == ["http://host.com/file.png", "http://host.com/file2.png"]
        
testURLparsing()