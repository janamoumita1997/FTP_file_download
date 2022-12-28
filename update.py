from datetime import date
from ftp_walk import *
import ftplib
import datetime
import os


today = date.today().isoformat()
x = today.replace('-','')

# lines=[]
# with open('/home/oem/ftp_download/LinkshareStore_name_to_be_included.txt','r') as f:    
#     contents = f.read()
#     for i in contents.split(","):
#         lines.append(i)


lines = ['45174','39006','45081']

# ftp = ftplib.FTP("aftp.linksynergy.com")
# ftp.login('BosLondi','Wawayeyelagos101')
# retry = True
# while (retry):
#     try:
ftp = ftplib.FTP("aftp.linksynergy.com", "BosLondi", "Wawayeyelagos101", timeout=100000)
x = ftp.set_debuglevel(2)
print("x ",x)
# print(ftp.pwd() )
ftpwalk = FTPWalk(ftp)

for top,dirs,nondirs in ftpwalk.walk():
    print(f"top : {top}, dirs : {dirs}, nndirs : {nondirs}")
    try:
        if top[1:] in lines:
            for each_file in nondirs:
                if '.xml' in each_file:
                    path = f"{top}/{each_file}"
                    modtime = ftp.voidcmd(f"MDTM {path}")[4:-10].strip()
                    if(modtime==x):
                        try:
                        # if os.path.isfile(path):
                            print(f"downloading file {each_file}.....")
                            ftp.retrbinary(f"RETR {each_file}" ,open("/home/oem/ftp_download/xml/" + each_file, 'wb').write)
                            print("--------------downlord complete------------------")
                            # ftp.quit()
                        except EOFError as x:
                            print(x)
                            pass
    except:
        pass


    #     retry = False
    # except IOError as e:
    #     print ("I/O error({0}): {1}".format(e.errno, e.strerror))
    #     print ("Retrying...")
    #     retry = True




  
