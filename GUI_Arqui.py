import tkinter as tk
import threading
import time

class GUI(tk.Tk,threading.Thread):
 
   def __init__(self):
      tk.Tk.__init__(self)
      threading.Thread.__init__(self)
      self.title("Modelo de protocolo para coherencia de cache en sistemas multiprocesador")
      self.geometry("1430x600")
      self.resizable(width=False, height=False)
      self.configure(bg = "black")
      
      self.label1= tk.Label(self,text="Processors",fg = "Yellow",font=("Helvetica", 14),bg = "black")
      self.label1.place(y=5, x=680,width=100, height=20)
      
      self.label2= tk.Label(self,text="Cache Memory",fg = "Yellow",font=("Helvetica", 14),bg = "black")
      self.label2.place(y=240, x=660,width=150, height=20)

      self.label3= tk.Label(self,text=" Principal Memory",fg = "Yellow",font=("Helvetica", 14),bg = "black")
      self.label3.place(y=475, x=650,width=180, height=20)

      self.Core1 = tk.Text(self)
      p1 = "Core 1 Action"
      self.Core1.insert(tk.INSERT, p1 +'\n')
      self.Core1.place(y=30, x=0, width=350, height=200)

      self.Core2 = tk.Text(self)
      p2 = "Core 2 Action"
      self.Core2.insert(tk.INSERT, p2 +'\n')
      self.Core2.place(y=30, x=360, width=350, height=200)

      self.Core3 = tk.Text(self)
      p3 = "Core 3 Action"
      self.Core3.insert(tk.INSERT, p3 +'\n')
      self.Core3.place(y=30, x=720, width=350, height=200)

      self.Core4 = tk.Text(self)
      p4 = "Core 4 Action"
      self.Core4.insert(tk.INSERT, p4 +'\n')
      self.Core4.place(y=30, x=1080, width=350, height=200)

      self.Cache1 = tk.Text(self)
      m1 = "Cache 1"
      self.Cache1.insert(tk.INSERT, m1 +'\n')
      self.Cache1.place(y=260, x=315, width=800, height=50)

      self.Cache2 = tk.Text(self)
      m2 = "Cache 2"
      self.Cache2.insert(tk.INSERT, m2 +'\n')
      self.Cache2.place(y=315, x=315, width=800, height=50)

      self.Cache3 = tk.Text(self)
      m3 = "Cache 3"
      self.Cache3.insert(tk.INSERT, m3 +'\n')
      self.Cache3.place(y=370, x=315, width=800, height=50)

      self.Cache4 = tk.Text(self)
      m4 = "Cache 4"
      self.Cache4.insert(tk.INSERT, m4 +'\n')
      self.Cache4.place(y=425, x=315, width=800, height=50)

      self.Memory = tk.Text(self)
      mem =[(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0)]
      self.Memory.insert(tk.INSERT, mem)
      self.Memory.place(y=500, x=315, width=800, height=50)
      
      self.stoprequest = threading.Event()

   def printCo(self,ind,param):
      if ind == "1":
         self.Core1.insert(tk.INSERT, param+'\n')
      elif ind == "2":
         self.Core2.insert(tk.INSERT, param+'\n')
      elif ind == "3":
         self.Core3.insert(tk.INSERT, param+'\n')
      elif ind == "4":
         self.Core4.insert(tk.INSERT, param+'\n')  

   def printCa(self,ind,param):
      if ind == "1":
         self.Cache1.delete("2.0", tk.END)
         self.Cache1.insert(tk.INSERT, '\n' + param)
      elif ind == "2":
         self.Cache2.delete("2.0", tk.END)
         self.Cache2.insert(tk.INSERT, '\n' + param)
      elif ind == "3":
         self.Cache3.delete("2.0", tk.END)
         self.Cache3.insert(tk.INSERT, '\n' + param)
      elif ind == "4":
         self.Cache4.delete("2.0", tk.END)
         self.Cache4.insert(tk.INSERT, '\n' + param)
      

"""
def main ():
   app = GUI()
   a = "prueba"
   b = "prueba 2"
   app.printCo("1",a)
   app.printCo("1",a)
   app.printCo("3",a)
   app.printCa("1",a)
   app.printCa("1",b)
   app.mainloop()
   app.start()

if __name__ == "__main__":
   main()
"""
