import os
import glob
import re

blog_files = glob.glob('blog/*.html')

share_section_replacement = """
      <div class="mt-16 pt-8 border-t border-black/5 dark:border-white/5 flex flex-col sm:flex-row items-center justify-between gap-6">
        <div class="flex flex-col items-center sm:items-start text-center sm:text-left gap-1">
          <span class="text-xs font-bold uppercase tracking-widest text-neutral-900 dark:text-white">Faydalı buldunuz mu?</span>
          <span class="text-sm text-neutral-500 dark:text-neutral-400">Bu içeriği kendi ağınızla paylaşarak bana destek olabilirsiniz.</span>
        </div>
        <div class="flex items-center gap-3 w-full sm:w-auto">
          <button onclick="showToast('Link kopyalandı!')" class="flex-1 sm:flex-none flex items-center justify-center gap-2 px-6 py-2.5 rounded-full text-sm font-medium border border-neutral-200 dark:border-neutral-800 text-neutral-600 dark:text-neutral-300 hover:bg-neutral-100 dark:hover:bg-neutral-800 transition-colors">
            <span class="iconify" data-icon="lucide:share-2" data-width="14"></span> Paylaş
          </button>
          <a href="../index.html" class="flex-1 sm:flex-none flex items-center justify-center gap-2 px-6 py-2.5 rounded-full text-sm font-medium bg-neutral-900 dark:bg-white text-white dark:text-neutral-900 hover:opacity-90 transition-colors">
            Tüm Yazılar <span class="iconify" data-icon="lucide:arrow-right" data-width="14"></span>
          </a>
        </div>
      </div>
"""

def fix_blog_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract head content securely
    head_match = re.search(r'<head>(.*?)</head>', content, re.DOTALL | re.IGNORECASE)
    if not head_match:
        return
    head_content = head_match.group(1).strip()
    
    # Strip <title> to inject our dynamic one
    title_match = re.search(r'<title>(.*?)</title>', head_content, re.IGNORECASE)
    title = title_match.group(1) if title_match else 'Ömer Özbay - Blog'
    head_content = re.sub(r'<title>.*?</title>', '', head_content, flags=re.IGNORECASE).strip()

    # Get main element
    main_match = re.search(r'(<main[^>]*>.*?</main>)', content, re.DOTALL | re.IGNORECASE)
    if not main_match:
        return
    main_content = main_match.group(1).strip()

    # Remove existing "Bu yazıyı faydalı buldunuz mu?" section from main_content using regex
    # The existing block starts with `<div class="mt-12 pt-8 border-t...` and ends before `<div class="mt-8">`
    main_content = re.sub(
        r'<div class="mt-12 pt-8 border-t[^>]*>.*?<span class="text-sm dark:text-neutral-400 text-neutral-500">Bu yazıyı faydalı buldunuz mu\?</span>.*?</div>\s*</div>',
        share_section_replacement,
        main_content,
        flags=re.DOTALL | re.IGNORECASE
    )

    new_html = f"""<!DOCTYPE html>
<html lang="tr" class="dark scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  {head_content}
  <style>
    /* Modern Scrollbar */
    ::-webkit-scrollbar {{ width: 6px; }}
    ::-webkit-scrollbar-track {{ background: transparent; }}
    ::-webkit-scrollbar-thumb {{ background: #3f3f46; border-radius: 10px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: #52525b; }}
    html {{ -webkit-tap-highlight-color: transparent; }}
    
    /* Elegant underline animation for nav */
    .nav-link::after {{
      content: '';
      position: absolute;
      width: 100%;
      transform: scaleX(0);
      height: 1px;
      bottom: -2px;
      left: 0;
      background-color: currentColor;
      transform-origin: bottom right;
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .nav-link:hover::after {{
      transform: scaleX(1);
      transform-origin: bottom left;
    }}
    .nav-active::after {{
      transform: scaleX(1);
    }}
  </style>
</head>
<body class="min-h-screen bg-[#FAFAFA] dark:bg-[#0A0A0A] text-neutral-800 dark:text-neutral-200 antialiased selection:bg-neutral-200 dark:selection:bg-neutral-800 selection:text-neutral-900 dark:selection:text-white font-sans">
  <div id="scroll-progress" class="h-[2px] bg-neutral-900 dark:bg-white fixed top-0 left-0 z-[100] transition-all duration-300 ease-out" style="width: var(--scroll-width, 0%);"></div>
  
  <div id="toast" class="toast fixed bottom-6 left-1/2 -translate-x-1/2 z-[200] px-5 py-3 rounded-full text-sm font-medium shadow-2xl flex items-center gap-2 dark:bg-[#1A1A1A] bg-white border dark:border-neutral-800 border-neutral-200 transition-all duration-300">
    <span class="iconify text-green-500" data-icon="lucide:check-circle-2"></span>
    <span id="toast-message"></span>
  </div>

  <!-- Header -->
  <header class="sticky top-0 z-50 backdrop-blur-md bg-[#FAFAFA]/70 dark:bg-[#0A0A0A]/70">
    <div class="max-w-4xl mx-auto px-5 h-20 sm:h-24 flex items-center justify-between">
      <a href="../index.html" class="flex items-center group shrink-0">
        <span class="font-extrabold text-[16px] sm:text-[18px] dark:text-white text-neutral-900 tracking-[0.15em] uppercase" style="font-family: 'Inter', sans-serif;">Ömer Özbay</span>
      </a>
      
      <nav class="hidden md:flex items-center gap-8">
        <a href="../index.html" class="relative pb-1 text-[13px] uppercase tracking-widest transition-all duration-300 nav-link text-neutral-900 dark:text-white font-semibold nav-active">Blog</a>
        <a href="../hakkimda.html" class="relative pb-1 text-[13px] uppercase tracking-widest transition-all duration-300 nav-link text-neutral-500 dark:text-neutral-400 hover:text-neutral-900 dark:hover:text-white">Hakkımda</a>
        <a href="../iletisim.html" class="relative pb-1 text-[13px] uppercase tracking-widest transition-all duration-300 nav-link text-neutral-500 dark:text-neutral-400 hover:text-neutral-900 dark:hover:text-white">İletişim</a>
      </nav>
      
      <div class="flex items-center gap-4">
        <button onclick="toggleTheme()" class="flex items-center justify-center dark:text-neutral-400 text-neutral-500 hover:text-neutral-900 dark:hover:text-white transition-colors duration-300 shrink-0" title="Tema">
          <span class="iconify text-[20px] theme-icon dark-icon" data-icon="solar:moon-linear"></span>
          <span class="iconify text-[20px] theme-icon light-icon hidden" data-icon="solar:sun-linear"></span>
        </button>
        <button onclick="toggleMobileMenu()" class="flex md:hidden items-center justify-center dark:text-neutral-400 text-neutral-500 hover:text-neutral-900 dark:hover:text-white transition-colors duration-300 shrink-0">
          <span class="iconify text-[24px]" data-icon="solar:hamburger-menu-linear"></span>
        </button>
      </div>
    </div>
  </header>

  <!-- Mobile Menu -->
  <div id="mobile-menu-overlay" class="fixed inset-0 bg-black/20 dark:bg-black/60 backdrop-blur-sm z-[60] opacity-0 pointer-events-none transition-all duration-400 ease-out" onclick="toggleMobileMenu()"></div>
  <div id="mobile-menu" class="fixed top-0 right-0 w-full h-[600px] max-h-screen bg-[#FAFAFA] dark:bg-[#0A0A0A] border-b border-black/5 dark:border-white/5 z-[70] transform -translate-y-full transition-transform duration-500 ease-[cubic-bezier(0.16,1,0.3,1)] flex flex-col items-center justify-center">
    <button onclick="toggleMobileMenu()" class="absolute top-8 right-6 w-10 h-10 flex items-center justify-center dark:text-neutral-400 text-neutral-500 hover:text-neutral-900 dark:hover:text-white transition-colors">
      <span class="iconify text-2xl" data-icon="lucide:x"></span>
    </button>
    
    <nav class="flex flex-col items-center gap-8 text-center">
      <a href="../index.html" class="text-2xl sm:text-3xl transition-colors duration-400 text-neutral-900 dark:text-white font-semibold opacity-100 tracking-widest">Blog</a>
      <a href="../hakkimda.html" class="text-2xl sm:text-3xl transition-colors duration-400 text-neutral-400 dark:text-neutral-500 hover:text-neutral-900 dark:hover:text-white opacity-80 hover:opacity-100 tracking-widest">Hakkımda</a>
      <a href="../iletisim.html" class="text-2xl sm:text-3xl transition-colors duration-400 text-neutral-400 dark:text-neutral-500 hover:text-neutral-900 dark:hover:text-white opacity-80 hover:opacity-100 tracking-widest">İletişim</a>
    </nav>
    
    <div class="absolute bottom-12 flex gap-6">
      <a href="https://github.com/sandrotonal" target="_blank" class="dark:text-neutral-400 text-neutral-500 hover:text-neutral-900 dark:hover:text-white transition-colors hover:-translate-y-1 duration-300"><span class="iconify text-2xl" data-icon="mdi:github"></span></a>
      <a href="https://x.com/gucluyumhe" target="_blank" class="dark:text-neutral-400 text-neutral-500 hover:text-neutral-900 dark:hover:text-white transition-colors hover:-translate-y-1 duration-300"><span class="iconify text-[22px]" data-icon="ri:twitter-x-fill"></span></a>
      <a href="https://t.me/islamakhachev" target="_blank" class="dark:text-neutral-400 text-neutral-500 hover:text-neutral-900 dark:hover:text-white transition-colors hover:-translate-y-1 duration-300"><span class="iconify text-2xl" data-icon="mdi:telegram"></span></a>
    </div>
  </div>

  {main_content}

  <!-- Minimal Footer -->
  <footer class="mt-20 py-8 border-t border-black/5 dark:border-white/5 mx-auto max-w-4xl px-5 flex flex-col md:flex-row items-center justify-between gap-6">
    <div class="flex items-center gap-4 text-sm font-medium dark:text-neutral-500 text-neutral-500">
      <a href="../index.html" class="hover:text-neutral-900 dark:hover:text-white transition-colors">Blog</a>
      <span>&middot;</span>
      <a href="../hakkimda.html" class="hover:text-neutral-900 dark:hover:text-white transition-colors">Hakkımda</a>
      <span>&middot;</span>
      <a href="../iletisim.html" class="hover:text-neutral-900 dark:hover:text-white transition-colors">İletişim</a>
    </div>
    
    <div class="text-[12px] dark:text-neutral-500 text-neutral-400 flex items-center gap-1">
      © 2026 Ömer Özbay.
    </div>

    <div class="flex items-center gap-4">
      <a href="https://github.com/sandrotonal" target="_blank" class="dark:text-neutral-500 text-neutral-400 hover:text-neutral-900 dark:hover:text-white transition-colors"><span class="iconify text-[18px]" data-icon="mdi:github"></span></a>
      <a href="https://x.com/gucluyumhe" target="_blank" class="dark:text-neutral-500 text-neutral-400 hover:text-neutral-900 dark:hover:text-white transition-colors"><span class="iconify text-[16px]" data-icon="ri:twitter-x-fill"></span></a>
    </div>
  </footer>

  <script src="../js/main.js"></script>
</body>
</html>"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Bitti: {filepath}")

for filepath in blog_files:
    fix_blog_file(filepath)
