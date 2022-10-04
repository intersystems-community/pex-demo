import iris.pex

class KafkaProcess(iris.pex.BusinessProcess):

    TOPIC = str("")
    # commented because seemed like this config let just oly one varible being found by PEX...
    # TOPIC_info_var = {
    #     'Description': "Kafka topic",
    #     'IsRequired': True
    # }
    # @classmethod
    # def TOPIC_info(self)->TOPIC_info_var:
    #     pass

    TargetConfigName = str("")
    # commented because seemed like this config let just oly one varible being found by PEX...
    # TargetConfigName_info_var = {
    #     'Description': "Production target",
    #     'IsRequired': True
    # }
    # @classmethod
    # def TargetConfigName_info(self)->TargetConfigName_info_var:
    #     pass

    def OnInit(self):
        self.LOGINFO("[Python] ...KafkaProcess:OnInit() is called")
        return

    def OnTearDown(self):
        self.LOGINFO("[Python] ...KafkaProcess:OnTearDown() is called")
        return

    def OnRequest(self, request):
        # called from business service, message is of type dc.KafkaRequest with property Text
        try:
          value = int(request.get("Text"))
          self.LOGINFO("[Python] ...MyBusinessProcess:OnRequest() is called wth request: " + str(value))
        except:
          self.LOGERROR("Unable to convert request to int.")
          return
        if value > 0:
          callrequest = iris.GatewayContext.getIRIS().classMethodObject("dc.KafkaRequest", "%New")
          callrequest.set("Topic", self.TOPIC)
          callrequest.set("Text", str(value - 1))
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