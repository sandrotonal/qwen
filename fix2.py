
with open("c:/z.ai/index.html", "r", encoding="utf-8") as f:
    c = f.read()
import re
c = re.sub(
    r"<!-- Social Links -->\s*<div class=\"anim-init animate-fade-up-delay-4 mt-6 flex items-center gap-3\">\s*<a href=\"https://github.com/sandrotonal\"[^>]+>\s*<span class=\"iconify text-lg\" data-icon=\"mdi:github\"></span>\s*</a>\s*<a href=\"https://t.me/islamakhachev\"[^>]+>\s*<span class=\"iconify text-lg\" data-icon=\"mdi:telegram\"></span>\s*</a>\s*<a href=\"https://www.instagram.com/00mer04/\"[^>]+>\s*<span class=\"iconify text-lg\" data-icon=\"mdi:instagram\"></span>\s*</a>\s*</div>",
    r"""<!-- Social Links -->
      <div class="anim-init animate-fade-up-delay-4 mt-6 flex items-center gap-3">
        <a href="https://github.com/sandrotonal" target="_blank"
          class="w-10 h-10 rounded-xl flex items-center justify-center dark:text-neutral-400 text-neutral-500 dark:hover:text-white hover:text-neutral-900 dark:hover:bg-surface hover:bg-neutral-100 transition-all">
          <span class="iconify text-lg" data-icon="mdi:github"></span>
        </a>
        <a href="https://x.com/gucluyumhe" target="_blank"
          class="w-10 h-10 rounded-xl flex items-center justify-center dark:text-neutral-400 text-neutral-500 dark:hover:text-white hover:text-neutral-900 dark:hover:bg-surface hover:bg-neutral-100 transition-all">
          <span class="iconify text-lg" data-icon="ri:twitter-x-fill"></span>
        </a>
        <a href="https://www.instagram.com/00mer04/" target="_blank"
          class="w-10 h-10 rounded-xl flex items-center justify-center dark:text-neutral-400 text-neutral-500 dark:hover:text-white hover:text-neutral-900 dark:hover:bg-surface hover:bg-neutral-100 transition-all">
          <span class="iconify text-lg" data-icon="mdi:instagram"></span>
        </a>
        <a href="https://t.me/islamakhachev" target="_blank"
          class="w-10 h-10 rounded-xl flex items-center justify-center dark:text-neutral-400 text-neutral-500 dark:hover:text-white hover:text-neutral-900 dark:hover:bg-surface hover:bg-neutral-100 transition-all">
          <span class="iconify text-lg" data-icon="mdi:telegram"></span>
        </a>
      </div>""",
    c
)
with open("c:/z.ai/index.html", "w", encoding="utf-8") as f:
    f.write(c)
print("done")

