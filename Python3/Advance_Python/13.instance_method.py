'''
There are three types of methods:
	1.Instance_methods
	2.Class_methods
	3.Static_methods
		
There are two types of instance_methods
	1.Accessor_methods
	2.Mutator_methods

Instance methods are the methods which act upon the instance variables of the class.
Instance_method need to know the memory address of the instance which is provided through self variable by default as first parameter of the instance_method.
2:30/13:50
'''

##Instance_method without Parameter/Formal_argument
def method_name(self):
	function body

##Instance_method with Parameter/Formal_argument
def method_name(self, f1, f2):
	function body