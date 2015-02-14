#!/usr/bin/python
# -*- coding: UTF-8 -*-

def costo_del_vuelo(ciudad):
    cities = {
        "Córdoba": 821,
        "Iguazú": 941,
        "Ushuaia": 1280,
        "Bariloche": 1848,
    }
    return cities[ciudad]

print costo_del_vuelo("Córdoba")
