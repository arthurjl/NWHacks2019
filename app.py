from flask import Flask, render_template, url_for
import networkx as nx
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt
from InstragramDataScraping import get_data

G=nx.star_graph(0)

# Posts == array of dictionaries/objects given by selenium
# posts = [{'src': 'https://instagram.fyvr1-1.fna.fbcdn.net/vp/2901cae5f91c3749859c3135b94ac860/5CE8DE19/t51.2885-15/e35/50300096_301480393758229_3987981158001670975_n.jpg?_nc_ht=instagram.fyvr1-1.fna.fbcdn.net', 'poster': 'instagram', 'likes': '379,095'}, {'src': 'https://instagram.fyvr1-1.fna.fbcdn.net/vp/a823d923266d9e06b62478ef5991190d/5CE7B8A1/t51.2885-15/e35/49753212_233226567611508_395983073781492838_n.jpg?_nc_ht=instagram.fyvr1-1.fna.fbcdn.net', 'poster': 'prattprattpratt', 'likes': '142,845'}, {'src': 'https://instagram.fyvr1-1.fna.fbcdn.net/vp/3c4f5ba1f68615180c8bdb041891664d/5C4FFC5E/t51.2885-15/e15/49792400_293877844820682_2398668401181985046_n.jpg?_nc_ht=instagram.fyvr1-1.fna.fbcdn.net', 'poster': 'chrisbrownofficial', 'likes': 'n/a'}]

# pictureArray = []
# for i, post in enumerate(posts):
# 	response = requests.get(i.get("Picture"))
# 	img = Image.open(BytesIO(response.content))
# 	pictureArray.append(img)
# 	G.add_edge([0,1]) 

app = Flask(__name__)

@app.route('/')
def home():
	posts = get_data()
	return render_template('index.html', posts = posts)
	

if __name__ == '__main__':
	app.run(debug=True)


    
    
    
