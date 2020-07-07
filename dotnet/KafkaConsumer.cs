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
        /// Configuration item(s) to which to send file stream messages
        /// </summary>
        public string TargetConfigNames;

        /// <summary>
        /// Configuration item(s) to which to send file stream messages, parsed into string[]
        /// </summary>
        private string[] targets;

        /// <summary>
        /// Connection to InterSystems IRIS
        /// </summary>
        private IRIS iris;

        /// <summary>
        /// Connection to Kafka
        /// </summary>
        private IConsumer<Ignore, string> consumer;

        /// <summary>
        /// Initialize connections 
        ///  - Kafka Consumer
        ///  - Reentrancy to InterSystems IRIS
        /// </summary>
        public override void OnInit()
        {
            LOGINFO("Initialization started");
            var conf = new ConsumerConfig
            {
                GroupId = "test-consumer-group",
                BootstrapServers = SERVERS,
                // Note: The AutoOffsetReset property determines the start offset in the event
                // there are not yet any committed offsets for the consumer group for the
                // topic/partitions of interest. By default, offsets are committed
                // automatically, so in this example, consumption will only start from the
                // earliest message in the topic 'my-topic' the first time you run the program.
                AutoOffsetReset = AutoOffsetReset.Earliest
            };

            consumer = new ConsumerBuilder<Ignore, string>(conf).Build();

            consumer.Subscribe(TOPIC);

            if (TargetConfigNames != null)
            {
                targets = TargetConfigNames.Split(",");
            }
            iris = GatewayContext.GetIRIS();

            LOGINFO("Initialized!");
        }

        public override object OnProcessInput(object messageInput)
        {
            bool atEnd = false;
            while (atEnd is false)
            {
                ConsumeResult<Ignore, string> message = consumer.Consume(1000);
                if (message is null)
                {
                    atEnd = true;
                } else {
                    string text = message.Message.Value;
                    foreach (string target in targets)
                    {
                        IRISObject request = (IRISObject)iris.ClassMethodObject("Ens.StringContainer", "%New", text);
                        SendRequestAsync(target, request);
                    }
                }
            }
            return null;
        }

        public override void OnTearDown()
        {
            iris.Close();
        }
    }
}
