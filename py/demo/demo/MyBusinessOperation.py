import iris.pex
import demo.MyResponse

class MyBusinessOperation(iris.pex.BusinessOperation):
    
    def OnInit(self):
        print("[Python] ...MyBusinessOperation:OnInit() is called")
        return

    def OnTeardown(self):
        print("[Python] ...MyBusinessOperation:OnTeardown() is called")
        return

    def OnMessage(self, messageInput):
        # called from ticker service, message is of type MyRequest with property requestString
        #print("[Python] ...MyBusinessOperation:OnMessage() is called with message: " + messageInput.requestString)
        print("[Python] ...MyBusinessOperation:OnMessage() is called with message: " + messageInput.get("StringValue"))
        response = demo.MyResponse.MyResponse("...MyBusinessOperation:OnMessage() echos")
        return response