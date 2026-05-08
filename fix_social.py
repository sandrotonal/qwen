import sys
html_path = 'c:/z.ai/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

import re
old_str = r'<!-- Social Links -->.*?</div>'

def replacer(match):
    return '''<!-- Social Links -->
      <div class=\
anim-init
animate-fade-up-delay-4
mt-6
flex
items-center
gap-3\>
        <a href=\https://github.com/sandrotonal\ target=\_blank\
          class=\w-10
h-10
rounded-xl
flex
items-center
justify-center
dark:text-neutral-400
text-neutral-500
dark:hover:text-white
hover:text-neutral-900
dark:hover:bg-surface
hover:bg-neutral-100
transition-all\>
          <span class=\iconify
text-lg\ data-icon=\mdi:github\></span>
        </a>
        <a href=\https://x.com/gucluyumhe\ target=\_blank\
          class=\w-10
h-10
rounded-xl
flex
items-center
justify-center
dark:text-neutral-400
text-neutral-500
dark:hover:text-white
hover:text-neutral-900
dark:hover:bg-surface
hover:bg-neutral-100
transition-all\>
          <span class=\iconify
text-lg\ data-icon=\ri:twitter-x-fill\></span>
        </a>
        <a href=\https://www.instagram.com/00mer04/\ target=\_blank\
          class=\w-10
h-10
rounded-xl
flex
items-center
justify-center
dark:text-neutral-400
text-neutral-500
dark:hover:text-white
hover:text-neutral-900
dark:hover:bg-surface
hover:bg-neutral-100
transition-all\>
          <span class=\iconify
text-lg\ data-icon=\mdi:instagram\></span>
        </a>
        <a href=\https://t.me/islamakhachev\ target=\_blank\
          class=\w-10
h-10
rounded-xl
flex
items-center
justify-center
dark:text-neutral-400
text-neutral-500
dark:hover:text-white
hover:text-neutral-900
dark:hover:bg-surface
hover:bg-neutral-100
transition-all\>
          <span class=\iconify
text-lg\ data-icon=\mdi:telegram\></span>
        </a>
      </div>'''

new_content, count = re.subn(r'<!-- Social Links -->\s*<div class=\anim-init
animate-fade-up-delay-4
mt-6
flex
items-center
gap-3\>.*?</div>', replacer, content, count=1, flags=re.DOTALL)
if count > 0:
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Updated successfully')
else:
    print('Not found')

