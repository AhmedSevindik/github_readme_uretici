import requests
import os
import base64

GITHUB_TOKEN= os.environ.get("GITHUB_TOKEN" , "")

def repo_bilgisi_al(repo_url: str) -> dict:
    temiz_url = repo_url.rstrip("/").replace(".git", "")
    sahibi, repo_adi = temiz_url.split("/")[-2:]
    return {"sahibi": sahibi, "repo_adi": repo_adi}

def dosyalari_getir(sahibi:str,repo_adi:str)->list:
    url=f"https://api.github.com/repos/{sahibi}/{repo_adi}/git/trees/main?recursive=1"
    headers={"Authorization":f"token {GITHUB_TOKEN}"}
    yanit=requests.get(url,headers=headers)
    if yanit.status_code != 200:
        print(f"Hata: {yanit.status_code} - {yanit.json().get('message','')}")
        return[]
    return yanit.json().get("tree",[])

def dosya_icerigini_oku(sahibi:str , repo_adi:str,dosya_yolu:str)->str:
    url=f"https://api.github.com/repos/{sahibi}/{repo_adi}/contents/{dosya_yolu}"
    headers={"Authorization":f"token {GITHUB_TOKEN}"}
    yanit=requests.get(url,headers=headers)
    if yanit.status_code != 200:
        return ""
    icerik=yanit.json().get("content", "")
    return base64.b64decode(icerik).decode("utf-8",errors="ignore")

def onemli_dosyalar(dosya_listesi:list)->list:
    uzantilar = [".py", ".js", ".ts", ".java", ".cpp", ".go", ".rs"]
    ozel_dosyalar = ["requirements.txt", "package.json", "README.md", "Dockerfile"]

    secilen= []
    for dosya in dosya_listesi:
        if dosya["type"] != "blob":
            continue

        yol=dosya["path"]
        if any(yol.endswith(u) for u in uzantilar):
            secilen.append(yol)

        elif any(yol.endswith(u) for u in ozel_dosyalar):
            secilen.append(yol)

    return secilen

def readme_push_et(sahibi:str,repo_adi:str,icerik:str)->bool:
    url=f"https://api.github.com/repos/{sahibi}/{repo_adi}/contents/README.md"
    headers={"Authorization":f"token {GITHUB_TOKEN}"}

    mevcut = requests.get(url,headers=headers)
    sha=mevcut.json().get("sha","") if mevcut.status_code ==200 else ""

    veri= {
        "message":"README.md otomatik güncellendi",
        "content" : base64.b64encode(icerik.encode("utf-8")).decode("utf-8"),
    }
    if sha:
        veri["sha"] = sha

    yanit = requests.put(url, headers=headers, json=veri)
    if yanit.status_code not in (200, 201):
        print(f"Push hatası: {yanit.status_code} - {yanit.json().get('message', '')}")
    return yanit.status_code in (200,201)

