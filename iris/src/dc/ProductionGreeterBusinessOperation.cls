Class dc.ProductionGreeterBusinessOperation Extends Ens.Production
{

XData ProductionDefinition
{
<Production Name="dc.ProductionGreeterBusinessOperation" TestingEnabled="true" LogGeneralTraceEvents="false">
  <Description></Description>
  <ActorPoolSize>2</ActorPoolSize>
  <Item Name="GreeterBusinessOperation" Category="" ClassName="dc.GreeterBusinessOperation" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
    <Setting Target="Host" Name="%remoteClassname">grpc_hello_world.greeter_business_operation.GreeterBusinessOperation</Setting>
    <Setting Target="Adapter" Name="%gatewayHost"></Setting>
    <Setting Target="Adapter" Name="%gatewayPort"></Setting>
    <Setting Target="Adapter" Name="%remoteClassname">grpc_hello_world.greeter_outbound_adapter.GreeterOutboundAdapter</Setting>
    <Setting Target="Adapter" Name="%useHostConnection">1</Setting>
    <Setting Target="Host" Name="%gatewayExtraClasspaths">/irisrun/repo/grpc_hello_world</Setting>
    <Setting Target="Host" Name="%gatewayHost">pygw</Setting>
    <Setting Target="Host" Name="%gatewayPort">55557</Setting>
    <Setting Target="Adapter" Name="%remoteSettings">gRPCHost=localhost
gRPCPort=50051</Setting>
  </Item>
</Production>
}

}
