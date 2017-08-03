# -*- coding: utf-8 -*-
####給四個參數 網址,'鄉鎮市區','土地區段位置或建物區門牌', '交易年月'
####印出符合這些條件的成交價平均值 (交易年月指判斷年)

import urllib
import json
import sys      #for argc, argv
import re       #for regular espression

if len(sys.argv) < 5:
  print "error"
  sys.exit(0)

#url = 'http://www.datagarage.io/api/5365dee31bc6e9d9463a0057'
url = sys.argv[1]
page = urllib.urlopen(url).read()
#print page
data = json.loads(page)

money = 0.0	#總房屋成交價
count = 0   #數了幾間房

####parse all of the data
for item in data:
	if item[u'鄉鎮市區'] == sys.argv[2].decode('utf-8'):
		# print item[u'鄉鎮市區']
		if re.search(sys.argv[3].decode('utf-8'), item[u'土地區段位置或建物區門牌']):
			#print item[u'土地區段位置或建物區門牌']
			year = item[u'交易年月'] / 100    #delete the month
			sysyear = int(sys.argv[4])
			if year >= sysyear:
				#print type(item[u'總價元'])
				money += item[u'總價元']
				count += 1
if count == 0:
	print u"沒有資料"
else:
	print (int)(money/count)

	
	
