#! /usr/bin/python

import animalgame.json_pb2
import sys

# This function fills in a Person message based on user input.
def fillProtobuf(protobuf):

    protobuf.question = "hello my name is shuixi"


# Main procedure:  Reads the entire address book from a file,
#   adds one person based on user input, then writes it back out to the same
#   file.

# if len(sys.argv) != 2:
#   print "Usage:", sys.argv[0], "ADDRESS_BOOK_FILE"
#   sys.exit(-1)
#
# address_book = addressbook_pb2.AddressBook()

# Read the existing address book.
# try:
#   f = open(sys.argv[1], "rb")
#   address_book.ParseFromString(f.read())
#   f.close()
# except IOError:
#   print sys.argv[1] + ": Could not open file.  Creating a new one."

# Add an address.

# # Write the new address book back to disk.
# f = open(sys.argv[1], "wb")
# f.write(address_book.SerializeToString())
# f.close()
