class IP():
    def __init__(self, ipaddress):
        self.averageNetworkTraffic = 0
        self.totalNetworkTraffic = 1
        self.ipsrc = ipaddress
        self.time = 0
        self.dstList = []
        super().__init__()

    def updateInfo(self,dst):
        self.dstList.append(dst)
    
    def updateTime(self,timePassed):
        self.time = timePassed
        self.averageNetworkTraffic = self.totalNetworkTraffic / self.time

