### Implementation of the Observer Design Pattern,
###  Found here: http://code.activestate.com/recipes/131499-observer-pattern/
###
class Subject:
   def __init__(self):
      self._observers = []
   def attach(self, observer):
      if not observer in self._observers:
         self._observers.append(observer)

   def detach(self,observer):
      try:
         self._observers.remove(observer)
      except ValueError:
         pass
         
   def notify(self, modifier=None):
      for observer in self._observers:
         if modifier != observer:
            observer.update(self)
      
class Data(Subject):
   def __init__(self, name = ''):
      Subject.__init__(self)
      self.name = name
      self.data = 0
      
   def setData(self,data):
      self.data = data
      self.notify()
      
   def getData(self):
      return self.data
      
class HexViewer:
   def update(self, subject):
      print "The DATA PLEASE Hex!"
      print str(subject.name) + str(subject.getData())
  
      
class DecimalViewer:
   def update(self, subject):
      print "The DATA PLEASE Decimal!"
      print str(subject.name) + str(subject.getData())

      
def main():      
   data1 = Data('Data 1')  # 
   data2 = Data('Data 2')  # 

   view1 = DecimalViewer()
   view2 = HexViewer()

   data1.attach(view1)
   data1.attach(view2)
   data2.attach(view1)
   data2.attach(view2)

   print "setting data 1 = 10"
   data1.setData(10)
   print "setting data 2 = 15"
   data1.setData(15)
   print "setting data 1 = 3"
   data1.setData(3)
   print "setting data 2 = 5"
   data1.setData(5)
   print "Detaching HexViewer from Data and Data2"
   data1.detach(view1)
   data2.detach(view1)

   print "setting data 1 = 10"
   data1.setData(10)
   print "setting data 2 = 15"
   data1.setData(15)

if __name__=='__main__':
   main()
