
###################################################################################################
#																								  #
# Yazar: Mehmet Selim BILGIN	mselimbilgin[at]yahoo.com					 					  #
# Tarih: 25 Ocak 2013																			  #
# Dosya adi: zipYukle.py											  							  #
# Aciklama: GeoServer 'a ZIP olarak arsivlenmis vektor veri (Shapefile) yuklemek icin kullanilir. #
# Lisans: GPL v2																				  #
#																								  #
###################################################################################################

import urllib2
import arcpy
	

zipDosya = str(arcpy.GetParameterAsText(0))	
geoserverRestUrl = str(arcpy.GetParameterAsText(1))
workspaceAdi = str(arcpy.GetParameterAsText(2))
kAdi = str(arcpy.GetParameterAsText(3))
sifre  = str(arcpy.GetParameterAsText(4))

binaryVeri = open(zipDosya, 'rb').read()
girisBasic = 'Basic ' + (kAdi + ':' + sifre).encode('base64').rstrip()

url = geoserverRestUrl + '/workspaces/' + workspaceAdi + '/datastores/' + os.path.basename(zipDosya)[:-4] + '/file.shp'
istek = urllib2.Request(url)
istek.add_header("Authorization", girisBasic)
istek.add_header("Content-type", "application/zip")
istek.add_header("Accept", "*/*")
istek.add_data(binaryVeri)
istek.get_method = lambda: 'PUT'
urllib2.urlopen(istek)