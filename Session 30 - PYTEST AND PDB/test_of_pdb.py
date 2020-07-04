##PDB: PYTHON DEBUGGER
# DEBUGGING => TRYING TO FIND BUG/MISTAKES IN
# CODE
# pdb is builtin

a = 50
b = 700
c = "akhila madhu"

breakpoint()

print(a+b)

print("on 13 line")

print("on 15 line now")

def this_function(a,b):
    print("we are inside this_function")
    print(a+b)

this_function(a,b)



# cmd: py test_of_pdb.py
# cmd: python .pytest_of_pdb

# (pdb) comes automatically after above cmd
# cmd: (pdb) print(a)
# cmd: (pdb) print(b)
# cmd: (pdb) whatis a
# cmd: (pdb) whatis c

# cmd: (pdb) n => next
# cmd: (pdb) c => continue (run the whole code till the end)
# cmd: (pdb) s => step inside