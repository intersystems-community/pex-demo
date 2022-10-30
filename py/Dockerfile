ARG IRIS_IMAGE
FROM ${IRIS_IMAGE} AS iris

FROM python:3.8-slim

ENV GWLIBDIR /app

# copy and run gateway code
COPY --from=iris \
     /usr/irissys/dev/python/*.whl \
     ${GWLIBDIR}/


RUN python -m pip install --upgrade ${GWLIBDIR}/*.whl

COPY demo ${GWLIBDIR}

RUN cd ${GWLIBDIR} && python setup.py bdist_wheel

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

CMD python -m iris PythonGateway ${PYTHON_GATEWAY} "" "" 0.0.0.0 "" 2>&1
