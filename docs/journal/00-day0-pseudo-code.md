# Day 0: 起步前的伪代码练习

&gt; 记录于 2026-01-28  
&gt; 说明：以下是我第一天学Python时写的练习，当时还不知道Python必须用英文关键字（def/print）。这些不是可执行代码，只是思维草稿。

---

## 练习1：Hello World（中文思维版）
print("Hello, 月之暗面！")
print("我是罗天佑，从建筑学出发。")
# 计算一下距离2028年12月还有多少天
import datetime
today = datetime.date.today()
target = datetime.date(2028, 12, 20)  # 考研时间
days_left = (target - today).days
print(f"距离目标还有 {days_left} 天")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
