integration-test:
	rm -rf target && mkdir target
	pushd test-data && python -m SimpleHTTPServer 8787 &
	sleep 2 && python run.py --urls=test-data/testURLs.txt --output=target
