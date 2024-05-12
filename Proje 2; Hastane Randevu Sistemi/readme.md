# Hastane Randevu Sistemi

Bu proje, Python ve PyQt5 kütüphanesi kullanılarak geliştirilmiş bir Hastane Randevu Sistemi uygulamasıdır. Uygulama, hastaların doktor randevusu almasını, randevu geçmişini görüntülemesini ve randevu iptalini sağlar. Ayrıca, doktorların müsaitlik durumlarını gösterir.

## Kurulum

1. Bu depoyu klonlayın veya indirin.
2. Gerekli Python kütüphanelerini kurun:
pip install PyQt5

## Kullanım

1. Projenin ana dizinindeki `randevu.py` dosyasını çalıştırın.
2. Hasta bilgilerini (isim, soyisim, TC numarası) girin.
3. Doktor seçimi yapın.
4. Randevu tarihini ve saatini girin.
5. "Randevu Al" düğmesine tıklayın.
6. Randevu geçmişini görüntülemek için "Randevu Geçmişi" bölümüne bakın.
7. Randevu iptal etmek için, "Randevu İptal" düğmesine tıklayın ve iptal edilecek randevuyu seçin.

## Proje Yapısı

- `randevu.py`: Ana uygulama dosyası, kullanıcı arayüzünü ve randevu işlemlerini içerir.
- `musaitlik_takvimi.py`: Doktorların müsaitlik takvimini gösteren bir pencere oluşturur.

Proje, aşağıdaki sınıfları ve veri yapılarını kullanır:

- `Hasta`: İsim, soyisim, TC numarası ve randevu geçmişi bilgilerini tutar.
- `Doktor`: İsim, uzmanlık alanı, müsaitlik durumu ve müsaitlik takvimi bilgilerini tutar.
- `Randevu`: Randevu tarihi, doktor ve hasta bilgilerini tutar.

## Katkıda Bulunma

Bu proje, bir öğrenci projesidir ve katkıda bulunmak için açık değildir. Ancak, öneriler veya hataları bildirmek için lütfen bir Issue açın.

## Lisans

Bu proje, MIT Lisansı altında lisanslanmıştır.

## Uygulama görselleri


![hastane](https://github.com/numyy/Python-pyqt5-Projeleri/assets/148050750/162062a9-8b9f-40ed-a414-c2235da6cf12)
