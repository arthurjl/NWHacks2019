from flask import Flask, render_template
import networkx as nx
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt

G=nx.star_graph(0)

# Posts == array of dictionaries/objects given by selenium
# posts = [{
# 	"Picture": URL,
# 	"Score": 5,
# 	"Profile": James,
# 	"Date": 1/26
# }]

pictureArray = []
for i, post in enumerate(posts):
	response = requests.get(i.get("Picture"))
	img = Image.open(BytesIO(response.content))
	pictureArray.append(img)
	G.add_edge([0,1]) 

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
    
    
    
