# PEX demo
Demo showcasing InterSystems IRIS integration with Kafka via [PEX](https://docs.intersystems.com/irislatest/csp/docbook/Doc.View.cls?KEY=EPEX).

# PEX

The Production EXtension (PEX) framework provides you with a choice of implementation languages when you are developing interoperability productions. Interoperability productions enable you to integrate systems with different message formats and communication protocols. If you are not familiar with interoperability productions, see [Introduction to Productions](https://docs.intersystems.com/irislatest/csp/docbook/Doc.View.cls?KEY=EGIN_intro#EGIN_productions).
As of July 2020, PEX supports Java and the .NET languages. PEX provides flexible connections between business services, processes, and operations that are implemented in PEX-supported languages or in InterSystems ObjectScript. In addition, you can use PEX to develop, inbound and outbound adapters. The PEX framework allows you to create an entire production in Java or .NET or to create a production that has a mix of Java, .NET, or ObjectScript components. Once integrated, the production components written in Java and .NET are called at runtime and use the PEX framework to send messages to other components in the production. 


# Running the demo

1. Install:
    - [docker](https://docs.docker.com/get-docker/)
    - [docker-compose](https://docs.docker.com/compose/install/)
    - [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
2. Execute:
```
git clone https://github.com/intersystems-community/pex-demo.git
cd pex-demo
docker-compose pull
docker-compose up -d
```

For Docker Desktop on Windows you'll need to share the repository folder with Docker before running `docker-compose up -d`.

# Demo Production

1. Open Production and test `KafkaProducer` operation by sending a `dc.KafkaRequest` message (topic: `test`, with any text). It would send a message to Kafka via Java Gateway.
2. Open Kafka Manager and Navigate to `Resources` > `Topics` > `test` > `Browse Data` > `Fetch` to see that your message is enqueued.
3. Open [Message Viewer](http://localhost:52773/csp/user/EnsPortal.MessageViewer.zen?SOURCEORTARGET=KafkaConsumer) on `KafkaConsumer` service
4. Start `KafkaConsumer` service. It would start receiving messages from `test` topic via .Net Gateway. If you want to receive messages from another topic, modify `Remote Settings` value for the Service.
5. Refresh Message Viewer to see new messages.

# What's inside

## UI

- InterSystems IRIS: `http://localhost:52773/csp/user/EnsPortal.ProductionConfig.zen`
- Eco Kafka Manager: `http://localhost:8082`

## Other ports

- SuperServer: `51773`
- Java Gateway: `55555`
- .Net gateway: `55556`
- Zookeeper: `2181`
- Kafka: `9092`

