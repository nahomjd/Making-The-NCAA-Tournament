import requests
import csv

urlTemp = 'https://d17lgqwvsissft.cloudfront.net/short/cbb/inc/players_search_list.csv'
'''
':authority': 'd17lgqwvsissft.cloudfront.net'
:'method': 'GET'
:'path': '/short/cbb/inc/players_search_list.csv'
:'scheme': 'https'
'accept': '*/*'
'accept-encoding': 'gzip, deflate, br'
'accept-language': 'en-US,en;q=0.9'
#######'if-modified-since': 'Sat, 07 Mar 2020 10:21:14 GMT' (Causes blank)
#######'if-none-match': '"5e63759a-4dfbff"' (Causes blank)
'if-modified-since': 'Sat, 07 Mar 2020 10:21:14 GMT','if-none-match': '"5e63759a-4dfbff"'
'origin': 'https://www.sports-reference.com'
'referer': 'https://www.sports-reference.com/cbb/schools/connecticut/'
'sec-fetch-dest': 'empty'
'sec-fetch-mode': 'cors'
'sec-fetch-site': 'cross-site'
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36
'''
headers = {'authority': 'd17lgqwvsissft.cloudfront.net','method': 'GET','path': '/short/cbb/inc/players_search_list.csv',\
'scheme': 'https','accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9',\
'if-modified-since': 'Sat, 07 Mar 2020 10:21:14 GMT','if-none-match': '"5e63759a-4dfbff"','origin': 'https://www.sports-reference.com'\
,'referer': 'https://www.sports-reference.com/cbb/schools/connecticut/',\
'sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'cross-site',\
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

'''
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',\
'referer':'https://www.sports-reference.com/cbb/schools/connecticut/','accept':'*/*','authority':'d17lgqwvsissft.cloudfront.net',\
'method':'GET','path':'/short/cbb/inc/players_search_list.csv','scheme':'https','accept-encoding':'gzip, deflate, br','accept-language':'en-US,en;q=0.9',\
'if-modified-since':'Thu, 05 Mar 2020 10:22:24 GMT','if-none-match':'"5e60d2e0-4dfc2c"','origin':'https://www.sports-reference.com','sec-fetch-dest':'empty',\
'sec-fetch-mode':'cors','sec-fetch-site':'cross-site'}
'''
proxies = {'https': 'http://107.190.148.202:50854'}

file = 'temp24.csv'
f = open(file,'wb')
CSV = requests.get(urlTemp, headers=headers)
f.write(CSV.text.encode('ascii'))
'''
page = response.text.split('\n')
for line in page:
	if '<tr >' in line:
		print(line)

print(response.content)
'''