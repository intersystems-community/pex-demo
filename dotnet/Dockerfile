FROM mcr.microsoft.com/dotnet/core/sdk:2.1 AS build

ENV DOTNET_CLI_TELEMETRY_OPTOUT 1
ENV ISC_PACKAGE_INSTALLDIR /usr/irissys
ENV GWLIBDIR /source/lib
ENV ISC_LIBDIR ${ISC_PACKAGE_INSTALLDIR}/dev/dotnet/bin/Core21

WORKDIR /source
COPY --from=containers.intersystems.com/intersystems/iris-community:2021.2.0.649.0 $ISC_LIBDIR/*.* $GWLIBDIR/

# copy csproj and restore as distinct layers
COPY *.csproj ./

# copy and publish app and libraries
COPY . .
RUN dotnet publish -c release -o /app

# final stage/image
FROM mcr.microsoft.com/dotnet/core/runtime:2.1

ENV DOTNET_CLI_TELEMETRY_OPTOUT 1

WORKDIR /app
COPY --from=build /app ./

# Configs to start the Gateway Server
RUN cp KafkaConsumer.runtimeconfig.json IRISGatewayCore21.runtimeconfig.json && \
    cp KafkaConsumer.deps.json IRISGatewayCore21.deps.json

ENV PORT 55556

CMD dotnet IRISGatewayCore21.dll $PORT "" "7a4a48227048:IRIS:%DotNet Server" 0.0.0.0 ""