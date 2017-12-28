## This readme will explain how to perform the following tests:

Disclaimer: This readme has been written for when you use the provided p4 VM in labroom 21e402.

### Compile the p4 code: 
```
p4c-bmv --json switch.json p4src/switch.p4   | while standing in the root folder of the git project.
```
### Starting the switch: 
```
/path/TO_BMV2/bmv2/targets/simple_switch/simple_switch -i 0@veth1 -i 1@veth3 -i 2@veth5 --nanolog ipc:///tmp/bm-log.ipc --log-console' /PATHTO/switch.json
```
### Populate the switch tables:
```
sudo ./sswitch_CLI /PATH/TO/GITFOLDER/p4_INT_BWcalc/switch.json < /PATH/TO/GITFOLDER/p4_INT_BWcalc/command_files/*COMMANDFILE*
```
### Run the Switch CLI to check registers etc: 
```
sudo ./sswitch_CLI /PATH/TO/GITFOLDER/p4_INT_BWcalc
```
### Start receiver script:
```
sudo receiver veth3
```
### Start sender script: 
```
sudo sender 10.0.1.10 veth0
```

### Intro test:
In this test we will see how we can populated our switches tables so that it can forward a packet to our desired destination.

* In switch.p4 in both ingress and egress control the only code that should uncommented is apply(ipv4_fib_lpm) and apply(forward). After doing this recompile and the start the switch.

* In another terminal window populate the table with the file command_base.txt

* In two other terminal windows start the receiver and then the sender to generate a packet and send it to its destination.

* When the packet has been sent it can bee seen in the switch log, receiver terminal window and in wireshark.

### First test:
* In switch.p4 the following code should be uncommented in control ingress & egress: apply(ipv4_fib_lpm);, apply(forward); and egress_header();
* Recompile and start the switch. Pupolate the table with commands_add_header.txt 
* Start the receiver and the sender scripts.
* result can be viwed in wireshark, receiver terminal and in the switch log. 
### Second test:
* In switch.p4 the following code should be uncommented in control ingress & egress: apply(ipv4_fib_lpm);, apply(forward);. egress_header(); and egress_cloning();
* Recompile and start the switch. Pupolate the table with commands_clone.txt 
* Start the receiver and the sender scripts.
* result can be viwed in wireshark, receiver terminal and in the switch log. 
### Third test:
* In switch.p4 the following code should be uncommented in control ingress & egress: apply(ipv4_fib_lpm);, apply(forward);. egress_header();[in the ingress control] and int_bw_ingress();. Aswell as in int_transit.p4 file the apply(int_bw_original);[control int_bw_ingress] should be uncommented.
* Recompile and start the switch. Pupolate the table with commands_ingress_original.txt 
* Start the receiver and the sender scripts.
* result can be viwed in wireshark, receiver terminal and in the switch log. 
### Fourth test:
* In switch.p4 the following code should be uncommented in control ingress & egress: apply(ipv4_fib_lpm);, apply(forward);. egress_header();[in the ingress control] and int_bw_ingress();. Aswell as in int_transit.p4 file the apply(int_bw_clone);[control int_bw_ingress] should be uncommented.
* Recompile and start the switch. Pupolate the table with commands_ingress_original.txt
* Start the receiver and the sender scripts.
* result can be viwed in wireshark, receiver terminal and in the switch log. 
### Futher work and tests:
* Add another switch and run a mininet instance where each switch has its own commands file. So we can test that our calculation and clone detection can be evaluated correctly and not
just emulated as in test 4.

