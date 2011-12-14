import csv
from django.utils import simplejson

R = csv.reader(file('cities.csv','r'))

C = []
for r in R:
  C.append({
    "pk": len(C), 
    "model": "stanley_darpa.city", 
    "fields": {
      "name": r[0],
      "state": r[1],
      "population": int(r[2])
    }
  })

print simplejson.dumps( C )

