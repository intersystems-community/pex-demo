ARG IRIS_IMAGE
FROM ${IRIS_IMAGE}

USER ${ISC_PACKAGE_MGRUSER}

COPY --chown=$ISC_PACKAGE_MGRUSER:$ISC_PACKAGE_IRISGROUP irissession.sh /
COPY --chown=$ISC_PACKAGE_MGRUSER:$ISC_PACKAGE_IRISGROUP src /tmp

RUN chmod +x /irissession.sh

SHELL ["/irissession.sh"]

RUN \
  zn "USER" \
  do $SYSTEM.OBJ.LoadDir("/tmp", "ck", , 1) \
  do ##class(%File).RemoveDirectoryTree("/tmp") \
  set production = "dc.Production" \
  set ^Ens.Configuration("csp","LastProduction") = production \
  for user = "UnknownUser", "Admin", "SuperUser", "_SYSTEM" {set ^EnsPortal.Settings(user, "PreferredCategory", production)="Kafka"} \
  do ##class(Ens.Director).SetAutoStart(production)

# bringing the standard shell back
SHELL ["/bin/bash", "-c"]