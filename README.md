# XII Workshop de Pesquisa Experimental da Internet do Futuro (WPEIF 2021)
* Extrator de metricas
* Experimentos

-- Installing MQTT Brocker
sudo apt-get install mosquitto

-- Configuring IP and Port for MQTT Broker
sudo vim /etc/mosquitto/mosquitto.conf

Insert those lines in mosquitto.conf
** bind_address 10.0.0.4
** allow_anonymous true
Resetar Mosquitto Service
sudo service mosquitto restart


-- Installing required Packages
* sudo apt-get install python3-pip
* sudo apt-get install golang

-- Intalling MQTT Bench
go get github.com/krylovsk/mqtt-benchmark

-- Installing PSUTIL
* pip3 install psutil numpu

