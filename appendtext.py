from sys import argv
script, fname = argv
print('this is the content of the file before edit')
f = open(fname)
print(f.read())
f.close()
f = open(fname, 'a')
txt = input('enter the new text here: ')
f.write(txt)
f.close()
print('this is the content of the file after editing')
f = open(fname)
print(f.read())
