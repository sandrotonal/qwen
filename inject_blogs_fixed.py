import os
import re

index_file = 'index.html'
with open(index_file, 'r', encoding='utf-8') as f:
    content = f.read()

new_cards = """
          <!-- Post Card NEW AI -->
          <a href="blog/ai-driven-development-2026.html" class="blog-card card-glow rounded-2xl overflow-hidden border dark:border-border border-border-light dark:bg-card bg-white group" data-category="artificial-intelligence">
            <div class="aspect-[16/10] overflow-hidden">
              <img src="https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&h=375&fit=crop" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
            </div>
            <div class="p-5">
              <div class="flex items-center gap-2 mb-3">
                <span class="tag-pill px-2.5 py-0.5 rounded-full text-[0.65rem] font-medium dark:bg-surface bg-neutral-100 dark:text-neutral-400 text-neutral-500">Yapay Zeka</span>
              </div>
              <h3 class="text-[0.95rem] font-semibold dark:text-white text-neutral-900 leading-snug tracking-tight mb-2 group-hover:text-accent transition-colors line-clamp-2">2026'da Yapay Zeka Odaklı Yazılım Geliştirme</h3>
              <p class="text-xs dark:text-neutral-500 text-neutral-400 leading-relaxed line-clamp-2 mb-3">Agentic AI sistemleri ve çoklu model orkestrasyonları sayesinde yazılım süreçlerinin evrimi.</p>
              <div class="flex items-center gap-3 text-[0.7rem] dark:text-neutral-600 text-neutral-400">
                <span class="flex items-center gap-1"><span class="iconify" data-icon="lucide:clock" data-width="11"></span>8 dk</span>
                <span>Yeni</span>
              </div>
            </div>
          </a>

          <!-- Post Card NEW FRONTEND -->
          <a href="blog/modern-monorepo-architectures.html" class="blog-card card-glow rounded-2xl overflow-hidden border dark:border-border border-border-light dark:bg-card bg-white group" data-category="frontend">
            <div class="aspect-[16/10] overflow-hidden">
              <img src="https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&h=375&fit=crop" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
            </div>
            <div class="p-5">
              <div class="flex items-center gap-2 mb-3">
                <span class="tag-pill px-2.5 py-0.5 rounded-full text-[0.65rem] font-medium dark:bg-surface bg-neutral-100 dark:text-neutral-400 text-neutral-500">Frontend</span>
              </div>
              <h3 class="text-[0.95rem] font-semibold dark:text-white text-neutral-900 leading-snug tracking-tight mb-2 group-hover:text-accent transition-colors line-clamp-2">Modern Frontend: Micro-Frontends ve Monorepo</h3>
              <p class="text-xs dark:text-neutral-500 text-neutral-400 leading-relaxed line-clamp-2 mb-3">Turborepo, Nx ve Module Federation ile büyüyen projeleri yönetmenin kuralları.</p>
              <div class="flex items-center gap-3 text-[0.7rem] dark:text-neutral-600 text-neutral-400">
                <span class="flex items-center gap-1"><span class="iconify" data-icon="lucide:clock" data-width="11"></span>12 dk</span>
                <span>Yeni</span>
              </div>
            </div>
          </a>

          <!-- Post Card NEW BACKEND -->
          <a href="blog/serverless-edge-computing-2026.html" class="blog-card card-glow rounded-2xl overflow-hidden border dark:border-border border-border-light dark:bg-card bg-white group" data-category="backend">
            <div class="aspect-[16/10] overflow-hidden">
              <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&h=375&fit=crop" loading="lazy" decoding="async" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
            </div>
            <div class="p-5">
              <div class="flex items-center gap-2 mb-3">
                <span class="tag-pill px-2.5 py-0.5 rounded-full text-[0.65rem] font-medium dark:bg-surface bg-neutral-100 dark:text-neutral-400 text-neutral-500">Backend</span>
              </div>
              <h3 class="text-[0.95rem] font-semibold dark:text-white text-neutral-900 leading-snug tracking-tight mb-2 group-hover:text-accent transition-colors line-clamp-2">Serverless Mimari ve Edge Computing'in Yükselişi</h3>
              <p class="text-xs dark:text-neutral-500 text-neutral-400 leading-relaxed line-clamp-2 mb-3">Edge ile ışık hızında global performans algoritmaları.</p>
              <div class="flex items-center gap-3 text-[0.7rem] dark:text-neutral-600 text-neutral-400">
                <span class="flex items-center gap-1"><span class="iconify" data-icon="lucide:clock" data-width="11"></span>10 dk</span>
                <span>Yeni</span>
              </div>
            </div>
          </a>
"""

# Insert right after <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5" id="posts-grid">
if '<!-- Post Card NEW AI -->' not in content:
    content = re.sub(
        r'(<div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5" id="posts-grid">)',
        r'\1\n' + new_cards,
        content
    )

    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated index.html to include new blogs!")
else:
    print("Already injected.")
