import random
#Opens text document
with open('krewes.txt', 'r') as f:
    krewes = f.read()
#Get a random key from a dictionary
def getsRandKrew(dic):
    keys = list(dic.keys())
    keyIndex = random.randint(0, len(keys)-1)
    return keys[keyIndex]

def getDevo():
  list = krewes.split("@@@")#Makes list with each devos info
  d_pd = {} #makes dictionary with name as key and period as value
  d_ducky = {}#makes dictionary with name as key and ducky as value
  for i in list: #Splits each devos info
      m = i.split("$$$")
      d_pd[m[1]] = m[0]#Adds name and pd
      d_ducky[m[1]] = m[2]#Adds name and ducky


  p = getRandKrew(d_pd)#Gets random devo

  print("name:", p,"period:", d_pd[p],"ducky:", d_ducky[p]) #prints devo and their values





getDevo()
