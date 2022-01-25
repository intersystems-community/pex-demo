import iris.pex
import demo.MyResponse

class MyBusinessOperation(iris.pex.BusinessOperation):
    
    def OnInit(self):
        self.LOGINFO("[Python] ...MyBusinessOperation:OnInit() is called")
        return

    def OnTeardown(self):
        self.LOGINFO("[Python] ...MyBusinessOperation:OnTeardown() is called")
        return

    def OnMessage(self, messageInput):
        # called from ticker service, message is of type MyRequest with property requestString
        #print("[Python] ...MyBusinessOperation:OnMessage() is called with message: " + messageInput.requestString)
        self.LOGINFO("[Python] ...MyBusinessOperation:OnMessage() is called with message: " + messageInput.get("StringValue"))
        self.LOGINFO(str(dir(messageInput)))
        response = demo.MyResponse.MyResponse(str(dir(iris.pex)))
        return response