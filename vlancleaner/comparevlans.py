#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

def desgranaje_sw(vlans_sw):
   
        lista_vlans = []
        unicas = []
        
        for x in range(0, len(vlans_sw)):
            
            trunk = vlans_sw[x].split(",")
        
            for rango in range(0, len(trunk)):
                
                if trunk[rango].find("-") != -1:
                    
                    r = trunk[rango].split("-")
                    
                    for y in range(int(r[0]), int(r[1])+1):
                        
                        lista_vlans.append(y)                 
                    
                else:
            
                        lista_vlans.append(int(trunk[rango]))
                        
        for i in lista_vlans:
        
            if i not in unicas:
            
                unicas.append(i)        
                    
        return unicas
        
    
def desgranaje_esx(lista_vlans_esx):
        
    for x in range(0, len(lista_vlans_esx)):
        
        lista_vlans_esx[x] = int(lista_vlans_esx[x])
        
    return lista_vlans_esx   
            
        
def comparacion_vlans_swesx(vlans_sw, lista_vlans_esx):
    
    comparadas = []
    
    for i in vlans_sw:
        
        if i not in lista_vlans_esx:
            
            comparadas.append(i)   
            
    return comparadas
    
    
def comparacion_trunks_gral(comparadas, trunks_gral):
    
    compar = []
    
    for i in comparadas:
        
        if i not in trunks_gral:
            
            compar.append(i)   
            
    return compar

def comparacion_puertos_gral(compar, vlans_puertos_gral):
    
    compar2 = []
    
    for i in compar:
        
        if i not in vlans_puertos_gral:
            
            compar2.append(i)   
            
    return compar2

def comparicion_portchannel_core(compar2, vlans_portchannel):
    
    compar3 = []
    
    for i in range(0, len(compar2)-1):
        
        if compar2[i] in vlans_portchannel:
            
            compar3.append(compar2[i])
                   
                  
    return compar3

def corre_vlan_nombre(compar3, vlans_id, fich7, fich8):
    
    fichero8 = open(fich8, "w")
   
    for x in range(0, len(vlans_id)):
        
        vlans_id[x] = int(vlans_id[x])
        

    for i in compar3:
            
        if i in vlans_id:
            
            vlan_nombre = subprocess.check_output("awk '$1=="+str(i)+"{print $0}' "+fich7, shell=True)
            
            fichero8.write(vlan_nombre)    
            
        else:
            
            fichero8.write(str(i) + " VLAN NO EXISTE \n")

    fichero8.close()       
    
