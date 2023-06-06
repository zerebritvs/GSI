#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, hashlib, os

BUFFSIZE = 2048

inFile = sys.argv[1]

with open(inFile,'r') as file:                               #abro el fichero de entrada en modo lectura        
    lines = file.readlines()

    for line in lines:                                       #recorro cada linea del fichero de entrada
        line = line.replace('\n', '')                        #quito el caracter \n de cada linea
        comps = line.split(';')                              #separo la linea por ;

        hash = hashlib.sha256()
    
        with open(comps[0], 'rb') as binfile:               #abro el archivo del fichero de entrada en lectura binaria
            buffer = binfile.read(BUFFSIZE)
            while buffer:
                    hash.update(buffer)
                    hashFile = hash.hexdigest()             #creo el primer hash en hexadecimal
                    buffer = binfile.read(BUFFSIZE)

        stats = os.stat(comps[0])                           #obtengo las propiedades del archivo
        stats = repr(stats).encode()
        hash.update(stats)
        hashStats = hash.hexdigest()                        #creo el segundo hash en hexadecimal

        if(hashFile == comps[1]):
            print('El contenido de '+comps[0]+' no ha sido modificado')
        else:
            print('El contenido de '+comps[0]+' ha sido modificado')
        if(hashStats == comps[2]):
            print('Las propiedades de '+comps[0]+' no han sido modificadas\n')
        else:
            print('Las propiedades de '+comps[0]+' han sido modificadas\n')


