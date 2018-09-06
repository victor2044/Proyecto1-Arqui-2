import tkinter as tk
import threading
import time

class GUI(threading.Thread):
 
   def __init__(self):
      threading.Thread.__init__(self)
      self.root = tk.Tk()
      self.root.Core1 = tk.Text(self.root)
      self.root.Core2 = tk.Text(self.root)
      self.root.Core3 = tk.Text(self.root)
      self.root.Core4 = tk.Text(self.root)
      self.root.Memory = tk.Text(self.root)
      self.root.Misses = tk.Text(self.root)
      self.root.Cache1 = tk.Text(self.root)
      self.root.Cache2 = tk.Text(self.root)
      self.root.Cache3 = tk.Text(self.root)
      self.root.Cache4 = tk.Text(self.root)

      self.p1 = "Core 1 Action \n"
      self.p2 = "Core 2 Action \n"
      self.p3 = "Core 3 Action \n"
      self.p4 = "Core 4 Action \n"
      self.m1 = "Cache 1"
      self.m2 = "Cache 2"
      self.m3 = "Cache 3"
      self.m4 = "Cache 4"


      
   def run(self):
      self.root = tk.Tk()
      self.root.Core1 = tk.Text(self.root)
      self.root.Core2 = tk.Text(self.root)
      self.root.Core3 = tk.Text(self.root)
      self.root.Core4 = tk.Text(self.root)
      
      self.root.Memory = tk.Text(self.root)

      self.root.Misses = tk.Text(self.root)

      self.root.Cache1 = tk.Text(self.root)
      self.root.Cache2 = tk.Text(self.root)
      self.root.Cache3 = tk.Text(self.root)
      self.root.Cache4 = tk.Text(self.root)

      self.root.title("Modelo de protocolo para coherencia de cache en sistemas multiprocesador")
      self.root.geometry("1430x600")
      self.root.resizable(width=False, height=False)
      self.root.configure(bg = "black")
   
      print(self.p1)
      self.root.label1= tk.Label(self.root,text="Processors",fg = "Yellow",font=("Helvetica", 14),bg = "black")
      self.root.label1.place(y=5, x=680,width=100, height=20)
      
      self.root.label2= tk.Label(self.root,text="Cache Memory",fg = "Yellow",font=("Helvetica", 14),bg = "black")
      self.root.label2.place(y=240, x=515,width=150, height=20)

      self.root.label2= tk.Label(self.root,text="Cache Misses",fg = "Yellow",font=("Helvetica", 14),bg = "black")
      self.root.label2.place(y=240, x=1115,width=150, height=20)

      self.root.label3= tk.Label(self.root,text=" Principal Memory",fg = "Yellow",font=("Helvetica", 14),bg = "black")
      self.root.label3.place(y=475, x=650,width=180, height=20)


      
      self.root.Core1.place(y=30, x=0, width=350, height=200)

      
      self.root.Core2.place(y=30, x=360, width=350, height=200)

      
      self.root.Core3.place(y=30, x=720, width=350, height=200)

      
      self.root.Core4.place(y=30, x=1080, width=350, height=200)

      
      self.root.Cache1.place(y=260, x=170, width=800, height=50)

      self.root.Cache2.place(y=315, x=170, width=800, height=50)


      self.root.Cache3.place(y=370, x=170, width=800, height=50)

      self.root.Cache4.place(y=425, x=170, width=800, height=50)

      
      self.root.Misses.place(y=260, x=1000, width=350, height=200)

      
      self.root.Memory.place(y=500, x=315, width=800, height=50)
   
      self.root.mainloop()

   def printCore(self,ind,param):
      
      if ind == "1":
         print("OCUPO SABER QUE SI ESta LLEGANDO AQUI",ind,param)
         self.p1 += param+'\n'
         self.root.Core1.delete('1.0',tk.END)
         self.root.Core1.insert('end',self.p1)
      elif ind == "2":
         self.p2 += param+'\n'
         self.root.Core2.delete('1.0',tk.END)
         self.root.Core2.insert('end',self.p2)

      elif ind == "3":
         self.p3 += param+'\n'
         self.root.Core3.delete('1.0',tk.END)
         self.root.Core3.insert('end',self.p3)

      elif ind == "4":
         self.p4 += param+'\n'
         self.root.Core4.delete('1.0',tk.END)
         self.root.Core4.insert('end',self.p4)

   def printMemory(self,mem):
         self.root.Memory.delete('1.0',tk.END)
         self.root.Memory.insert('end',self.p4)
      
      
   def printCache(self,ind,param):
      if ind == "1":
         self.m1 = "Cache 1" +'\n'+param +'\n'
         self.root.Cache1.delete('1.0',tk.END)
         self.root.Cache1.insert('end',self.p4)
      elif ind == "2":
         self.m2 = "Cache 2" +'\n'+param +'\n'
         self.root.Cache2.delete('1.0',tk.END)
         self.root.Cache2.insert('end',self.p4)
      elif ind == "3":
         self.m3 = "Cache 3" +'\n'+param +'\n'
         self.root.Cache3.delete('1.0',tk.END)
         self.root.Cache3.insert('end',self.p4)
      elif ind == "4":
         self.m4 = "Cache 4" +'\n'+param +'\n'
         self.root.Cache4.delete('1.0',tk.END)
         self.root.Cache4.insert('end',self.p4)
      


def main ():
   app = GUI()
   a = "prueba"
   b = "prueba 2"
   app.start()
   app.printCore("1",a)
   app.printCore("1",b)
   app.printCore("3",a)
   app.printCache("1",a)
   app.printCache("1",b)
   app.root.Cache1.delete("2.0", tk.END)
   app.root.Cache1.insert(tk.INSERT, '\n' + b)
   
   
##if __name__ == "__main__":
##   main()

