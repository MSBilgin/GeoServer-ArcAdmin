
###############################################################################
#																			  #
# Yazar: Mehmet Selim BILGIN	mselimbilgin[at]yahoo.com					  #
# Tarih: 15 Ocak 2014														  #
# Dosya adi: sldUygula.py											 		  #
# Aciklama: GeoServer 'daki katmanýn stilin deðiþtirmek icin kullanilir. 	  #
# Lisans: GPL v2															  #
#																			  #
###############################################################################

import urllib2
import arcpy

geoserverRestUrl = str(arcpy.GetParameterAsText(0))
katmanAdi = str(arcpy.GetParameterAsText(1))
sldAdi = str(arcpy.GetParameterAsText(2))
kAdi = str(arcpy.GetParameterAsText(3))
sifre  = str(arcpy.GetParameterAsText(4))

girisBasic = 'Basic ' + (kAdi + ':' + sifre).encode('base64').rstrip()

url = geoserverRestUrl + '/layers/' + katmanAdi
istek = urllib2.Request(url)
istek.add_header("Authorization", girisBasic)
istek.add_header("Content-type", "text/xml")
istek.add_header("Accept", "*/*")
istek.add_data('<layer><defaultStyle><name>' + sldAdi + '</name></defaultStyle></layer>')
istek.get_method = lambda: 'PUT'
response = urllib2.urlopen(istek)

