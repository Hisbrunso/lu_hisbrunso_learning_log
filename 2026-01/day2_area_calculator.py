# 建筑面积快速计算器
# 作者：罗天佑
# 日期：2026-01-29

print("=== 建筑师的Python工具 ===")

# 1. 输入数据（使用input函数）
length = input("请输入建筑长度（米）：")
width = input("请输入建筑宽度（米）：")
height = input("请输入层高（米）：")

# 2. 数据转换（input得到的是文字，要变成数字）
length = float(length)
width = float(width)
height = float(height)

# 3. 计算（你的建筑学公式）
area = length * width
volume = area * height

# 4. 输出结果（带单位）
print(f"占地面积：{area} 平方米")
print(f"建筑体积：{volume} 立方米")

# 5. 检查规范（简单的条件判断，为明天预热）
if area > 1000:
    print("⚠️ 注意：超过1000㎡，需要设置两个安全出口")
else:
    print("✅ 面积合规，可设置一个安全出口")
