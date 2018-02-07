



1. 打开windows设置，点击更新和安全
2. 点击针对开发人员，旁加载应用切换到选择开发人员模式。
3. 在设置种输入“windows 功能”然后打开
4. 在“适用于linux的windows子系统”前打勾
5. 管理员身份打开“powershell”，默认地址是“C:\Users\XXX\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Windows PowerShell”下。
6. 输入命令”Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux“。
接下来，你就可以在cmd或者是powershell或者是直接搜索bash来运行了。
7. 进入microsoft store 搜索Ubuntu获取

ubuntu安装在系统：
  C:\Users\keets\AppData\Local\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalState\rootfs
  
  
如果需要进入windows系统D盘：$ cd /mnt/d  