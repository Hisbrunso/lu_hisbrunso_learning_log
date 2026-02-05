# day3_robust_calculator.py
# 目标：异常情况处理

print("=== 建筑面积计算器 v2.0 ===")
print("（请勿输入无效数据）\n")

while True:
    try:
        length = float(input("请输入建筑长度（米）/ Enter length (m): "))
    width = float(input("请输入建筑宽度（米）/ Enter width (m)："))
    
    area = length * width
    
    print(f"\n占地面积：{area} 平方米")
    
    if area > 1000:
        print("⚠️ 注意：超过1000㎡，需要设置两个安全出口")
    else:
        print("✅ 面积合规，可设置一个安全出口")
        
except ValueError:
    print("\n❌ 输入错误：请输入纯数字")

print("\n程序非正常结束，重新输入")
