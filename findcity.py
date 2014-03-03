names={'LS':'lishuo','HRG':'huangruge','GCY':'GUOCHAOYU','ZZL':'ZHANGZILONG'}

def find_name(namemap,name):
    if name in namemap:
       return namemap[name]
    else :
       return "not found"
names['_find']=find_name

while True:
      print "enter name >"
      name = raw_input()
      if not name: break
     
      allname=names['_find'](names,name)
      print allname

