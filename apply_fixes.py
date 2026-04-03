import re
import os

files = ['index.html', 'hakkimda.html', 'iletisim.html']

def rewrite_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract contents safely
    head_match = re.search(r'<head>(.*?)</head>', content, re.DOTALL | re.IGNORECASE)
    if not head_match:
        return
    head_content = head_match.group(1).strip()
    
    title = 'Blog — Ömer Özbay'
    active_nav = 'blog'
    if filename == 'hakkimda.html':
        title = 'Hakkımda — Ömer Özbay'
        active_nav = 'hakkimda'
    elif filename == 'iletisim.html':
        title = 'İletişim — Ömer Özbay'
        active_nav = 'iletisim'

    head_content = re.sub(r'<title>.*?</title>', '', head_content, flags=re.IGNORECASE).strip()

    main_match = re.search(r'(<main[^>]*>.*?</main>)', content, re.DOTALL | re.IGNORECASE)
    if not main_match:
        return
    main_content = main_match.group(1).strip()
    
    # Minimal sleek nav classes
    def nav_class(name, is_mobile=False):
        if is_mobile:
            if name == active_nav:
                return 'text-neutral-900 dark:text-white font-semibold opacity-100 tracking-widest'
            return 'text-neutral-400 dark:text-neutral-500 hover:text-neutral-900 dark:hover:text-white opacity-80 hover:opacity-100 tracking-widest'
        else:
            if name == active_nav:
                return 'text-neutral-900 dark:text-white font-semibold'
            return 'text-neutral-500 dark:text-neutral-400 hover:text-neutral-900 dark:hover:text-white'

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
      <a href="index.html" class="flex items-center group shrink-0">
        <span class="font-extrabold text-[16px] sm:text-[18px] dark:text-white text-neutral-900 tracking-[0.15em] uppercase" style="font-family: 'Inter', sans-serif;">Ömer Özbay</span>
      </a>
      
      <nav class="hidden md:flex items-center gap-8">
        <a href="index.html" class="relative pb-1 text-[13px] uppercase tracking-widest transition-all duration-300 nav-link {nav_class('blog')} {'nav-active' if active_nav == 'blog' else ''}">Blog</a>
        <a href="hakkimda.html" class="relative pb-1 text-[13px] uppercase tracking-widest transition-all duration-300 nav-link {nav_class('hakkimda')} {'nav-active' if active_nav == 'hakkimda' else ''}">Hakkımda</a>
        <a href="iletisim.html" class="relative pb-1 text-[13px] uppercase tracking-widest transition-all duration-300 nav-link {nav_class('iletisim')} {'nav-active' if active_nav == 'iletisim' else ''}">İletişim</a>
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
      <a href="index.html" class="text-2xl sm:text-3xl transition-colors duration-400 {nav_class('blog', True)}">Blog</a>
      <a href="hakkimda.html" class="text-2xl sm:text-3xl transition-colors duration-400 {nav_class('hakkimda', True)}">Hakkımda</a>
      <a href="iletisim.html" class="text-2xl sm:text-3xl transition-colors duration-400 {nav_class('iletisim', True)}">İletişim</a>
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
      <a href="index.html" class="hover:text-neutral-900 dark:hover:text-white transition-colors">Blog</a>
      <span>&middot;</span>
      <a href="hakkimda.html" class="hover:text-neutral-900 dark:hover:text-white transition-colors">Hakkımda</a>
      <span>&middot;</span>
      <a href="iletisim.html" class="hover:text-neutral-900 dark:hover:text-white transition-colors">İletişim</a>
    </div>
    
    <div class="text-[12px] dark:text-neutral-500 text-neutral-400 flex items-center gap-1">
      © 2026 Ömer Özbay.
    </div>

    <div class="flex items-center gap-4">
      <a href="https://github.com/sandrotonal" target="_blank" class="dark:text-neutral-500 text-neutral-400 hover:text-neutral-900 dark:hover:text-white transition-colors"><span class="iconify text-[18px]" data-icon="mdi:github"></span></a>
      <a href="https://x.com/gucluyumhe" target="_blank" class="dark:text-neutral-500 text-neutral-400 hover:text-neutral-900 dark:hover:text-white transition-colors"><span class="iconify text-[16px]" data-icon="ri:twitter-x-fill"></span></a>
    </div>
  </footer>

  <script src="js/main.js"></script>
</body>
</html>"""

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Rewrote {filename} successfully.")

for file in files:
    if os.path.exists(file):
        rewrite_file(file)
