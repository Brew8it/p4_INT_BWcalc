## P4_INT_BWcalc
This is our final project for the course Computer Communication II at Karlstad University 

*Disclaimer: To be able to run our code you need to have installed the P4 behavior model prior to following this readme. 
We used the supplied VM at the university lab room.*

### Installing the project's dependencies
* Install linux kernel 3.19.
```
    sudo apt-get install linux-generic-lts-vivid
```
* Build and install the VXLAN-GPE driver taken from p4-factory redo in:
```
cd p4factory/apps/int/vxlan-gpe
make
sudo ./install_driver.sh
```
* Install the P4 PTF library:
```
cd ptf-master/
sudo python setup.py install
```
* Install P4's modified scapy library so that VxLAN mask bits can be set:
```
cd scapy-vxlan-master/
sudo python setup.py install
```

### Run the projects provided tests:
See [README.md](https://github.com/Brew8it/p4_INT_BWcalc/tree/master/command_files) in command_files folder.

