Class dc.Production2 Extends Ens.Production
{

XData ProductionDefinition
{
<Production Name="dc.Production" TestingEnabled="true" LogGeneralTraceEvents="true">
  <Description></Description>
  <ActorPoolSize>2</ActorPoolSize>
  <Item Name="KafkaProducer" Category="Kafka" ClassName="EnsLib.PEX.BusinessOperation" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
    <Setting Target="Host" Name="%gatewayPort">55555</Setting>
    <Setting Target="Host" Name="%remoteClassname">dc.rmq.KafkaOperation</Setting>
    <Setting Target="Host" Name="%gatewayExtraClasspaths"></Setting>
    <Setting Target="Host" Name="%remoteSettings">CONFIG=/jgw/producer.properties</Setting>
    <Setting Target="Host" Name="%gatewayHost">jgw</Setting>
  </Item>
  <Item Name="KafkaConsumer" Category="Kafka" ClassName="EnsLib.PEX.BusinessService" PoolSize="1" Enabled="false" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
    <Setting Target="Adapter" Name="CallInterval">0.1</Setting>
    <Setting Target="Host" Name="%remoteClassname">dc.KafkaConsumer</Setting>
    <Setting Target="Host" Name="%gatewayExtraClasspaths">/app/KafkaConsumer.dll</Setting>
    <Setting Target="Host" Name="%gatewayPort">55556</Setting>
    <Setting Target="Host" Name="%gatewayHost">netgw</Setting>
    <Setting Target="Host" Name="%remoteSettings">SERVERS=kafka:29092
TOPIC=test
TargetConfigNames=KafkaProcess</Setting>
  </Item>
  <Item Name="MyBusinessOperation" Category="Python" ClassName="EnsLib.PEX.BusinessOperation" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
    <Setting Target="Host" Name="%gatewayHost">pygw</Setting>
    <Setting Target="Host" Name="%gatewayPort">55557</Setting>
    <Setting Target="Host" Name="%remoteClassname">demo.MyBusinessOperation.MyBusinessOperation</Setting>
    <Setting Target="Host" Name="%gatewayExtraClasspaths">/irisrun/repo/demo/demo</Setting>
  </Item>
  <Item Name="KafkaProcess" Category="Kafka" ClassName="EnsLib.PEX.BusinessProcess" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
    <Setting Target="Host" Name="%gatewayHost">pygw</Setting>
    <Setting Target="Host" Name="%gatewayPort">55557</Setting>
    <Setting Target="Host" Name="%remoteClassname">demo.KafkaProcess.KafkaProcess</Setting>
    <Setting Target="Host" Name="%gatewayExtraClasspaths">/irisrun/repo/demo/demo</Setting>
    <Setting Target="Host" Name="%remoteSettings">TOPIC=test
TargetConfigName=KafkaProducer</Setting>
  </Item>
  <Item Name="KafkaConsumerJava" Category="Kafka" ClassName="EnsLib.PEX.BusinessService" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
    <Setting Target="Host" Name="%gatewayHost">jgw</Setting>
    <Setting Target="Host" Name="%gatewayPort">55555</Setting>
    <Setting Target="Host" Name="%remoteClassname">dc.rmq.KafkaService</Setting>
    <Setting Target="Host" Name="%remoteSettings">TOPIC=test
TargetConfigNames=KafkaProcess
CONFIG=/jgw/consumer.properties</Setting>
    <Setting Target="Adapter" Name="CallInterval">1</Setting>
  </Item>
</Production>
}

}
