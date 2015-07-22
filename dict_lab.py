print u"Session 4 task 9 item 3"


s2 = ()
l2 = list(s2)
for i in range(21):
    if i % 2 == 0:
        l2.append(i)
print l2

s3 = ()
l3 = list(s3)
for i in range(21):
    if i % 3 == 0:
        l3.append(i)
print l3


s4 = ()
l4 = list(s4)
for i in range(21):
    if i % 4 == 0:
        l4.append == 0

print "*" * 10
print u"Here is the list of sets created:"
print s2
print s3
print s4
print "*" * 10
print "Here is a list of s2 that has numbers divisible by 2"
print l2
print "*" * 10
print "Here is a list of s3 that has numbers divisible by 3"
print l3
print "*" * 10
print "Here is a list of s4 that has numbers divisible by 4"
print l4

# Display if s3 is a subset of s2 (False)
print u"is s3 a subset of s2 is (False)"
print s3.issubset(s2)

# Display if s4 is a subset of s2 (True)
print u"is s4 a subset of s2 (True)"
print s4.issubset(s2)
