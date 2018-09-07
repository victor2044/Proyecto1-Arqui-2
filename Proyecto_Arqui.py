import time
import threading
from random import randint
from collections import deque

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


class processor(threading.Thread):
    
    def __init__(self, name, cache):
        threading.Thread.__init__(self)
        self.name = name
        self.cache = cache
        self.stoprequest = threading.Event()
        
    def write (self):
        pos = randint(0,15)
        data = int(self.name)
        if self.name == "1":
            core1 = open ("core1.txt", "a")
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

    def read (self):
        pos = randint(0,15)
        if self.name == "1":
            core1 = open ("core1.txt", "a")
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

    def processing (self):
        if self.name == "1":
            core1 = open ("core1.txt", "a")
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
        time.sleep(1)

    def run (self):
        i = 0
        while True:
            print(i)

            i+=1
            aleat = randint(0,2)

            if aleat == 1:
                self.write()

            elif aleat == 0:
                self.read()
                
            else:
                self.processing()

class cache(threading.Thread):
    global mutex
    
    def __init__(self, name, bus):
        threading.Thread.__init__(self)
        self.name = name
        self.mem_cache = [(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0)]
        self.control = control_unit(name,bus,self.mem_cache)
        self.control.start()
        self.bus = bus
        self.stoprequest = threading.Event()
        
    def write(self,pos,data):
        index = self.mem_cache[pos]
        msi = index[0]
        validate = self.control.write(msi)
        self.mem_cache[pos] = (validate,data)
        prot = [1,self.name,pos, data]
        time.sleep(0.5)
        bus.bus_princ(prot)

                   
    def read(self,pos):
        index = self.mem_cache[pos]
        msi = index[0]
        validate = self.control.read(msi)
        if validate == 0:
            new_data= index[1]
            time.sleep(0.25)
            return new_data
        elif validate == 1:
            misses = open ("misses.txt", "a")
            misses.write('\n' + "cache miss in the core " +self.name+",in the position :"+str(pos+1))
            misses.close()
            time.sleep(0.25)
            data = index[1]
            prot = [0,self.name,pos, data]
            self.bus.bus_princ(prot)
            while True:
                if self.bus.q_read:
                    break
            while True:
                read = self.bus.q_read[-1]
                if (read[0] == self.name and
                    read[1] == pos):
                    break
                    
            self.mem_cache[pos] = (2,read[2])
            return read[2]
        else:
            new_data= index[1]
            return new_data

    def run (self):
        while True:
            if self.name == "1":
                cache1 = open ("cache1.txt", "w")
                cache1.write('\n' +str(self.mem_cache))
                cache1.close()
            elif self.name == "2":
                cache2 = open ("cache2.txt", "w")
                cache2.write('\n' +str(self.mem_cache))
                cache2.close()
            elif self.name == "3":
                cache3 = open ("cache3.txt", "w")
                cache3.write('\n' +str(self.mem_cache))
                cache3.close()
            elif self.name == "4":
                cache4 = open ("cache4.txt", "w")
                cache4.write('\n' + str(self.mem_cache))
                cache4.close()

            time.sleep(0.5)
        

class control_unit(threading.Thread):
    global mutex
    
    def __init__(self, name, bus, mem_cache):
        threading.Thread.__init__(self)
        self.name = name
        self.bus = bus
        self.mem_cache = mem_cache
        self.stoprequest = threading.Event()

    def write(self,msi):
        if msi == 2:
            msi = 0
            #valor actualizado de S a M, proceder con la escritura
            return msi
        elif msi == 1:
            msi = 0
            #valor actualizado de I a M, proceder con la escritura
            return msi
        else:
            #valor actualizado de M a M, proceder con la escritura
            return msi

    def read(self,msi):
        if msi == 2:
            #print proceder con la lectura de cache S a S
            return msi
        elif msi== 1:
            #cache miss en lectura
            return msi
        else:
            #proceder con la lectura de cache M a M
            return msi        


    def run (self):
        while True:
            instr = self.bus.snoop()
            pos = instr[2]
            data = self.mem_cache[pos]
            data1 = data[1]
            if instr:
                if (instr[0] == 1 and
                    instr[1] != self.name):
                   self.mem_cache[instr[2]] = (1, data1)
                elif (instr[0] == 0 and
                      instr[1] != self.name and
                      self.mem_cache[instr[2]][0] == 2):
                    self.mem_cache[instr[2]] = (2,instr[3])

                                           
    
class bus (threading.Thread):
    global mutex
    queue = []
    q_read = []
    
    def __init__(self,name,memory):
        threading.Thread.__init__(self)
        self.name = name
        self.memory = memory
        self.stoprequest = threading.Event()

    def bus_w (self,instr):
            pos = instr[2]
            data = instr[3]
            self.memory.write(pos,data)

    def bus_r (self,instr):
            name = instr[1]
            pos = instr[2]
            data = self.memory.read(pos)
            read = [name,pos,data]
            self.q_read.append(read)

    def bus_princ (self,prot):
        self.queue.append(prot)     

    def snoop(self):
        q = self.queue
        if (len(q) > 0):   
            instr = q[0]
            return instr
        return [-1,-1,-1]

    def run (self):
        while True:
            if self.queue:
                instr = self.queue[0]
                if instr[0]== 1:
                    self.bus_w(instr)
                else:
                    self.bus_r(instr)
                self.queue = self.queue[1:]
        
    
class memory (threading.Thread):
    mem_princ = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    global mutex
    
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name
        self.stoprequest = threading.Event()

    def write (self, pos, data):
        time.sleep(2)
        self.mem_princ[pos] = data

    def read (self, pos):
        time.sleep(1)
        data = self.mem_princ[pos]
        return data

    def run (self):
        while True:
            mem = open("mem.txt","w")
            mem.write('\n' +str(self.mem_princ))
            mem.close()
            time.sleep(0.5)

mutex = threading.Lock()

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
