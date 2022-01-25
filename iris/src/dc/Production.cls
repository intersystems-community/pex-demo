Class dc.Production Extends Ens.Production
{

XData ProductionDefinition
{
<Production Name="dc.Production" TestingEnabled="true" LogGeneralTraceEvents="true">
  <Description></Description>
  <ActorPoolSize>2</ActorPoolSize>
  <Item Name="KafkaProducer" Category="" ClassName="EnsLib.PEX.BusinessOperation" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
    <Setting Target="Host" Name="%gatewayPort">55555</Setting>
    <Setting Target="Host" Name="%remoteClassname">dc.rmq.KafkaOperation</Setting>
    <Setting Target="Host" Name="%gatewayExtraClasspaths"></Setting>
    <Setting Target="Host" Name="%remoteSettings">SERVERS=kafka:29092
CLIENTID=PEXProd</Setting>
    <Setting Target="Host" Name="%gatewayHost">jgw</Setting>
  </Item>
  <Item Name="KafkaConsumer" Category="" ClassName="EnsLib.PEX.BusinessService" PoolSize="1" Enabled="false" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
    <Setting Target="Adapter" Name="CallInterval">0.1</Setting>
    <Setting Target="Host" Name="%remoteClassname">dc.KafkaConsumer</Setting>
    <Setting Target="Host" Name="%gatewayExtraClasspaths">/app/KafkaConsumer.dll</Setting>
    <Setting Target="Host" Name="%gatewayPort">55556</Setting>
    <Setting Target="Host" Name="%gatewayHost">netgw</Setting>
    <Setting Target="Host" Name="%remoteSettings">SERVERS=kafka:29092
TOPIC=test
TargetConfigNames=KafkaProcess</Setting>
  </Item>
  <Item Name="BP" Category="" ClassName="Ens.BusinessProcessBPL" PoolSize="1" Enabled="false" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
  </Item>
  <Item Name="PyOp" Category="" ClassName="EnsLib.PEX.BusinessOperation" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
    <Setting Target="Host" Name="%gatewayHost">pygw</Setting>
    <Setting Target="Host" Name="%gatewayPort">55557</Setting>
    <Setting Target="Host" Name="%remoteClassname">demo.MyBusinessOperation.MyBusinessOperation</Setting>
    <Setting Target="Host" Name="%gatewayExtraClasspaths">/app/dist/intersystems_demo_pex-3.2.0-py3-none-any.whl</Setting>
  </Item>
  
  <Item Name="KafkaProcess" Category="" ClassName="EnsLib.PEX.BusinessProcess" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
    <Setting Target="Host" Name="%gatewayHost">pygw</Setting>
    <Setting Target="Host" Name="%gatewayPort">55557</Setting>
    <Setting Target="Host" Name="%remoteClassname">demo.KafkaProcess.KafkaProcess</Setting>
    <Setting Target="Host" Name="%gatewayExtraClasspaths">/app/dist/intersystems_demo_pex-3.2.0-py3-none-any.whl</Setting>
    <Setting Target="Host" Name="%remoteSettings">TOPIC=test
TargetConfigName=KafkaProducer</Setting>
</Item>
</Production>
}

}
