# Katkı Rehberi

Bu repository, GitHub profil sayfamda görünen kişisel README'dir. Düzeltme önerileri (yazım hatası, bozuk bağlantı vb.) memnuniyetle karşılanır.

## Kurulum

1. Repository'yi fork'layıp klonlayın.
2. Python 3.12 yeterlidir; ek bağımlılık yoktur.

## Testleri çalıştırma

```bash
python -m unittest discover -s tests -v
```

## Pull request beklentileri

- `main` dalına doğrudan push yapmayın; ayrı bir dal açıp pull request gönderin.
- Pull request'i tek bir konuya odaklı tutun ve ne değiştiğini kısaca açıklayın.
- Testler yerelde geçmeli; GitHub Actions iş akışı (CI) yeşil olmalıdır.
- Gizli bilgi (anahtar, parola vb.) eklemeyin.
