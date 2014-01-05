
###############################################################################
#																			  #
# Yazar: Mehmet Selim BILGIN	mselimbilgin[at]yahoo.com					  #
# Tarih: 25 Ocak 2013														  #
# Dosya adi: rasterYukle.py											 		  #
# Aciklama: GeoServer 'a raster veri (TIFF) yuklemek icin kullanilir. 		  #
# Lisans: GPL v2															  #
#																			  #
###############################################################################


import urllib2
import os
import tempfile
import zipfile
import arcpy

katmanAdi = str(arcpy.GetParameterAsText(0))
geoserverRestUrl = str(arcpy.GetParameterAsText(1))
workspaceAdi = str(arcpy.GetParameterAsText(2))
kAdi = str(arcpy.GetParameterAsText(3))
sifre  = str(arcpy.GetParameterAsText(4))

tempKlasor = tempfile.mkdtemp("gecici")

geciciTif = tempKlasor + os.sep + os.path.splitext(katmanAdi)[0] + '.tif'   #Eger katmanAdi uzantiya sahip degilse (ornegin FGDB den geliyorsa) tif uzantisi eklenir. 
arcpy.management.CopyRaster(katmanAdi, geciciTif)							

zipDosya = zipfile.ZipFile((tempKlasor + os.sep + os.path.splitext(os.path.basename(geciciTif))[0] + '.zip'), 'w', zipfile.ZIP_DEFLATED) #zip dosyasinin adi direk olarak tif dosyasindan gelmektedir.
zipDosya.write(geciciTif, os.path.basename(geciciTif)) #zip dosyasi içerisine direkt olarak tif dosyasi eklenir. Klasor yolu eklenmez.
zipDosya.close()

binaryVeri = open(zipDosya.filename, 'rb').read()

def basic_authorization(user, password):
	s = user + ":" + password
	return "Basic " + s.encode("base64").rstrip()
	
url = geoserverRestUrl + '/workspaces/' + workspaceAdi + '/coveragestores/' + os.path.splitext(katmanAdi)[0] + '/file.geotiff'	#Burada ise katmanAdi degiskeni uzanti tasiyorsa uzantisi alinmaz.
istek = urllib2.Request(url)
istek.add_header("Authorization", basic_authorization(kAdi, sifre))
istek.add_header("Content-type", "application/zip")
istek.add_header("Accept", "*/*")
istek.add_data(binaryVeri)
istek.get_method = lambda: 'PUT'
urllib2.urlopen(istek)	
	
	
	
	
	