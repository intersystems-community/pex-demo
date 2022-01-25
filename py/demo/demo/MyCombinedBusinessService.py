import iris.pex
import demo.MyRequest

class MyCombinedBusinessService(iris.pex.BusinessService):
    
    def OnInit(self):
        self.min = int(self.min)
        self.max = int(self.max)
        print("[Python] ...MyCombinedBusinessService:OnInit() is called with min: %d and max: %d" % (self.min, self.max))
        self.mid = 0.5*(self.min + self.max)
        print("[Python] ...MyCombinedBusinessService:OnInit() has mid: %d" % self.mid)
        return

    def OnTeardown(self):
        print("[Python] ...MyCombinedBusinessService:OnTeardown() is called")
        return

    def OnProcessInput(self, messageInput):
        print("[Python] ...MyCombinedBusinessService:OnProcessInput() is called")
        tRequest = demo.MyRequest.MyRequest()
        tRequest.requestString = "request from my business service"
        self.SendRequestAsync("MyCombinedBusinessProcess", tRequest)
        return