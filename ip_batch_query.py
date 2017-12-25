from urllib import parse,request
import time
import datetime


def post(line):
    t=time.time()
    t=str(int(round(t*1000)))
    data={'ip':line}
    data = parse.urlencode(data).encode(encoding='utf-8')
    header_dict={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    url='http://ip.chinaz.com/ajaxsync.aspx?at=ip&callback=jQuery111301579963096168534_'+t
    req = request.Request(url=url,data=data,headers=header_dict)
    res = request.urlopen(req)
    res = res.read()
    res=res.decode(encoding='utf-8')
    res=res.split("'")
    f = open('ip_op.txt','a',encoding='utf-8')
    f.write(line+"\t"+res[7]+"\n")
    f.close()
    print(res[7])
    time.sleep(0.1)

def main():
    i=0
    for line in open("ip.txt"):
        if i in range(0,100) :
            line=line.replace('\n',"").replace('\t',"")
            print(line)
            print(i)
            post(line)
            i=i+1
        else:
            i=0
            time.sleep(10)


if __name__ == '__main__':
    main()
