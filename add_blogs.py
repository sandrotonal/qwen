import os
import re

index_file = 'index.html'
with open(index_file, 'r', encoding='utf-8') as f:
    content = f.read()

new_cards = """
      <a href="blog/ai-driven-development-2026.html" class="blog-card flex flex-col md:flex-row gap-5 p-6 rounded-2xl border dark:border-border border-border-light dark:bg-card bg-white group" data-category="ai">
        <div class="w-full md:w-56 aspect-[16/9] md:aspect-auto md:h-36 rounded-xl overflow-hidden shrink-0 relative">
          <img src="https://images.unsplash.com/photo-1677442136019-21780ecad995?w=500&h=320&fit=crop" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" decoding="async">
        </div>
        <div class="flex flex-col justify-center min-w-0">
          <div class="flex items-center gap-2 mb-3">
            <span class="px-2.5 py-1 rounded-sm text-[10px] uppercase font-bold tracking-wider dark:bg-surface bg-neutral-100 dark:text-neutral-400 text-neutral-500">Yapay Zeka</span>
            <span class="text-xs dark:text-neutral-500 text-neutral-400 font-mono">29 Mart 2026 &middot; 8 dk</span>
          </div>
          <h3 class="text-lg md:text-xl font-bold dark:text-white text-neutral-900 leading-snug mb-2 group-hover:text-accent transition-colors line-clamp-2">2026'da Yapay Zeka Odaklı Yazılım Geliştirme</h3>
          <p class="text-sm dark:text-neutral-400 text-neutral-500 line-clamp-2 leading-relaxed">Agentic AI sistemleri ve çoklu model orkestrasyonları sayesinde yazılım süreçlerinin evrimi.</p>
        </div>
      </a>

      <a href="blog/modern-monorepo-architectures.html" class="blog-card flex flex-col md:flex-row gap-5 p-6 rounded-2xl border dark:border-border border-border-light dark:bg-card bg-white group" data-category="frontend">
        <div class="w-full md:w-56 aspect-[16/9] md:aspect-auto md:h-36 rounded-xl overflow-hidden shrink-0 relative">
          <img src="https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=500&h=320&fit=crop" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" decoding="async">
        </div>
        <div class="flex flex-col justify-center min-w-0">
          <div class="flex items-center gap-2 mb-3">
            <span class="px-2.5 py-1 rounded-sm text-[10px] uppercase font-bold tracking-wider dark:bg-surface bg-neutral-100 dark:text-neutral-400 text-neutral-500">Frontend</span>
            <span class="text-xs dark:text-neutral-500 text-neutral-400 font-mono">15 Nisan 2026 &middot; 12 dk</span>
          </div>
          <h3 class="text-lg md:text-xl font-bold dark:text-white text-neutral-900 leading-snug mb-2 group-hover:text-accent transition-colors line-clamp-2">Modern Frontend: Micro-Frontends ve Monorepo</h3>
          <p class="text-sm dark:text-neutral-400 text-neutral-500 line-clamp-2 leading-relaxed">Turborepo, Nx ve Module Federation ile büyüyen frontend projelerini yönetmenin kuralları.</p>
        </div>
      </a>

      <a href="blog/serverless-edge-computing-2026.html" class="blog-card flex flex-col md:flex-row gap-5 p-6 rounded-2xl border dark:border-border border-border-light dark:bg-card bg-white group" data-category="backend">
        <div class="w-full md:w-56 aspect-[16/9] md:aspect-auto md:h-36 rounded-xl overflow-hidden shrink-0 relative">
          <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=500&h=320&fit=crop" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" decoding="async">
        </div>
        <div class="flex flex-col justify-center min-w-0">
          <div class="flex items-center gap-2 mb-3">
            <span class="px-2.5 py-1 rounded-sm text-[10px] uppercase font-bold tracking-wider dark:bg-surface bg-neutral-100 dark:text-neutral-400 text-neutral-500">Backend</span>
            <span class="text-xs dark:text-neutral-500 text-neutral-400 font-mono">20 Nisan 2026 &middot; 10 dk</span>
          </div>
          <h3 class="text-lg md:text-xl font-bold dark:text-white text-neutral-900 leading-snug mb-2 group-hover:text-accent transition-colors line-clamp-2">Serverless Mimari ve Edge Computing'in Yükselişi</h3>
          <p class="text-sm dark:text-neutral-400 text-neutral-500 line-clamp-2 leading-relaxed">Geleneksel serverless sorunlarından kurtulup Edge ile ışık hızında global performans sağlama rehberi.</p>
        </div>
      </a>
"""

# Insert right after <div id="blog-posts" class="...">
content = re.sub(
    r'(<div id="blog-posts" class="flex flex-col gap-6">)',
    r'\1\n' + new_cards,
    content
)

with open(index_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html to include new blogs!")
