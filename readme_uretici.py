import anthropic
import os

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", ""))

def readme_uret(repo_adi:str,dosya_icerikleri:dict)->str:
    dosyalar_metni=""
    for dosya_yolu , icerik in dosya_icerikleri.items():
        dosyalar_metni +=f"\n---{dosya_yolu}---\n{icerik[:500]}\n"

    prompt= f"""
    Aşağıdaki GitHub reposunun kod dosyalarını analiz et ve profesyonel bir README.md yaz.
    
    Repo adı: {repo_adi}
    
    Kod dosyaları:
    {dosyalar_metni}
    
    README şunları içermeli:
    - Proje başlığı ve kısa açıklama
    - Özellikler listesi
    - Kurulum adımları
    - Kullanım örneği
    - Kullanılan teknolojiler
    
    Markdown formatında yaz. Türkçe ve İngilizce yaz
    """

    yanit = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return yanit.content[0].text