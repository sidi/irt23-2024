import re

filename = 'conflicted_file.txt'
with open(filename, 'w') as f:
    f.write('Some combined content which resolves the merge issue')
# repo is a git.Repo instance
repo.index.add([filename])
repo.index.commit("Simulating user resolving a conflict"+filename)

def fff():
	aa=0
	bba=aa+1
	return("Hello ",bba)

print("Helloiss branches!")

