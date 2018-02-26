import wikipedia

x= wikipedia.summary("Facebook", sentences=1)

print x
print wikipedia.search("Naruto")
print wikipedia.page("Naruto").content