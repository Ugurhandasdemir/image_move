import os
import shutil


kaynak_klasor = "C:/Users/ugurh/Downloads/Veri Seti-20240404T141456Z-005/Veri Seti/TEKNOFEST UYZ 2022 Verileri/Oturum1_Part1-20221229T165645Z-002"
hedef_klasor = "C:/Users/ugurh/OneDrive/Masaüstü/test_veri"

for kok_dizin, alt_klasorler, dosyalar in os.walk(kaynak_klasor):
    for dosya in dosyalar:

        if dosya.endswith(('.jpg', '.png')):

            kaynak_dosya = os.path.join(kok_dizin, dosya)
            yeni_dosya_adi = "yeni_" + dosya
            hedef_dosya = os.path.join(hedef_klasor, yeni_dosya_adi)


            shutil.move(kaynak_dosya, hedef_dosya)

print("Resimler Taşındı")
