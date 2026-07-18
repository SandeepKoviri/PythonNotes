'''
day 4 tuple and dictionary
------------------18/07/26----------------------

tuple
------
 ----> it a collections of different datatype that are represented in () and seprated by ,
 ----> it's immutable
 methos
 ------
 indexing
 --------   ---->syntex: variable_name[index]
 count
 -----      ---->syntex: variable_name.count(item)
 go = (1,'java', [3,4],("python",78))
 print(type(go))
 print(go.index('java'))
 print(go[2][1])
 print(go.count('python'))#output : 0 because it will not take item inside of inside
 print(go.count(("python",78)))#like this it work
 output:<class 'tuple'>
1
4
0
1

list_ = (1, 2, 3, 4, 5, "hello", 3.14, True,[1, 2, [11,"world"],3])
print(type(list_))
print(list_[0])

dictionary
----------
----> dict is a key:value pair
----> key and values seprated by :
----> dict is represented by {} and pair is seprated by ,
----> only take immuttable values
man = {[1,2]: 5}# error
man = {1:9,
      "name":"sandeep",
      (1,2):5}
print(man)
output:{1: 9, 'name': 'sandeep', (1, 2): 5}

methods
--------
-keys
-----> syntex :dict.keys()
-values
-----> syntex: dict.values()
-items
-----> syntex: dict.items()
-update
----->syntex: dictx.update({key:value})
            details['name'] ='sandeepkoviri'
-clear
------>syntex
example:
details = {
    'name':'sandeep',
    'college':"gvp",
    'pan': 546446,
    'adhr':6876,
    'pin': 1234
}
print(details.keys())
print(details.values())
print(details.items())
details.update({'name':'koviri sandeep'})
details.update({'gender':'male'})
print(details)
details['name'] ='sandeepkoviri'
# details.clear()
print(details)
print(details['name'])#to get
output:
dict_keys(['name', 'college', 'pan', 'adhr', 'pin'])
dict_values(['sandeep', 'gvp', 546446, 6876, 1234])
dict_items([('name', 'sandeep'), ('college', 'gvp'), ('pan', 546446), ('adhr', 6876), ('pin', 1234)])
{'name': 'koviri sandeep', 'college': 'gvp', 'pan': 546446, 'adhr': 6876, 'pin': 1234, 'gender': 'male'}
{'name': 'sandeepkoviri', 'college': 'gvp', 'pan': 546446, 'adhr': 6876, 'pin': 1234, 'gender': 'male'}
sandeepkoviri
'''