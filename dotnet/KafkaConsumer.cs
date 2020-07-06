using System;
using InterSystems.Data.IRISClient.ADO;
using InterSystems.Data.IRISClient.Gateway;
using InterSystems.EnsLib.PEX;
using Confluent.Kafka;

namespace dc
{
    public class KafkaConsumer : BusinessService
    {
        /// <summary>
        /// Comma-separated list of Kafka partitions to connect to.
        /// </summary>
        public string SERVERS;

        /// <summary>
        /// Kafka topic, for this service to consume
        /// </summary>
        public string TOPIC;

        /// <summary>
        /// Connection to InterSystems IRIS
        /// </summary>
        private IRIS iris;

        /// <summary>
        /// Connection to Kafka
        /// </summary>
        private object consumer;

        /// <summary>
        /// Initialize connections 
        ///  - Kafka Consumer
        ///  - Reentrancy to InterSystems IRIS
        /// </summary>
        public override void OnInit()
        {
            LOGINFO("INIT");
            var conf = new ConsumerConfig
            {
                ///GroupId = "test-consumer-group",
                BootstrapServers = SERVERS,
                // Note: The AutoOffsetReset property determines the start offset in the event
                // there are not yet any committed offsets for the consumer group for the
                // topic/partitions of interest. By default, offsets are committed
                // automatically, so in this example, consumption will only start from the
                // earliest message in the topic 'my-topic' the first time you run the program.
                AutoOffsetReset = AutoOffsetReset.Earliest
            };

            consumer = new ConsumerBuilder<Ignore, string>(conf).Build();

            LOGINFO("Consumer type: " + consumer.GetType().Name);

            //consumer.Subscribe("my-topic");


            iris = GatewayContext.GetIRIS();
        }

        public override object OnProcessInput(object messageInput)
        {
            LOGINFO("OnProcessInput");
            // IRISObject request = (IRISObject)messageInput;

            //LOGINFO(string.Format("received: %s", request.GetString("StringValue")));

            //IRISObject response = (IRISObject)iris.ClassMethodObject("Ens.StringContainer", "%New", "Hello from .Net");
            //return response;
            return null;
        }

        public override void OnTearDown()
        {
            iris.Close();
        }
    }
}
