package dc.rmq;

import com.intersystems.enslib.pex.BusinessService;
import com.intersystems.gateway.GatewayContext;
import com.intersystems.jdbc.IRIS;
import com.intersystems.jdbc.IRISObject;
import org.apache.kafka.clients.consumer.*;
import org.apache.kafka.common.serialization.*;

import java.io.FileInputStream;
import java.io.IOException;
import java.time.Duration;
import java.util.Collections;
import java.util.Properties;


public class KafkaService extends BusinessService {
    // Connection to InterSystems IRIS
    private IRIS iris;

    // Connection to Kafka
    private Consumer<Long, String> consumer;

    // Kafka server address (comma separated if several)
    public String SERVERS;

    /// Kafka topic, for this service to consume
    public String TOPIC;

    /// Kafka Group Id
    public String GROUP;

    /// Path to Config File
    public String CONFIG;

    /// Configuration item(s) to which to send file stream messages
    public String TargetConfigNames;

    /// Configuration item(s) to which to send file stream messages, parsed into string[]
    private String[] targets;

    public void OnInit() throws Exception {

        iris = GatewayContext.getIRIS();
        LOGINFO("Initialized IRIS");

        LOGINFO(String.format("SERVERS: %s TOPIC: %s", SERVERS, TOPIC));
        consumer = createConsumer();
        LOGINFO("Initialized Kafka Consumer");

        consumer.subscribe(Collections.singletonList(TOPIC));

        if (TargetConfigNames != null) {
            targets = TargetConfigNames.split(",");
        }

        return;
    }

    public void OnTearDown() throws Exception {
        consumer.close();
        iris.close();
        return;
    }

    public Object OnProcessInput(Object messageInput) throws Exception {
        final ConsumerRecords<Long, String> consumerRecords = consumer.poll(Duration.ofMillis(1000));

        consumerRecords.forEach(record -> {
            for (String target : targets) {
                IRISObject request = (IRISObject) iris.classMethodObject("dc.KafkaRequest", "%New", record.topic(), record.key(), record.value());
                try {
                    SendRequestAsync(target, request);
                } catch (Exception e) {
                    LOGINFO("Can't send a message");
                    throw new RuntimeException(e);
                }
            }
        });

        consumer.commitAsync();
        return messageInput;
    }


    private Consumer<Long, String> createConsumer() throws IOException {
        Properties props = new Properties();
        if (CONFIG == null || CONFIG.isEmpty() || CONFIG.trim().isEmpty()) {
            LOGINFO("Trying settings config");
            props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, SERVERS);
            props.put(ConsumerConfig.GROUP_ID_CONFIG, GROUP);
            props.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");
            props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, LongDeserializer.class.getName());
            props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        } else {
            LOGINFO("Trying file config");
            FileInputStream in = new FileInputStream(CONFIG);
            props.load(in);
        }
        return new KafkaConsumer<>(props);
    }
}
