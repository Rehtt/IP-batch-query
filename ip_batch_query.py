#!/bin/python3
from urllib import parse,request

##采用“站长之家”的ip查询（http://ip.chinaz.com/siteip）
##查询完结果保存在“ip_op.txt”文件
def zzzj_ip_post(line):
    import time
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
    res=str(res).split("'")
    f = open('ip_op.txt','a')
    f.write(line+"\t"+res[7]+"\n")
    f.close()
    print(res[7])
    time.sleep(0.1)


##将要查询的ip地址放在“ip.txt”文件中
if __name__ == '__main__':
    for line in open("ip.txt"):
        line=line.replace('\n',"").replace('\t',"")
        print(line)
        # get(line)
        zzzj_ip_post(line)

