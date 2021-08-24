''''

    生产消费模型
    三个厨师做面包，蓝字中有500个面包，等两秒判断篮子是否满，若不满继续造
    六个客户抢面包，篮子面包不够时，等两秒再去买，每个人3000元，直到花光为止

'''
from threading import Thread
import time

breank = 500


class chushi(Thread):
    maker = ""

    def run(self) -> None:
        global breank  # 定义的面包声明为全局变量
        while True:
            if breank < 500:
                breank = breank + 1
                time.sleep(2)
                print(self.maker,"又做出来一个面包","篮子中还剩",breank, "个面包")
            elif breank == 500:
                print("篮子已满不需要做面包")


class buyer(Thread):
    nem = 0
    buy_money = 3000

    def run(self) -> None:
        global buymoney
        global breank
        while True:
            if breank >= 1:
                breank = breank - 1
                self.buy_money = self.buy_money - 3
                self.nem = self.nem + 1
                print(self.buyer, "买了一个面包！", "金钱剩余", self.buy_money, )
                time.sleep(1)
            elif self.buy_money < 0:
                print("您的余额不足无法继续购买")
                break


p1 = chushi()
p2 = chushi()
p3 = chushi()
a1 = buyer()
a2 = buyer()
a3 = buyer()
a4 = buyer()
a5 = buyer()
p1.maker = "大厨师"
p2.maker = "二厨师"
p3.maker = "三厨师"
a1.buyer = "张三"
a2.buyer = "李四"
a3.buyer = "王五"
a4.buyer = "赵六"
a5.buyer = "赵小宝"

p1.start()
p2.start()
p3.start()
a1.start()
a2.start()
a3.start()
a4.start()
a5.start()
