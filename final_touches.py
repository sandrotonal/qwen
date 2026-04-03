import os
import glob
import re

html_files = glob.glob('*.html') + glob.glob('blog/*.html')
js_file = 'js/main.js'

seo_meta_tags = """
  <meta name="description" content="Ömer Özbay - Full-Stack Engineer & Bandırma 17 Eylül University Computer Engineering student building AI-powered SaaS applications.">
  <meta name="keywords" content="Ömer Özbay, Full Stack Developer, Software Engineer, Web Development, React, Next.js, AI, SaaS, Bandırma 17 Eylül Üniversitesi, Bilgisayar Mühendisliği">
  <meta property="og:title" content="Ömer Özbay — Full Stack Engineer">
  <meta property="og:description" content="Computer Engineering student building AI-powered SaaS applications and modern web experiences.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://gucluyumhe.dev/">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Ömer Özbay — Full Stack Engineer">
  <meta name="twitter:description" content="Computer Engineering student building AI-powered SaaS applications and modern web experiences.">
  <link rel="canonical" href="https://gucluyumhe.dev/">"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. SEO & Meta tags
    if 'meta property="og:title"' not in content:
        content = re.sub(
            r'(<meta name="viewport" content="width=device-width, initial-scale=1.0">)',
            r'\1\n' + seo_meta_tags,
            content
        )

    # 2. PageSpeed Optimization (lazy load images mostly done, but defer JS)
    content = content.replace('<script src="js/main.js"></script>', '<script src="js/main.js" defer></script>')
    content = content.replace('<script src="../js/main.js"></script>', '<script src="../js/main.js" defer></script>')
    content = re.sub(r'<img(?!.*?loading="lazy")[^>]+>', lambda m: m.group(0).replace('<img', '<img loading="lazy" decoding="async"'), content)

    # 3. Fix Menu Drawer to Native Side-Drawer
    menu_regex = r'<div id="mobile-menu" class="fixed inset-0 w-full h-screen .*?flex flex-col items-center justify-center .*? opacity-0 pointer-events-none scale-95">'
    new_menu = """
  <!-- Mobile Menu Overlay -->
  <div id="mobile-menu-overlay" class="fixed inset-0 bg-black/20 dark:bg-black/60 backdrop-blur-sm z-[60] opacity-0 pointer-events-none transition-all duration-400 ease-out" onclick="toggleMobileMenu()"></div>
  
  <div id="mobile-menu" class="fixed top-0 right-0 w-full sm:w-80 h-screen bg-[#FAFAFA]/95 dark:bg-[#0A0A0A]/95 backdrop-blur-xl border-l border-black/5 dark:border-white/5 z-[70] transform translate-x-full transition-transform duration-400 ease-[cubic-bezier(0.16,1,0.3,1)] flex flex-col items-center justify-center">"""
    
    content = re.sub(menu_regex, new_menu, content, flags=re.DOTALL)

    # If already had overlay from previously before I deleted it? 
    # Just in case, if it resulted in multiple overlays:
    content = re.sub(r'(<div id="mobile-menu-overlay".*?></div>\s*){2,}', r'\1', content, flags=re.DOTALL)

    # 4. Updates for index.html text
    if filepath == 'index.html':
        content = content.replace('Software Engineer', 'Full Stack Developer')
        content = content.replace('Modern web teknolojileri, performans optimizasyonu ve yazılım mimarisi üzerine yazıyor.',
                                  'Bandırma 17 Eylül Üniversitesi Bilgisayar Mühendisliği öğrencisi. Karmaşık mantığı insan odaklı tasarımla birleştiren yüksek performanslı dijital mimariler ve AI destekli SaaS sistemleri geliştiriyor.')

    # 5. Updates for hakkimda.html
    if filepath == 'hakkimda.html':
        content = content.replace('Kod yazan,<br>öğrenen, paylaşan.', 'Building the Future<br>with AI & SaaS')
        content = content.replace("İstanbul'da yaşayan full-stack developer. 2019'dan beri React, Node.js ve PostgreSQL ekosisteminde çalışıyorum. Web performansı ve sistem tasarımı benim için sadece iş değil, tutku.",
                                  "Ben Ömer Özbay. Bandırma 17 Eylül Üniversitesi Bilgisayar Mühendisliği'nde okuyorum. 20 yaşında, karmaşık mantığı gelişmiş tasarımla buluşturan yüksek performanslı dijital mimariler oluşturmaya odaklanan bir Full-Stack Engineer'ım.<br><br>Yapay zeka sistemleri, SaaS çözümleri ve modern web uygulamaları üzerine çalışıyorum.")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Update JS for side drawer
with open(js_file, 'r', encoding='utf-8') as f:
    js_content = f.read()

new_js_toggle = """function toggleMobileMenu() {
  const menu = document.getElementById('mobile-menu');
  const overlay = document.getElementById('mobile-menu-overlay');
  if (!menu || !overlay) return;
  const isClosed = menu.classList.contains('translate-x-full');
  
  if (isClosed) {
    // Open menu
    menu.classList.remove('translate-x-full');
    overlay.classList.remove('opacity-0', 'pointer-events-none');
    overlay.classList.add('opacity-100', 'pointer-events-auto');
    document.body.style.overflow = 'hidden';
  } else {
    // Close menu
    menu.classList.add('translate-x-full');
    overlay.classList.remove('opacity-100', 'pointer-events-auto');
    overlay.classList.add('opacity-0', 'pointer-events-none');
    document.body.style.overflow = '';
  }
}"""

js_content = re.sub(r'function toggleMobileMenu\(\)\s*\{.*?(?:document\.body\.style\.overflow = .*?;|})\s*\}', new_js_toggle, js_content, flags=re.DOTALL)

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Global updates applied to {len(html_files)} files.")
