import pandas as pd
import numpy as np
import requests
import json

response = requests.get("https://api.the-odds-api.com/v4/sports/upcoming/odds/?regions=us&markets=h2h&oddsFormat=american&apiKey=fa59214500c3ee27dd499bf436405160")
jsonResponse = response.json()
#print(jsonResponse)
print(jsonResponse.keys)
print('test')