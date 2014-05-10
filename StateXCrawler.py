import re
import urllib

web =  raw_input("pega aqui la Url: ")
emails = []
patron= re.compile('''href=["'](.[^"']+)["']''')
patron2= re.compile("[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+.[a-zA-Z0-9_.]+")
busqueda = re.findall(patron, urllib.urlopen(web).read())
busqueda2= re.findall(patron2,urllib.urlopen(web).read())
emails.append(busqueda2)
d1 =  str(busqueda2)
ListaEmails = open('correos.txt','a+')
ListaEmails.write("--> "+ d1 +" <--")
ListaEmails.close()
for i in busqueda:
	 busqueda3 = re.findall(patron2,urllib.urlopen(i).read())
	 emails.append(busqueda3)
	 d2 =  str(busqueda3)
	 ListaEmails = open('correos.txt','a+')
	 ListaEmails.write("--> "+ d2 +" <--")
	 ListaEmails.close()
	 busqueda4 = re.findall(patron, urllib.urlopen(i).read())
	 for e in busqueda4:
	 	 busqueda5 = re.findall(patron2,urllib.urlopen(e).read())
	 	 emails.append(busqueda5)
	 	 d3 =  str(busqueda5)
	 	 ListaEmails = open('correos.txt','a+')
	 	 ListaEmails.write("--> "+ d3 +" <--")
	 	 ListaEmails.close()
print "URls Guardadas con Exito."