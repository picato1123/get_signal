# 本スクリプトはExcelと同じディレクトリで動作させること
import sys
import os
import datetime
import investpy

# カレントディレクトリ確認
#print('getcwd:      ', os.getcwd())    デバッグ用。
#print('__file__:    ', __file__)       デバッグ用

# 実行ディレクトリの取得
args = sys.argv
folder_path = os.path.dirname(args[0])
print("folder_path : " + folder_path)

# フォルダの存在を確認。なければ作成する
logfolder_path = folder_path + "/python_log"
print("logfolder_path : " + logfolder_path)
if not os.path.exists(logfolder_path):
    os.mkdir(logfolder_path)

# ファイルパスを folder_path/py_YYYYMMDD.log　とする
time = datetime.datetime.now()
today = time.strftime("%Y%m%d")
logfile_path = logfolder_path + "/py_" + today + ".log"
print("logfile_path : " + logfile_path)

# ファイルを追記モードで作成(ファイルがなければ新規作成)
pyfile = open(logfile_path, 'a+')
nowtime = time.strftime("%Y-%m-%d %H:%M:%S")
pyfile.write(nowtime + " FILE OPEN\n")


# 引数確認。不足していれば0を出力して終了。
if len(args) != 3:
    pyfile.write(nowtime + " ARGUMENTS MISMATCH : args is " + str(len(args)) + "\n")
    print('0')
    exit()

date_from = args[1]
date_to = args[2]

try:
    code = 'U.S. 10Y'
    market = 'united states'
    data = investpy.get_bond_historical_data(bond=code, from_date=date_from, to_date=date_to)
    data = data.pct_change(periods=1).tail(1)
    data = data.iat[0, 3]
    pyfile.write(nowtime + " COMPARE : " + str(data) + "\n")
except:
    pyfile.write(nowtime + " INVESTPY FAILED : Couldn't get the data\n")
    print('0')
else:
    if data >= 0:
        pyfile.write(nowtime + " SIGNAL : -1\n")
        print('-1')
    elif data < 0:
        pyfile.write(nowtime + " SIGNAL : 1\n")
        print('1')
    else:
        pyfile.write(nowtime + " SIGNAL : 0\n")
        print('0')


pyfile.close()