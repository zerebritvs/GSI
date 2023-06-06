#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, hashlib, os

BUFFSIZE = 2048

inFile = sys.argv[1]
outFile = sys.argv[2]
fich = open(outFile,'w')                                        #abro el fichero de salida en modo escritura

with open(inFile,'r') as file:                                  #abro el fichero de entrada en modo lectura
    lines = file.readlines()

    for path in lines:                                          #recorro cada linea del fichero de entrada
        path = path.replace('\n', '')                           #quito el caracter \n                      
        hash = hashlib.sha256()
    
        with open(path, 'rb') as binfile:                       #abro el archivo del fichero de entrada en lectura binaria
            buffer = binfile.read(BUFFSIZE)
            while buffer:
                    hash.update(buffer)
                    hashFile = hash.hexdigest()                 #creo el primer hash en hexadecimal
                    buffer = binfile.read(BUFFSIZE)

        stats = os.stat(path)                                   #obtengo las propiedades del archivo
        stats = repr(stats).encode()
        hash.update(stats)
        hashStats = hash.hexdigest()                            #creo el segundo hash en hexadecimal
        fich.write(path+';'+hashFile+';'+hashStats+'\n')        #escribo la ruta y los dos hash en el fichero salida

fich.close()

