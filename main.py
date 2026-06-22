import os
from dotenv import load_dotenv
load_dotenv()
from github_api import repo_bilgisi_al, dosyalari_getir, dosya_icerigini_oku, onemli_dosyalar, readme_push_et
from readme_uretici import readme_uret

def main():
    repo_url = input("GitHub repo URL gir: ").strip()

    print("Repo analiz ediliyor...")
    bilgi = repo_bilgisi_al(repo_url)
    sahibi = bilgi["sahibi"]
    repo_adi = bilgi["repo_adi"]

    dosya_listesi=dosyalari_getir(sahibi,repo_adi)
    secilen_dosyalar=onemli_dosyalar(dosya_listesi)
    print(f"{len(secilen_dosyalar)} dosya bulundu , içerikler incelenıyor ...")

    dosya_icerikleri = {}
    for dosya_yolu in secilen_dosyalar:
        icerik = dosya_icerigini_oku(sahibi ,repo_adi,dosya_yolu)
        if icerik:
            dosya_icerikleri[dosya_yolu]=icerik
            print(f"{dosya_yolu}")

    print("Claude README yazıyor...")
    readme = readme_uret(repo_adi, dosya_icerikleri)

    print("README repoya push ediliyor...")
    basarili = readme_push_et(sahibi, repo_adi, readme)

    if basarili:
        print(f"✓ README başarıyla güncellendi!")
        print(f"  https://github.com/{sahibi}/{repo_adi}")
    else:
        print("✗ Push başarısız. Token'ı kontrol et.")

if __name__ == "__main__":
    main()