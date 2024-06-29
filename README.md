# 无需监听模式网卡，支持Win, Python自动化破解WiFi密码

---

wifi-default-initial-passwords.txt 这是一些路由器的**默认登陆地址**和**默认管理员密码**

wordlist.txt 这些口令中包含了大量的19990101这种日期

weak-password-set.txt 这是弱口令

---

---

python脚本非常简单，有一些可以定义的东西，你可以修改这部分

```python
        if network.ssid == "likewendy":
            continue
        if network.ssid == "ChinaNet-acgx":
            continue
        if network.ssid == "":
            continue
        # if network.signal <= -75:
            # continue
        if network.ssid != "TP-LINK_DFB7":
            continue
```

---

---

默认对pywifi返回的SSID倒序遍历破解

```python
# 你可以修改这一句，去除reversed从而正序
# 如果你设置了 if network.signal <= -xx: 正序和倒序实际上都差不多
for i,network in enumerate(reversed(wifi_list)):
```

---

---

密码字典中有些密码好像是为WPA设计的，非常短，我设置了限制

```python
            if len(passwd) < 8:
                continue
```

如果有需要你可以修改此限制

---

对于成功概率，你是否听说过一句话，给一个猴子无限长的寿命和一个键盘，它总有一天能敲出Windows操作系统