from bs4 import BeautifulSoup
import requests
import re
import csv

HEADERS = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)'
                          'AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/45.0.2454.101 Safari/537.36'),
           'referer': 'http://stats.nba.com/scores/'}

# urls = ["https://www.hepsiburada.com/vestel-venus-v3-5580-vestel-garantili-p-HBV000003K73J-yorumlari?filtre=4", "https://www.hepsiburada.com/vestel-venus-v3-5580-vestel-garantili-p-HBV000003K73J-yorumlari?filtre=4&sayfa=2", "https://www.hepsiburada.com/vestel-venus-v3-5580-vestel-garantili-p-HBV000003K73J-yorumlari?filtre=4&sayfa=3",
#       "https://www.hepsiburada.com/vestel-venus-v3-5580-vestel-garantili-p-HBV000003K73J-yorumlari?filtre=4&sayfa=4", "https://www.hepsiburada.com/vestel-venus-v3-5580-vestel-garantili-p-HBV000003K73J-yorumlari?filtre=4&sayfa=5"]

# urls = ["https://www.hepsiburada.com/xiaomi-mi-8-128-gb-ithalatci-garantili-p-HBV00000CQAH9-yorumlari?filtre=1", "https://www.hepsiburada.com/xiaomi-mi-8-128-gb-ithalatci-garantili-p-HBV00000CQAH9-yorumlari?filtre=1&sayfa=2", "https://www.hepsiburada.com/xiaomi-mi-8-128-gb-ithalatci-garantili-p-HBV00000CQAH9-yorumlari?filtre=1&sayfa=3",
#      "https://www.hepsiburada.com/xiaomi-mi-8-128-gb-ithalatci-garantili-p-HBV00000CQAH9-yorumlari?filtre=1&sayfa=4", "https://www.hepsiburada.com/xiaomi-mi-8-128-gb-ithalatci-garantili-p-HBV00000CQAH9-yorumlari?filtre=1&sayfa=5"]

urls = ["https://www.hepsiburada.com/vestel-venus-v3-5580-vestel-garantili-p-HBV000003K73J-yorumlari?filtre=2", "https://www.hepsiburada.com/vestel-venus-v3-5580-vestel-garantili-p-HBV000003K73J-yorumlari?filtre=2&sayfa=2", "https://www.hepsiburada.com/vestel-venus-v3-5580-vestel-garantili-p-HBV000003K73J-yorumlari?filtre=2&sayfa=3", "https://www.hepsiburada.com/samsung-galaxy-m20-32-gb-samsung-turkiye-garantili-p-HBV00000HBKG5-yorumlari?filtre=2", "https://www.hepsiburada.com/samsung-galaxy-m20-32-gb-samsung-turkiye-garantili-p-HBV00000HBKG5-yorumlari?filtre=2&sayfa=2", "https://www.hepsiburada.com/lenovo-k6-note-lenovo-turkiye-garantili-p-HBV000003K70E-yorumlari?filtre=2", "https://www.hepsiburada.com/lenovo-k6-note-lenovo-turkiye-garantili-p-HBV000003K70E-yorumlari?filtre=2&sayfa=2", "https://www.hepsiburada.com/lenovo-k6-note-lenovo-turkiye-garantili-p-HBV000003K70E-yorumlari?filtre=2&sayfa=3"]
for pg in urls:
    response = requests.get(pg, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    comments = [sp.text.strip() for sp in soup.select('.review-text')]
    for comment in comments:
        with open('comments4.csv', "a", encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([comment])
