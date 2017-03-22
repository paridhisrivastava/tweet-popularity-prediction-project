__author__ = 'Aditya Murthy'
__author__ = 'Paridhi Srivastava'
__author__ = 'Vatsala Singh'
# Scrapes the top 1000 most followed handles from twitaholic.com, 
# requires Python 2.7 with BeautifulSoup.
# by Aditya S Murthy, Paridhi Srivastava and  Vatsala Singh, RIT

from BeautifulSoup import BeautifulSoup # import libraries
import urllib

url_list=[]
handle_list=[]

for i in range(100,1100,100):
	url_list.append('http://twitaholic.com/top'+str(i)+'/followers/') # generate the url list for top 1000

for url in url_list:
	page=urllib.urlopen(url).read() # open the page 
	soup=BeautifulSoup(page) # soupify
	boxed_handles = soup.findAll('td','statcol_name') # handles are in td tags with class statcol_name
	for account in boxed_handles:
		handle_list.append(str(account.a['href'].strip('/'))) # maintain a list of handles

with open('Twitter1000.csv', 'w') as f: # write into a csv file
	for i in range(0,len(handle_list)):
		f.write(str(i+1)+','+handle_list[i]+','+'1\n') # format: sl.no,handle,1
