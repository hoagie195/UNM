class registeredIPS:
    def __init__(self):
        self.ips = []
        super().__init__()

    def updateIPSTime(self,timePassed):
        for ip in self.ips:
            ip.updateTime(timePassed)
    
    def updateIPSInfo(self, dst):
        for ip in self.ips:
            ip.updateInfo(dst)