FROM docker.io/bitnami/spark:3.3
USER root
LABEL maintainer="Maestros"

# Install Python
RUN \
    apt-get update && \
    apt-get install -y python3 python3-dev python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Install PySpark and Numpy
RUN \
    pip install --upgrade pip && \
    pip install numpy && \
    pip install pyspark && \
    pip install py4j

# Define default command
CMD ["bash"]