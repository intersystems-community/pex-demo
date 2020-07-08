FROM mcr.microsoft.com/dotnet/core/sdk:2.1 AS build

ENV ISC_PACKAGE_INSTALLDIR /usr/irissys
ENV GWLIBDIR lib
ENV ISC_LIBDIR ${ISC_PACKAGE_INSTALLDIR}/dev/dotnet/bin/Core21

WORKDIR /source
COPY --from=store/intersystems/iris-community:2020.2.0.211.0 $ISC_LIBDIR/*.nupkg $GWLIBDIR/

# copy csproj and restore as distinct layers
COPY *.csproj ./
RUN dotnet restore

# copy and publish app and libraries
COPY . .
RUN dotnet publish -c release -o /app

# final stage/image
FROM mcr.microsoft.com/dotnet/core/runtime:2.1
WORKDIR /app
COPY --from=build /app ./

# Configs to start the Gateway Server
RUN cp KafkaConsumer.runtimeconfig.json IRISGatewayCore21.runtimeconfig.json && \
    cp KafkaConsumer.deps.json IRISGatewayCore21.deps.json

ENV PORT 55556

CMD dotnet IRISGatewayCore21.dll $PORT 0.0.0.0