import os
import glob
import re

html_files = glob.glob('*.html') + glob.glob('blog/*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix the mobile menu HTML classes (Fade + slight scale instead of translate-y)
    content = re.sub(
        r'<div id="mobile-menu" class="fixed top-0 right-0 w-full.*?z-\[70\].*?flex flex-col items-center justify-center">',
        '<div id="mobile-menu" class="fixed inset-0 w-full h-screen bg-[#FAFAFA]/95 dark:bg-[#0A0A0A]/95 backdrop-blur-xl z-[70] flex flex-col items-center justify-center transition-all duration-400 ease-[cubic-bezier(0.16,1,0.3,1)] opacity-0 pointer-events-none scale-95">',
        content, flags=re.DOTALL
    )
    
    content = re.sub(
        r'<div id="mobile-menu-overlay" class="fixed inset-0 bg-black/20 dark:bg-black/60 backdrop-blur-sm z-\[60\].*?onclick="toggleMobileMenu\(\)"></div>',
        '', # Completely remove overlay since the menu itself is now full screen
        content
    )

    # 2. Fix Fonts
    # Desktop Nav Active
    content = content.replace(
        'text-sm font-medium transition-all duration-300 nav-link text-neutral-900 dark:text-white nav-active',
        'text-[13px] font-medium tracking-wide transition-all duration-300 nav-link text-neutral-900 dark:text-white nav-active'
    )
    # Desktop Nav Inactive
    content = content.replace(
        'text-sm font-medium transition-all duration-300 nav-link text-neutral-500 dark:text-neutral-400 hover:text-neutral-900 dark:hover:text-white',
        'text-[13px] font-medium tracking-wide transition-all duration-300 nav-link text-neutral-500 dark:text-neutral-400 hover:text-neutral-900 dark:hover:text-white'
    )
    
    # Mobile Nav Active
    content = content.replace(
        'text-3xl sm:text-4xl font-medium tracking-tight transition-colors duration-400 text-neutral-900 dark:text-white opacity-100',
        'text-[22px] font-medium tracking-wide transition-colors duration-400 text-neutral-900 dark:text-white opacity-100'
    )
    # Mobile Nav Inactive
    content = content.replace(
        'text-3xl sm:text-4xl font-medium tracking-tight transition-colors duration-400 text-neutral-400 dark:text-neutral-500 hover:text-neutral-900 dark:hover:text-white opacity-80 hover:opacity-100',
        'text-[22px] font-medium tracking-wide transition-colors duration-400 text-neutral-500 dark:text-neutral-400 hover:text-neutral-900 dark:hover:text-white opacity-90 hover:opacity-100'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated HTML animation and fonts across {len(html_files)} files.")
