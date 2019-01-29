jflags = -g
jc = javac
.suffix: 
	.java .class

.java.class:
	$(jc) $(jflags) $*.java

CLASSES = Sorting.java

default: 
	classes

classes: 
	$(CLASSES: .java=.class)

clean:
	$(RM) *.class
