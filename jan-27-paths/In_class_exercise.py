import json

import pandas as pd



def birth_state():
    f = open("presidents.json")
    presidents = json.load(f)
    prezs = []
  
    for president in presidents :
        df = pd.DataFrame(presidents) 
        prez = df.sort_values(by='BirthState',ascending=True,)
        #prez = (president['First'])
        #prezs.append(prez)
    print(prez)
print(birth_state())
#test