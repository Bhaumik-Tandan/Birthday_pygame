import json
  
f = open('settings.json',)
d = json.load(f)
print(d["window width"]+1)
f.close()