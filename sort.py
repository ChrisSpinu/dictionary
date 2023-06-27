import json
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
objects = {}

f = open('dictionary.json')
json_data = json.load(f)

for i in alphabet:
    objects = {}
    for x in alphabet:
        objects = {}
        for y in json_data:
            if(y[0] == i):
                if(len(y) >= 2):
                    if(y[1] == x):
                        objects.update({y:json_data[y]})
        if((i+x) == 'ax'): print(len(objects))
        if(len(objects) != 0):
            z = open(i+x+".json", 'w')
            json.dump(objects,z,indent=2,ensure_ascii=False)

z = open("other.json", 'w')
objects = {}

for i in json_data:
    if(len(i) <= 1):
        objects.update({i:json_data[i]})
    if(i[0] not in alphabet):
        objects.update({i:json_data[i]})

json.dump(objects,z,indent=2,ensure_ascii=False)

f.close()
z.close()