import iris.pex

class KafkaProcess(iris.pex.BusinessProcess):

    def OnInit(self):
        self.LOGINFO("[Python] ...KafkaProcess:OnInit() is called")
        return

    def OnTearDown(self):
        self.LOGINFO("[Python] ...KafkaProcess:OnTearDown() is called")
        return

    def OnRequest(self, request):
        value = int(request.get("StringValue"))
        # called from business service, message is of type Ens.StringContainer with property StringValue
        self.LOGINFO("[Python] ...MyBusinessProcess:OnRequest() is called wth request: " + str(value))
        if value > 0:
          callrequest = self._irisHandle._iris.classMethodValue("dc.KafkaRequest", "%New")
          callrequest.invokeVoid("TopicSet", self.TOPIC)
          callrequest.invokeVoid("TextSet", str(value - 1))
          self.SendRequestAsync(self.TargetConfigName, callrequest, False)
        else:
          self.LOGINFO("[Python] ...MyBusinessProcess:OnRequest() value is not a positive int. Exit.")
        return

    def OnResponse(self, request, response, callRequest, callResponse, pCompletionKey):
        self.LOGINFO("[Python] ...KafkaProcess:OnResponse() is called")
        return

    def OnComplete(self, request, response):
        self.LOGINFO("[Python] ...KafkaProcess:OnComplete() is called")
        return