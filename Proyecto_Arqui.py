import time
import threading
from random import randint
from collections import deque

#Creacion de los archivos de texto a trabajar
#//////////////////////////////////
core1 = open("core1.txt","w")
core1.close()
cache1 = open("cache1.txt","w")
cache1.close()
core2 = open("core2.txt","w")
core2.close()
cache2 = open("cache2.txt","w")
cache2.close()
core3 = open("core3.txt","w")
core3.close()
cache3 = open("cache3.txt","w")
cache3.close()
core4 = open("core4.txt","w")
core4.close()
cache4 = open("cache4.txt","w")
cache4.close()
mem = open("mem.txt","w")
mem.close()
misses= open("misses.txt","w")
misses.close()
#//////////////////////////////////


#Clase que se encarga de ejecutar un ciclo en el cual se genera
#un numero aleatorio para seleccionar entre las 3 acciones write, read, processing
class processor(threading.Thread):

    #inicializacion de la clase
    def __init__(self, name, cache):
        threading.Thread.__init__(self)
        self.name = name
        self.cache = cache
        self.stoprequest = threading.Event()
        
    def write (self): # metodo encargado de llamar al metodo write de la memoria cache
        pos = randint(0,15) # generacion aleatoria de la posicion a memoria a leer
        data = int(self.name) # se guarda el dato a escribir correspondiente al nombre
        if self.name == "1":
            core1 = open ("core1.txt", "a")  #modificacion del archivo de texto
            core1.write('\n' + str("core " + self.name +" escribiendo en:"+str(pos+1)))
            core1.close()
        elif self.name == "2":
            core2 = open ("core2.txt", "a")
            core2.write('\n' + str("core " + self.name +" escribiendo en:"+str(pos+1)))
            core2.close()
        elif self.name == "3":
            core3 = open ("core3.txt", "a")
            core3.write('\n' + str("core " + self.name +" escribiendo en:"+str(pos+1)))
            core3.close()
        elif self.name == "4":
            core4 = open ("core4.txt", "a")
            core4.write('\n' + str("core " + self.name +" escribiendo en:"+str(pos+1)))
            core4.close()
        self.cache.write(pos,data)

    def read (self): #metodo encargado de llamar al metodo read de la memoria cache
        pos = randint(0,15)
        if self.name == "1":
            core1 = open ("core1.txt", "a")   #modificacion del archivo de texto
            core1.write('\n' + "core " + self.name +" leyendo en:"+str(pos+1))
            core1.close()
        elif self.name == "2":
            core2 = open ("core2.txt", "a")
            core2.write('\n' + "core " + self.name +" leyendo en:"+str(pos+1))
            core2.close()
        elif self.name == "3":
            core3 = open ("core3.txt", "a")
            core3.write('\n' + "core " + self.name +" leyendo en:"+str(pos+1))
            core3.close()
        elif self.name == "4":
            core4 = open ("core4.txt", "a")
            core4.write('\n' + "core " + self.name +" leyendo en:"+str(pos+1))
            core4.close()
        data = self.cache.read(pos)

    def processing (self): # metodo que se encarga de hacer la funcion de processing por que
        if self.name == "1":      #solo inserta una pausa en la ejecucion del sistema
            core1 = open ("core1.txt", "a")  #modificacion del archivo de texto
            core1.write('\n' + "core " + self.name +" procesando")
            core1.close()
        elif self.name == "2":
            core2 = open ("core2.txt", "a")
            core2.write('\n' + "core " + self.name +" procesando")
            core2.close()
        elif self.name =="3":
            core3 = open ("core3.txt", "a")
            core3.write('\n' + "core " + self.name +" procesando")
            core3.close()
        elif self.name == "4":
            core4 = open ("core4.txt", "a")
            core4.write('\n' + "core " + self.name +" procesando")
            core4.close()
        time.sleep(4)

    def run (self): # Ciclo que se encarga de generar aleatoriamente que instruccion se va a realizar
        i = 0   
        while True:
            i+=1
            aleat = randint(0,2)

            if aleat == 1: # 1 para escritura
                self.write()

            elif aleat == 0: # 0 para lectura
                self.read()
                
            else:           # 2 para processing
                self.processing()
                
#Esta clase se encarga de estar actualizando en un archivo txt el estado
#de la memoria cache de su core, ademas de realizar los procesos de escritura o lectura
#sobre la memoria cache
class cache(threading.Thread):

    #inicializacion de la clase
    def __init__(self, name, bus):
        threading.Thread.__init__(self)
        self.name = name
        #por el protocoloy la especificacion la memoria se inicializa en (2,0)
        self.mem_cache = [(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0)]
        #instancia de la clase control
        self.control = control_unit(name,bus,self.mem_cache)
        self.control.start()
        self.bus = bus
        self.stoprequest = threading.Event()
        
    def write(self,pos,data):           #metodo encargado de actualizar la memoria cache en la posición solicitada
        self.mem_cache[pos] = (0,data)  #actualizacion de la memoria cache con el nuevo dato y el bit de validez
        prot = [1,self.name,pos, data]  #generacion de la instruccion a enviar al bus para la escritura del dato en memoria principal
        time.sleep(4)                   #pausa debido al coste de la operacion.
        bus.bus_princ(prot)             #envio de la instruccion de escritura al bus

                   
    def read(self,pos):                #metodo encargado de leer la memoria cache en la posición solicitada
        index = self.mem_cache[pos]
        validate = index[0]            #obtencion del bit de validez de la posicion de memoria a realizar la lectura
        if validate == 0:              #se valida si el bit de validez esta en condicion de modificado si si
            new_data= index[1]         #se procede con la lectura del dato
            time.sleep(4)
            return new_data
        elif validate == 1:            #si el bits de validez esta como invalido se procede a generar el miss
            misses = open ("misses.txt", "a")
            misses.write('\n' + "cache miss in the core " +self.name+",in the position :"+str(pos+1))
            misses.close()             #escritura del miss en el archivo de texto
            data = index[1]
            prot = [0,self.name,pos, data]#generacion de la instrucion a enviar al bus para la lectura del dato desde memoria principal
            self.bus.bus_princ(prot)   #envio de la instruccion de lectura
            while True:                #ciclo en el que se valida que la cola q_read no este vacia
                if self.bus.q_read:    #si no esta vacia se quiebra el ciclo
                    break
            while True:                #ahora se procede a obtener el ultimo elemento de la cola en la cual esta la instruccion generada  
                read = self.bus.q_read[-1]  #de lectura
                if (read[0] == self.name and  #se valida que la instruccion tenga el mismo nombre que el core que la genero
                    read[1] == pos):   #se valida que la posicion ademas del campo leido coincide con el de la instrucion enviada por este core
                    break              # si si se quiebra el ciclo                  
            time.sleep(4)
            self.mem_cache[pos] = (2,read[2]) # se procede a actualizar la memoria cache con el dato leido desde memoria principal.
            return read[2]
        else:                          # si el dato tiene el bit de validez como compartido entonces se lee con exito
            time.sleep(4)
            new_data= index[1]
            return new_data

    def run (self):       #loop que se encarga de que el hilo se mantenga actualizando el archivo txt con el estado de la memoria cache 
        while True:
            if self.name == "1":
                cache1 = open ("cache1.txt", "w")  #modificacion del archivo de texto
                cache1.write("cache1"+'\n' +str(self.mem_cache))
                cache1.close()
            elif self.name == "2":
                cache2 = open ("cache2.txt", "w")
                cache2.write("cache2"+'\n' +str(self.mem_cache))
                cache2.close()
            elif self.name == "3":
                cache3 = open ("cache3.txt", "w")
                cache3.write("cache3"+'\n' +str(self.mem_cache))
                cache3.close()
            elif self.name == "4":
                cache4 = open ("cache4.txt", "w")
                cache4.write("cache4"+'\n' + str(self.mem_cache))
                cache4.close()

            time.sleep(1)
        
#clase encargada de realizar el monitoreo del bus del sistema y actualizar el estado del bit de validez de un dato en memoria cache
class control_unit(threading.Thread):

    #inicializacion de la clase
    def __init__(self, name, bus, mem_cache):
        threading.Thread.__init__(self)
        self.name = name
        self.bus = bus
        self.mem_cache = mem_cache
        self.stoprequest = threading.Event()       


    def run (self):  #ciclo que se encarga de monitorear el bus del sistema
        while True:
            instr = self.bus.snoop()   #se solicita la instruccion que esta procesando el bus del sistema
            pos = instr[2]             #se extrae la posicion de memoria que esta solicitando w/r esta instruccion
            data = self.mem_cache[pos] #se extrae la tupla de memoria cache en la posicion que se indica w/r 
            data1 = data[1]            #se extrae el dato de la tupla extraida anteriormente
            if instr:                  #ahora se verifica que la instruccion no este vacia
                if (instr[0] == 1 and  #se valida si la instruccion es una escritura y si no fue enviada por este core
                    instr[1] != self.name):
                   self.mem_cache[pos] = (1, data1) #si es asi se procede a actualizar el bit de validez a invalido de la
                                                    #posicion indicada
                elif (instr[0] == 0 and   #se valida si la instruccion es una lectura y si no fue enviada por este core
                      instr[1] != self.name and #ademas de que si el estado de ese bit de validez de la memoria es modificado
                      self.mem_cache[pos][0] == 0):
                    self.mem_cache[pos] = (2,data1) #si es asi se actualiza el estado a compartido del bit de validez

#Clase que se encarga de recibir todas las peticiones que realicen los procesadores y verificar si según 
#el protocolo corresponden a una lectura o una escritura, para enviarlos a memoria respectivamente a w/r                                         
class bus (threading.Thread):
    queue = []                         #cola del bus
    q_read = []                        #Cola de lectura del bus

    #inicializacion de la clase
    def __init__(self,name,memory):
        threading.Thread.__init__(self)
        self.name = name
        self.memory = memory
        self.stoprequest = threading.Event()

    def bus_w (self,instr):            #metodo encargado de llamar al metodo de escritura de la memoria  
            pos = instr[2]
            data = instr[3]
            self.memory.write(pos,data)

    def bus_r (self,instr):           #metodo encargado de llamar al metodo de lectura de la memoria 
            name = instr[1]
            pos = instr[2]
            data = self.memory.read(pos) #dato leido desde memoria
            read = [name,pos,data]    #generacion del protocolo para enviar el dato leido
            self.q_read.append(read)  #insercion de esta instruccion en la cola de lectura

    def bus_princ (self,prot):        #captura en la cola de todas las instrucciones que solcitan los multiples cores
        self.queue.append(prot)     

    def snoop(self):                  #metodo que se encarga de obtener la primera instruccion de la cola, con lo que
        q = self.queue                #se asegura que la misma es la que se esta ejecutando
        if (len(q) > 0):   
            instr = q[0]
            return instr              #y la retorna
        return [-1,-1,-1]

    def run (self):                   #ciclo que se encarga de que la cola no esta vacia y obtiene la primera instruccion 
        while True:                   #que llego a la cola para asi enviarsela a sus metodos de w/r respectivamente 
            if self.queue:
                instr = self.queue[0]
                if instr[0]== 1:
                    time.sleep(8)
                    self.bus_w(instr)
                else:
                    time.sleep(8)
                    self.bus_r(instr)
                self.queue = self.queue[1:] #borrado de la cola de la instruccion ejecutada
        

    
class memory (threading.Thread):
    mem_princ = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    #inicializacion de la clase
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name
        self.stoprequest = threading.Event()

    def write (self, pos, data):   #metodo encargado de escribir en memoria el dato solicitado
        self.mem_princ[pos] = data
 
    def read (self, pos):          #metodo encargado de leer de memoria el dato solicitado y retornarlo
        data = self.mem_princ[pos]
        return data

    def run (self):               #metodo encargado de escribir en elarchivo txt el estado de la memoria
        while True:
            mem = open("mem.txt","w")
            mem.write('\n' +str(self.mem_princ))
            mem.close()
            time.sleep(1)


#//////////////////////////////////////////////
#Secuencia de inicializaion del programa
#/////////////////////////////////////////////

#hilos unicos                   
princ_mem = memory("principal_memory")
bus = bus("principal_bus", princ_mem)
#Caches
cache1 = cache("1", bus)
cache2 = cache("2", bus)
cache3 = cache("3", bus)
cache4 = cache("4", bus)
#Cores
core1 = processor("1",cache1)
core2 = processor("2",cache2)
core3 = processor("3",cache3)
core4 = processor("4",cache4)

#inicializacion de hilos
princ_mem.start()
bus.start()
cache1.start()
cache2.start()
cache3.start()
cache4.start()
core1.start()
core2.start()
core3.start()
core4.start()
#indicacion de que los cores deben de esperar
core1.join()
core2.join()
core3.join()
core4.join()
