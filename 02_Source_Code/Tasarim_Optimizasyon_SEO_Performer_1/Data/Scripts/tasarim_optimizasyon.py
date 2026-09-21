import os
from PIL import Image

def baskiya_hazirla_v2(in_OptimizeFilePath, out_NewFilePath):
    print(f"Islem Basliyor: {in_OptimizeFilePath}")

    # 1. AYARLAR: POD Standartları
    CANVAS_GENISLIK = 4500
    CANVAS_YUKSEKLIK = 5400
    DPI_AYARI = (300, 300) 
    
    # 2. KONUMLANDIRMA AYARLARI
    UST_BOSLUK = 300 
    ALT_BOSLUK = 100 
    MAX_RESIM_YUKSEKLIGI = CANVAS_YUKSEKLIK - UST_BOSLUK - ALT_BOSLUK

    try:
        # Şeffaf Resmi Yükle
        img = Image.open(in_OptimizeFilePath).convert("RGBA")
        
        # Hedef Genişlik (Tuvalin %85'i)
        hedef_genislik_limit = int(CANVAS_GENISLIK * 0.85)
        oran_genislik = hedef_genislik_limit / img.width
        oran_yukseklik = MAX_RESIM_YUKSEKLIGI / img.height
        final_oran = min(oran_genislik, oran_yukseklik)
        
        yeni_genislik = int(img.width * final_oran)
        yeni_yukseklik = int(img.height * final_oran)

        # Kaliteli Boyutlandırma
        img_yeni = img.resize((yeni_genislik, yeni_yukseklik), Image.Resampling.LANCZOS)
        print(f"Resim boyutlandirildi: {yeni_genislik}x{yeni_yukseklik} px")

        # Boş Tuval Yarat
        final_canvas = Image.new("RGBA", (CANVAS_GENISLIK, CANVAS_YUKSEKLIK), (0, 0, 0, 0))

        # Konumlandırma (Yatayda Ortala)
        pos_x = (CANVAS_GENISLIK - img_yeni.width) // 2
        pos_y = UST_BOSLUK 
        
        # Yapıştır
        final_canvas.paste(img_yeni, (pos_x, pos_y), img_yeni)

        # Kaydet
        final_canvas.save(out_NewFilePath, dpi=DPI_AYARI)
        print(f"SORUN COZULDU! Dosya hazir: {out_NewFilePath}")
        
        # Orijinal dosyayı temizle
        if os.path.exists(in_OptimizeFilePath):
            os.remove(in_OptimizeFilePath)

        return "SUCCESS"

    except Exception as e:
        print(f"Hata: {e}")
        return "FAILED"