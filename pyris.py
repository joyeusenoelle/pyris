""" Takes an input citation file and formats it as a Refman (RIS) file.
"""

__author__ = "Noëlle Anthony"
__version__ = "0.1.0"

import sys, os

class Citation:
	def __init__(self, filename):
		chunks = filename.split(".")
		if len(chunks) == 1: # has no extension
			self.fn, self.ext = chunks[0], ""
		elif len(chunks) >= 3: # has multiple periods in filename, last one indicates extension
			self.fn, self.ext = ".".join(chunks[:-1]), chunks[-1]
		else: # has one period in filename
			self.fn, self.ext = chunks[0], chunks[1]
		with open(filename, 'r') as f:
			self.contents = f.read()
		self.outfile = self.fn + ".ris"

	def toString(self):
		rstr = "Current infile: {}.{}".format(self.fn, self.ext)
		rstr += "\n"
		rstr += "Current outfile: {}".format(self.outfile)
		return rstr

	def print(self):
		rstr = "Current infile: {}.{}".format(self.fn, self.ext)
		rstr += "\n"
		rstr += "Current outfile: {}".format(self.outfile)
		print(rstr)

def main(filename):
	cite = Citation(filename)

if __name__ == "__main__":
	args = sys.argv()
	if len(args) < 2:
		print("Input file required.")
		os.exit(0)
	main(args[1])