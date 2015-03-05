
init = []
final = []

a = float(raw_input("Enter the grain parameter for hexagonal grains\n"))

for i in range(7):
	for j in range(4):
		init = init + [((10.0/50)*(a + a*(3**0.5)*i), (5.0/50)*(a + 3*j*a),j+4*i+1,1)]
		init = init + [((10.0/50)*(a - (3**0.5)*a/2 + a*(3**0.5)*i), (5.0/50)*(a + a/2 + 3*j*a),j+4*i+1,2)]
		init = init + [((10.0/50)*(a - (3**0.5)*a/2 + a*(3**0.5)*i),(5.0/50)*(a + 3*a/2 + 3*j*a),j+4*i+1,3)]
		init = init + [((10.0/50)*(a + a*(3**0.5)*i), (5.0/50)*(a + 2*a + 3*j*a),j+4*i+1,4)]
		


for i in init:
	final = final + [(i[0]*(5.0/10) ,i[1]*(10.0/5) ,i[2],i[3])]



text_file = open("ebsd1.rtf","w")
text_file.write('\n'.join('%s %s %s %s' % x for x in init))
text_file.close()

text_file = open("ebsd2.rtf","w")
text_file.write('\n'.join('%s %s %s %s' % x for x in final))
text_file.close()

