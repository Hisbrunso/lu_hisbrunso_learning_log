print("Hello, 月之暗面！")
print("我是罗天佑，从建筑学出发。")

# 计算一下距离2028年12月还有多少天
import datetime
today = datetime.date.today()
target = datetime.date(2028, 12, 20)  # 考研时间
days_left = (target - today).days
print(f"距离目标还有 {days_left} 天")