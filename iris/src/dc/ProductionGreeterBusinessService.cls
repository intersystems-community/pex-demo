Class dc.ProductionGreeterBusinessService Extends Ens.Production
{

XData ProductionDefinition
{
<Production Name="dc.ProductionGreeterBusinessService" TestingEnabled="true" LogGeneralTraceEvents="false">
  <Description></Description>
  <ActorPoolSize>2</ActorPoolSize>
  <Item Name="GreeterBusinessService" Category="" ClassName="dc.GreeterBusinessService" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
    <Setting Target="Host" Name="%remoteClassname">grpc_hello_world.greeter_business_service.GreeterBusinessService</Setting>
    <Setting Target="Adapter" Name="%remoteClassname">grpc_hello_world.greeter_inbound_adapter.GreeterInboundAdapter</Setting>
    <Setting Target="Adapter" Name="%useHostConnection">1</Setting>
    <Setting Target="Host" Name="%gatewayExtraClasspaths">/irisrun/repo/grpc_hello_world</Setting>
    <Setting Target="Adapter" Name="%gatewayHost"></Setting>
    <Setting Target="Adapter" Name="%gatewayPort"></Setting>
    <Setting Target="Host" Name="%gatewayHost">pygw</Setting>
    <Setting Target="Host" Name="%gatewayPort">55557</Setting>
    <Setting Target="Adapter" Name="CallInterval">1</Setting>
    <Setting Target="Adapter" Name="%remoteSettings">gRPCPort=50051</Setting>
  </Item>
</Production>
}

}
