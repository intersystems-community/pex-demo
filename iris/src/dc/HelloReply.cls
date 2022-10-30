Class dc.HelloReply Extends Ens.Request
{

Property message As %VarString;

Method %OnNew(message As %VarString = "") As %Status
{
	Set ..message = message
	Quit $$$OK
}

Storage Default
{
<Data name="HelloReplyDefaultData">
<Subscript>"HelloReply"</Subscript>
<Value name="1">
<Value>message</Value>
</Value>
</Data>
<DefaultData>HelloReplyDefaultData</DefaultData>
<Type>%Storage.Persistent</Type>
}

}
