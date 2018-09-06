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

      self.root.Cache1 = tk.Text(self.root)
      self.root.Cache2 = tk.Text(self.root)
      self.root.Cache3 = tk.Text(self.root)
      self.root.Cache4 = tk.Text(self.root)

   def run(self):   
      self.root = tk.Tk()
      self.root.Core1 = tk.Text(self.root)
      self.root.Core2 = tk.Text(self.root)
      self.root.Core3 = tk.Text(self.root)
      self.root.Core4 = tk.Text(self.root)
      self.root.Memory = tk.Text(self.root)

      self.root.Cache1 = tk.Text(self.root)
      self.root.Cache2 = tk.Text(self.root)
      self.root.Cache3 = tk.Text(self.root)
      self.root.Cache4 = tk.Text(self.root)

      self.root.title("Modelo de protocolo para coherencia de cache en sistemas multiprocesador")
      self.root.geometry("1430x600")
      self.root.resizable(width=False, height=False)
      self.root.configure(bg = "black")
   
      
      self.root.label1= tk.Label(self.root,text="Processors",fg = "Yellow",font=("Helvetica", 14),bg = "black")
      self.root.label1.place(y=5, x=680,width=100, height=20)
      
      self.root.label2= tk.Label(self.root,text="Cache Memory",fg = "Yellow",font=("Helvetica", 14),bg = "black")
      self.root.label2.place(y=240, x=660,width=150, height=20)

      self.root.label3= tk.Label(self.root,text=" Principal Memory",fg = "Yellow",font=("Helvetica", 14),bg = "black")
      self.root.label3.place(y=475, x=650,width=180, height=20)

      p1 = "Core 1 Action"
      self.root.Core1.insert(tk.INSERT, p1 +'\n')
      self.root.Core1.place(y=30, x=0, width=350, height=200)

      p2 = "Core 2 Action"
      self.root.Core2.insert(tk.INSERT, p2 +'\n')
      self.root.Core2.place(y=30, x=360, width=350, height=200)

      p3 = "Core 3 Action"
      self.root.Core3.insert(tk.INSERT, p3 +'\n')
      self.root.Core3.place(y=30, x=720, width=350, height=200)

      p4 = "Core 4 Action"
      self.root.Core4.insert(tk.INSERT, p4 +'\n')
      self.root.Core4.place(y=30, x=1080, width=350, height=200)


      m1 = "Cache 1"
      self.root.Cache1.insert(tk.INSERT, m1 +'\n')
      self.root.Cache1.place(y=260, x=315, width=800, height=50)

      m2 = "Cache 2"
      self.root.Cache2.insert(tk.INSERT, m2 +'\n')
      self.root.Cache2.place(y=315, x=315, width=800, height=50)

      m3 = "Cache 3"
      self.root.Cache3.insert(tk.INSERT, m3 +'\n')
      self.root.Cache3.place(y=370, x=315, width=800, height=50)

      m4 = "Cache 4"
      self.root.Cache4.insert(tk.INSERT, m4 +'\n')
      self.root.Cache4.place(y=425, x=315, width=800, height=50)

      
      mem =[(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0)]
      self.root.Memory.insert(tk.INSERT, mem)
      self.root.Memory.place(y=500, x=315, width=800, height=50)
   
      self.root.mainloop()

   def printCo(self,ind,param):
      if ind == "1":
         self.root.Core1.insert(tk.INSERT, param +'\n')
      elif ind == "2":
         self.root.Core2.insert(tk.INSERT, param +'\n')
      elif ind == "3":
         self.root.Core3.insert(tk.INSERT, param +'\n')
      elif ind == "4":
         self.root.Core4.insert(tk.INSERT, param +'\n')  

   def printCa(self,ind,param):
      if ind == "1":
         self.root.Cache1.delete("2.0", tk.END)
         self.root.Cache1.insert(tk.INSERT, '\n' + param)
      elif ind == "2":
         self.root.Cache2.delete("2.0", tk.END)
         self.root.Cache2.insert(tk.INSERT, '\n' + param)
      elif ind == "3":
         self.root.Cache3.delete("2.0", tk.END)
         self.root.Cache3.insert(tk.INSERT, '\n' + param)
      elif ind == "4":
         self.root.Cache4.delete("2.0", tk.END)
         self.root.Cache4.insert(tk.INSERT, '\n' + param)
      


def main ():
   app = GUI()
   a = "prueba"
   b = "prueba 2"
   app.printCo("1",a)
   app.printCo("1",a)
   app.printCo("3",a)
   app.printCa("1",a)
   app.printCa("1",b)
   app.root.Cache1.delete("2.0", tk.END)
   app.root.Cache1.insert(tk.INSERT, '\n' + b)
   app.start()
  # app.mainloop()
   
if __name__ == "__main__":
   main()

