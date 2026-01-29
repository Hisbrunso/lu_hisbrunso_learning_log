# day3_robust_calculator.py
# 目标：学会异常处理，让程序更健壮

print("=== 健壮的建筑面积计算器 v2.0 ===")
print("（提示：这次输入'abc'试试看会发生什么）\n")

try:
    length = float(input("请输入建筑长度（米）："))
    width = float(input("请输入建筑宽度（米）："))
    
    area = length * width
    
    print(f"\n占地面积：{area} 平方米")
    
    if area > 1000:
        print("⚠️ 注意：超过1000㎡，需要设置两个安全出口")
    else:
        print("✅ 面积合规，可设置一个安全出口")
        
except ValueError:
    print("\n❌ 输入错误：请输入纯数字（如 8.5），不要输入文字或单位")
    print("程序没有崩溃，而是优雅地退出了。这就是异常处理。")

print("\n程序正常结束。")
