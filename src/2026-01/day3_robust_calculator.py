# day4_persistent_calculator.py
# 目标：循环询问 + 异常处理 + 分阶段验证

print("=== 建筑面积计算器 v3.0 (循环验证版) ===\n")

# ========== 第一阶段：获取长度 ==========
while True:
    try:
        length = float(input("请输入建筑长度（米）："))
        if length <= 0:
            print("⚠️ 长度必须大于0，请重新输入\n")
            continue
        print(f"✅ 长度已记录：{length} 米\n")
        break  # 正确了才跳出
    except ValueError:
        print("❌ 输入错误：请输入纯数字\n")

# ========== 第二阶段：获取宽度 ==========
while True:
    try:
        width = float(input("请输入建筑宽度（米）："))
        if width <= 0:
            print("⚠️ 宽度必须大于0，请重新输入\n")
            continue
        print(f"✅ 宽度已记录：{width} 米\n")
        break  # 正确了才跳出
    except ValueError:
        print("❌ 输入错误：请输入纯数字\n")

# ========== 第三阶段：计算 ==========
area = length * width
print(f"占地面积：{area} 平方米")

if area > 1000:
    print("⚠️ 注意：超过1000㎡，需要设置两个安全出口")
else:
    print("✅ 面积合规，可设置一个安全出口")

print("\n程序正常结束。")
