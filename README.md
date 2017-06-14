# WeChatMpDemo
WeChat mpdemo|Python|Flask 一个用Python写的微信公众号开发接口Demo，使用到了Flask。

- 在微信公众号后台，可以配置使用服务器接口接管用户和公众号的互动，用户发的每一条消息都会通过http reques转发给你指定的后台接口。  
- 收到消息以后你在5s内回复该http request特定格式的内容，你回复的信息就会透传给用户。

## 如何接入
- 上传mp_demp.py到你的服务器
- ```python mp_demp.py```
- 在公众号后台配置你的URL。token和key实际使用会用到，demo暂不考虑。保存配置以后，微信会给你指定的接口发一个GET请求让你校验通过以后再返回echostr，我这里不做校验全部通过。
- 实际用户给你发送的消息都是通过POST请求发来的，格式是：
```
<xml>
 <ToUserName><![CDATA[toUser]]></ToUserName>
 <FromUserName><![CDATA[fromUser]]></FromUserName>
 <CreateTime>1348831860</CreateTime>
 <MsgType><![CDATA[text]]></MsgType>
 <Content><![CDATA[this is a test]]></Content>
 <MsgId>1234567890123456</MsgId>
 </xml>
```
- 我们取出给你发消息的用户名msg_to，你自己的用户名msg_from，内容content，使用send方法提供的模板回复消息,用户就能收到了！

![](https://raw.githubusercontent.com/blue1244/static/master/WeChatMpDemo/1.jpeg)
![](https://raw.githubusercontent.com/blue1244/static/master/WeChatMpDemo/2.jpeg)
![](https://raw.githubusercontent.com/blue1244/static/master/WeChatMpDemo/3.jpeg)



- 参考   
https://mp.weixin.qq.com/wiki   
http://jayveehe.github.io/2015/01/26/nginx-flask/
