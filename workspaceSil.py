
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

def basic_authorization(user, password):
	s = user + ":" + password
	return "Basic " + s.encode("base64").rstrip()
	
geoserverRestUrl = str(arcpy.GetParameterAsText(0))
workspaceAdi = str(arcpy.GetParameterAsText(1))
kAdi = str(arcpy.GetParameterAsText(2))
sifre  = str(arcpy.GetParameterAsText(3))

istek = urllib2.Request(geoserverRestUrl + '/workspaces/' + workspaceAdi + '?recurse=true')
istek.add_header("Authorization", basic_authorization("admin", "123"))
istek.get_method = lambda: 'DELETE'
urllib2.urlopen(istek)