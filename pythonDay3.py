'''
#__________________17/07/26________________
            data types
            ----------
    to find date type of a variable we can use type() function
    ------>syntex : type( variable_name )
    to find memory location of a variable we can use id() function
    ------>syntex : id( variable_name )

integers - 1, 2, 3, 4, 5# it's not iterable 
floats - 1.0, 2.0, 3.0, 4.0, 5.0
strings
--------
it is a sequence of characters which is enclosed in single quotes(' '), double quotes(" "), triple single quotes(''' ''') or triple double quotes(""" """)
 - "Hello", 'World', '' Python'', """ Programming"""
 it's is immutable--- not modifiable

 it is iterable and indexable

 methods of string
-----------------
replace() - it is used to replace a particular character with another character in a string
    example :               #---------->syntax : variable_name.replace(old_character, new_character, count)#count is optional-- how many times we want to replace the character 
    str = "Hello World"
    print(str.replace("World", "Python"))
    print(str)# immutable 

join() - this method will add the new character after every character of the string
    example :               ---------->syntax : 'new_string'.join(variable_name)
    str = "hello everyone"
    print(' '.join(str))

split() - it is used to split the string into a list of words based on a particular character
    example :               ---------->syntax : variable_name.split(character)
    str = "hello_everyone"
    print(str.split("_"))#output : ['hello', 'everyone']

    time_ = input("Enter the time in 24 hour format : ")
    time =time_.split(":")
    print(f'time: {int(time[0])-12}:{time[1]}:{time[2]} ')

index() - it is used to find the index of a particular character in a string(it tells the first occurence of the character in the string)
    example :               ---------->syntax : variable_name.index(character)
    str = "hello everyone"
    print(str.index("e"))#output : 1
count() - it is used to find the number of occurences of a particular character in a string
    example :               ---------->syntax : variable_name.count(character)
    str = "hello everyone"
    print(str.count("e"))#output : 4
indexing 
    example :               ---------->syntax : variable_name[index]
    str = "hello everyone"
    print(str[0], str[1], str[2])#output : h e l

list - [1, 2, 3, 4, 5]# collection of different data types # it is mutable and iterable 
            representation of list is in square brackets[] and separated by commas ,
    example :               ---------->syntax : variable_name[index]
    list_ = [1, 2, 3, 4, 5, "hello", 3.14, True,[1, 2, [11,"world"],3]]
    print(list_[0], list_[1], list_[5], list_[8], list_[8][2][1][2]) #output : 1 2 hello [1, 2, [11, 'world'], 3] r
    mutable - we can change the values of the list
    example :               ---------->syntax : variable_name[index] = new_value
    list_ = [1, 2, 3, 4, 5]
    list_[0] = 10
    print(list_)#output : [10, 2, 3, 4, 5]
 methods of list
-----------------
append() - it is used to add a new element at the end of the list
    example :               ---------->syntax : variable_name.append(new_element)   
    list_ = [1, 2, 3, 4, 5]
    list_.append(6)
    print(list_)#output : [1, 2, 3, 4, 5, 6]
extend() - it is used to add multiple elements at the end of the list by seprate indexes
    example :               ---------->syntax : variable_name.extend(new_elements)
    list_ = [1, 2, 3, 4, 5]
    list_.extend([6, 7, 8])
    print(list_)#output : [1, 2, 3, 4, 5, 6, 7, 8]

    example :   for difference of append extend
    list_.append("python")
    print(list_)# output : [1, 2, 3, 4, 5, 'python']
    list_.extend("python")
    print(list_)# output : [1, 2, 3, 4, 5, 'python', 'p', 'y', 't', 'h', 'o', 'n']

remove() - it is used to remove a particular element from the list
    example :               ---------->syntax : variable_name.remove(element)
    list_ = [1, 2, 3, 4, 5]
    list_.remove(3)# delete the item based on the value given if not present it will give error
    print(list_)#output : [1, 2, 4, 5]

pop() - it is used to remove a particular element from the list based on the index
    example :               ---------->syntax : variable_name.pop(index)    
    list_ = [1, 2, 3, 4, 5]
    list_.pop(2)# delete the item based on the index position given if not present it will give error(out of range)
    print(list_)#output : [1, 2, 4, 5]
    list_.pop()# delete the last item of the list
    print(list_)#output : [1, 2, 4]



'''
