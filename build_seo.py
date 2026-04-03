import os
import glob
import re
from datetime import datetime

base_url = "https://omerozbay.vercel.app"

html_files = glob.glob('*.html')
blog_files = glob.glob('blog/*.html')
all_html_files = html_files + blog_files

# 1. Create sitemap.xml
sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for f in all_html_files:
    # Set priority
    if f == 'index.html':
        priority = "1.0"
        changefreq = "weekly"
    elif 'blog/' in f:
        priority = "0.8"
        changefreq = "monthly"
    else:
        priority = "0.7"
        changefreq = "monthly"
        
    url = f"{base_url}/{f.replace(os.sep, '/')}"
    # Replace index.html with just the base path for SEO reasons
    if url.endswith('/index.html'):
        url = url[:-11]
        
    lastmod = datetime.now().strftime('%Y-%m-%d')
    sitemap_content += f"""  <url>
    <loc>{url}</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>\n"""

sitemap_content += '</urlset>'

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_content)

# 2. Create robots.txt
robots_txt = f"""User-agent: *
Allow: /

Sitemap: {base_url}/sitemap.xml
"""
with open('robots.txt', 'w', encoding='utf-8') as f:
    f.write(robots_txt)

# 3. Inject JSON-LD Schema to index.html and update Canonical URLs globally
json_ld = f"""
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Ömer Özbay",
    "alternateName": "gucluyumhe",
    "url": "{base_url}",
    "jobTitle": "Full Stack Developer",
    "alumniOf": {{
      "@type": "CollegeOrUniversity",
      "name": "Bandırma 17 Eylül Üniversitesi"
    }},
    "sameAs": [
      "https://github.com/sandrotonal",
      "https://x.com/gucluyumhe",
      "https://t.me/islamakhachev",
      "https://gucluyumhe.dev/"
    ],
    "description": "Bandırma 17 Eylül Üniversitesi Bilgisayar Mühendisliği öğrencisi. Karmaşık mantığı insan odaklı tasarımla birleştiren yüksek performanslı dijital mimariler ve AI destekli SaaS sistemleri geliştiriyor."
  }}
  </script>
"""

for filepath in all_html_files:
    with open(filepath, 'r', encoding='utf-8') as doc:
        content = doc.read()
        
    # Replace old gucluyumhe.dev references in meta/canonical
    content = content.replace('href="https://gucluyumhe.dev/"', f'href="{base_url}/"')
    content = content.replace('content="https://gucluyumhe.dev/"', f'content="{base_url}/"')
    
    # Optional: ensure correct canonical for each specific page
    # But for a simple static site, base_url is often fine or we can omit it if it replaces globally incorrectly.
    # Currently we globally replaced `https://gucluyumhe.dev/` with `https://omerozbay.vercel.app/`.

    if filepath == 'index.html':
        if 'application/ld+json' not in content:
            content = content.replace('</head>', json_ld + '</head>')
            
    with open(filepath, 'w', encoding='utf-8') as doc:
        doc.write(content)

print("SEO Infrastructure (Sitemap, Robots.txt, JSON-LD Schema, Canonical Meta) generated successfully.")
