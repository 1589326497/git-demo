print("你好 世界")

b1=10   # 整型
b2=2.33    #浮点型
b3="20"  #字符串
b4=False #布尔
b5=None #空值类型

# b6=input("输入")  #输入
# print(b6)
# while not input("输入")=='1':
   # pass


if b1>20:
    print("假")
elif b1==20:
    print("真")
else:
    print("其他")

# 逻辑运算 and or not
if  b1>20:
    print("假")
elif b1==20:
    print("真")
else:
    print("其他")

# 链表
l1=[12,34,2.33,True]
l1[0]=99
print(l1)

# 元组 元组不可变
l2=(12,34,2.33,30)

# 字典 key value
l3={"k1":30,"k2":40}
l3["k1"]=20
print(l3)

# for循环
for i in l2:
    i=i+10
    print(i)

for i in range(1,100):
    print(i)
# while
i=20
while i>10:
    print(i)
    i=i-1

#函数
def add(x,y):
    print(x+y)

add(2,3)

#类
class Cat:
    def __init__(self,name,age):
        self.m_name=name
        self.m_age=age
    def speak(self):
        print("喵"*3)
        print(f"名字: {self.m_name} 年龄: {self.m_age}")
        # print("名字: {str_name} 年龄: {str_age}".format(str_name=self.m_name,str_age=self.m_age))


cat1=Cat("喵喵",3)
cat1.speak()

cat2=Cat("咪咪",4)
cat2.speak()

cat3=Cat("4",5)
cat3.speak()