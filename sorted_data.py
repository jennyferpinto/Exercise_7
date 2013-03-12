from sys import argv
import string

script, filename = argv
dictionary = {}

for line in open(filename, 'r'):
	new_string = line.split(":")
	dictionary[new_string[0]] = new_string[1].rstrip("\n")

sorted_list = [x for x in dictionary.items()]
sorted_list.sort(key=lambda x: x[0]) # sorts by key

for items in sorted_list:
	print "Restaurant %r is rated at %r" % (items[0], items[1])