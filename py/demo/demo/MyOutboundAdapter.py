import iris.pex

class MyOutboundAdapter(iris.pex.OutboundAdapter):
    
    def OnInit(self):
        print("[Python] ...MyOutboundAdapter:OnInit() is called")
        return

    def OnTearDown(self):
        print("[Python] ...MyOutboundAdapter:OnTeardown() is called")
        return

    def printString(self, string):
        print("\n[Python] ...MyOutboundAdapter:printString(): " + string)
        return "printed successfully"

    def printThreeStrings(self, string1, string2, string3):
        print("\n[Python] ...MyOutboundAdapter:printThreeStrings(): "+string1+", "+string2+", "+string3)
        return "printed successfully"