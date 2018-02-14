import sched, time

def print_time(*msg):#?为什么用只写msg 必须为可变参数
    print("当前时间", time.time(), msg)

s = sched.scheduler(time.time, time.sleep)
print(time.time())
s.enter(5, 1, print_time, argument = ("延时5s,优先级1"))
s.enter(3, 2, print_time, argument = ("延时3s,优先级2"))
s.enter(3, 1, print_time, argument = ("延时3s,优先级1"))
s.run()
print(time.time())