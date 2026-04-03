import os
import shutil

# Template file
template_file = 'blog/docker-multistage.html'

posts = [
    {
        "filename": "blog/ai-driven-development-2026.html",
        "title": "2026'da Yapay Zeka Odaklı Yazılım Geliştirme",
        "category": "Yapay Zeka",
        "date": "29 Mart 2026",
        "read_time": "8 dk",
        "views": "3.2K",
        "img": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=1400&h=560&fit=crop",
        "content": """
      <p>Yapay zeka (AI) artık sadece kod tamamlama veya öneriler sunma aşamasını çoktan geçti. 2026 itibariyle, Agentic AI sistemleri ve çoklu model orkestrasyonları sayesinde yazılım geliştirme süreçleri tamamen farklı bir boyuta ulaştı.</p>
      
      <h2>Yapay Zekanın Yeni Rolü: Asistandan Otonom Geliştiriciye</h2>
      <p>Eskiden Copilot benzeri araçlar kod snippet'ları yazarak zaman kazandırıyordu. Günümüzde ise AI ajanlarına "Bir kimlik doğrulama mikro servisi oluştur" komutunu verdiğinizde, mimari kararları alıyor, testlerini yazıyor ve CI/CD süreçlerini konfigüre ederek hazır bir branch sunuyor.</p>
      
      <pre><div class="prose-code" id="code-block-1"># Örnek bir Agentic AI Workflow tanımı
name: AI-Driven Auth Service
agent_roles:
  - architect: "Güvenlik standartlarını (OAuth2, JWT) belirler."
  - developer: "Go ile mikro servisi yazar."
  - qa: "Unit ve integration testlerini oluşturur."
  - devops: "Dockerfile ve Kubernetes manifestlerini hazırlar."</div></pre>
      
      <h2>Pragmatik Geliştirici Olmak</h2>
      <p>Bu yeni dönemde yazılımcıların rolü "kod yazıcı" olmaktan çıkıp "sistem tasarımcısı" ve "AI orkestratörü" olmaya kayıyor. <strong>AI'ın ürettiği kodu körü körüne kabul etmek yerine,</strong> bu sistemlere doğru bağlamı (context) sağlamak ve güvenlik/performans denetimlerini (code review) layıkıyla yapabilmek en değerli beceri haline geldi.</p>
      
      <h3>Başarı İçin 3 Temel Kural</h3>
      <ul>
        <li><strong>Prompt Engineering'den Sistem Tasarımına:</strong> Artık iyi prompt yazmak yeterli değil. AI ajanlarına projenizin sınırlarını, iş kurallarını ve bağımlılıklarını izole edilmiş ortamlar (sandboxing) üzerinden eksiksiz aktarmalısınız.</li>
        <li><strong>Sıfır Güven (Zero-Trust) Kod İncelemesi:</strong> AI modelleri ne kadar gelişirse gelişsin halüsinasyon görebilir. Kendi yazmadığınız kodlardaki performans darboğazlarını veya zafiyetleri gözden kaçırmayın.</li>
        <li><strong>Domain Driven Design (DDD) Önemi:</strong> İş mantığını iyi kurgulayan yazılımcılar, AI'ın teknik üretim hızını kullanarak olağanüstü ürünler ortaya koyabilir. AI kodu yazar, siz stratejiyi belirlersiniz.</li>
      </ul>
      
      <h2>Sonuç</h2>
      <p>Yazılım dünyası son derece pragmatik bir evrim geçiriyor. AI'ı izole bir araç olarak değil, ekibinizin yeni ve hızlı junior / mid-level mühendisi olarak konumlandırdığınızda hızınıza yetişmek imkansız olacak.</p>
        """
    },
    {
        "filename": "blog/modern-monorepo-architectures.html",
        "title": "Modern Frontend: Micro-Frontends ve Monorepo Yaklaşımları",
        "category": "Frontend",
        "date": "15 Nisan 2026",
        "read_time": "12 dk",
        "views": "2.5K",
        "img": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=1400&h=560&fit=crop",
        "content": """
      <p>Frontend ekipleri büyüdükçe ve projeler karmaşıklaştıkça, geleneksel tekil (monolith) SPA uygulamaları yönetilemez hale gelir. Bu noktada Micro-Frontends mimarisi ve Monorepo yönetim araçları (Turborepo, Nx) devreye giriyor.</p>
      
      <h2>Neden Monorepo?</h2>
      <p>Farklı repolara bölünmüş frontend projeleri, paylaşılan tasarım sistemlerinde (Design Systems) bağımlılık tiranlığı yaratır. Bir butondaki ufacık değişikliğin 5 farklı projeye dağıtılması haftalar alabilir. Monorepo ise tüm paylaşılan paketleri ve uygulamaları tek bir repoda toplayarak güncellemeleri saniyelere indirir.</p>
      
      <pre><div class="prose-code" id="code-block-1">// Turbo Pipeline Örneği (turbo.json)
{
  "$schema": "https://turbo.build/schema.json",
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**", ".next/**"]
    },
    "lint": {},
    "dev": {
      "cache": false,
      "persistent": true
    }
  }
}</div></pre>

      <h2>Micro-Frontends (Module Federation)</h2>
      <p>Webpack Module Federation (veya Vite kullananlar için Native Federation), çalışma zamanında (runtime) kod paylaşımına izin verir. Böylece A takımının geliştirdiği 'Sepet' komponenti, B takımının 'Ürün Detay' uygulamasında anında güncellenmiş olarak render edilir. Üstelik sıfır build maliyetiyle!</p>
      
      <h3>Pragmatik Bir Geçiş Stratejisi</h3>
      <ul>
        <li><strong>Gereksiz Kompleksiteden Kaçının:</strong> Sadece 2-3 kişilik bir ekibiniz varsa doğrudan Micro-Frontend'e atlamak devops cehennemi yaratır. Bunun yerine düzenli klasör yapısıyla yönetilen sıkı bir Monolith tercih edin.</li>
        <li><strong>Bileşen Sınırlarını Eğitime Dayandırın:</strong> Micro-frontends'i takımların iş planına göre bölün (Bounded Context). Ekranda rastgele görsel alanları takımlara atamayın.</li>
        <li><strong>CI/CD Boru Hattı Hayatidir:</strong> Turborepo'nun Remote Caching özelliğini kullanarak, bulut ortamında sadece değişen uygulamaların build alınmasını sağlayın. Vercel veya kendi self-hosted çözümünüz ile dakikalar süren build'leri saniyelere indirebilirsiniz.</li>
      </ul>
      
      <h2>Sonuç: Monorepo Micro-Frontend İle Buluşunca</h2>
      <p>Doğru planlandığında, Monorepo projelerde organizasyonu sağlarken, Module Federation runtime esnekliğini getirir. İkisini birlikte kullanarak ölçeklenebilirlik devrimini yaşayabilirsiniz.</p>
        """
    },
    {
        "filename": "blog/serverless-edge-computing-2026.html",
        "title": "Serverless Mimari ve Edge Computing'in Yükselişi",
        "category": "Backend",
        "date": "20 Nisan 2026",
        "read_time": "10 dk",
        "views": "4.1K",
        "img": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1400&h=560&fit=crop",
        "content": """
      <p>Kullanıcılar milisaniyelik gecikmelere (latency) bile tahammülsüzleşti. Serverless (sunucusuz) mimari bizi altyapı yönetme derdinden kurtarırken, Edge Computing veriyi kullanıcıya en yakın fiziksel lokasyona (CDN ucuna) taşıyarak ışık hızında bir deneyim sunuyor.</p>
      
      <h2>Serverless 2.0: Artık Sadece Fonksiyon Değil</h2>
      <p>İlk dönem AWS Lambda gibi Serverless fonksiyonlar soğuk başlangıç (cold start) sorunlarıyla ünlüydü. Günümüzde V8 isolate tabanlı modern serverless platformları (Vercel Edge Functions, Cloudflare Workers) ile cold start sorunları sıfırlandı.</p>
      
      <pre><div class="prose-code" id="code-block-1">// Next.js Middleware ile Edge Edge Computing Örneği
import { NextResponse } from 'next/server';

export function middleware(request) {
  // Kullanıcının coğrafi konumuna Edge noktasından çok hızlı erişim
  const country = request.geo.country || 'US';
  
  if (country === 'TR') {
    return NextResponse.rewrite(new URL('/tr', request.url));
  }
  return NextResponse.next();
}

export const config = {
  matcher: '/',
};</div></pre>

      <h2>Veritabanları da Artık Serverless ve Edge'de</h2>
      <p>Kodumuz Edge'e taşındı ancak veritabanı hala Frankfurt'ta ise latency yine de yüksek olacaktır. Pragmatik bir çözüm olarak Supabase, Neon ve PlanetScale gibi dağıtık, sunucusuz veritabanı servisleri ortaya çıktı. Edge fonksiyonlarından bu servislere doğrudan, bağlantı havuzu (connection polling) olmadan HTTP üzerinden bağlanmak artık bir standart.</p>
      
      <h3>Pragmatik Dönüşüm Adımları</h3>
      <ul>
        <li><strong>Statik ve Dinamiği Ayırın:</strong> Geleneksel SSR (Server Side Rendering) yerine ISR (Incremental Static Regeneration) kullanarak, veriyi build time'da oluşturun ama belli aralıklarla arkaplanda tazeleyin.</li>
        <li><strong>Doğru Yerde Doğru Teknoloji:</strong> Ağır PDF işlemleri veya CPU yoğun işler için geleneksel serverless (AWS Lambda) kullanırken, A/B testing, yönlendirme (routing), bot önleme gibi işleri Edge Functions'da çözün.</li>
        <li><strong>Durum Bilgisini Hafifletin:</strong> Edge üzerinde stateless (durumsuz) token yapıları (JWT) kullanarak merkezi Redis/DB sorgularından kaçının.</li>
      </ul>
      
      <h2>Sonuç</h2>
      <p>Edge Computing, uygulamanızın kod bloklarını dünya geneline yayma gücü verir. Serverless ve Edge yaklaşımları birleştirildiğinde global ölçekte ve sıfır altyapı maliyeti ile çalışan müthiş uygulamalar üretebilirsiniz.</p>
        """
    }
]

import re

# Read template
with open(template_file, 'r', encoding='utf-8') as f:
    template_content = f.read()

for post in posts:
    content = template_content
    
    # Replace title tag
    content = re.sub(r'<title>(.*?)</title>', f"<title>{post['title']} — Ömer Özbay</title>", content)
    
    # Replace Image
    content = re.sub(
        r'<img src="https://images\.unsplash\.com/[^"]+" alt="Docker"',
        f'<img src="{post["img"]}" alt="Thumbnail"',
        content
    )
    
    # Replace category
    content = re.sub(
        r'<span class="px-3 py-1 rounded-full text-xs font-medium dark:bg-surface bg-neutral-100 dark:text-neutral-400 text-neutral-500">.*?</span>',
        f'<span class="px-3 py-1 rounded-full text-xs font-medium dark:bg-surface bg-neutral-100 dark:text-neutral-400 text-neutral-500">{post["category"]}</span>',
        content, count=1
    )
    
    # Replace h1 title
    content = re.sub(
        r'<h1 class="text-2xl sm:text-3xl md:text-4xl[^>]*>.*?</h1>',
        f'<h1 class="text-2xl sm:text-3xl md:text-4xl font-bold tracking-tight dark:text-white text-neutral-900 leading-tight mb-4 page-enter-delay-1">{post["title"]}</h1>',
        content, flags=re.DOTALL
    )
    
    # Replace meta info (date, read time, views)
    # Finding the matching container
    meta_html = f"""<div class="flex flex-wrap items-center gap-4 text-sm dark:text-neutral-500 text-neutral-400 mb-10 pb-10 border-b dark:border-border border-border-light page-enter-delay-2">
      <span class="flex items-center gap-1.5"><span class="iconify" data-icon="lucide:calendar" data-width="14"></span>{post['date']}</span>
      <span class="flex items-center gap-1.5"><span class="iconify" data-icon="lucide:clock" data-width="14"></span>{post['read_time']} okuma</span>
      <span class="flex items-center gap-1.5"><span class="iconify" data-icon="lucide:eye" data-width="14"></span>{post['views']} görüntülenme</span>
    </div>"""
    
    content = re.sub(
        r'<div class="flex flex-wrap items-center gap-4 text-sm dark:text-neutral-500 text-neutral-400 mb-10 pb-10 border-b dark:border-border border-border-light page-enter-delay-2">.*?</div>',
        meta_html,
        content, flags=re.DOTALL
    )
    
    # Replace article content
    # Look for <article class="prose max-w-none page-enter-delay-3"> ... </article>
    content = re.sub(
        r'<article class="prose max-w-none page-enter-delay-3">.*?</article>',
        f'<article class="prose max-w-none page-enter-delay-3">{post["content"]}</article>',
        content, flags=re.DOTALL
    )
    
    # Write new file
    with open(post['filename'], 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created: {post['filename']}")
