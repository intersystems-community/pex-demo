Class dc.Production Extends Ens.Production
{

XData ProductionDefinition
{
<Production Name="dc.Production" TestingEnabled="true" LogGeneralTraceEvents="false">
  <Description></Description>
  <ActorPoolSize>2</ActorPoolSize>
  <Item Name="EnsLib.PEX.BusinessOperation" Category="" ClassName="EnsLib.PEX.BusinessOperation" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
    <Setting Target="Host" Name="%gatewayPort">55555</Setting>
    <Setting Target="Host" Name="%remoteClassname">dc.rmq.KafkaOperation</Setting>
    <Setting Target="Host" Name="%gatewayExtraClasspaths"></Setting>
    <Setting Target="Host" Name="%remoteSettings">SERVERS=kafka:29092
CLIENTID=PEXProd</Setting>
    <Setting Target="Host" Name="%gatewayHost">jgw</Setting>
  </Item>
  <Item Name="EnsLib.PEX.BusinessService" Category="" ClassName="EnsLib.PEX.BusinessService" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
    <Setting Target="Host" Name="%remoteClassname">dc.KafkaConsumer</Setting>
    <Setting Target="Host" Name="%gatewayExtraClasspaths">/app/KafkaConsumer.dll</Setting>
    <Setting Target="Host" Name="%gatewayPort">55556</Setting>
    <Setting Target="Host" Name="%gatewayHost">netgw</Setting>
    <Setting Target="Host" Name="%remoteSettings">SERVERS=kafka:29092
TOPIC=test</Setting>
  </Item>
</Production>
}

}