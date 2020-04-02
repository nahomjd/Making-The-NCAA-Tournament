import requests
import urllib.request
import time
base =  'https://www.sports-reference.com'
url = 'https://www.sports-reference.com/cbb/schools/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
proxies = {'https': 'http://107.190.148.202:50854'}

response = requests.get(url, headers=headers)
page = response.text.split('\n')
file2 = open('names.txt','w+')
htmlPages = []
#file2.write('[')
i = 0

for line in page:
	if '<tr >' in line:
		school = line.split('"')
		links = []
		links.append(base+school[13]+'\n')
		links.append(school[13].split('/')[3]+'.html')
		htmlPages.append(links)
		#file2.write("'"+school[13].split('/')[3]+"'"+',')
		print(i)
		i += 1
#file2.write(']')
i=0
'''
for link in htmlPages:
	print(link[0])
	print(link[1])
	if i > 50:
		time.sleep(5)
		i = 0
	urllib.request.urlretrieve(link[0], link[1])	

urllib.request.urlretrieve(htmlPages[0][0], htmlPages[0][1])	
'''


file2.close()

'''
<tr ><th scope="row" class="right " data-stat="ranker" csk="1" >1</th><td class="left " data-stat="school_name" >
<a href="/cbb/schools/abilene-christian/">Abilene Christian Wildcats</a></td><td class="left " data-stat="location" csk="TX" >
Abilene, Texas</td><td class="center " data-stat="year_min" >1971</td><td class="center " data-stat="year_max" >2020</td><td class="right " data-stat="years" >10</td>
<td class="right " data-stat="g" >293</td><td class="right " data-stat="wins" >147</td><td class="right " data-stat="losses" >146</td>
<td class="right " data-stat="win_loss_pct" >.502</td><td class="right " data-stat="srs" >-10.95</td><td class="right " data-stat="sos" >-6.88</td>
<td class="right iz" data-stat="poll_final" >0</td><td class="right iz" data-stat="conf_champ_count" >0</td><td class="right " data-stat="conf_champ_post_count" >1</td>
<td class="right "data-stat="ncaa_count" >1</td><td class="right iz" data-stat="ncaa_final_four_count" >0</td><td class="right iz" data-stat="ncaa_champ_count" >0</td></tr>
'''