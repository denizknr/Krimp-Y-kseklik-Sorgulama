# Krimp-Y-kseklik-Sorgulama

**Krimp Yükseklik Sorgulama** — ERPNext/Frappe üzerinde interaktif ve görsel olarak gelişmiş yönetim modülü.

---

## Özellikler

- 📋 **KrimpYukseklik** adlı özel DocType: Açıklama, Atanan Kişi, Durum, Öncelik, Referans Tipi, Vade Tarihi alanları
- 🎨 **Koyu tema desteği** ve modern kullanıcı arayüzü (ERPNext'in yerel ToDo listesi tasarımına uygun)
- 🏷️ **Renkli durum rozetleri**: Açık (kırmızı), Kapalı (yeşil), Beklemede (turuncu), İptal (gri)
- 🔴🟡🟠 **Öncelik rozetleri**: Düşük, Orta, Yüksek, Acil
- 🔍 Varsayılan filtreler ve gelişmiş filtreleme çubuğu
- ⚡ Tek tıkla "Kapat" aksiyonu (Açık/Beklemede kayıtlar için)

---

## Kurulum

### 1. Uygulamayı Frappe bench'e ekleyin

```bash
cd /path/to/frappe-bench
bench get-app https://github.com/denizknr/Krimp-Y-kseklik-Sorgulama
bench --site <site-adı> install-app krimp_yukseklik
bench migrate
bench build
```

### 2. (Geliştirme) Yerel olarak ekleyin

```bash
cd /path/to/frappe-bench/apps
git clone https://github.com/denizknr/Krimp-Y-kseklik-Sorgulama krimp_yukseklik_app
cd krimp_yukseklik_app
# Frappe app klasörünü bench'e tanıtın
cd /path/to/frappe-bench
bench --site <site-adı> install-app krimp_yukseklik
bench migrate
```

---

## Kullanım

1. ERPNext/Frappe'ye giriş yapın.
2. Sol menüden **Krimp Yukseklik** modülüne gidin ya da arama çubuğuna `KrimpYukseklik` yazın.
3. **Yeni** butonuyla kayıt oluşturun: Açıklama, atanan kişi, durum, öncelik ve vade tarihi girin.
4. Liste görünümünde renkli durum ve öncelik rozetlerini, filtreleme çubuğunu kullanın.
5. Açık/Beklemede kayıtlar için satır sonundaki **Kapat** butonuyla durumu hızlıca güncelleyin.

---

## DocType Alanları

| Alan               | Tip     | Açıklama                                  |
|--------------------|---------|-------------------------------------------|
| Açıklama           | Data    | Krimp yükseklik sorgu başlığı/açıklaması  |
| Atanan Kişi        | Link    | Atanan kullanıcı (User)                   |
| Atamayı Yapan      | Link    | Görevi oluşturan kullanıcı (User)         |
| Durum              | Select  | Açık / Kapalı / Beklemede / İptal         |
| Öncelik            | Select  | Düşük / Orta / Yüksek / Acil             |
| Referans Tipi      | Select  | Toplantı / Yapılacaklar / Krimp Kontrolü  |
| Vade Tarihi        | Date    | Son tamamlanma tarihi                     |
| Notlar             | Text    | Ek notlar                                 |

---

## Dizin Yapısı

```
krimp_yukseklik/
├── hooks.py                         # Frappe uygulama kancaları (CSS dahil)
├── modules.txt                      # Modül tanımı
├── requirements.txt
├── setup.py
├── public/
│   └── css/
│       └── krimp_yukseklik.css      # Koyu tema & liste görünümü stilleri
└── krimp_yukseklik/
    └── doctype/
        └── krimp_yukseklik/
            ├── krimp_yukseklik.json       # DocType şeması
            ├── krimp_yukseklik.py         # Python kontrolcüsü
            └── krimp_yukseklik_list.js    # Liste görünümü özelleştirmeleri
```

---

## Referans

- [Frappe DocType Belgeleri](https://frappeframework.com/docs/user/en/basics/doctypes)
- [ERPNext ToDo Modülü](https://docs.erpnext.com/docs/user/manual/en/to-do)
- Orijinal sorgulama aracı: `KrimpDefteriSorgulama.py` ve `krimp_lookup.html`
