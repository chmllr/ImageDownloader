integration-test:
	rm -rf target && mkdir target
	pushd test && python -m SimpleHTTPServer 8787 &
	sleep 2 && python run.py --urls=test/testURLs.txt --output=target
