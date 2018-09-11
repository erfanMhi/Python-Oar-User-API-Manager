import requests
root_url = "http://frontend.lis-lab.fr:6668/oarapi/"
class OarRequest(requests.Session) :
    def __init__(self,user=None,password=None) :
        super(OarRequest, self).__init__()
        if user and password :
            self.auth = (user,password)
    
    def add_job(self) :
        pass

    def delete_job(self) :
        pass

    def get_auth_user(self) :
        self.get(root_url + "/whoami")
from requests.auth import HTTPDigestAuth,HTTPBasicAuth
if __name__ == '__main__' :
    s = requests.Session()
    s.auth = ('ghasem.mirroshandel','GaDeep1397?')
    s.headers = {'accept'}
    or_r = OarRequest('ghasem.mirroshandel','GaDeep1397?')
    # print(root_url + "whoami")
    # print(requests.get('http://frontend.lis-lab.fr:6668/oarapi/resources.yaml?structure=simple'))
    print(requests.get(root_url + "jobs/3.json",auth=HTTPBasicAuth('ghasem.mirroshandel','GaDeep1397?')).json())
    # print(s.get(root_url + "/whoami").json())