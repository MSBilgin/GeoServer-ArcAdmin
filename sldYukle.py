
###############################################################################
#																			  #
# Yazar: Mehmet Selim BILGIN	mselimbilgin[at]yahoo.com					  #
# Tarih: 15 Ocak 2014														  #
# Dosya adi: sldYukle.py											 		  #
# Aciklama: GeoServer 'a SLD stil dosyasi yuklemek icin kullanilir. 		  #
# Lisans: GPL v2															  #
#																			  #
###############################################################################

import urllib2
import os
import arcpy

sldDosyaYol = str(arcpy.GetParameterAsText(0))
geoserverRestUrl = str(arcpy.GetParameterAsText(1))
kAdi = str(arcpy.GetParameterAsText(2))
sifre  = str(arcpy.GetParameterAsText(3))

girisBasic = 'Basic ' + (kAdi + ':' + sifre).encode('base64').rstrip()	
sldDosya = os.path.basename(sldDosyaYol)
sldAdi = os.path.splitext(sldDosya)[0]
binaryVeri = open(sldDosyaYol ,'rb').read() 
	
	
#Var ise GeoServer 'daki SLD siliniyor.
url = geoserverRestUrl + '/styles/' + sldAdi +'?recurse=true'
istek = urllib2.Request(url)
istek.add_header("Authorization", girisBasic)
istek.get_method = lambda: 'DELETE'
try:
	urllib2.urlopen(istek)
except: 
	pass
  
	
#Yeni SLD olusturuluyor.
url = geoserverRestUrl + '/styles'
istek = urllib2.Request(url)
istek.add_header("Authorization", girisBasic)
istek.add_header("Content-type", "text/xml")
istek.add_header("Accept", "*/*")
istek.add_data('<style><name>' + sldAdi + '</name><filename>' + sldDosya + '</filename></style>')
response = urllib2.urlopen(istek)


#SLD dosyasý GeoServer 'a yukleniyor.
url = geoserverRestUrl + '/styles/' + sldAdi
istek = urllib2.Request(url)
istek.add_header("Authorization", girisBasic)
istek.add_header("Content-type", "application/vnd.ogc.sld+xml")
istek.add_header("Accept", "*/*")
istek.add_data(binaryVeri)
istek.get_method = lambda: 'PUT'
urllib2.urlopen(istek)













