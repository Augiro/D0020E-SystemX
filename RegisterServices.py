import requests

def do_request(xml_location):
    HOST = 'http://130.240.5.130:8045/servicediscovery/publish'
    xml =open(xml_location,"r").read()
    headers = {'Content-Type': 'application/xml'}
    r = requests.post(HOST,data = xml,headers = headers).text;
    print(r)



do_request("regjobs.xml")
do_request("regsetup.xml")




