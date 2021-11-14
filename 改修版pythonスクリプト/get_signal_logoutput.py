import sys
import os
import datetime
import investpy
import logging

# フォルダの存在を確認。なければ作成する
folder_path = "./python_log"
if not os.path.exists(folder_path):
    print(os.path.exists(folder_path))
    os.mkdir(folder_path)

# ファイルパスに folder_path/py_YYYYMMDD.log　を入れる
time = datetime.datetime.now()
today = time.strftime("%Y%m%d")
file_path = folder_path + "/py_" + today + ".log"

# ファイルを追記モードで作成(ファイルがなければ新規作成)
pyfile = open(file_path, 'a+')
nowtime = time.strftime("%Y-%m-%d %H:%M:%S")
pyfile.write(nowtime + " FILE OPEN\n")
logging.basicConfig(filename=pyfile, level=logging.DEBUG)

# 引数確認
args = sys.argv
if len(args) != 3:
    pyfile.write(nowtime + " ARGUMENTS MISMATCH : args is " + str(len(args)) + "\n")
    print('0')
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
　　logger = logging.getLogger(__name__)
    logger.error("日付が正しくありません")
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
    logging.exception("処理エラーが発生しました")
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