
# coding: utf-8

# In[23]:


def print_all_friends(list_f,person):
    list_ff=[]
    set_ff=set()
    
    list_ff.append(person)
    set_ff.add(person)
    
    while list_ff:
        test = list_ff.pop(0)
        for s in list_f[test]:
            if s not in set_ff:
                list_ff.append(s)
                set_ff.add(s)
    print(set_ff)
    

fr_info = {
    'Summer' : ['John', 'Justin', 'Mike'],
    'John' :['Summer', 'Justin'],
    'Justin' : ['John', 'Summer', 'Mike', 'May'],
    'Mike':['Summer', 'Justin'],
    'May':['Justin', 'Kim'],
    'Kim':['May'],
    'Tom':['Jerry'],
    'Jerry':['Tom']
}

print_all_friends(fr_info, 'Summer')


# In[ ]:


def print_all_node(gr_info,st_node):
    list_n=[]
    set_n=set()

    list_n.append(st_node)
    set_n.add(st_node)

    while list_n:
        for x in gr_info[list_n.pop(0)]:
            if x not in list_n:
                list_n.append(x)
                set_n.add(x)
    print(set_n)



gr_info = {
    '4' : ['2'],
    '2' : ['4','1','5'],
    '1' : ['2','3'],
    '3' : ['1'],
    '5' : ['2']
}

print_all_node(gr_info,'1')

