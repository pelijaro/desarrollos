#!/usr/bin/env python
# -*- coding: utf-8 -*-

import filecleaner
import comparevlans
import sys
import subprocess

subpth = sys.argv[1]

pth = "files/"

#subpth02 = "02"
#subpth03 = "03"
#subpth04 = "04"

filecleaner.filecleaner(subpth)


fich1 = pth + subpth +"/"+subpth+"_trunks.txt"
fich2 = pth + subpth +"/ESX_Cliente_vlan.csv"
fich3 = pth + subpth +"/no_coincidentes.txt"
fich4 = pth + subpth +"/"+subpth+"_trunks_gral.txt"
fich5 = pth + subpth +"/"+subpth+"_puertos_gral.txt"
fich6 = pth + subpth +"/core_trunks.txt"
fich7 = pth + subpth +"/vlans_core.txt"
fich8 = pth + subpth + "/cruce_vlan_nombre.txt"


#puertos = subprocess.check_output("awk '{print $1}' "+fich1, shell=True).strip().split()
vlans_sw = subprocess.check_output("awk '{print $2}' "+fich1, shell=True).strip().split("\n")
vlans_esx = subprocess.check_output("awk -F ';' '{print $2}' "+fich2, shell=True).strip().split()
trunks_gral = subprocess.check_output("awk '{print $2}' "+fich4, shell=True).strip().split()
vlans_puertos_gral = subprocess.check_output("awk '{print $2}' "+fich5, shell=True).strip().split()
vlans_portchannel = subprocess.check_output("awk '{print $2}' "+fich6, shell=True).strip().split()
vlans_id = subprocess.check_output("awk '{print $1}' "+fich7, shell=True).strip().split()
#vlans_nombre = subprocess.check_output("awk '{print $0}' "+fich7, shell=True).strip().split()



comparevlans.corre_vlan_nombre(comparevlans.comparicion_portchannel_core(comparevlans.comparacion_puertos_gral(comparevlans.comparacion_trunks_gral(comparevlans.comparacion_vlans_swesx(comparevlans.desgranaje_sw(vlans_sw), comparevlans.desgranaje_esx(vlans_esx)), comparevlans.desgranaje_sw(trunks_gral)), comparevlans.desgranaje_esx(vlans_puertos_gral)), comparevlans.desgranaje_sw(vlans_portchannel)), vlans_id, fich7, fich8)

#print comparevlans.comparicion_portchannel_core(comparevlans.comparacion_puertos_gral(comparevlans.comparacion_trunks_gral(comparevlans.comparacion_vlans_swesx(comparevlans.desgranaje_sw(vlans_sw), comparevlans.desgranaje_esx(vlans_esx)), comparevlans.desgranaje_sw(trunks_gral)), comparevlans.desgranaje_esx(vlans_puertos_gral)), comparevlans.desgranaje_sw(vlans_portchannel))