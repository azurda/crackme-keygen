import sys

""" author: entdark_
	args: <name> <HWID1> <HWID2> """

if len(sys.argv) < 3:
  print 'Por favor introduce correctamente los argumentos'
  print "args: <name> <HWID1> <HWID2>"
  print "Ejemplo: entdark 873264873264 918209382109382103"
  sys.exit()

s = sys.argv[1]
askii = '%d'*len(s) % tuple(map(ord, s))

part_1 = int(askii[:5])  ^ 0x6b016
part_2 = int(sys.argv[2][:6]) ^ int(sys.argv[3][:6])
part_3 = int(sys.argv[3][:6])

print str(part_1) + "-" + str(part_2) + "-" + str(part_3)
