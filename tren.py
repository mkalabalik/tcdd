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

    #tarayıcı.get_current_form().print_summary()
    #tarayıcı.launch_browser()

    response = tarayıcı.submit_selected()
    #print(type(response))
    #print(response.text)
    
    #tarayıcı.get_current_page().find_all('tr')
    page = tarayıcı.get_current_page()
    tablo = page.find('tbody', id = "mainTabView:gidisSeferTablosu_data")
    #print(type(tablo))
    seferler = tablo.find_all("tr", role="row")
    for sefer in seferler:
        saat = sefer.find('td', class_ = "whiteSortIcon").find('span').text
        koltuklar = sefer.find("div", class_ = "ui-selectonemenu ui-widget ui-state-default ui-corner-all ui-helper-clearfix vagonTipiCombo").text
        yeniBilgiler[saat] = koltuklar
        if bilgiler.get(saat):
            if bilgiler[saat] == yeniBilgiler[saat]:
                continue
            else:
                print("eski bilgiler")
                print(saat)
                print(bilgiler[saat])
                print("yeni bilgiler")
                print(yeniBilgiler[saat])
                print("*************************************************************************************************")
                print("Saat {}'de değişiklik var \n {}".format(saat, koltuklar))
                print("*************************************************************************************************")                
                bilgiler[saat] = yeniBilgiler[saat]
        else:
            bilgiler[saat] = yeniBilgiler[saat]
    #cık()
if __name__ == "__main__":
    URL = "https://ebilet.tcddtasimacilik.gov.tr/"
    nereden = "Ankara Gar"
    nereye  = "İstanbul(Pendik)"
    gidisTarihi = "26.07.2019"

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
            #hata_yaz()
            #print("Bilgiler okunurken hata oldu!")
            #print("Devam edilemiyor")
            print("hata")
            #sys.exit()
        time.sleep(10)
