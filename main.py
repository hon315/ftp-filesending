import ftplib, os, argparse, shutil, datetime

logs_path = 'C:\\Users\\Said-Azizkhon\\OneDrive\\Рабочий стол\\logs_solution\\logs_client\\'

shutil.make_archive(logs_path + str(datetime.date.today()), 'zip', logs_path)

parser = argparse.ArgumentParser()
parser.add_argument("--name", help="directory name upload")
parser.add_argument("--folder", help="directory name download")
args = parser.parse_args()

dirname = 'atm1'

if args.name:
    dirname = args.name

ftp = ftplib.FTP('176.57.210.144')

ftp.login(user='co95971_test', passwd='b7GVEeGz')

ftp.cwd('data_ftp')
is_exist = False
for elem in ftp.nlst():
    if not(ftp.nlst(elem) == [elem]) and elem == dirname:
        is_exist = True

if not is_exist:
    ftp.mkd(dirname)

ftp.cwd(dirname)

ftp.encoding = 'utf-8'

with open(logs_path + str(datetime.date.today()) + ".zip", "rb") as zipfile:
    ftp.storbinary('STOR ' + str(datetime.date.today()) + ".zip", zipfile)


for f in os.scandir(logs_path):
    if f.is_file() and f.path.split('.')[-1].lower() == 'txt':
        print(f.name)
        with open(f.path, 'rb') as logfile:
            ftp.storbinary('STOR ' + f.name, logfile)
