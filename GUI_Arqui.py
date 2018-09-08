import tkinter as tk
from tkinter import *
from threading import Thread
import time
from tkinter.scrolledtext import ScrolledText

ventana = tk.Tk()
ventana.title("Modelo de protocolo para coherencia de cache en sistemas multiprocesador")
ventana.geometry("1430x600")
ventana.resizable(width=False, height=False)
ventana.configure(bg = "black")

label1= Label(ventana,text="Processors",fg = "Yellow",font=("Helvetica", 14),bg = "black")
label1.place(y=5, x=680,width=100, height=20)
      
label2= Label(ventana,text="Cache Memory",fg = "Yellow",font=("Helvetica", 14),bg = "black")
label2.place(y=240, x=515,width=150, height=20)

label3= Label(ventana,text="Cache Misses",fg = "Yellow",font=("Helvetica", 14),bg = "black")
label3.place(y=240, x=1115,width=150, height=20)

label4= Label(ventana,text=" Principal Memory",fg = "Yellow",font=("Helvetica", 14),bg = "black")
label4.place(y=475, x=650,width=180, height=20)

Canva1 = Canvas(ventana)
Canva1.place(y=30, x=0, width=350, height=200)

Canva2 = Canvas(ventana)
Canva2.place(y=30, x=360, width=350, height=200)

Canva3 = Canvas(ventana)
Canva3.place(y=30, x=720, width=350, height=200)

Canva4 = Canvas(ventana)
Canva4.place(y=30, x=1080, width=350, height=200)

Canva5 = Canvas(ventana)
Canva5.place(y=260, x=170, width=800, height=50)

Canva6 = Canvas(ventana)
Canva6.place(y=315, x=170, width=800, height=50)

Canva7 = Canvas(ventana)
Canva7.place(y=370, x=170, width=800, height=50)

Canva8 = Canvas(ventana)
Canva8.place(y=425, x=170, width=800, height=50)

Canva9 = Canvas(ventana)
Canva9.place(y=260, x=1000, width=400, height=215)

Canva10 = Canvas(ventana)
Canva10.place(y=500, x=315, width=800, height=50)

Core1 = ScrolledText(Canva1)
Core1.place(y=0, x=0, width=350, height=200)
Core2 = Text(Canva2)
Core2.place(y=0, x=0, width=350, height=200)
Core3 = Text(Canva3)
Core3.place(y=0, x=0, width=350, height=200)
Core4 = Text(Canva4)
Core4.place(y=0, x=0, width=350, height=200)


Cache1 = Text(Canva5)
Cache1.place(y=0, x=0, width=800, height=50)
Cache2 = Text(Canva6)
Cache2.place(y=0, x=0, width=800, height=50)
Cache3 = Text(Canva7)
Cache3.place(y=0, x=0, width=800, height=50)
Cache4 = Text(Canva8)
Cache4.place(y=0, x=0, width=800, height=50)

Misses = Text(Canva9)
Misses.place(y=0, x=0, width=400, height=215)

Memory = Text(Canva10)
Memory.place(y=0, x=0, width=800, height=50)

      
def printCore1():
   while True:
      f= open("core1.txt", "r")
      Core1.delete('1.0',END)
      Core1.insert('1.0',f.read())
      time.sleep(0.5)

def printCore2():
   while True:
      f= open("core2.txt", "r")
      Core2.delete('1.0',END)
      Core2.insert('1.0',f.read())
      time.sleep(0.5)

def printCore3():
   while True:
      f= open("core3.txt", "r")
      Core3.delete('1.0',END)
      Core3.insert('1.0',f.read())
      time.sleep(0.5)

def printCore4():
   while True:
      f= open("core4.txt", "r")
      Core4.delete('1.0',END)
      Core4.insert('1.0',f.read())
      time.sleep(0.5)

def printMemory():
   while True:
      f= open("mem.txt", "r")
      Memory.delete('1.0',END)
      Memory.insert('1.0',f.read())
      time.sleep(0.5)
      
def printMisses():
   while True:
      f= open("misses.txt", "r")
      Misses.delete('1.0',END)
      Misses.insert('1.0',f.read())
      time.sleep(0.5)
   
def printCache1():
   while True:
      f= open("cache1.txt", "r")
      Cache1.delete('1.0',END)
      Cache1.insert('1.0',f.read())
      time.sleep(0.5)

def printCache2():
   while True:
      f= open("cache2.txt", "r")
      Cache2.delete('1.0',END)
      Cache2.insert('1.0',f.read())
      time.sleep(0.5)

def printCache3():
   while True:
      f= open("cache3.txt", "r")
      Cache3.delete('1.0',END)
      Cache3.insert('1.0',f.read())
      time.sleep(0.5)

def printCache4():
   while True:
      f= open("cache4.txt", "r")
      Cache4.delete('1.0',END)
      Cache4.insert('1.0',f.read())
      time.sleep(0.5)
   

def main ():
   hilo1 = Thread(target=printCore1, args=())
   hilo2 = Thread(target=printCore2, args=())
   hilo3 = Thread(target=printCore3, args=())
   hilo4 = Thread(target=printCore4, args=())
   hilo5 = Thread(target=printMemory, args=())
   hilo6 = Thread(target=printMisses, args=())
   hilo7 = Thread(target=printCache1, args=())
   hilo8 = Thread(target=printCache2, args=())
   hilo9 = Thread(target=printCache3, args=())
   hilo10 = Thread(target=printCache4, args=())
   hilo1.start()
   hilo2.start()
   hilo3.start()
   hilo4.start()
   hilo5.start()
   hilo6.start()
   hilo7.start()
   hilo8.start()
   hilo9.start()
   hilo10.start()

   
   
if __name__ == "__main__":
   main()

ventana.mainloop()
