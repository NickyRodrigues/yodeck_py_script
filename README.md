# 📰 Painel de Notícias Automáticas para Yodeck com RSS do G1

Este projeto exibe **notícias atualizadas automaticamente** do portal **G1 - Tecnologia**, utilizando **Python**, **GitHub Actions** e **Netlify** para alimentar um **ticker de manchetes em rolagem contínua**, ideal para uso em **displays digitais (Yodeck)**.

---

## ✅ O que este projeto faz

- Consulta automaticamente o **RSS do G1 - Tecnologia** (`https://g1.globo.com/dynamo/tecnologia/rss2.xml`)
- Extrai os títulos das últimas notícias
- Gera um arquivo `index.html` com **animação CSS de rolagem lateral**
- Publica o conteúdo atualizado via **Netlify**
- Atualiza o conteúdo **automaticamente a cada hora**
- Pode ser usado em **players do Yodeck**, tanto Web Player quanto dispositivos físicos

---

## ⚙️ Como funciona

1. O script `gerar_index.py` lê o RSS do G1 e gera um `index.html` com as manchetes.
2. O GitHub Actions roda esse script **a cada 1 hora** (`cron: '0 * * * *'`).
3. O arquivo gerado é commitado automaticamente no repositório.
4. O Netlify detecta as mudanças no `index.html` e publica automaticamente.
5. O Yodeck consome esse link como uma **Web Page**, exibindo as notícias em tempo real.

---

## 🛠️ Tecnologias usadas

- [Python](https://www.python.org/)
- [GitHub Actions](https://docs.github.com/actions)
- [feedparser](https://pypi.org/project/feedparser/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [Netlify](https://www.netlify.com/)
- [Yodeck](https://www.yodeck.com/) (como player de exibição)

---

## 📄 Estrutura do projeto

```
.
├── gerar_index.py               # Script principal para gerar o HTML
├── index.html                   # Arquivo gerado com as notícias
├── requirements.txt             # Dependências para o workflow
└── .github/
    └── workflows/
        └── rss_atualizacao.yml  # GitHub Actions que atualiza o conteúdo
```

---

## 🚀 Como usar

1. Faça o fork ou clone deste repositório
2. Conecte-o ao Netlify (deploy automático via GitHub)
3. Use o link final do Netlify no **Web Page do Yodeck**
4. Pronto! Seu painel de notícias estará sempre atualizado 🎉

---

## 🧠 Créditos e ideias futuras

Criado para exibição em monitores corporativos, TVs de recepção ou murais digitais via Yodeck.

💡 Futuras melhorias podem incluir:
- Suporte a múltiplos feeds (G1, CNN, R7)
- Filtragem por palavra-chave
- Emojis contextuais para manchetes
