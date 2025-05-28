import feedparser
from bs4 import BeautifulSoup

rss_url = "https://g1.globo.com/dynamo/tecnologia/rss2.xml"
feed = feedparser.parse(rss_url)

noticias = []
for entry in feed.entries:
    title = BeautifulSoup(entry.title, "html.parser").get_text()
    noticias.append(title)

manchetes = "  •  ".join(noticias)

html = f"""<!DOCTYPE html>
<html lang='pt-BR'>
<head>
<meta charset='UTF-8' />
<meta name='viewport' content='width=device-width, initial-scale=1.0'>
<title>Notícias G1</title>
<style>
body, html {{
  margin: 0; padding: 0; width: 100%; height: 100%;
  background: #FFFFFF;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  font-family: Arial, sans-serif;
}}
.scroll-container {{
  white-space: nowrap;
  display: inline-block;
  animation: scroll-left 350s linear infinite;
  font-size: 42px;
  font-weight: bold;
  padding-left: 100%;
  color: #000000;
}}
@keyframes scroll-left {{
  0% {{ transform: translateX(0%); }}
  100% {{ transform: translateX(-100%); }}
}}
</style>
</head>
<body>
  <div class='scroll-container'>{manchetes}</div>
</body>
</html>
""" 

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
