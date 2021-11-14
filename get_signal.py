import sys
import investpy

args = sys.argv

if len(args) != 3:
    # print('0')を表示して、終了
    print('0')
    exit()

date_from = args[1]
date_to = args[2]

try:
    code = 'U.S. 10Y'
    market = 'united states'
    data = investpy.get_bond_historical_data(bond=code, from_date=date_from, to_date=date_to)
    #print(data.pct_change(periods=1).tail(3))
    data = data.pct_change(periods=1).tail(1)
    data = data.iat[0, 3]
except:
    print('0')
else:
    if data >= 0:
        print('-1')
    elif data < 0:
        print('1')
    else:
        print('0')
