import importlib.metadata as metadata

info = metadata.metadata('matplotlib')
dependencies = metadata.requires('matplotlib')
dep = []
for i in dependencies:
    s = ''
    for j in i:
        if j != '>' and j != "!" and j != ";" and j != '<':
            s += j
        else:
            dep.append(s)
            break
