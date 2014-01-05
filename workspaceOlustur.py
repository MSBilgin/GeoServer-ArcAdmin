
###############################################################################
#																			  #
# Yazar: Mehmet Selim BILGIN	mselimbilgin[at]yahoo.com					  #
# Tarih: 25 Ocak 2013														  #
# Dosya adi: workspaceOlustur.py											  #
# Aciklama: GeoServer uzerinde yeni workspace olusturmak icin kullanilir.     #
# Lisans: GPL v2															  #
#																			  #
###############################################################################

import urllib2


def basic_authorization(user, password):
	s = user + ":" + password
	return "Basic " + s.encode("base64").rstrip()
	
geoserverRestUrl = str(arcpy.GetParameterAsText(0)) + '/workspaces'	
workspaceAdi  = '<workspace><name>' + str(arcpy.GetParameterAsText(1)) +'</name></workspace>'
kAdi = str(arcpy.GetParameterAsText(2))
sifre  = str(arcpy.GetParameterAsText(3))
	
request = urllib2.Request(geoserverRestUrl)
request.add_header("Authorization", basic_authorization(kAdi, sifre))
request.add_header("Content-type", "text/xml")

request.add_header("Accept", "*/*")
request.add_data(workspaceAdi)
response = urllib2.urlopen(request)



