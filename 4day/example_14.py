import keyword
kwlist = keyword.kwlist
print(kwlist)
for kw in kwlist[:]:
    if len(kw) < 8:
        kwlist.remove(kw)
print(kwlist)
