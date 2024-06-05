class student:
   def __init__(self):
      self.name = "Sameer"
      self.subs = self.subjects()
      return
   def show(self):
      print ("Name:", self.name)
      self.subs.display()
   class subjects:
      def __init__(self):
         self.sub1 = "Python"
         self.sub2 = "Java"
         return
      def display(self):
         print ("Subjects:",self.sub1, self.sub2)   
s1 = student()
s1.show()