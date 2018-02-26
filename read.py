import urllib

link = "https://archive.ics.uci.edu/ml/machine-learning-databases/ionosphere/ionosphere.data"
f = urllib.urlopen(link)
myfile = f.read()
print len(myfile)
f=open('pso.txt','w')
f.write(myfile)
f.close()