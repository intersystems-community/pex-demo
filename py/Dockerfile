FROM python:3.8-slim

ENV GWLIBDIR /app

# copy and run gateway code
COPY --from=containers.intersystems.com/intersystems/iris-community:2021.2.0.649.0 \
     /usr/irissys/dev/python/*.whl \
     ${GWLIBDIR}/


RUN python -m pip install --upgrade ${GWLIBDIR}/*.whl

COPY demo ${GWLIBDIR}

RUN cd ${GWLIBDIR} && python setup.py bdist_wheel

CMD python -m iris PythonGateway 55557 "" "" 0.0.0.0 "" 2>&1
