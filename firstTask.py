import importlib.metadata as metadata

info = metadata.metadata('matplotlib')
dep = metadata.requires('matplotlib')
dependencies = []
homePage = info['Project-URL'].split(' ')[1]
author = info['Author']

for i in dep:
    s = ''
    for j in i:
        if j != '>' and j != "!" and j != ";" and j != '<':
            s += j
        else:
            dependencies.append(s)
            break

