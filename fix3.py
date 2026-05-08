
import glob
import re

def fix(path):
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    # Mobile menu / Hero absolute bottom fix
    c = re.sub(
        r"<a href=\"https://t.me/islamakhachev\" target=\"_blank\"\s+class=\"dark:text-neutral-400 text-neutral-500 hover:text-neutral-900 dark:hover:text-white transition-colors hover:-translate-y-1 duration-300\"><span\s+class=\"iconify text-2xl\" data-icon=\"mdi:telegram\"></span></a>\s*</div>",
        r"""<a href="https://t.me/islamakhachev" target="_blank"
        class="dark:text-neutral-400 text-neutral-500 hover:text-neutral-900 dark:hover:text-white transition-colors hover:-translate-y-1 duration-300"><span
          class="iconify text-2xl" data-icon="mdi:telegram"></span></a>
      <a href="https://www.instagram.com/00mer04/" target="_blank"
        class="dark:text-neutral-400 text-neutral-500 hover:text-neutral-900 dark:hover:text-white transition-colors hover:-translate-y-1 duration-300"><span
          class="iconify text-2xl" data-icon="mdi:instagram"></span></a>
    </div>""",
        c
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(c)

for f in list(glob.glob("*.html")):
    fix(f)
print("Done")

