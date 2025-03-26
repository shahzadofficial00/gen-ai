# SETS:-
# set is unordered
# we are not used index and range in set

# st = {"hello","world"}
# st = set((False,True,"hello","world","!",0,1,"yes","true"))
# st2 = set(("philospher","hello menu"))

# st.add("philospher")"                 # Add one value
# st.update(st2)                        join new value
# st.pop()                              delete random value

# ls = list(st)
# print (ls)                             set to make list

# print(type(st))
# print(st)




# st = {"hello","world","!",'hello world'}

# st.remove("hello")                         # remove method
# st.discard("hello")                        # remove method
# st.clear()                                 # clear: empty string
# del st                                     # delete all set

# print(st)



# st1 = {"hello","world","!"}
# st2 = {"hello","menu"}

# st3 = st1.union(stt2)                        # union method
# st3 = st1.intersection(stt2)                 # intersection method
# st3 = st1 & st2                              # intersection method
# st3 = st1.difference(st2)                    # common things delete
# st3 = st1-st2                                  # minus things

# print(st3)


#ASSignment of SEt: change into typle and set and inpack

# st = {"item 1","item 2"}
# st1,st2 = st

# ls = list(st)
# print(type(ls))
# print(type(st))

# ls = (tuple(st))
# print(type(ls))

# Assignment of set union intersection and difference

# ls = set(["hello","world"])
# tup = set(("hello", "item"))

# nt = ls.intersection(tup)
# un = ls.union(tup)
# df = ls.difference(tup)
# print(nt,un,df)

#assignment unpack and make into list and append


# tup = ("a", "b", "c","d","e","f","g","h","i","f")
# st1,*st2,st3= tup

# print(st2)
# v = list(tup)
# print(type(v))
# v.append("453455")
# print(v)


# assignment

st1 = {"hello","world"}
st2 = {"how","are"}
set3 = {"you","fine"}
st4 = st1.union(st2,set3)
st5 = st4
ls = list(st5)
tup = tuple(st5)
print(st4)
print(type(ls),type(tup))




