package dc.rmq;

import com.intersystems.enslib.pex.*;
import com.intersystems.jdbc.IRISObject;
import com.intersystems.jdbc.IRIS;
import com.intersystems.gateway.GatewayContext;

import org.apache.kafka.clients.producer.*;
import org.apache.kafka.common.serialization.LongSerializer;
import org.apache.kafka.common.serialization.StringSerializer;

import java.util.Properties;


public class KafkaOperation extends BusinessOperation {
    // Connection to InterSystems IRIS
    private IRIS iris;

    // Connection to Kafka
    private Producer<Long, String> producer;

    // Kafka server address (comma separated if several)
    public String SERVERS;

    // Name of our Producer
    public String CLIENTID;

    public void OnInit() throws Exception {

        iris = GatewayContext.getIRIS();
        LOGINFO("Initialized IRIS");

        LOGINFO(String.format("SERVERS: %s CLIENTID: %s", SERVERS, CLIENTID));
        producer = createProducer();
        LOGINFO("Initialized Kafka Producer");

        return;
    }

    public void OnTearDown() throws Exception {
        producer.flush();
        producer.close();
        return;
    }

    public Object OnMessage(Object request) throws Exception {
        IRISObject req = (IRISObject) request;
        LOGINFO("Received object: " + req.invokeString("%ClassName", 1));

        // Create record
        String value = req.getString("Text");
        String topic = req.getString("Topic");
        final ProducerRecord<Long, String> record = new ProducerRecord<>(topic, value);

        // Send new record
        RecordMetadata metadata = producer.send(record).get();

        // Return record info
        IRISObject response = (IRISObject)(iris.classMethodObject("Ens.StringContainer","%New",metadata.offset()));
        return response;
    }

    private Producer<Long, String> createProducer() {
        Properties props = new Properties();
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, SERVERS);
        props.put(ProducerConfig.CLIENT_ID_CONFIG, CLIENTID);
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, LongSerializer.class.getName());
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        return new KafkaProducer<>(props);
    }
}
