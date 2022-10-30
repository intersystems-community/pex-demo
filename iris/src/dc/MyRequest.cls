Class dc.MyRequest Extends Ens.Request
{

Property requestString As %VarString;

Method %OnNew(requestString As %VarString = "") As %Status
{
	Set ..requestString = requestString
	Quit $$$OK
}

Storage Default
{
<Data name="MyRequestDefaultData">
<Subscript>"MyRequest"</Subscript>
<Value name="1">
<Value>requestString</Value>
</Value>
</Data>
<DefaultData>MyRequestDefaultData</DefaultData>
<Type>%Storage.Persistent</Type>
}

}
