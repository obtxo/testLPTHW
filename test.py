'''
print "test test test" #coment comment comment
print "test test test"

for i in range(1,5):
    print 'test'
#else:
#    print 'fin.'

print "maths", 2 + 2 - 2 * 2 / 2
print "maths", 3 + 2 < 5 - 7
print "maths", 10 % 3
print 3 + 2 < 5 - 7
print 3 + 2 > 5 - 7
print 3 + 2 <= 5 - 0
print 3 + 2 <= 5 - -2
print 3 + 2 >= 5 - 7
print 3 + 2 >= 5 - 7
print 2.5 + 2.5
print 5.0 / 2
#force integer
print int (10.0 / 3.0)
#force float
print float (10 / 3)
lol = 1 # set as int
wut = 2.0 # set as float
print float(wut + lol) #maths
print int(wut + lol) # maths

wtf = 'string of text'
lolwut = 'kthxbye'
shiiit = 42
fucku = 34
srsly = 19
print "word word word %s." % wtf
print "word word %d word" % shiiit
print "word %s word %s." % (wtf, lolwut)
print "so %d plus %d plus %d is: %d" % (shiiit, fucku, srsly, shiiit + fucku + srsly)

megabitclaimed = 101.00 # set claimed speed
megabyte = megabitclaimed / 8.00 # .125 MB = 1 Mb
print "Actual speed is: %d MegaByte/s" % megabyte
print "Claimed: %d megabit\nActual: %d megabyte" % (megabitclaimed, megabyte)
print ""
string1 = 'words1'
string2 = 'words2'
string3 = 'words3'
var1 = 1
var2 = 2
var3 = 3
print " %r %r %r, why?\n%r and %r math %r" % (string1, string2, string3, var1, var2, var1 + var2)
print "%r = r on a string\n%r = r on a int" % (string1, var3)

x = "what the fuck, %d meh" % 99
word = "this is a word"
no_you = "nou"
print x + word + no_you
print "blah " * 10
print string1 + string2 + string3
print string1 + string2 + string3, # , adds a space to linked strings
print string3 + string2 + string1 # this is on the above line ^^

formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four") # single quote wrapped
print formatter % (True, False, False, True)
print formatter % (
    "I had this thing.", 
	"That you could type up right.",
	"But it didn't sing.", # apostrophe forces double quotes when %r converts
	"So I said goodnight."
)

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print "words words", days
print "more words", months
print """
testing testing testing
blah blah blah
meh meh meh
fuuuuuckkkkk
"""

print "type number", # trailing , keeps input on same line
num1 = raw_input()
print "type number"  #see <--
num2 = raw_input()
print "type letters?",
let1 = raw_input()
print "num: %r\nnum: %r\nletter: %r" % (num1, num2, let1)

randominput = raw_input("type something: ",)
print "random characters bleh %r" % randominput

from sys import argv

script, first, second, third = argv
print "words bleh:", script
print "words bleh:", first
print "words bleh:", second
print "words bleh:", third

from sys import argv
script, username = argv
prompt = '> '
print "user: %s, script: %s" % (username, script)
print " string "
print "prompt %s for (Y / N)" % (username)
yorn1 = raw_input(prompt)
print "prompt %s for (Y / N)" % (username), 
yorn2 = raw_input(prompt)
print "prompt %s for [1, 2 3]" % (username),
yorn3 = raw_input(prompt)
print """
blah blah blah blah
input 1: %r input 2: %r input 3: %r
blah blah blah
""" % (yorn1, yorn2, yorn3)

from sys import argv # import argv module 
script,filename = argv # script name and filename set as arguments
txt = open(filename) # store text from filename as txt
txtclose = 'file 1 closed'
txt_againclose = 'file 2 closed'
print "here's your file %r:" % filename 
print txt.read() # print content read from txt
print "type filename:"
file_again = raw_input() # take user input, set as file_again
txt_again = open(file_again) # store contents of file_again as txt_again
print txt_again.read() # read contents of txt_again and print to screen
txt.close()
txt_again.close()

'''
'''
# close -- Closes the file. Like File->Save.. in your editor.
# read -- Reads the contents of the file, you can assign the result to a variable.
# readline -- Reads just one line of a text file.
# truncate -- Empties the file, watch out if you care about the file.
# write(stuff) -- Writes stuff to the file.
from sys import argv
script, filename = argv

print "erase %r?" % filename
print "Enter to continue"
raw_input('> ')

print "opening %r" % filename
target = open(filename, 'w')

print "Blowing away %r!!" % filename
target.truncate()

print " write 3 new lines:"
line1 = raw_input('> ')
line2 = raw_input('> ')
line3 = raw_input('> ')

print "writing %r" % filename
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "closing %r" % filename
target.close()

from sys import argv
script, filename = argv
def main() :
	print """
	Print File (1)
	Erase File (2)
	Append File (3)
	Overwrite File (4)
	Exit (9)
	"""
	option = raw_input()
	print option
	return option
	
def writeFunc(filename) :

    # open file and re write from start
    target = open(filename, 'w')
    while True:
        n=raw_input('Save? (Y) > ')
        if n.strip()=='Y':
	        break
        target.write(n)
        target.write("\n")
    target.close()
	
def appendFunc(filename) :

    # open file and re write from start
    target = open(filename, 'a')
    while True:
        n=raw_input('Save? (Y) > ')
        if n.strip()=='Y':
	        break
        target.write(n)
        target.write("\n")
    target.close()
	
def eraseFunc(filename) :
	
	# Blow away contents of file
	target = open(filename, 'w')
	target.truncate()
	target.close()

def printFunc(filename) :
	target = open(filename, 'r')
	print target.read()
	target.close()


main(option)
int(option)

print "%d" % option

while True: 
	if opttion==1:
		printFunc(filename)
		break



#writeFunc(filename)
#eraseFunc(filename)
#appendFunc(filename)
#printFunc(filename)











'''





















