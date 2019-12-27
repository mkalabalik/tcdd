import mechanicalsoup   # En önemli modülümüz
import time             # Süre ölçmek için
import sys              # Argv ve Çıkış yapmak 

def tarayıcı_olustur():
    return mechanicalsoup.StatefulBrowser()

def cık():
    print("Kapanıyor.....")
    time.sleep(1)
    sys.exit()

def hata_yaz():
    print("\n\n***************************************")
    print("\n***\nhata tipi")
    print(sys.exc_info()[0])
    print("\n***\nhata değeri")
    print(sys.exc_info()[1])
    print("\n***\ntraceback")
    print(sys.exc_info()[2])
    print("***************************************\n\n")


def main():

    
    #tarayıcı.open(URL)
    tarayıcı.open(URL)
    #print("sonuc tipi = " + str(type(sonuc)))
    #print("dir response = ")
    #print(dir(sonuc))
    
    print("Sayfa okundu")
    #print(tarayıcı.get_current_page())

    tarayıcı.select_form('form[id="biletAramaForm"]')
    #print(dir(tarayıcı.select_form('form[id="biletAramaForm"]')))

    #tarayıcı.get_current_form().print_summary()

    tarayıcı["nereden"] = nereden
    tarayıcı["nereye"]  = nereye
    tarayıcı["trCalGid_input"]  = gidisTarihi
    tarayıcı["tipradioIslemTipi"] = 1
    #tarayıcı.get_current_form().print_summary()
    
    #tarayıcı.launch_browser()
    
    response = tarayıcı.submit_selected()
    #print(type(response))
    #print(response.text)
    
    #tarayıcı.get_current_page().find_all('tr')
    page = tarayıcı.get_current_page()
    #print(type(page))
    tablo = page.find('tbody', id = "mainTabView:gidisSeferTablosu_data")
    #print(type(tablo))

    #seferleri bul
    seferler = tablo.find_all("tr", role="row")
    #tarayıcı.launch_browser()
    
##    for sefer in seferler: # saatleri bul
##        saat = sefer.find('td', class_ = "whiteSortIcon").find('span').text
##        #koltuklar = sefer.find("div", class_ = "ui-selectonemenu ui-widget ui-state-default ui-corner-all ui-helper-clearfix vagonTipiCombo").text
##        #koltuklar = page.find_all("div", id="j_idt82")
##        #print(koltuklar)
##        #time.sleep(100)
##        yeniBilgiler[saat] = ""
####        if bilgiler.get(saat):
####            if bilgiler[saat] == yeniBilgiler[saat]:
####                continue
####            else:
####                if saat=="19:28":
####                    print("\a")
####                print("eski bilgiler")
####                print(saat)
####                print(bilgiler[saat])
####                print("yeni bilgiler")
####                print(yeniBilgiler[saat])
####                print("*************************************************************************************************")
####                print("Saat {}'de değişiklik var \n {}".format(saat, koltuklar))
####                print("*************************************************************************************************")                
####                bilgiler[saat] = yeniBilgiler[saat]
####        else:
####            bilgiler[saat] = yeniBilgiler[saat]

    for seferNo, sefer in enumerate(seferler):
        #Sefer saatlerini bul
        saat = sefer.find('td', class_ = "whiteSortIcon").find('span').text

        #Seferlerin doluluk durumlarını bul
        seferUygunluk = page.find("div", id="mainTabView:gidisSeferTablosu:{}:seferBilgileriDataList:0:j_idt82".format(seferNo)).text

        #Koltukları sayılarını bul
        vagonlar = page.find("div", id="mainTabView:gidisSeferTablosu:{}:j_idt105:0:somVagonTipiGidis1_panel".format(seferNo)).find_all("li")
        
        for vagon in vagonlar:
            print(vagon.text)
            koltuklar = {}
            
            #Text'i parse ediyoruz
            vagonAdi, koltukSayisi = vagon.text.rsplit(" ", 1)
            koltukSayisi = int(koltukSayisi[1:-1])
            koltuklar[vagonAdi] = koltukSayisi
        
        #Bilgileri sözlükte tut
        yeniBilgiler[saat] = [seferUygunluk, koltuklar]
        print("p")
        print(yeniBilgiler)
        sys.exit() ##sözlüğü düzenle!!!
##        if bilgiler.get(saat):
##            if bilgiler[saat] == yeniBilgiler[saat]:
##                continue
##            else:
##                if saat=="19:28":
##                    print("\a")
##                print("eski bilgiler")
##                print(saat)
##                print(bilgiler[saat])
##                print("yeni bilgiler")
##                print(yeniBilgiler[saat])
##                print("*************************************************************************************************")
##                print("Saat {}'de değişiklik var \n {}".format(saat, koltuklar))
##                print("*************************************************************************************************")                
##                bilgiler[saat] = yeniBilgiler[saat]
##        else:
##            bilgiler[saat] = yeniBilgiler[saat]


    
    seferUygunluk = []
    for seferNo in range(len(seferler)): # koltukları bul
        seferUygunluk.append(page.find("div", id="mainTabView:gidisSeferTablosu:{}:seferBilgileriDataList:0:j_idt82".format(seferNo)).text)
        print(seferUygunluk)
        
    #cık()
if __name__ == "__main__":
    URL = "https://ebilet.tcddtasimacilik.gov.tr/"
##    print('Adana','Adapazarı','Adatepe (Pingen)','Adnanmenderes Havaalanı','Afyon A.Çetinkaya','Ahatlı','Ahmetler',
##          'Ahmetli','Akgedik','Akhisar','Aksakal','Akyaka','Akyamaç','Akyarma','Akçadağ','Akçagöze','Akçakale',
##          'Akçakoyunlu','Akçamağara','Akşehir','Alaybey','Alayunt','Alaşehir','Alifuatpaşa','Alpu','Altay','Altunkent',
##          'Altınbaşak','Alvar','Alöve','Amasya','Ambar','Ankara Gar','Araplı','Argıthan','Arifiye','Artova','Arıkbaşı',
##          'Arıkören','Atalar','Atasanayi','Atma','Atça','Avşar','Aydın','Aydıntepe','Ayran','Ayrancı','Ayvaz','Azot',
##          'Azot K','Ağapınar','Ağaver','Aşit','Aşkale','Bahçe','Bahçeli (Km.755+290 S)','Bahçetepe','Bahçeşehir',
##          'Bahçıvanova','Bakacakkadı','Bakır','Balabanlı','Ballıhoca','Balmahmut','Balıkesir','Balıköy','Balışıh',
##          'Banaz','Bandırma Şehir','Baraklı','Baskil','Batman','Battalgazi','Bayraklı','Bayramlı','Bayındır',
##          'Bayındır MYO','Bağderesi durağı','Bağlar','Bağıştaş','Başgedik','Başkimse','Bedirli','Bekdiğin','Bekçiler',
##          'Belediye Evleri','Belediyeevleri','Belemedik','Bereket','Beyce','Beydeğirmeni','Beyhan','Beyköy','Beylikköprü',
##          'Beylikova','Beyoğlu','Beytiköy','Beşiri','Beşköprü','Beşköprü Durağı','Bilecik','Bilecik YHT','Bismil','Biçer',
##          'Biçerova','Bor','Bostankaya','Bozanönü','Bozarmut','Bozkurt','Bozüyük','Bozüyük YHT','Boğazköprü',
##          'Boğazköprü Müselles','Buharkent','Bulgurlu','Burdur','Buzluk','Buğra','Böğecik','Büyükderbent','Büyükçobanlar',
##          'Caferli','Candoğan','Cankurtaran','Cebeciler','Cebesoy','Cevizli','Ceyhan','Ceylanpınar','Coşkunoğulları',
##          'Cürek','Dada','Dazkırı','Dazlak','Deliklikaya','Demirciköy','Demirciören','Demirdağ','Demiriz','Demirkapı',
##          'Demirköprü','Demirköprü','Demirli','Demirlibahçe durağı','Demiryurt','Demirözü','Denizli','Derebaşı',
##          'Derecikören','Derince Liman','Derince YHT','Develiköy','Değirmenözü','Değirmisaz','Dibekli','Dikbıyık',
##          'Dinar','Divriği','Diyarbakır','Doyranlı','Doğanca','Doğanşehir','Doğukapı','Dumlupınar','Durak','Dursunbey',
##          'Dörtyol','Döğer','Dülük','ERYAMAN YHT','Edirne Şehir','Egekent-1','Egekent-2','Ekerek','Ekinova','Elazığ',
##          'Elifli','Elifoğlu','Elmadağ','Elmalı','Elvankent duragı','Emiralem','Emirler','Enveriye',
##          'Enveriye (Alayunt BM)','Enveriye (Haydarpaşa BM)','Erbaş','Erbeyli','Ereğli','Ergani','Eriç','Erzincan',
##          'Erzurum','Erçek','Eskişehir','Evciler','Eğirdir','Eşme','Fatih','Fehimli','Feneryolu','Fevzipaşa','Filyos',
##          'Florya','Furunlu','Fırat','Gazellidere','Gazi Orer','Gaziantep','Gaziemir','Gazlıgöl','Gebze','Gelemen','Genç',
##          'Germencik','Germiyan','Geyik','Gezin','Goncalı','Goncalı (Denizli BM)','Goncalı (Sütlaç BM)','Goncalı Müselles',
##          'Goçar','Göbü','Gökbayır','Gökdere','Gökçayır','Gökçeali','Gökçedağ','Gökçekısık','Gökçeler','Gökçeören',
##          'Gölbaşı Gar','Gölceğiz','Gölcük','Göltaş','Gölçayır','Gözmen','Gözpınarı','Göztepe','Göçenli','Göçentaşı',
##          'Gücük','Güdeli','Güllübağ','Gültepe','Gülveren durağı','Gümüş','Gümüşgün','Gümüşçayı','Güneyköy D','Güneş',
##          'Gürgür','Gürpınar','Gürpınar','Güzelyalı','Güzelyurt','Güşhane','Hacıkırı','Hacırahmanlı','Halispaşa',
##          'Halkapınar','Hamzalı','Hanlı','Harmanören','Harput İstasyon','Hasanbey','Hasankale','Hasanoğlan','Hasançelebi',
##          'Hatundere','Havza','Haydarlı Sayding','Haydarpaşa','Haydarpaşa Liman','Hayrettin','Hekimhan','Hereke YHT','Hilal',
##          'Himmetdede','Hodan','Horasan','Horozköy','Horozluhan YHT','Horsunlu','Huzurkent','Hüyük','Hızırilyas','Ibrıcak',
##          'Ilgın','Ilıca','Irgıllı','Irmak','Islahiye','Isparta','Işıkveren','Kababürük','Kabakça','Kabazlı','Kadılı',
##          'Kadınhan','Kaklık','Kalkancık','Kalkım','Kalın','Kalın Köyü','Kanarya','Kandilli','Kanlıca','Kapaklar','Kapaklı',
##          'Kapuz','Kapıdere İstasyonu','Karaali','Karaali','Karaağaçlı','Karabasamak','Karabük','Karacailyas','Karagözler',
##          'Karaisalıbucağı','Karakuyu','Karaköy','Karalar','Karalıköy','Karaman','Karaosman','Karapınar','Karasar','Karasenir',
##          'Karasu','Karaurgan','Karaçuha','Karaözü','Karpuzlu','Kars','Karşıyaka','Kavak','Kavaklı','Kavaklı','Kavaklıdere',
##          'Kayabeyli','Kayapınar','Kayaçivi','Kayaş','Kaynarca','Kayseri','Kayıkçılar','Kayışlar','Kazanpınar','Kazköy',
##          'Kazlıçeşme','Kazlıçeşme MR','Kaşınhan','Kelebek','Keleş','Kemah','Kemaliye Çaltı','Kemerhisar','Kerimbey',
##          'Kesikköprü','Kesiktaş','Keçiborlu','Kilimli','Killik','Kirazlık','Kirazlıyalı','Kiremithane','Kiremithane',
##          'Kireç','Km.148+500','Km.156 Durak','Km.171+000','Km.176+000','Km.286+250','Km.286+500','Km.41+500','Km.54+000',
##          'Km.638+907','Km.746+840','Kocaağa','Kocamustafapaşa','Kocatepe','Konak','Konak','Konaklar','Konakoba','Konar',
##          'Konya','Konya YHT','Koruma','Kozdere','Kozpınarı','Koşu Durağı','Kuleönü','Kumkapı','Kumlu Sayding','Kunduz',
##          'Kurbağalı','Kurfallı','Kurnaz','Kurt','Kurtalan','Kurtuluş durağı','Kurudere','Kuruçeşme','Kuyucak','Kuyumcular',
##          'Kuzudere','Kuşcenneti','Kuşsarayı','Kölemen','Köprüağzı','Köprüköy','Köprüören','Köroğlu','Köseali','Köseköy',
##          'Köseköy YHT','Köstence durağı','Köşk','Küpeli','Kürk','Kütahya','Küçükyalı','Küçükçekmece','Kılıçlar','Kıradağ',
##          'Kırcasalih','Kırkağaç','Kırkpınar','Kırıkkale','Kırıkçayır','Kızılca','Kızılcaköy','Kızılinler','Kızılpınar',
##          'Kızıltoprak','Lale YHT','Maden','Mahmudiye','Mahmutlar','Malatya','Malıköy','Mamure','Mandıra','Manisa',
##          'Marşandiz (Banliyö)','Marşandiz Gar (ANKARA)','Mavişehir','Maşukiye','Melik','Menekşe','Menemen',
##          'Menemen (Aliağa BM)','Menemen (Manisa BM)','Menemen Müselles','Menteşe','Mercan','Merci','Mersin','Meydanekbez',
##          'Mezitler','Mezraa','Meşelidüz','Mithatpaşa','Motor Fabrikası durağı','Muradiye','Murat','Muratlı  (Muratlı BM)',
##          'Muratlı (Kapıkule BM)','Muratlı (Tekirdağ BM)','Muslu','Mustafa Kemal Paşa','Mustafabeyli','Muş','Müsellimköy',
##          'Naldöken','Nallıkaya','Narlı Gar','Nazilli','Nenek','Nergiz','Niğde','Nohutova','Nurdağ','Nurkavak','Nusaybin',
##          'Nusrat','Okçugöl','Organize D.','Ortaklar','Osmancık','Osmaneli','Osmangazi','Osmaniye','Oturak','Otuzikievler Durağı',
##          'Ovacık','Ovaköy','Ovasaray','Oymapınar','Palu','Pancar','Pazarcık İstasyonu','Paşalı','Piribeyler','Pirinçlik',
##          'Piyadeler','Polatlı','Polatlı YHT','Porsuk','Poyraz','Pozantı','Pınarlı','Razi','Regülatör','Reşadiye',
##          'Sabuncupınar','Salat','Salhane','Salihli','Sallar','Saltukova','Saluca','Samsun','Samsun Liman','Samurçay',
##          'Sanayi','Sandal','Sandıklı','Sapanca','Sarayköy','Sarayönü','Sarfaklar','Sarmaşık','Sarnıç','Sarsap','Saruhanlı',
##          'Sarıdemir','Sarıkamış','Sarıkent','Sarılar','Sarımsaklı','Sarıoğlan','Sarıçayır','Savaştepe','Sayding - 1',
##          'Sayding - 2','Sayding - 3','Sayding - 4','Sayding - 5','Sayding Km.19+007','Sazlıköy','Sazlımalkoç','Sazpınarı',
##          'Sazılar','Saçakköy','Sağlık','Sefercik','Sekili','Selim','Selimağa','Selçuk','Semt Garajı','Seramik','Seraserli',
##          'Serçehan','Sevindik','Seydili','Seyithasan','Seyitler','Seyitömer','Sincan','Sindirler','Sivas','Sivrice',
##          'Solhan','Soma','Soğucak','Soğuksu','Sudurağı','Sultandağı','Sultanhisar','Suluova','Sundurlu','Susurluk','Suveren',
##          'Suçatı','Söke','Söylemez','Söğütlü Durak','Süleymanlı','Süngütaşı','Sünnetçiler','Süreyyaplajı','Sütlaç','Sıcaksu',
##          'Sığırcı','Tahtaköprü','Tanyeri','Tarsus','Tatbekirli','Tatvan Gar','Tatvan İsk','Tavşanlı','Tayyakadın','Taşağıl',
##          'Taşdemir','Taşkesik','Taşlıdere','Taşoluk','Tecer','Tekeköy','Tekin','Tekirdağ Liman','Tekkeköy','Temelli',
##          'Tepeköy','Tersane','Tire','Topaç','Topdağı','Topkaya durağı','Toprakkale','Toprakkale (Fevzipaşa BM)',
##          'Toprakkale (İskenderun BM)','Toprakkale Müselles','Topulyurdu','Topçu','Torbalı','Toruntepe','Tosunali','Tunçbilek',
##          'Turgutlu','Turhal','Türkali','Türkmentepe','Türkobası','Türkoğlu','Tütünçiftlik','Tınaztepe','Tırmıl','Ulam','Ulaş',
##          'Ulaş D','Ulugüney','Uluköy','Ulukışla','Uluova','Umurlu','Urganlı','Uzunkum','Uçak','Uğur','Uşak','Van Gar',
##          'Van İsk','Velimeşe','Vezirhan','Yahniler','Yahşiler','Yakaköy','Yakapınar','Yamukören','Yanarsu','Yanıkköy',
##          'Yaraşlı','Yarbaşı','Yarımca YHT','Yassıca','Yayla','Yaylıca','Yazlak','Yağlı','Yedikule','Yekabat','Yeni Karasar',
##          'Yenibaşak','Yenice','Yenidoğan','Yenifakılı','Yenikangal','Yeniköy','Yeniköy D','Yenimahalle','Yeniterminal Durağı',
##          'Yeniçubuk','Yerköy','Yeşilbayır','Yeşildağ','Yeşilhisar','Yeşilhüyük','Yeşilkavak','Yeşilköy','Yeşilyenice',
##          'Yeşilyurt','Yeşilyurt','Yolçatı','Yoncalıhamamı','Yunus','Yunusemre','Yıldırımkemal','Yıldızeli','Zenginova',
##          'Zeytinburnu','Zile','Ziraat  Durağı','Ziraidonatım','Ziveyir','Zonguldak','Çadırkaya','Çakaldere','Çakmak',
##          'Çakşur','Çalıköy','Çamlaraltı','Çamlık','Çandır','Çankırı','Çapalı','Çardak','Çardakbaşı','Çarşamba','Çatalağzı',
##          'Çavundur','Çavuşcugöl','Çay','Çaybağı','Çaycuma','Çayırdere','Çayırova','Çağdariç','Çeken','Çelik Sayding',
##          'Çeltek','Çerikli','Çerkeş','Çetinkaya','Çetinkaya (Doğukapı BM)','Çetinkaya (Malatya BM)','Çetinkaya Müselles',
##          'Çiftehan','Çimenova','Çivril','Çizözü','Çiçekli','Çiğli','Çobanbey','Çobanhasan','Çobanisa','Çukurhüseyin',
##          'Çumra','Çöltepe','Çöğürler','Çınarlı','Ödemiş Gar','Ödemiş Şehir','Ömerköy','Ömerköy','Ömerli','Öncüler','Özden',
##          'Üreğil durağı','Üsküdar MR','Üzerlik','Üçburgu','İdealtepe','İhsaniye','İhsanlı','İliç','İlkkurşun','İlören',
##          'İnay','İnağzı','İnceköy','İncesu','İncesu(Kayseri)','İnceğiz','İncirlik','İncirliova','İnkılap','İnönü','İsabeyli',
##          'İsdemir','İshakçelebi','İskenderun','İsmailbey','İstanbul(Bakırköy)','İstanbul(Bostancı)','İstanbul(Halkalı)',
##          'İstanbul(Pendik)','İstanbul(Sğtlü.Çeşme)','İzmir (Alsancak)','İzmir (Basmane)','İzmit YHT','İzzettin','İçme',
##          'İğciler','Şahnalar','Şakirpaşa','Şarkışla','Şefaatli','Şefkat','Şehitlik','Şerbettar','Şerefoğlu','Şirinyalı','Şirinyer',
##          sep="~")
    nereden = "ERYAMAN YHT" #input("Nereden?(ERYAMAN YHT) : ") #"ERYAMAN YHT"
    nereye  = "Eskişehir" #input("Nereye?(Eskişehir) : ") #"Eskişehir"
    gidisTarihi = "31.12.2019" #input("Ne Zaman?(gg.aa.yyyy) : ") #"13.12.2019"

    tarayıcı = tarayıcı_olustur()
    #print("tarayıcı'nın tipi")
    #print(type(tarayıcı))
    print("Tarayıcı oluşturuldu")
    
    bilgiler = {}
    yeniBilgiler =  {}
    while True:
        time.sleep(1)
        try:
            main()
        except:
            hata_yaz()
            #print("Bilgiler okunurken hata oldu!")
            #print("Devam edilemiyor")
            print("hata")
            sys.exit()
        time.sleep(2)
