import sys
from scapy.all import *
from xnt import *

packet = Ether()/IP(src="1.2.3.4",dst=sys.argv[1])

vxlan_int_pkt = vxlan_gpe_int_src_packet(
                               eth_dst='00:77:66:55:44:33', #does this matter?
                               eth_src='00:22:22:22:22:22', # ?
                               ip_id=0,
                               ip_dst='10.0.1.10',
                               ip_src='1.2.3.4',
                               ip_ttl=64,
                               udp_sport=101,
                               with_udp_chksum=False,
                               vxlan_vni=0x1234,
                               int_inst_mask=0xFF00, # 8000 was just switch id 
						     # ff00 should set all first 8 bits
                               int_inst_cnt=8,
			       inner_frame=packet)


vxlan_int_pkt = vxlan_gpe_int_packet_add_hop_info(Packet=vxlan_int_pkt,val=0x66666666, bos=True)



sendp(vxlan_int_pkt,iface=sys.argv[2])




