t = []
with open("states.txt","r+") as f:
	k = f.readlines()
	for i in range(len(k)):
		u = 28922+i
		t.append('https://www.tripadvisor.com/Hotels-g'+f'{u}-'+k[i].replace("\n","").replace(" ","_")+'-Hotels.html')
print(t)
# https://www.tripadvisor.com/Hotels-g28922-Alabama-Hotels.html
