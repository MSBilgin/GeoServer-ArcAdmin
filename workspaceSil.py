
###############################################################################
#																			  #
# Yazar: Mehmet Selim BILGIN	mselimbilgin[at]yahoo.com					  #
# Tarih: 25 Ocak 2013														  #
# Dosya adi: workspaceSil.py											      #
# Aciklama: GeoServer 'da bulunan workspace 'leri silmek icin kullanilir.     #
# Lisans: GPL v2															  #
#																			  #
###############################################################################

import urllib2	

	
geoserverRestUrl = str(arcpy.GetParameterAsText(0))
workspaceAdi = str(arcpy.GetParameterAsText(1))
kAdi = str(arcpy.GetParameterAsText(2))
sifre  = str(arcpy.GetParameterAsText(3))

girisBasic = 'Basic ' + (kAdi + ':' + sifre).encode('base64').rstrip()

url = geoserverRestUrl + '/workspaces/' + workspaceAdi + '?recurse=true'
istek = urllib2.Request(url)
istek.add_header("Authorization", girisBasic)
istek.get_method = lambda: 'DELETE'
urllib2.urlopen(istek)