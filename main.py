import pyvisa as visa

class owon:
    def _init__(self):
        self.usb = None
    
    def appVolt(self, v):
        self.channel

if __name__ == "__main__":
    #while(True):
        rm = visa.ResourceManager()
        res = rm.list_resources()
        num = list(range(0, len(res)))
        dic = list(zip(num, res))
        dev = int(input("Enter your devices correspoding number:\n" + str(dic) + "\n"))
        print(dic[dev])
        # obj = rm.open_resource(dev)
