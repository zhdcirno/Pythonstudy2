def SayHello(name):
    print("你好，{0}".format(name))
    print("Done.........")

if __name__ == "__main__":
    print('***' * 10)
    name = input("你的名字：")
    print(SayHello(name=name))
    print('@@@' * 10)