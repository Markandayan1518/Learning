import urllib.request
import sys
request_obj=urllib.request.urlopen("http://127.0.0.1:9999/currency_convert?convert="+sys.argv[1])
output=request_obj.read()
print("response is :",output.decode("utf-8"))
