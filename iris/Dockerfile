ARG IRIS_IMAGE
FROM ${IRIS_IMAGE}

USER root

RUN apt-get update && apt-get install -y python3-venv

USER ${ISC_PACKAGE_MGRUSER}

COPY --chown=$ISC_PACKAGE_MGRUSER:$ISC_PACKAGE_IRISGROUP iris/irissession.sh /
COPY --chown=$ISC_PACKAGE_MGRUSER:$ISC_PACKAGE_IRISGROUP iris/src /tmp
COPY --chown=$ISC_PACKAGE_MGRUSER:$ISC_PACKAGE_IRISGROUP py /tmp

RUN chmod +x /irissession.sh

SHELL ["/irissession.sh"]

RUN \
  zn "USER" \
  do $SYSTEM.OBJ.LoadDir("/tmp", "ck", , 1) \
  do ##class(%File).RemoveDirectoryTree("/tmp") \
  set production = "dc.Production" \
  set ^Ens.Configuration("csp","LastProduction") = production \
  for user = "UnknownUser", "Admin", "SuperUser", "_SYSTEM" {set ^EnsPortal.Settings(user, "PreferredCategory", production)="Kafka"} \
  do ##class(Ens.Director).SetAutoStart(production) \
  ZN "%SYS" \
  Set tProxy = ##class(%ZEN.proxyObject).%New() \
  Set tProxy.AllowedIPAddresses = "0.0.0.0" \
  Set tProxy.ConnectionTimeout = "5" \
  Set tProxy.HeartbeatFailureAction = "R" \
  Set tProxy.HeartbeatFailureRetry = "300" \
  Set tProxy.HeartbeatFailureTimeout = "30" \
  Set tProxy.HeartbeatInterval = "10" \
  Set tProxy.InitializationTimeout = "5" \
  Set tProxy.Name = "pex-demo-python" \
  Set tProxy.Port = "55557" \
  Set tProxy.Server = "0.0.0.0" \
  Set tProxy.Type = "Python" \
  Set tProxy.UsePassphrase = 0 \
  Set tProxy.UseSharedMemory = 0 \
  ZW ##class(%CSP.UI.Portal.ExternalLanguageServer).SaveData(tProxy, 1) \
  ZN "USER" \
  ZW ##class(%Net.Remote.Service).StartGateway("pex-demo-python") \
  ZW ##class(EnsLib.PEX.Utils).RegisterComponent("demo.KafkaProcess.KafkaProcess", "pex-demo-python", "/tmp/demo/demo", 1, "demo.KafkaProcess", 0) \
  ZW ##class(EnsLib.PEX.Utils).RegisterComponent("demo.MyBusinessOperation.MyBusinessOperation", "pex-demo-python", "/tmp/demo/demo", 1, "demo.MyBusinessOperation", 0)

# bringing the standard shell back
SHELL ["/bin/bash", "-c"]