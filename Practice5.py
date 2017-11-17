user_name = raw_input("Hello, Welcome to File Reader. May I have your name? ")

print "Hello %s, nice to meet you, which file do you want to open today? " % user_name
file = raw_input()

print "Loading ..." 

# We add the 'w' so we can open the file in write mode instead of read
txt = open(file, 'w')

print "Here are the contents of the file:\n"
print txt.read()


print "Do you want to add any contents to the file?(y/n)"
answer = raw_input()


if answer == "y":
 print "How many lines do you want to add to the file?"
 numline = int(raw_input())
 txt = open(file, 'w')
 
 
 for i in range(numline):
   print "Please add a line of text to the file."
   rewrite = raw_input()
   txt.write(rewrite)
   txt.write("\n")
   txt.close()

 else:
  print "Thank you for using File Reader"