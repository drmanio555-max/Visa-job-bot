import requests
from bs4 import BeautifulSoup

def get_visa_jobs():
    # نیوزی لینڈ میں ڈیری فارم کی ویزا سپانسر جابز کی تلاش
    query = "Dairy+Farm+worker+visa+sponsorship+New+Zealand"
    url = f"https://www.google.com/search?q={query}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    jobs_found = []
    
    # سرچ رزلٹس سے ڈیٹا نکالنا
    for g in soup.find_all('div', class_='tF2Cxc'):
        title = g.find('h3').text
        link = g.find('a')['href']
        jobs_found.append(f"Job: {title}\nLink: {link}\n")
    
    # رزلٹ کو ایک فائل میں محفوظ کرنا
    with open("latest_jobs.txt", "w", encoding="utf-8") as f:
        if jobs_found:
            f.write("--- تازہ ترین ویزا سپانسر جابز ---\n\n")
            f.write("\n".join(jobs_found))
        else:
            f.write("آج کوئی نئی جاب نہیں ملی۔")
    
    print("کامیابی! جابز 'latest_jobs.txt' فائل میں محفوظ کر دی گئی ہیں۔")

if __name__ == "__main__":
    get_visa_jobs()
