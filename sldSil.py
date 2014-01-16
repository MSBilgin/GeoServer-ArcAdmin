
###############################################################################
#																			  #
# Yazar: Mehmet Selim BILGIN	mselimbilgin[at]yahoo.com					  #
# Tarih: 15 Ocak 2014														  #
# Dosya adi: sldSil.py										     	 		  #
# Aciklama: GeoServer 'a SLD stil dosyasi yuklemek icin kullanilir. 		  #
# Lisans: GPL v2															  #
#																			  #
###############################################################################

import urllib2
import arcpy

geoserverRestUrl = str(arcpy.GetParameterAsText(0))
sldAdi = str(arcpy.GetParameterAsText(1))
kAdi = str(arcpy.GetParameterAsText(2))
sifre  = str(arcpy.GetParameterAsText(3))

girisBasic = 'Basic ' + (kAdi + ':' + sifre).encode('base64').rstrip()

url = geoserverRestUrl + '/styles/' + sldAdi + '?recurse=true'
istek = urllib2.Request(url)
istek.add_header("Authorization", girisBasic)
istek.get_method = lambda: 'DELETE'
urllib2.urlopen(istek)