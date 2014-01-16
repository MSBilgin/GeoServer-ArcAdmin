
###############################################################################
#																			  #
# Yazar: Mehmet Selim BILGIN	mselimbilgin[at]yahoo.com					  #
# Tarih: 15 Ocak 2014														  #
# Dosya adi: workspaceOlustur.py											  #
# Aciklama: GeoServer uzerinde yeni workspace olusturmak icin kullanilir.     #
# Lisans: GPL v2															  #
#																			  #
###############################################################################

import urllib2
import arcpy
	
geoserverRestUrl = str(arcpy.GetParameterAsText(0))
workspaceAdi  = str(arcpy.GetParameterAsText(1))
kAdi = str(arcpy.GetParameterAsText(2))
sifre  = str(arcpy.GetParameterAsText(3))

girisBasic = 'Basic ' + (kAdi + ':' + sifre).encode('base64').rstrip()

veri  = '<workspace><name>' + workspaceAdi + '</name></workspace>'

url = geoserverRestUrl + '/workspaces/'
istek = urllib2.Request(url)
istek.add_header("Authorization", girisBasic)
istek.add_header("Content-type", "text/xml")
istek.add_header("Accept", "*/*")
istek.add_data(veri)
response = urllib2.urlopen(istek)



