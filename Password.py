'''
Password change
'''
import traceback,sys #pylint:disable=multiple-imports
from Login import Login
from bs4 import BeautifulSoup


CHANGE_PASSWORD_PAGE="https://ums.lpu.in/lpuums/frmchangepassword.aspx"
USER=""
PSWD=""
TEMP=""
#carefull

class Password:#pylint:disable=missing-docstring,wrong-import-order,trailing-whitespace, multiple-imports, too-few-public-methods
    def __init__(self,user,pswd,new_pswd):
        self.user=user
        self.pswd=pswd
        self.new_pswd=new_pswd
    def change_password(self):#pylint:disable=missing-docstring,wrong-import-order,trailing-whitespace, multiple-imports
        try:
            a=Login(user=self.user,password=self.pswd)#pylint:disable=invalid-name
            session=a.get_session()
            change_password_html=session.get(CHANGE_PASSWORD_PAGE)
            soup_data=change_password_html.text
            soup=BeautifulSoup(soup_data,"html.parser")
            state=soup.find(id="__VIEWSTATE")
            viewstate=state["value"]

            payload={
                   "__EVENTTARGET":"",
                   "__EVENTARGUMENT":"",
                   " __VIEWSTATE":viewstate,
                    "txtOldPassword":self.pswd,
                    "txtNewPassword":self.new_pswd,
                    "txtConfirmPassword":self.new_pswd,
                    "btnUpdate":"Change Password",
                    "hdPasswordLength":6,
                    "hdRollid":3
            }
            session.post(CHANGE_PASSWORD_PAGE,data=payload,verify=False)
        
        except:#pylint:disable=bare-except
            traceback.print_exc(file=sys.stdout)
def main():#pylint:disable=missing-docstring
    Password(USER,PSWD,TEMP).change_password()
    Password(USER,TEMP,PSWD).change_password()
    print("done")

if __name__=="__main__":
    main()
