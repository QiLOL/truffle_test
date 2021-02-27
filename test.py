import json
import pycurl
try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO


def test(url):
    time_list = []
    for i in range(100):
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
    # HTTP response code, e.g. 200.
        #print('Status: %d' % c.getinfo(c.RESPONSE_CODE))
    # Elapsed time for the transfer.
        #print('Time: %f' % c.getinfo(c.TOTAL_TIME))
        #print(buffer.getvalue())
        if c.getinfo(c.RESPONSE_CODE) == 200:
            time_list.append(c.getinfo(c.TOTAL_TIME))
    # getinfo must be called before close.
        c.close()
    #print(time_list)
    print(sum(time_list)/len(time_list))
    
address = ["0xF2A08313FC79A01AdbC5E700B063ed83Ed07B446"]
privatekey = ["7a1ef7c273aa1ea4ed2a018ba3e491cc345fdca0df6cdce85924f66673ba140a"]

with open('api.json') as json_file:
    api = json.load(json_file)

with open('testdata.json') as json_file:
    data = json.load(json_file)

for key in api:
    print(key)
    curr_api = api[key]
    if 'parameters' in curr_api:
        parameters = curr_api['parameters']
        url_t = curr_api['template']

        parameter_len = len(parameters)
        if parameter_len == 1:
            for p0 in data[parameters[0]]:
                print(p0)
                url = ""
                url = url_t + "&"+parameters[0]+"="+p0
                url += "&apikey=BPS6G2415Z1J5KV85FP76QFD3MXM1U39BU"
                test(url)

        if parameter_len == 2:
            for p0 in data[parameters[0]]:
                for p1 in data[parameters[1]]:
                    print(p0,p1)
                    url = ""
                    url = url_t + "&"+parameters[0]+"="+p0 + "&"+parameters[1]+"="+p1
                    url += "&apikey=BPS6G2415Z1J5KV85FP76QFD3MXM1U39BU"
                    test(url)
        
        if parameter_len == 3:
            for p0 in data[parameters[0]]:
                for p1 in data[parameters[1]]:
                    for p2 in data[parameters[2]]:
                        print(p0,p1,p2)
                        url = ""
                        url = url_t + "&"+parameters[0]+"="+p0 + "&"+parameters[1]+"="+p1 + "&"+parameters[2]+"="+p2
                        url += "&apikey=BPS6G2415Z1J5KV85FP76QFD3MXM1U39BU"
                        test(url)

        


    



