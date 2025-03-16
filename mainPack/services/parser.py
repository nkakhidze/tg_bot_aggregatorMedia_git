import requests
from bs4 import BeautifulSoup

def fetch_news(url):
    """Получает заголовок и краткое описание новости"""
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        return f"Ошибка запроса: {e}"

    soup = BeautifulSoup(response.text, "lxml")

    # Популярные структуры новостных сайтов
    title = soup.find("h1") or soup.find("title")
    description = soup.find("meta", attrs={"name": "description"})

    title_text = title.get_text(strip=True) if title else "Заголовок не найден"
    desc_text = description["content"] if description else "Описание отсутствует"

    return f"📰 {title_text}\n\n{desc_text}\n🔗 {url}"
