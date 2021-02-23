import pycurl
try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO




buffer = BytesIO()
c = pycurl.Curl()
url = "https://api-ropsten.etherscan.io/api?module=proxy&action=eth_getTransactionByHash&txhash=0xa5c8e897a57dc3dfb676ea8983d5d11d50d21f1f6e3770d869c58786791481f1&apikey=YourApiKeyToken"
c.setopt(c.URL, url)
c.setopt(c.WRITEDATA, buffer)
c.perform()




# HTTP response code, e.g. 200.
print('Status: %d' % c.getinfo(c.RESPONSE_CODE))
# Elapsed time for the transfer.
print('Time: %f' % c.getinfo(c.TOTAL_TIME))

print(buffer.getvalue())

# getinfo must be called before close.
c.close()
