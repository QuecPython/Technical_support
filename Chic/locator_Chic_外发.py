import cellLocator
ret = cellLocator.getLocation("www.queclocator.com", 80, "aw7e1", 8, 1)  # 保密 不可外发
print("基站定位：",ret)


from wifilocator import wifilocator
wifilocator = wifilocator("aw7e1") # 保密 不可外发
ret = wifilocator.getwifilocator()
print("WiFi定位：",ret)


# 混合定位
import cellLocator
ret = cellLocator.startLocation("www.queclocator.com", 80, "aw7e1", 8, 1, 2)
print("混合定位：",ret)
