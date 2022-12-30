import pandas as pd
import numpy as np
import requests

response = requests.get("https://api.the-odds-api.com/v4/sports/upcoming/odds/?regions=us&markets=h2h&oddsFormat=american&apiKey=fa59214500c3ee27dd499bf436405160")
print(response)