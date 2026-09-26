# GeoPort4CN

> 本项目 fork 自 [davesc63/GeoPort](https://github.com/davesc63/GeoPort)，在原版基础上针对中国大陆网络环境进行了适配改造。感谢原作者 [@davesc63](https://github.com/davesc63) 的出色工作。

<p align="center">
  <a href="https://github.com/dyhuzh/GeoPort4CN/releases">📦 下载适配中国大陆网络的最新版本</a>
</p>

---

## 中国大陆适配说明

原版 GeoPort 在中国大陆使用时存在以下问题：

- 地图使用 OpenStreetMap / Google Maps，需要翻墙才能正常加载
- 搜索地点使用 OSM Nominatim，国内访问受限
- 坐标系为 WGS-84，而中国大陆地图普遍使用 GCJ-02（火星坐标），直接定位会产生偏移
- 程序启动时请求 GitHub 获取版本信息，在 GFW 环境下会导致卡顿

**GeoPort4CN 的改进：**

- 改用高德地图（无需 API Key，无需翻墙）
- 支持高德 API 地点搜索（可选，需自行申请免费 Key）
- 在中国大陆模式下自动进行 GCJ-02 → WGS-84 坐标转换，用户无感知
- 中国大陆模式下跳过 GitHub 网络请求

### 下载与使用

1. 前往 [Releases](https://github.com/dyhuzh/GeoPort4CN/releases) 下载对应平台的安装包
2. **macOS 用户**：（注意区分 Apple Silicon 版本和 Intel 版本）打开 DMG，将应用拖入「应用程序」文件夹，首次运行需在「系统设置 → 隐私与安全性」中点击「仍要打开」，每次运行均需输入用户密码
3. **Windows 用户**：解压 zip，以管理员身份运行 `GeoPort4CN.exe`

### 工作机制

程序启动时会检测当前 IP 地址，如果判断为中国大陆 IP，则自动启用中国大陆模式。用户也可以在页面右上角手动开启或关闭。

启用中国大陆模式后：

- 地图自动切换为高德地图（普通图、卫星图、混合图）
- 在地图上点击选点时，坐标自动从 GCJ-02 转换为 WGS-84 后再发送给 iOS 设备
- 地点搜索使用高德 API（可选，如果不提供则回退至 OSM Nominatim API，定位会存在偏差）

### 高德 API Key 申请

高德地点搜索功能需要一个免费的 API Key（仅地图加载不需要）：

1. 前往 [高德开放平台](https://lbs.amap.com) 注册/登录
2. 进入「控制台」→「应用管理」→「我的应用」→「创建新应用」
3. 在应用下点击「添加 Key」，服务平台选择 **Web 服务**
4. 复制生成的 Key，填入 GeoPort4CN 设置页面即可

注意：Key 不会上传至任何服务器，且支持本地持久化保存，避免每次运行重复设置。

### ☕️ 请我喝杯咖啡

如果你觉得项目对你有用，可以请我或原作者喝杯咖啡，感谢你的支持！

![./images/PayQrcode.png](images/PayQrcode.png)

---

## Changes from the original / 对原作者的说明

*For [@davesc63](https://github.com/davesc63) and anyone reviewing this fork:*

This fork adds a **China Mainland Mode** to make GeoPort usable without a VPN in mainland China. 

---

# GeoPort: Your Location, Anywhere! 🌍

<p align="center">
  <a href="https://www.buymeacoffee.com/davesc63">
    <img src="https://img.buymeacoffee.com/button-api/?text=Buy%20me%20a%20beer&emoji=🍺&slug=davesc63&button_colour=FFDD00&font_colour=000000&outline_colour=000000&coffee_colour=ffffff" alt="Buy me a beer">
  </a><br> https://geoport.me
</p>

[![Join Discord](https://img.shields.io/badge/Discord-Join%20Us-7289DA?logo=discord&style=for-the-badge)](https://discord.gg/genRca55Nb)<br>
<a href="https://github.com/davesc63/GeoPort/releases/tag/v4.0.2">Release Notes and Downloads</a><br><p>
<a href="https://github.com/davesc63/GeoPort/blob/main/FAQ.md">Need Help? - FAQ</a><br><p>
<a href="https://www.surveymonkey.com/r/BLQ8M75">Your feedback helps - Fill out the Survey</a>

<p align="center"><strong>GeoPort needs your help.</p></strong> </p>
Please consider <strong>donating</strong> and supporting the project. Your support helps to grow the platform and features.<br><p></p><br><p></p>

Immerse yourself in a world of possibilities with **GeoPort**, the ultimate location simulation app. GeoPort allows you to take control of your virtual presence, letting you be anywhere on the globe at the touch of a button. Whether you want to explore distant cities, surprise friends with exotic check-ins, or test location-based apps, GeoPort is your passport to a limitless world.

## Key Features

- **Global Presence**
  Spoof your location and appear as if you're in any city, country, or landmark globally.

- **Explore with Ease**
  Experience the thrill of virtual travel without leaving your comfort zone. Wander the streets of Tokyo, relax on a beach in Bali, or stroll through the historic alleys of Rome—all from the palm of your hand.

- **Test Apps Effectively**
  Developers, take note! GeoPort is your go-to tool for testing location-based features in your apps. Simulate diverse scenarios effortlessly.

- **Privacy and Security**
  Your privacy matters. GeoPort ensures a secure experience, allowing you to control when and where your virtual self appears.

- **User-Friendly Interface**
  Seamlessly navigate GeoPort's intuitive interface. Set your desired location with a few taps and teleport within seconds.

- **Unleash Your Imagination with GeoPort!**
  Download now and elevate your location experience beyond boundaries. Teleportation has never been this easy—**GeoPort**, where every location is just a click away!

<p align="center">
  <img src="https://raw.githubusercontent.com/davesc63/GeoPort/main/images/geoport2.png" alt="geoport" width="50%"><br><br>
   <img src="https://raw.githubusercontent.com/davesc63/GeoPort/main/images/geoport-demo.gif" alt="geoport">
</p>

## Fuel Mode:

For the :australia: Aussies :australia: who love to fire up their choppers and get their *Frugal Fuels* from the KwikiMart.
the **"Fuel"** mode of GeoPort to easily select the best prices across Australia! There is even the ability to select **state-based** pricing

<p align="center">
<img src="https://github.com/davesc63/GeoPort/blob/main/images/fuel.png" alt="fuel" width="50%">
</p>

## Developer Mode

**Developer Mode:** Enable developer mode on connected iOS devices.

They've made it harder to enable Developer Mode, but GeoPort handles it with ease. If you don't have Developer Mode enabled on your iOS device - you will need to temporarily remove your passcode to allow GeoPort to enable Developer Mode (Don't worry, GeoPort will let you know when running the app)

<p align="center">
<img src="https://github.com/davesc63/GeoPort/blob/main/images/devmode.png" alt="devmode" width="50%">
</p>

**Passcode Handling**

<p align="center">
<img src="https://github.com/davesc63/GeoPort/blob/main/images/passcode.png" alt="passcode" width="50%">
</p>

## Prerequisites

An iOS device and a sense of adventure!
*That's Right* - you do not need to install complex apps like python for **GeoPort** to work

**Windows Users**
You will need to install iTunes (we need their USB service so we can discover the iOS device!)

## Installation

- [Download](https://github.com/davesc63/GeoPort/releases/) the package for your operating system
- Run the application
- Explore the world and **Simulate Location**

## App Notes

- iOS 17 & iOS 18 are supported on both Windows and Mac
- Administrator / Sudo permissions are required for iOS17
- If you forget to reset your location when you disconnect, Don't worry! Simply connect your device again and "Stop Location"

## Tech Stuff and recognition

GeoPort is built with python, flask and pymobiledevice3
Interface inspired by the popular iFakeLocation, GeoPort is built for familiarity with the addition of iOS17 and Windows support (Windows release imminent)

Pymobiledevice3 - https://github.com/doronz88/pymobiledevice3<br>
iFakeLocation - https://github.com/master131/iFakeLocation

## Keywords

iOS 17, location spoofing, ios17 location simulation, ios17 windows support<br>
iOS 18, location spoofing, ios18 location simulation, ios18 windows support

## Pay it forward

If this tools helps you, please consider buying me a beer so I can keep this app going!<br>

<p align="center">
  <a href="https://www.buymeacoffee.com/davesc63">
    <img src="https://img.buymeacoffee.com/button-api/?text=Buy%20me%20a%20beer&emoji=🍺&slug=davesc63&button_colour=FFDD00&font_colour=000000&outline_colour=000000&coffee_colour=ffffff" alt="Buy me a beer">
  </a>
</p>
