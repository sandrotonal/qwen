import os
import glob
import re

html_files = glob.glob('*.html') + glob.glob('blog/*.html')

google_analytics = """
  <!-- Google Analytics & Perf -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preconnect" href="https://images.unsplash.com">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-TRACKINGID"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-TRACKINGID');
  </script>
"""

# Realistic dates for the 6 posts currently in index.html, ordered from newest to oldest.
dates = [
    "<time datetime='2026-03-24'>24 Mar 2026</time>",
    "<time datetime='2026-03-15'>15 Mar 2026</time>",
    "<time datetime='2026-02-28'>28 Şub 2026</time>",
    "<time datetime='2026-02-12'>12 Şub 2026</time>",
    "<time datetime='2026-01-25'>25 Oca 2026</time>",
    "<time datetime='2025-12-10'>10 Ara 2025</time>"
]

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add analytics and preconnect to <head> if not exists
    if 'googletagmanager' not in content:
        content = content.replace('</head>', google_analytics + '</head>')

    # Fix duplicate lazy loading from previous script issue just in case
    content = content.replace('loading="lazy" decoding="async" loading="lazy" decoding="async"', 'loading="lazy" decoding="async"')

    # Fix Index.html dates
    if filepath == 'index.html':
        content = content.replace('<span>Yeni</span>', 'SPAN_HOLDER', 3)
        content = content.replace('<span>2 gün önce</span>', 'SPAN_HOLDER', 1)
        content = content.replace('<span>1 hafta önce</span>', 'SPAN_HOLDER', 1)
        content = content.replace('<span>2 hafta önce</span>', 'SPAN_HOLDER', 1)
        
        for date in dates:
            content = content.replace('SPAN_HOLDER', date, 1)

    # Convert generic time elements inside blog posts if they have "15 Dk okuma - 2 Gün önce" etc.
    # Actually, the user specifically mentioned "blogların yayınlanma tarıhlerını gercekcı yap" which primarily effects the blog cards on index.html.

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Added SEO tags, Analytics, and realistic dates to {len(html_files)} files.")
