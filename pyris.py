""" Takes an input citation file and formats it as a Refman (RIS) file.
"""

__author__ = "Noëlle Anthony"
__version__ = "0.1.0"

import sys, os

class Citation:
	def __init__(self):
		self.type = ""
		self.authors = {}
		self.authorcount = 0
		self.title = ""
		self.date = {
			year: "",
			month: "",
			day: "",
			info: ""
		}

	def addAuthor(self, author):
		fmtAuthor = ",".join(list(map(lambda x: x.strip(), author.split(','))))
		self.authors[self.authorcount] = fmtAuthor
		self.authorcount += 1

	def getAuthors(self):
		astr = ""
		for author in self.authors:
			astr += "A1  - {}\n".format(author)
		return astr

	def addType(self, ctype):
		self.type = ctype

	def getType(self):
		return "TY  - {}\n".format(self.type)

	def addTitle(self, ctitle):
		self.title = ctitle

	def getTitle(self):
		return "TI  - {}\n".format(self.title)

	def addDate(self, yr=None, mn=None, dy=None, info=None):
		self.date.year = "" if yr == None else yr
		self.date.month = "" if mn == None else mn
		self.date.day = "" if dy == None else dy
		self.date.info = "" if info == None else info

	def getDate(self):
		return "CY  - {}/{}/{}/{}\n".format(self.date.year, self.date.month, self.date.day, self.date.info)


class CiteList:
	def __init__(self, filename):
		self.citations = {}
		self.idx = 0
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
	cList = CiteList(filename)

if __name__ == "__main__":
	args = sys.argv()
	if len(args) < 2:
		print("Input file required.")
		os.exit(0)
	main(args[1])