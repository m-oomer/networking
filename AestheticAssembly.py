import random, string, time, console, sys

logo = """ \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88  \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88  \xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84  \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x93 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88  \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \n\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88    \xe2\x96\x92 \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x93\xe2\x96\x88   \xe2\x96\x80 \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x80 \xe2\x96\x80\xe2\x96\x88  \xe2\x96\x93  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x92 \xe2\x96\x93\xe2\x96\x92\xe2\x96\x93\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x92 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x93\xe2\x96\x88   \xe2\x96\x80 \n\xe2\x96\x91 \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84   \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x93\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88   \xe2\x96\x92\xe2\x96\x93\xe2\x96\x88    \xe2\x96\x84 \xe2\x96\x92 \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91 \xe2\x96\x92\xe2\x96\x91\xe2\x96\x93\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x91\xe2\x96\x84\xe2\x96\x88 \xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88   \n  \xe2\x96\x92   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\xe2\x96\x93\xe2\x96\x92 \xe2\x96\x92\xe2\x96\x92\xe2\x96\x93\xe2\x96\x88  \xe2\x96\x84 \xe2\x96\x92\xe2\x96\x93\xe2\x96\x93\xe2\x96\x84 \xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x91 \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x93 \xe2\x96\x91 \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\xe2\x96\x88\xe2\x96\x84  \xe2\x96\x92\xe2\x96\x93\xe2\x96\x88  \xe2\x96\x84 \n\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92 \xe2\x96\x91  \xe2\x96\x91\xe2\x96\x91\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92 \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x80 \xe2\x96\x91  \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92 \xe2\x96\x91 \xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x93 \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x91\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\n\xe2\x96\x92 \xe2\x96\x92\xe2\x96\x93\xe2\x96\x92 \xe2\x96\x92 \xe2\x96\x91\xe2\x96\x92\xe2\x96\x93\xe2\x96\x92\xe2\x96\x91 \xe2\x96\x91  \xe2\x96\x91\xe2\x96\x91\xe2\x96\x91 \xe2\x96\x92\xe2\x96\x91 \xe2\x96\x91\xe2\x96\x91 \xe2\x96\x91\xe2\x96\x92 \xe2\x96\x92  \xe2\x96\x91  \xe2\x96\x92 \xe2\x96\x91\xe2\x96\x91   \xe2\x96\x91 \xe2\x96\x92\xe2\x96\x93 \xe2\x96\x91\xe2\x96\x92\xe2\x96\x93\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91 \xe2\x96\x92\xe2\x96\x91 \xe2\x96\x91\n\xe2\x96\x91 \xe2\x96\x91\xe2\x96\x92  \xe2\x96\x91 \xe2\x96\x91\xe2\x96\x91\xe2\x96\x92 \xe2\x96\x91      \xe2\x96\x91 \xe2\x96\x91  \xe2\x96\x91  \xe2\x96\x91  \xe2\x96\x92       \xe2\x96\x91      \xe2\x96\x91\xe2\x96\x92 \xe2\x96\x91 \xe2\x96\x92\xe2\x96\x91 \xe2\x96\x91 \xe2\x96\x91  \xe2\x96\x91\n\xe2\x96\x91  \xe2\x96\x91  \xe2\x96\x91  \xe2\x96\x91\xe2\x96\x91          \xe2\x96\x91   \xe2\x96\x91          \xe2\x96\x91        \xe2\x96\x91\xe2\x96\x91   \xe2\x96\x91    \xe2\x96\x91   \n      \xe2\x96\x91              \xe2\x96\x91  \xe2\x96\x91\xe2\x96\x91 \xe2\x96\x91                  \xe2\x96\x91        \xe2\x96\x91  \xe2\x96\x91\n                         \xe2\x96\x91"""

melt = """
\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84 \xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x93\xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x93  \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x93\xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84  \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88     \xe2\x96\x88\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84    \xe2\x96\x88 \n\xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x80\xe2\x96\x88\xe2\x96\x80 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x93\xe2\x96\x88   \xe2\x96\x80 \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92  \xe2\x96\x93  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x92 \xe2\x96\x93\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x80 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x8c\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x93\xe2\x96\x88\xe2\x96\x91 \xe2\x96\x88 \xe2\x96\x91\xe2\x96\x88\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x80\xe2\x96\x88   \xe2\x96\x88 \n\xe2\x96\x93\xe2\x96\x88\xe2\x96\x88    \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88   \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91  \xe2\x96\x92 \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91 \xe2\x96\x92\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x8c\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x91 \xe2\x96\x88 \xe2\x96\x91\xe2\x96\x88\xe2\x96\x93\xe2\x96\x88\xe2\x96\x88  \xe2\x96\x80\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\n\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88    \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x92\xe2\x96\x93\xe2\x96\x88  \xe2\x96\x84 \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91  \xe2\x96\x91 \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x93 \xe2\x96\x91 \xe2\x96\x91\xe2\x96\x93\xe2\x96\x88\xe2\x96\x84   \xe2\x96\x8c\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x91 \xe2\x96\x88 \xe2\x96\x91\xe2\x96\x88\xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92  \xe2\x96\x90\xe2\x96\x8c\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\n\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92   \xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x91\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92 \xe2\x96\x91 \xe2\x96\x91\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x93 \xe2\x96\x91 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x93\xe2\x96\x92\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x93\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91   \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91\n\xe2\x96\x91 \xe2\x96\x92\xe2\x96\x91   \xe2\x96\x91  \xe2\x96\x91\xe2\x96\x91\xe2\x96\x91 \xe2\x96\x92\xe2\x96\x91 \xe2\x96\x91\xe2\x96\x91 \xe2\x96\x92\xe2\x96\x91\xe2\x96\x93  \xe2\x96\x91\xe2\x96\x92 \xe2\x96\x91\xe2\x96\x91    \xe2\x96\x92\xe2\x96\x92\xe2\x96\x93  \xe2\x96\x92 \xe2\x96\x91 \xe2\x96\x92\xe2\x96\x91\xe2\x96\x92\xe2\x96\x91\xe2\x96\x92\xe2\x96\x91 \xe2\x96\x91 \xe2\x96\x93\xe2\x96\x91\xe2\x96\x92 \xe2\x96\x92 \xe2\x96\x91 \xe2\x96\x92\xe2\x96\x91   \xe2\x96\x92 \xe2\x96\x92 \n\xe2\x96\x91  \xe2\x96\x91      \xe2\x96\x91 \xe2\x96\x91 \xe2\x96\x91  \xe2\x96\x91\xe2\x96\x91 \xe2\x96\x91 \xe2\x96\x92  \xe2\x96\x91  \xe2\x96\x91     \xe2\x96\x91 \xe2\x96\x92  \xe2\x96\x92   \xe2\x96\x91 \xe2\x96\x92 \xe2\x96\x92\xe2\x96\x91   \xe2\x96\x92 \xe2\x96\x91 \xe2\x96\x91 \xe2\x96\x91 \xe2\x96\x91\xe2\x96\x91   \xe2\x96\x91 \xe2\x96\x92\xe2\x96\x91\n\xe2\x96\x91      \xe2\x96\x91      \xe2\x96\x91     \xe2\x96\x91 \xe2\x96\x91   \xe2\x96\x91       \xe2\x96\x91 \xe2\x96\x91  \xe2\x96\x91 \xe2\x96\x91 \xe2\x96\x91 \xe2\x96\x91 \xe2\x96\x92    \xe2\x96\x91   \xe2\x96\x91    \xe2\x96\x91   \xe2\x96\x91 \xe2\x96\x91 \n       \xe2\x96\x91      \xe2\x96\x91  \xe2\x96\x91    \xe2\x96\x91  \xe2\x96\x91          \xe2\x96\x91        \xe2\x96\x91 \xe2\x96\x91      \xe2\x96\x91            \xe2\x96\x91 \n                                  \xe2\x96\x91
"""

def rand_hex():
	return random.choice(string.hexdigits.upper())+random.choice(string.hexdigits.upper())

def rand_point():
	s = "0x"
	while len(s) < 11:
		s += rand_hex()
		if random.randint(0,2) == 0:
			s += s[(len(s)-1):]
	return s[:11]

def rand_line(depth=1):
	line = ""
	l = rand_point()
	while line.count(" ") < depth:
		line += rand_point()
		line += " "
	return line

def rand_out(rate=0.05,t=20):
	for _ in range(t*2):
		r = random.randint(0,3)
		for i in range(t):
			b = rand_line(r)
			if r == 0:
				for _ in range(12):
					b += rand_hex() + " "
			if r == 1:
				for _ in range(8):
					b += rand_hex() + " "
			if r == 2:
				for _ in range(4):
					b += rand_hex() + " "
			if True:
				for _ in range(6):
					if random.randint(0,1) == 0:
						b += "."
					else:
						b += random.choice(string.printable[:92])
			if len(b) > 5:
				print b
			time.sleep(rate)

def typeit(msg):
	for _ in msg:
		sys.stdout.write(_)
		time.sleep(0.05)

def seg1():
	seg = ""
	while len(seg) < random.randint(12,22):
		seg += "".join(random.sample(string.digits+string.ascii_lowercase*2,random.randint(2,8)))+","+"*"*random.randint(0,3)+" "
	seg = seg.replace("*","")
	while len(seg) < 21:
		seg += " "
	return seg[:20]+" ;"

class pointer():
	def next(self):
		p = hex(self.i)[2:].zfill(len(str(self.i)))
		s = "0x"
		p = s+"0"*(8-len(p))+p
		self.i += 1
		return p
		
	def __init__(self,start=0):
		self.i = start

def seg2():
	seg = ""
	opt = [
		"".join(random.sample(string.ascii_lowercase*3,random.randint(4,6)))+" = ",
		"."+"".join(random.sample(string.ascii_uppercase*3,random.randint(4,6)))+" "*4,
		"."+"".join(random.sample(string.ascii_uppercase*3,random.randint(4,6)))+" "*4,
		"."+"".join(random.sample(string.ascii_uppercase*3,random.randint(4,6)))+" "*4,
		]
	while len(seg) < random.randint(18,30):
		seg += rand_hex()+" "
	seg += rand_hex()
	while len(seg) < 32:
		seg += " "
	seg = seg[:32]
	sg = random.choice(opt)
	while len(sg) < 15:
		sg += " "
	return sg+seg
	

def spectre():
	time.sleep(1)
	console.set_font("Menlo",10)
	console.set_color(0.9,0,0)
	print "\n"
	print logo
	print
	time.sleep(2.5)
	console.set_color()
	console.set_font("Menlo",7)
	pr = pointer(47839215)
	lc = False
	for _ in range(500*2):
		if lc:
			console.set_color()
			lc = False
		if not random.randint(0,35):
			console.set_color(1,0,0)
			lc = True
		o1 = pr.next()+"  "+seg1()+" "+seg2()
		o2 = pr.next()+" "*25+seg2()
		o3 = pr.next()
		print random.choice([o1,o1,o1,o2,o2,o3])
		if lc:
			time.sleep(0.02)
		time.sleep(0.01)
	
	console.set_font("Menlo",8.62)
	console.set_color(0.9,0,0)
	print "\n"
	for _ in melt.split("\n"):
		print _
		time.sleep(0.01)
	time.sleep(2.5)
	console.set_color()
	console.set_font("Menlo",14)
	typeit("Leaking Memory "+"."*18+" [  OK  ]")
	pr = pointer(47839215)
	print
	for _ in range(5000):
		sys.stdout.write("\rMemory Address "+"."*12+" [ "+pr.next()+" ]")
		time.sleep(0.01)
	
	

spectre()
