import requests

def request_unsub(xml_location):
    HOST = 'http://130.240.5.130:8045/servicediscovery/unpublish'
    xml =open(xml_location,"r").read()
    headers = {'Content-Type': 'application/xml'}
    r = requests.post(HOST,data = xml,headers = headers).text;
    print(r)


request_unsub("unsubjobs.xml")
request_unsub("unsubsetup.xml")



