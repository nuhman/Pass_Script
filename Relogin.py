'''
Log Me IN BACK!!!
'''
import traceback,sys #pylint:disable=multiple-imports
from bs4 import BeautifulSoup
import requests


PAGE="http://172.17.90.32:8090/httpclient.html"
#Provide Your Credentials

USER=""
PSWD=""

class Password:#pylint:disable=missing-docstring,wrong-import-order,trailing-whitespace, multiple-imports, too-few-public-methods
    def __init__(self,user,pswd):
        self.user=user
        self.pswd=pswd
    def logMeBack(self):#pylint:disable=missing-docstring,wrong-import-order,trailing-whitespace, multiple-imports
        try:
            r = requests.get(PAGE)
            soup = BeautifulSoup(r.text, 'html.parser')

            payload={
                    "mode":"191",
                    "username":self.user,
                    "password":self.pswd,
                    "btnSubmit":"Login",
            }
            r = requests.post(PAGE,data=payload,verify=False)
            print(r.text)    
        except:#pylint:disable=bare-except
            traceback.print_exc(file=sys.stdout)
def main():#pylint:disable=missing-docstring
    Password(USER,PSWD).logMeBack()
    print("done")

if __name__=="__main__":
    main()
