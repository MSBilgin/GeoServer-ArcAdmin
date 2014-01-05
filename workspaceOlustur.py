
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
	
geoserverRestUrl = str(arcpy.GetParameterAsText(0)) + '/workspaces'	
workspaceAdi  = str(arcpy.GetParameterAsText(1))
kAdi = str(arcpy.GetParameterAsText(2))
sifre  = str(arcpy.GetParameterAsText(3))

girisBasic = 'Basic ' + (kAdi + ':' + sifre).encode('base64').rstrip()

veri  = '<workspace><name>' + workspaceAdi + '</name></workspace>'
	
request = urllib2.Request(geoserverRestUrl)
request.add_header("Authorization", girisBasic)
request.add_header("Content-type", "text/xml")
request.add_header("Accept", "*/*")
request.add_data(veri)
response = urllib2.urlopen(request)



