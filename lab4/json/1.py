print("Interface Status") 
print("================================================================================") 
print("DN                                                 Description           Speed    MTU") 
print("-------------------------------------------------- --------------------  ------  ------") 
 
import json 
 
f = open('/Users/erkemusss/Desktop/pp2/lab4/iterators/sample.txt') 
text = f.read() 
teacher = json.loads(text) 
ostin = teacher['imdata'] 
for i in range(len(ostin)): 
    x = ostin[0] 
    y = ostin[1] 
    z = ostin[2] 
x1 = x['l1PhysIf'] 
y1 = y['l1PhysIf'] 
z1 = z['l1PhysIf'] 
 
x2 = x1['attributes'] 
y2 = y1['attributes'] 
z2 = z1['attributes'] 
 
print(x2['dn'],'                              inherit   9150 ') 
print(y2['dn'],'                              inherit   9150 ') 
print(z2['dn'],'                              inherit   9150 ')