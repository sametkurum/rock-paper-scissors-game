# Taş, Kağıt, Makas Oyunu

## Proje Özeti
Bu proje, klasik "Taş, Kağıt, Makas" oyununun basit bir Python uygulamasıdır. Bu proje, açık kaynaklı projelere katkı sağlamayı teşvik etmek amacıyla hazırlanmıştır. Kodun bazı bölümleri bilerek eksik bırakılmıştır ve bu sayede katılımcılar oyunun işlevselliğini geliştirebilir.

## Mevcut İşlevler
- Oyuncu, bilgisayara karşı oynayabilir.
- Bilgisayar rastgele bir seçim yapar: "rock" "paper" veya "scissors"
- Oyun, kazananı şu kurallara göre belirler:
  - Taş, Makası yener.
  - Makas, Kağıdı yener.
  - Kağıt, Taşı yener.
- Her turun sonunda oyuncuya tekrar oynama veya çıkış yapma seçeneği sunulur.

## Katkı Fırsatları
Uygulamada iki problem bulunmaktadır. Katkıda bulunmak isteyenler bu alanları geliştirebilir:

### 1. Problem
Kullanıcı  "rock" seçecekse bunu "Rock","ROCK","rOck" vb. şekilde girdiğinde program "you wrote wrong" çıktısı vermektedir.
Aynı küçük-büyük harf hassasiyeti "Do you wanna play again (Yes or no):" girdisinde de vardır.
Gerekli fonksiyonu ekleyerek hatayı düzeltebilirsiniz.

### 2. Problem
Bilgisayarın "taş" seçmesi durumunda kazananı belirlemek için gerekli mantık eksiktir. Bu mantığı uygun kod bölümüne ekleyerek oyunun işlevselliğini tamamlayabilirsiniz.

## Nasıl Katkı Sağlanır?
1. **Projeyi Forklayın:** Öncelikle projeyi GitHub hesabınıza forklayın.
2. **Projeyi Klonlayın:** Forkladığınız projeyi yerel bilgisayarınıza klonlayın.
3. **Değişiklik Yapın:** Yukarıda belirtilen eksik özelliklerden birini veya her ikisini uygulayın.
4. **Değişiklikleri Test Edin:** Oyunu çalıştırarak işlevselliğin doğru şekilde çalıştığından emin olun.
5. **Pull Request Gönderin:** Değişikliklerinizi forkunuza pushladıktan sonra inceleme için bir pull request gönderin.

## Oyunu Çalıştırma
Oyunu çalıştırmak için sisteminizde Python kurulu olmalıdır. Terminal veya komut istemcisinde aşağıdaki komutu çalıştırın:
```bash
python rock_paper_scissors.py
```

## Lisans
Bu proje açık kaynaklıdır ve MIT Lisansı altında sunulmaktadır. Kodu kullanabilir, değiştirebilir ve dağıtabilirsiniz.

## Teşekkür
Bu projeye katkıda bulunduğunuz ve işlevselliğini geliştirdiğiniz için teşekkür ederiz!

