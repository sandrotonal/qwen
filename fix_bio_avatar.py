import os
import glob
import re

files = glob.glob('*.html') + glob.glob('blog/*.html')
for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Avatar oval to full rounded
    # The avatar is in index.html and hakkimda.html
    # Look for rounded-[40%] and rounded-[40%...]
    content = content.replace('w-28 h-28 sm:w-36 sm:h-36 rounded-[40%]', 'w-28 h-28 sm:w-36 sm:h-36 rounded-full')
    content = content.replace('w-20 h-20 sm:w-28 sm:h-28 rounded-[40%]', 'w-20 h-20 sm:w-28 sm:h-28 rounded-full')

    # 2. Shorten bio text across files if present
    long_bio = "Bandırma 17 Eylül Üniversitesi Bilgisayar Mühendisliği öğrencisi. Karmaşık mantığı insan odaklı tasarımla birleştiren yüksek performanslı dijital mimariler ve AI destekli SaaS sistemleri geliştiriyor."
    short_bio = "Bilgisayar Müh. öğrencisi. AI ve modern SaaS mimarileri üzerine çalışıyorum."
    
    content = content.replace(long_bio, short_bio)
    
    # 3. Wait, in `hakkimda.html` he also said it was long maybe? No he said "blog kısmındaki bu açıklamayı kısa tut"
    # Actually, in blog html files maybe the bio is there?
    # No, wait! "blog ksımındakı bu acıklmayı kısa tut" - He might mean the bio text in the blog posts. 
    # Let me make a generic replace for it.
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Ovals fixed, and bio shortened.')
