import glob

tag = '<meta name="google-site-verification" content="OB7WLZaiiMlTjwYtUOACquTXNpK4ZHEbcA49gz6LOxA" />'

for file in glob.glob('*.html') + glob.glob('blog/*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if tag not in content:
        content = content.replace('</head>', f'  {tag}\n</head>')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Meta tags added to all HTML files successfully.")
