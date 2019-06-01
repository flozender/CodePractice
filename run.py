#By Tayeeb Hasan
def likes(names):
    if len(names)==0:
        string="no one likes this"
        return string
    elif len(names)==1:
        string="%s likes this" %(names[0])
        return string
    elif len(names)==2:
        string="%s and %s like this" %(names[0],names[1])
        return string
    elif len(names)==3:
        string="%s, %s and %s like this" %(names[0],names[1],names[2])
        return string
    elif len(names)>=4:
        string="%s, %s and %d others like this" %(names[0],names[1], len(names)-2)
        return string
   
count=likes(['John','Jacob','Jessica','Johan','Javier'])
print(count)
