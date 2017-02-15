#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil

pth = "files/"


def filecleaner(subpth):
    
    ruta_puertos_gral = pth + subpth + "/" + subpth + "_puertos_gral.txt"
    ruta_trunks = pth + subpth + "/" + subpth + "_trunks.txt"
    ruta_trunks_gral = pth + subpth + "/" + subpth + "_trunks_gral.txt"
    ruta_vlans_core = pth + subpth + "/vlans_core.txt"
    ruta_core_trunks = pth + subpth + "/core_trunks.txt"
    #ruta_esx_vlans = pth + subpth + "/ESX_Cliente_vlan.csv"
    
    lista_fich = [ruta_puertos_gral, ruta_trunks, ruta_trunks_gral, ruta_vlans_core, ruta_core_trunks]
    
    try:
        
        shutil.move(pth + subpth + "/puertos_gral.txt", ruta_puertos_gral)
        shutil.move(pth + subpth + "/trunks.txt", ruta_trunks)
        shutil.move(pth + subpth + "/trunks_gral.txt", ruta_trunks_gral)
        
    except:
        
        print "Ya están renombrados!"
        
        
    for f in lista_fich:
              
        fichero = open(f, "r")
    
        clean = ""
     
        for linea in fichero:
            
            linea = linea.strip()
            clean = clean + linea + "\n"
            
        fichero.close()

        os.remove(f)
        
        fichero = open(f, "w")
        
        fichero.write(clean)
        
        fichero.close()