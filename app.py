from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

url='https://www.worldometers.info/coronavirus/#countries'
req=requests.get(url)
bsObj=BeautifulSoup(req.text,"html.parser")

data=bsObj.find('table',{'class':'wikitable sortable mw-collapsible'})

table_data=[]
trs=bsObj.select('table tr')

for tr in trs[9:223]:
	row=[]
	for t in tr.select('td')[:20]:
		row.extend([t.text.strip()])
	table_data.append(row)
data=table_data

app=Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html',data=data)





if __name__ == '__main__':
	app.run(debug=True)