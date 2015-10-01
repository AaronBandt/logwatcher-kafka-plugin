# logwatcher-kafka-plugin
Plugin for LogWatcher to send Log Lines to Kafka
# Requirements
Requires:
LogWatcher - https://github.com/CityGrid/logwatcher
kafka-python - https://github.com/mumrah/kafka-python

# Install
    pip install logwatcher-kafka-plugin

# Use
Add the following option to your logwatcher ini file to enable the plugin
    
    plugins: kafka_logger

and the following configuration clause
    
    [kafka_logger]
    broker: [kafka server 1]:port,[kafka server N]:port
    topic: [kafka topic name]
    send_when_debug: True
