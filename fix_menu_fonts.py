import os
import glob
import re

html_files = glob.glob('*.html') + glob.glob('blog/*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Desktop Nav Active
    content = content.replace(
        'text-[13px] uppercase tracking-widest transition-all duration-300 nav-link text-neutral-900 dark:text-white font-semibold nav-active',
        'text-sm font-medium transition-all duration-300 nav-link text-neutral-900 dark:text-white nav-active'
    )
    # Desktop Nav Inactive
    content = content.replace(
        'text-[13px] uppercase tracking-widest transition-all duration-300 nav-link text-neutral-500 dark:text-neutral-400 hover:text-neutral-900 dark:hover:text-white',
        'text-sm font-medium transition-all duration-300 nav-link text-neutral-500 dark:text-neutral-400 hover:text-neutral-900 dark:hover:text-white'
    )
    
    # Mobile Nav Active
    content = content.replace(
        'text-2xl sm:text-3xl transition-colors duration-400 text-neutral-900 dark:text-white font-semibold opacity-100 tracking-widest',
        'text-3xl sm:text-4xl font-medium tracking-tight transition-colors duration-400 text-neutral-900 dark:text-white opacity-100'
    )
    # Mobile Nav Inactive
    content = content.replace(
        'text-2xl sm:text-3xl transition-colors duration-400 text-neutral-400 dark:text-neutral-500 hover:text-neutral-900 dark:hover:text-white opacity-80 hover:opacity-100 tracking-widest',
        'text-3xl sm:text-4xl font-medium tracking-tight transition-colors duration-400 text-neutral-400 dark:text-neutral-500 hover:text-neutral-900 dark:hover:text-white opacity-80 hover:opacity-100'
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated menu fonts across {len(html_files)} files!")
