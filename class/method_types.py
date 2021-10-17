#!/bin/env python3

# stm => STatic Method
# inm => INstance Method
# clm => CLass Method
class Class1:
	@staticmethod		# without it, returns error when calling
	def stm(x):
		return x
	def inm(self, x):
		return x
	@classmethod		# without it, does not return error when calling from instance, but return error for class itself
	def clm(cls, x):
		return x

a = Class1()
print(a.stm(1))
print(a.inm(2))
print(a.clm(3))
print(Class1.clm(4))
print(Class1.stm(5))

class Class2:
	variable1 = None
	@staticmethod
	def stm(x):
		variable1 = x						# class attribute does not change
	def inm(self, x):
		x = x
		self.variable1 = x			# Instance attribute changes, but not class attribute
	@classmethod
	def clm(cls, x):					# Class Attribute changes, but once instance attribute has been set, do not change
		cls.variable1 = x

a = Class2()
b = Class2()

a.stm(1)
print(a.variable1)
a.inm(2)
print(a.variable1)
print(b.variable1)
a.clm(3)
print(a.variable1)
print(b.variable1)
Class2.clm(4)
print(a.variable1)
print(b.variable1)
b.inm(5)
print(a.variable1)
print(b.variable1)

class Class3:
	@staticmethod
	def stm(x):
		variable1 = x
	def inm(self,x):
		self.variable1 = x
	@classmethod
	def clm(cls, x):
		cls.variable1 = x

a = Class3()
a.stm(1)
# print(a.variable1)
a.clm(2)
print(a.variable1)
a.inm(3)
print(a.variable1)

class Class4:
	# z = 3
	# @staticmethod
	# def stm1(x):				# staicmethod cannot call other methods in the same class
	# 	return z
	@staticmethod
	def stm2(y):
		return y
	@classmethod
	def clm1(cls, x):
		cls.stm2(x)
		cls.clm2(x)
		cls.inm2(cls,x)			# when classmethod call instance method, cls should be placed in self position
	@classmethod
	def clm2(cls, x):
		return x
	def inm1(self, x):
		self.stm2(x)
		self.clm2(x)				# when instance method call classmethod, it does not require any
		self.inm2(x)
	def inm2(slef, x):
		return x

a = Class4()
a.clm1(3)
a.inm1(3)

class Class5:
	@classmethod
	def clm1(cls, x):
		cls.variable1 = "clm1_" + str(x)
		cls.inm1(cls,x)
	def inm1(self, x):
		self.variable1 = "inm1_"  + str(x)
	def inm2(self, x):
		self.variable2 = "inm2_"  + str(x)
		self.clm2(x)
	@classmethod
	def clm2(cls, x):
		cls.variable2 = "clm2_"  + str(x)
	@classmethod
	def clm3(cls, x):
		cls.variable3 = "clm3_" + str(x)
		cls.inm3(cls, x)
	def inm3(self, x):
		self.variable4 = "inm3_" + str(x)
a = Class5()
a.clm1(3)
print(a.variable1)
b = Class5()
print(b.variable1)				# if class method calls instance method, it effects all instances (including later instances)
a.inm2(3)
print(a.variable2)
print(b.variable2)
a.clm3(3)
print(a.variable3)
print(a.variable4)
print(b.variable4)

class Class6:
	@classmethod
	def clm(cls):
		print(type(cls))
		print(cls)
	def inm(self):
		print(type(self))
		print(self)
a = Class6()
a.clm()
a.inm()

class Class7:
	def clm(cls):
		cls.var = "3"

a = Class7()
b = Class7()
a.clm()
print(a.var)
# print(b.var)

class Class8:
	def inm(self):
		self.x = 3

a = Class8()
# a.inm(Class8)

class Class9:
	@classmethod
	def clm(cls):
		cls.var1 = "clm"
Class9.clm()
print(Class9.var1)
a = Class9()
print(a.var1)