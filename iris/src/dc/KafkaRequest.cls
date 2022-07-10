Class dc.KafkaRequest Extends Ens.Request
{

Property Topic As %String(MAXLEN = 255) [ Required ];

Property Key As %String(MAXLEN = 1000);

Property Text As %VarString;

Method %OnNew(Topic As %String = "", Key As %String = "", Text As %VarString = "") As %Status
{
	Set ..Topic = Topic
	Set ..Key = Key
	Set ..Text = Text
	Quit $$$OK
}

}
