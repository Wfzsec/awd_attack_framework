# awd_attack_framework
awd攻防常用脚本+不死马+crontab+防御方法
## 文件描述：
awd_attack.py  
------awd批量攻击主框架  
利用主办方欲留后门进行攻击  
rsa_client.php  
------rsa加密后门客户端  
加密攻击的payload并发送给种植在其他队伍服务器上的rsa_server.php  
rsa_server.php  
------rsa加密后门服务端  
解密攻击payload并返回执行结果  
rsa_attack.py  
------rsa木马测试  
测试rsa客户端和服务端是否可以实现互相通信  
nodie.php  
------不死马  
主要负责写入rsa不死马  
crontab.py  
------定时任务写入脚本  
crontab.txt  
------定时任务要写入的内容  
kill_crontab.php  
------清除crontab  
kill.php  
------清除不死马

