
###############################################################################
#																			  #
# Yazar: Mehmet Selim BILGIN	mselimbilgin[at]yahoo.com					  #
# Tarih: 25 Ocak 2013														  #
# Dosya adi: coveragestoreSil.py											  #
# Aciklama: GeoServer 'da bulunan Coverage Store lari silmek icin kullanilir. #
# Lisans: GPL v2															  #
#																			  #
###############################################################################


import urllib2


geoserverRestUrl = str(arcpy.GetParameterAsText(0))
workspaceAdi = str(arcpy.GetParameterAsText(1))
coverageAdi = str(arcpy.GetParameterAsText(2))
kAdi = str(arcpy.GetParameterAsText(3))
sifre  = str(arcpy.GetParameterAsText(4))

girisBasic = 'Basic ' + (kAdi + ':' + sifre).encode('base64').rstrip()

url = geoserverRestUrl + '/workspaces/' + workspaceAdi + '/coveragestores/' + coverageAdi + '?recurse=true'
istek = urllib2.Request(url)
istek.add_header("Authorization", girisBasic)
istek.get_method = lambda: 'DELETE'
urllib2.urlopen(istek)