from ftplib import FTP
from datetime import date
import os


today = date.today().isoformat()
x = today.replace('-','')



ftp = FTP('server address')
ftp.login("user_name","password")
dirname = "/3184/"
ftp.cwd(dirname)
files = ftp.nlst()

for file_name in files:
    print("file_name : ",file_name)
    if '.xml' in file_name:
        try:
            path = dirname + file_name
            modtime = ftp.voidcmd(f"MDTM {path}")[4:-10].strip()
            if(modtime==x):
                print("downloading ... ")
                ftp.retrbinary(f"RETR {file_name}" ,open("/home/oem/ftp_download/test/" + file_name, 'wb').write)
        except ConnectionResetError as exc:
            print('Oh no, conection error', str(exc))
            ftp = FTP('aftp.linksynergy.com')
            ftp.login("BosLondi","Wawayeyelagos101")


ftp.close()

