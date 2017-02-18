"""main login"""
import traceback,sys,requests,warnings,urllib.request #pylint:disable=missing-docstring,wrong-import-order,trailing-whitespace, multiple-imports 
from bs4 import BeautifulSoup #pylint:disable=wrong-import-order,trailing-whitespace, multiple-imports, missing-docstring

LOGIN = 'https://ums.lpu.in/lpuums/loginnew.aspx'


class Login: #pylint:disable=wrong-import-order,trailing-whitespace, multiple-imports, missing-docstring
    def __init__(self,**kwargs):  #pylint:disable=wrong-import-order,trailing-whitespace, multiple-imports, missing-docstring
        self.session=-1
        self.user=kwargs.get("user","")
        self.pswd=kwargs.get("password","")
        self.sign_in() 
        
    def sign_in(self):
        try:
            warnings.filterwarnings("ignore")
            get_login_page=urllib.request.urlopen(LOGIN)
            soup=BeautifulSoup(get_login_page,'html.parser')
            state=soup.find(id="__VIEWSTATE")
            viewstate=state["value"]
            payload = {
                       "__VIEWSTATE":viewstate,
                       "TextBox1":self.user,
                       "TextBox2":self.pswd,
                       "DropDownList1":1,
                       "ddlStartWith":"default3.aspx",
                       "iBtnLogin.x":18,
                       "iBtnLogin.y":28
                       }
            self.session=requests.Session()
            self.session.post(LOGIN,data=payload,verify=False)
        except: #pylint:disable=bare-except
            traceback.print_exc(file=sys.stdout)    
        
    def get_session(self):
        return self.session   