
import glob
import re

def fix(path):
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    # Footer fix
    c = re.sub(
        r"<a href=\"https://x.com/gucluyumhe\" target=\"_blank\"\s+class=\"dark:text-neutral-500 text-neutral-400 hover:text-neutral-900 dark:hover:text-white transition-colors\"><span\s+class=\"iconify text-\[16px\]\" data-icon=\"ri:twitter-x-fill\"></span></a>",
        r"""<a href="https://x.com/gucluyumhe" target="_blank"
        class="dark:text-neutral-500 text-neutral-400 hover:text-neutral-900 dark:hover:text-white transition-colors"><span
          class="iconify text-[16px]" data-icon="ri:twitter-x-fill"></span></a>
      <a href="https://t.me/islamakhachev" target="_blank"
        class="dark:text-neutral-500 text-neutral-400 hover:text-neutral-900 dark:hover:text-white transition-colors"><span
          class="iconify text-[18px]" data-icon="mdi:telegram"></span></a>
      <a href="https://www.instagram.com/00mer04/" target="_blank"
        class="dark:text-neutral-500 text-neutral-400 hover:text-neutral-900 dark:hover:text-white transition-colors"><span
          class="iconify text-[18px]" data-icon="mdi:instagram"></span></a>""",
        c
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(c)

for f in list(glob.glob("*.html")) + list(glob.glob("blog/*.html")):
    fix(f)
print("Done")

