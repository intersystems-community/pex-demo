Class dc.HelloRequest Extends Ens.Request
{

Property name As %VarString;

Method %OnNew(name As %VarString = "") As %Status
{
	Set ..name = name
	Quit $$$OK
}

Storage Default
{
<Data name="HelloRequestDefaultData">
<Subscript>"HelloRequest"</Subscript>
<Value name="1">
<Value>name</Value>
</Value>
</Data>
<DefaultData>HelloRequestDefaultData</DefaultData>
<Type>%Storage.Persistent</Type>
}

}
