# GPIO-lib-for-OrangePi
把gpio.py放置在你的python代码路径下。
Put the gpio.py to your code's local.
然后用 "import gpio"来加载它。
Then "import gpio".
用法:
Use:
[The PIN name must be spell in CAPITAL.As:"PA4","PD9"]
[PIN管脚名字必须大写，例如:"PA4","PD9"]
[And the PIN number must be units.]
[PIN管脚的第三位数字只能是单位，这个以后会修复...:)]

gpio.pinMount("PIN name") #To export the PIN. 挂载这个管脚

gpio.pinUmount("PIN name") #To Unexport the PIN. 卸载这个管脚

gpio.pinMode("PIN name","INPUT/OUTPUT","on/off") #To set the PIN mode(INPUT/OUPUT). 设置管脚模式(输入/输出)

gpio.pinValue("PIN name","Value/high/low","on/off") #To set the PIN value.[high = 1,low = 0] 设置管脚输出等级.[high为1，low为0]

更多功能以后会添加
当然你也可以自己添加，毕竟开源
转载的话注明一下这个网址就是了
【英语不太好的我:(】
