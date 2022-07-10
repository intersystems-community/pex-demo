FROM openjdk:8 AS builder

ARG APP_HOME=/tmp/app

COPY src $APP_HOME/src

COPY --from=intersystemsdc/jgw:2021.2 /jgw/*.jar $APP_HOME/jgw/

WORKDIR $APP_HOME/jar/
ADD https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/2.5.0/kafka-clients-2.5.0.jar .
ADD https://repo1.maven.org/maven2/ch/qos/logback/logback-classic/1.2.3/logback-classic-1.2.3.jar .
ADD https://repo1.maven.org/maven2/ch/qos/logback/logback-core/1.2.3/logback-core-1.2.3.jar .
ADD https://repo1.maven.org/maven2/org/slf4j/slf4j-api/1.7.30/slf4j-api-1.7.30.jar .

WORKDIR $APP_HOME/src

RUN javac -classpath $APP_HOME/jar/*:$APP_HOME/jgw/* dc/rmq/KafkaOperation.java dc/rmq/KafkaService.java && \
    jar -cvf $APP_HOME/jar/KafkaOperation.jar dc/rmq/KafkaOperation.class dc/rmq/KafkaService.class && \
    ls -al dc/rmq

FROM intersystemsdc/jgw:2021.2

COPY --from=builder /tmp/app/jar/*.jar $GWDIR/

COPY *.properties $GWDIR/

