**1.北京大学某单位的某台机器IP地址为162.105.80.160, 子网掩码为255.255.255.192，**

        1) 该单位的网络号(网络+子网)是多少？

        2) 该单位理论上可容纳多少主机？

        3) 北大可以有多少个这样的子网(假定北大全部是162.105网段)？

答：1）162.105.80

2）254是错的  62

3）65536是错的  1024

**2.解释TCP协议建立连接为什么设计为三步握手（3-way handshake）？**

答：*三次握手的目的*:
第一次： A->B，证明A能够传输信息。  
                 
第二次： ->B && B->A，证明B能够接收并传输信息。 
                  
第三次： A->B，证明A能够接收信息。

如果两次，那么B无法确定B的信息A是否能收到，若B未收到A的ACK，会超时重传自己的SYN同步信号，陷入死循环；如果四次，那么就造成了浪费，因为在三次结束之后，就已经可以保证A可以给B发信息，也可以收到B的信息； B可以给A发信息，也可以收到A的信息，即二者可建立连接。

**3.有哪些恶意软件, 如何防范恶意软件？**

答：*恶意软件有*：计算机病毒、蠕虫、木马、间谍软件、广告软件、Botnet等。

*如何防范*：恶意软件利用：软件的相似性、软件缺陷、未经许可的软件运行、用户权限过大、可执行程序的权限过大等漏洞，可通过安装杀毒软件/安全防护软件, 及时打补丁；使用防火墙； 禁止外部计算机通过网络访问本机；不随便下载运行可执行程序；不打开未知的邮件附件；U 盘通常带毒, 打开前要先查毒；不随便暴露自己e mail、生日、手机等重要信息；不以 Administrator 权限操作计算机等方式进行防范。
