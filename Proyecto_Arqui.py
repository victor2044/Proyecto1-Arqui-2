import time
import threading
from random import randint
from collections import deque
 
class processor(threading.Thread):
    
    def __init__(self, name, cache):
        threading.Thread.__init__(self)
        self.name = name
        self.cache = cache
        self.stoprequest = threading.Event()
        
    def write (self):
        print ("core " + self.name +" escribiendo\n")
        self.cache.write(0,1)

    def read (self):
        print ("core " + self.name +" leyendo\n")
        pos = 0
        data = self.cache.read(pos)
        print (data)

    def processing (self):
        print ("core " + self.name +" processing\n")
        time.sleep(1)

    def run (self):
        i = 0
        while i < 10:
            i+=1
            aleat = randint(0,2)
            #aleat = 0

            if aleat == 0: 
                self.write()
            elif aleat == 1:
                self.read()
            else:
               self.processing()

class cache(threading.Thread):
    mem_cache = [(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0)]
 
    def __init__(self, name, control_unit, bus):
        threading.Thread.__init__(self)
        self.name = name
        self.control = control_unit
        self.bus = bus
        self.stoprequest = threading.Event()
        
    def write(self,pos,data):
        index = self.mem_cache[pos]
        msi = index[0]
        validate = self.control.write(msi)
        if validate == 0:
            self.mem_cache[pos] = (validate,data)
            prot = [1,self.name,pos, data]
            time.sleep(2)
            bus.bus_princ(prot)
            print ("escritura exitosa")
            print (self.mem_cache)
        elif validate == 1:
            print ("cache miss in the position :" + pos)
            time.sleep(2)
            prot = [0,self.name,pos, data]
            new_data = bus.bus_princ(prot)
            mem_cache[pos] = (2,new_data[2])      
                   
    def read(self,pos):
        index = self.mem_cache[pos]
        msi = index[0]
        validate = self.control.read(msi)
        if validate == 0:
            new_data= index[1]
            print ("lectura exitosa")
            return new_data
        elif validate == 1:
            print ("cache miss in the position :" + pos)
            time.sleep(2)
            prot = [0,self.name,pos, data]
            new_data = bus.bus_princ(prot)
            self.mem_cache[pos] = (2,new_data[2])
            return new_data[2]
        else:
            new_data= index[1]
            return new_data

    def run (run):
        while True:
            instr = self.control.snoop()
            print ("estoy corriendo")
            if instr:
                index = mem_cache[instr[2]]
                data = index[1]
                if instr[0] == 0:
                    mem_cache[instr[2]] = (1,data)
                    print ("cache actualizada por lectura")
                else:
                    mem_cache[instr[2]] = (2,data)
                    print ("cache actualizada por escritura")
        

class control_unit(threading.Thread):
    
    def __init__(self, name, bus):
        threading.Thread.__init__(self)
        self.name = name
        self.bus = bus
        self.stoprequest = threading.Event()

    def write(self,msi):
        if msi == 2:
            msi = 0
            print ("valor actualizado de S a M, proceder con la escritura")
            return msi
        elif msi == 1:
            print ("cache miss en escritura")
            return msi
        else:
            print ("valor actualizado de M a M, proceder con la escritura")
            return msi

    def read(self,msi):
        if msi == 2:
            print ("proceder con la lectura de cache S a S")
            return msi
        elif msi== 1:
            print ("cache miss en lectura")
            return msi
        else:
            print ("proceder con la lectura de cache M a M")
            return msi        

    def snoop (self):
        work = bus.snoop()
        if work:
            instr = work[0]
            if instr[1]!= self.name:
                print ("actualizando cache snoop")
                return instr
                    
    
class bus (threading.Thread):    
    queue = deque([])
    
    def __init__(self,name,memory):
        threading.Thread.__init__(self)
        self.name = name
        self.memory = memory
        self.stoprequest = threading.Event()

    def bus_w (self):
            instr = self.queue.popleft()
            pos = instr[2]
            data = instr[3]
            self.memory.write(pos,data)
            print ("escritura exitosa hacia memoria")

    def bus_r (self):
            instr = self.queue.popleft()
            name = instr[1]
            pos = instr[2]
            data = self.memory.read(pos)
            read = [name,pos,data]
            return read
            print ("lectura exitosa desde memoria")

    def bus_princ (self,prot):
        self.queue.append(prot)
        while self.queue:
            if prot[0]== 1:
                self.bus_w()
            else:
                read = self.bus_r()
                return read

    def snoop(self):
        return self.queue
        
    
class memory (threading.Thread):
    mem_princ = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name
        self.stoprequest = threading.Event()

    def write (self, pos, data):
        self.mem_princ[pos] = data

    def read (self, pos):
        data = self.mem_princ[pos]
        return data
            
                    
princ_mem = memory("principal_memory")
bus = bus("principal_bus", princ_mem)
control_unit1 = control_unit("1", bus)
control_unit2 = control_unit("2", bus)
cache1 = cache("1", control_unit1, bus)
cache2 = cache("2", control_unit2, bus)
core1 = processor("1",cache1)
core2 = processor("2",cache2)
core1.start()
core2.start()
cache1.start()
cache2.start()

cache1.join()
core1.join()
