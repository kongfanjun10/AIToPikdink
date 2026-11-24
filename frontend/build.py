#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Transform all 20 Stitch code.html screens into a localized, navigable
static frontend.

Keeps the exact Stitch markup/components (high-fidelity replication);
only swaps CDN/remote assets for local copies and wires inter-page navigation.
"""
import os, re

OUT = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(OUT)
DESIGN = os.path.join(ROOT, 'design')

# ---- Stable URL -> local image map (from image_map.tsv) ----
url_map = {}
map_file = os.path.join(OUT, 'image_map.tsv')
with open(map_file, encoding='utf-8') as f:
    for line in f:
        if '\t' in line:
            name, url = line.rstrip('\n').split('\t', 1)
            url_map[url] = f'assets/img/{name}'
print(f'Loaded {len(url_map)} image mappings')

# ---- Shared head replacement ----
LOCAL_HEAD = '''<link href="assets/font_pj.css" rel="stylesheet"/>
<link href="assets/font_ms.css" rel="stylesheet"/>
<link href="assets/app.css" rel="stylesheet"/>
<script src="assets/vendor/tailwind.js"></script>'''

# Stitch screen -> (output filename, page id)
PAGES = {
    's01': ('index.html', 'home'),
    's02': ('news.html', 'news'),
    's03': ('news-detail.html', 'news-detail'),
    's04': ('tutorials.html', 'tutorials'),
    's05': ('tutorial-detail.html', 'tutorial-detail'),
    's06': ('courts.html', 'courts'),
    's07': ('court-detail.html', 'court-detail'),
    's08': ('gear.html', 'gear'),
    's09': ('gear-detail.html', 'gear-detail'),
    's10': ('profile.html', 'profile'),
    's11': ('favorites.html', 'favorites'),
    's12': ('search.html', 'search'),
    's13': ('search-results.html', 'search-results'),
    's14': ('login.html', 'login'),
    's15': ('account.html', 'account'),
    's16': ('about.html', 'about'),
    's17': ('feedback.html', 'feedback'),
    's18': ('image-preview.html', 'image-preview'),
    's19': ('agreement.html', 'agreement'),
    's20': ('components.html', 'components'),
}

# Bottom tab bar data-path -> target (covers both naming schemes used by Stitch)
TAB_TARGETS = {
    'home': 'index.html', 's01-home': 'index.html',
    'news': 'news.html', 's02-news': 'news.html',
    'tutorials': 'tutorials.html', 's04-courses': 'tutorials.html',
    'courts': 'courts.html', 's06-courts': 'courts.html',
    'gear': 'gear.html', 's08-gear': 'gear.html',
    'profile': 'profile.html', 's10-profile': 'profile.html',
}

# Detail pages whose back button needs a no-history fallback
DETAIL_BACK = {'s03', 's05', 's07', 's09', 's11', 's12', 's13', 's14',
               's15', 's16', 's17', 's18', 's19', 's20'}

def localize_head(html):
    pattern = re.compile(
        r'<link[^>]*fonts\.googleapis\.com[^>]*>\s*'
        r'<link[^>]*fonts\.googleapis\.com[^>]*>\s*'
        r'<link[^>]*fonts\.gstatic\.com[^>]*>\s*'
        r'<link[^>]*fonts\.googleapis\.com[^>]*>\s*'
        r'<link[^>]*fonts\.googleapis\.com[^>]*>\s*'
        r'<script src="https://cdn\.tailwindcss\.com"></script>', re.S)
    new, n = pattern.subn(LOCAL_HEAD, html)
    if n == 0:
        new = re.sub(r'<link[^>]*fonts\.(googleapis|gstatic)\.com[^>]*>', '', html)
        new = new.replace('<script src="https://cdn.tailwindcss.com"></script>', LOCAL_HEAD)
    return new

def localize_images(html):
    for url, local in url_map.items():
        html = html.replace(url, local)
    return html

def wire_tabs(html):
    def repl(m):
        path = m.group(1)
        return f'data-path="{path}" href="{TAB_TARGETS.get(path, "index.html")}"'
    return re.sub(r'data-path="([^"]+)"\s+href="#"', repl, html)

def wire_quick_access(html, screen):
    if screen == 's01':
        # 5-grid: 每日资讯 / 匹克教学 / 最美场地 / 装备种草 / 我的收藏
        targets = ['news.html', 'tutorials.html', 'courts.html', 'gear.html', 'favorites.html']
        i = [0]
        def repl(m):
            tag = m.group(0)
            if i[0] < len(targets):
                t = targets[i[0]]; i[0] += 1
                return tag.replace('href="#"', f'href="{t}"')
            return tag
        html = re.sub(r'<a class="flex flex-col items-center gap-1\.5 group" href="#">', repl, html)
    return html

def make_clickable(html, marker, target):
    """Add a location.href onclick to the first element whose exact opening tag
    contains `marker` (a unique class string)."""
    idx = html.find(marker)
    if idx == -1:
        return html
    # find enclosing '<' before marker and the closing '>' after
    start = html.rfind('<', 0, idx)
    end = html.find('>', idx)
    if start == -1 or end == -1:
        return html
    tag = html[start:end + 1]
    if 'onclick=' in tag:
        return html
    newtag = tag.replace('<div ', f'<div role="link" tabindex="0" onclick="location.href=\'{target}\'" ', 1)
    if newtag == tag:
        newtag = tag.replace('<article ', f'<article role="link" tabindex="0" onclick="location.href=\'{target}\'" ', 1)
    if newtag == tag:
        newtag = tag.replace('<button ', f'<button onclick="location.href=\'{target}\'" ', 1)
    return html[:start] + newtag + html[end + 1:]

def wire_cards(html, screen):
    if screen == 's08':
        old = '<div class="group flex flex-col bg-surface-container-lowest/95 backdrop-blur-xl rounded-[22px] overflow-hidden shadow-[0_8px_24px_-4px_rgba(148,163,184,0.15)] transition-all duration-200">'
        new = old.replace('<div ', '<div role="link" tabindex="0" onclick="location.href=\'gear-detail.html\'" ', 1).replace('transition-all', 'cursor-pointer transition-all')
        html = html.replace(old, new)
    if screen == 's01':
        # venue feed card (2nd) -> courts, gear showcase card -> gear detail
        venue_cls = 'rounded-[22px] bg-white/80 backdrop-blur-xl p-3 shadow-[0_8px_24px_-4px_rgba(148,163,184,0.18)] flex flex-col gap-3 group'
        marker = '<div class="' + venue_cls + '">'
        first = html.find(marker)
        second = html.find(marker, first + len(marker)) if first != -1 else -1
        if second != -1:
            rep = f'<div role="link" tabindex="0" onclick="location.href=\'courts.html\'" class="{venue_cls} cursor-pointer">'
            html = html[:second] + rep + html[second + len(marker):]
        gear_cls = 'rounded-[22px] bg-white/80 backdrop-blur-xl p-3.5 shadow-[0_8px_24px_-4px_rgba(148,163,184,0.18)] flex flex-col gap-3 group'
        old = '<div class="' + gear_cls + '">'
        html = html.replace(old, old.replace('<div ', '<div role="link" tabindex="0" onclick="location.href=\'gear-detail.html\'" ', 1).replace('group"', 'group cursor-pointer"'))
    if screen == 's02':
        # news list articles -> news detail
        art = '<article class="bg-surface-container-lowest/90 backdrop-blur-md rounded-2xl p-3.5 shadow-[0_6px_20px_-3px_rgba(15,23,42,0.06)] active:bg-surface-container-low/60 transition-colors">'
        html = html.replace(art, art.replace('<article ', '<article role="link" tabindex="0" onclick="location.href=\'news-detail.html\'" ', 1).replace('transition-colors', 'cursor-pointer transition-colors'))
    if screen == 's04':
        # tutorial cards -> tutorial detail (link the card wrapper containing aspect-video)
        def repl(m):
            tag = m.group(0)
            if 'onclick=' in tag:
                return tag
            return tag.replace('<div ', '<div role="link" tabindex="0" onclick="location.href=\'tutorial-detail.html\'" ', 1)
        html = re.sub(r'<div class="group[^"]*rounded-\[20px\][^"]*">', repl, html)
    if screen == 's06':
        # venue masonry cards -> court detail
        def repl(m):
            tag = m.group(0)
            if 'onclick=' in tag:
                return tag
            return tag.replace('<div ', '<div role="link" tabindex="0" onclick="location.href=\'court-detail.html\'" ', 1)
        html = re.sub(r'<div class="group[^"]*rounded-\[20px\][^"]*">', repl, html)
    if screen == 's10':
        # Favorites tiles are <a> tags with their own classes; route each by
        # the visible label inside it. Menu rows are <button>/<a> as well.
        for label, target in [('资讯收藏', 'favorites.html'), ('教学收藏', 'favorites.html'),
                              ('场地收藏', 'favorites.html'), ('装备收藏', 'favorites.html'),
                              ('账号与绑定', 'account.html'), ('意见反馈', 'feedback.html'),
                              ('关于匹小将', 'about.html')]:
            # Use the LAST occurrence: labels also appear in HTML comments
            # ("<!-- 1. 资讯收藏 -->") before the visible text node.
            pos = html.rfind(label)
            if pos == -1:
                continue
            # Find the nearest opening tag before the label that starts a
            # clickable element (a/button) and has no onclick/href yet.
            candidates = []
            for m in re.finditer(r'<(a|button)\b[^>]*>', html[:pos]):
                candidates.append(m)
            if not candidates:
                continue
            m = candidates[-1]
            tag = m.group(0)
            if 'onclick=' in tag or ('href=' in tag and 'href="#"' not in tag):
                continue
            if tag.startswith('<a'):
                nt = re.sub(r'href="#"', f'href="{target}"', tag, count=1)
                if nt == tag:
                    nt = tag.replace('<a ', f'<a href="{target}" ', 1)
            else:
                nt = tag.replace('<button ', f'<button onclick="location.href=\'{target}\'" ', 1)
            html = html[:m.start()] + nt + html[m.end():]
    if screen == 's11':
        html = html.replace(
            '<button class="w-full h-12 rounded-full bg-text-primary text-surface-container-lowest flex items-center justify-center gap-2 shadow-xl hover:bg-on-surface transition-all active:scale-95">',
            '<button onclick="location.href=\'courts.html\'" class="w-full h-12 rounded-full bg-text-primary text-surface-container-lowest flex items-center justify-center gap-2 shadow-xl hover:bg-on-surface transition-all active:scale-95">')
    if screen == 's12':
        # search input -> search results on Enter; remove autofocus so the
        # static preview is not auto-scrolled away from the top (Stitch image
        # shows the search bar in its natural top position).
        html = html.replace(' autofocus=""', '')
        html = html.replace('type="text"', 'type="text" onkeydown="if(event.key===\'Enter\')location.href=\'search-results.html\'"')
    if screen == 's13':
        # result cards -> corresponding detail
        for label, target in [('教学', 'tutorial-detail.html'), ('资讯', 'news-detail.html'),
                              ('装备', 'gear-detail.html'), ('场地', 'court-detail.html')]:
            pass  # detail routing handled by result type pills below
        # result result rows are <article>/<div> with type label; route by first matching type
        def route_results(html):
            out = []
            pos = 0
            pat = re.compile(r'<div class="[^"]*rounded-\[16px\][^"]*"[^>]*>')
            for m in pat.finditer(html):
                seg = html[m.end():m.end() + 600]
                tgt = None
                for label, t in [('教学', 'tutorial-detail.html'), ('资讯', 'news-detail.html'),
                                 ('装备', 'gear-detail.html'), ('场地', 'court-detail.html')]:
                    if label + ' ·' in seg:
                        tgt = t; break
                if not tgt:
                    continue
                tag = m.group(0)
                if 'onclick=' in tag:
                    continue
                nt = tag.replace('<div ', '<div role="link" tabindex="0" onclick="location.href=\'' + tgt + '\'" ', 1)
                out.append((m.start(), m.end(), nt))
            for s, e, nt in reversed(out):
                html = html[:s] + nt + html[e:]
            return html
        html = route_results(html)
    if screen in ('s03', 's05', 's07'):
        # share/bookmark CTAs keep their own JS; nothing extra to wire
        pass
    if screen == 's14':
        # login card: 暂不登录 -> home; 协议 -> agreement
        html = html.replace('暂不登录，继续浏览', '暂不登录，继续浏览')
        for label, target in [('《用户服务协议》', 'agreement.html'), ('《隐私政策》', 'agreement.html')]:
            idx = html.find(label)
            if idx == -1: continue
            start = html.rfind('<', 0, idx)
            tag = html[start:html.find('>', idx) + 1]
            if 'onclick=' not in tag:
                nt = tag.replace('<a ', '<a href="' + target + '" ', 1) if '<a ' in tag else tag.replace('<button ', '<button onclick="location.href=\'' + target + '\'" ', 1)
                html = html[:start] + nt + html[html.find('>', idx) + 1:]
    if screen == 's20':
        html = html.replace('去逛逛（回首页）', '去逛逛（回首页）')
        pos = html.find('去逛逛（回首页）')
        if pos != -1:
            start = html.rfind('<', 0, pos)
            tag = html[start:html.find('>', pos) + 1]
            if 'onclick=' not in tag:
                nt = tag.replace('<button ', '<button onclick="location.href=\'index.html\'" ', 1)
                html = html[:start] + nt + html[html.find('>', pos) + 1:]
    return html

def inject_back_fallback(html, screen):
    if screen in DETAIL_BACK:
        html = html.replace(
            'onclick="history.back()"',
            "onclick=\"if(history.length>1){history.back()}else{location.href='index.html'}\"")
    return html


# ---- Wire up modules that the Stitch prototypes left inert ----
TOAST_BLOCK = '''<div id="pxj-toast" role="status" aria-live="polite" style="position:fixed;left:50%;bottom:96px;transform:translateX(-50%) translateY(16px);z-index:9999;background:rgba(15,23,42,.92);color:#fff;padding:10px 18px;border-radius:999px;font-size:13px;line-height:1.4;opacity:0;pointer-events:none;transition:opacity .25s,transform .25s;box-shadow:0 10px 30px rgba(0,0,0,.22);white-space:nowrap;max-width:88vw;overflow:hidden;text-overflow:ellipsis"></div>
<script>
function pxjToast(msg){
  var t=document.getElementById('pxj-toast');
  if(!t)return;
  t.textContent=msg;
  t.style.opacity='1';
  t.style.transform='translateX(-50%) translateY(0)';
  clearTimeout(window._pxjToastTimer);
  window._pxjToastTimer=setTimeout(function(){
    t.style.opacity='0';
    t.style.transform='translateX(-50%) translateY(16px)';
  },2000);
}
</script>'''


def _nearest_open_tag(html, pos, pattern):
    last = None
    for m in re.finditer(pattern, html[:pos]):
        last = m
    return last


def _patch_tag(html, m, newtag):
    return html[:m.start()] + newtag + html[m.end():]


def wire_nav_label(html, label, target):
    pos = html.rfind(label)
    if pos < 0:
        return html
    m = _nearest_open_tag(html, pos, r'<(?:a|button)\b[^>]*>')
    if not m:
        return html
    tag = m.group(0)
    if 'onclick=' in tag or ('href=' in tag and 'href="#"' not in tag):
        return html
    if tag.startswith('<a'):
        nt = tag.replace('href="#"', f'href="{target}"', 1) if 'href="#"' in tag else tag.replace('<a ', f'<a href="{target}" ', 1)
    elif tag.startswith('<button'):
        nt = tag[:-1] + f" onclick=\"location.href='{target}'\">"
    else:
        return html
    return _patch_tag(html, m, nt)


def wire_toast_label(html, label, msg):
    pos = html.rfind(label)
    if pos < 0:
        return html
    m = _nearest_open_tag(html, pos, r'<(?:a|button)\b[^>]*>')
    if not m:
        return html
    tag = m.group(0)
    if 'onclick=' in tag:
        return html
    nt = tag[:-1] + f" onclick=\"pxjToast('{msg}')\">"
    return _patch_tag(html, m, nt)


def wire_card_label(html, label, target):
    pos = html.rfind(label)
    if pos < 0:
        return html
    m = _nearest_open_tag(html, pos, r'<div class="[^"]*rounded-\[22px\][^"]*"')
    if not m:
        return html
    tag = m.group(0)
    if 'onclick=' in tag:
        return html
    nt = tag.replace('<div ', f'<div role="link" tabindex="0" onclick="location.href=\'{target}\'" ', 1)
    nt = nt.replace('group"', 'group cursor-pointer"', 1)
    return _patch_tag(html, m, nt)


def inject_toast(html):
    if 'id="pxj-toast"' in html:
        return html
    return html.replace('</body>', TOAST_BLOCK + '</body>')


def wire_missing_modules(html, screen):
    if screen == 's01':
        html = wire_card_label(html, '零基础入门', 'tutorial-detail.html')
        html = wire_card_label(html, '2025城市匹克球公开赛', 'news-detail.html')
        html = wire_nav_label(html, '全部探索', 'news.html')
    elif screen == 's05':
        pos = html.rfind('+ 关注')
        if pos >= 0:
            m = _nearest_open_tag(html, pos, r'<button\b[^>]*>')
            if m and 'onclick=' not in m.group(0):
                tag = m.group(0)
                nt = tag[:-1] + " onclick=\"var on=this.dataset.on==='1';this.dataset.on=on?'0':'1';this.textContent=on?'✚ 关注':'✓ 已关注';pxjToast(on?'已取消关注':'已关注该创作者')\">"
                html = _patch_tag(html, m, nt)
    elif screen == 's10':
        html = wire_nav_label(html, '双端实时同步', 'favorites.html')
        html = wire_nav_label(html, '用户协议与隐私政策', 'agreement.html')
        html = wire_toast_label(html, '退出当前登录', '已退出登录，收藏数据已保留')
    elif screen == 's14':
        html = html.replace('closeModal = () => {', 'closeModal = (dest) => {')
        html = html.replace("sheet.parentElement.style.display = 'none';", "if(dest){location.href=dest;}else{sheet.parentElement.style.display = 'none';}")
        html = html.replace("btnClose.addEventListener('click', closeModal)", "btnClose.addEventListener('click', () => closeModal('index.html'))")
        html = html.replace("btnDismiss.addEventListener('click', closeModal)", "btnDismiss.addEventListener('click', () => closeModal('index.html'))")
        html = html.replace("backdrop.addEventListener('click', closeModal)", "backdrop.addEventListener('click', () => closeModal('index.html'))")
        html = re.sub(r"closeModal\(\);(\s*\},\s*1200\);)", r"closeModal('profile.html');\1", html)
        html = re.sub(r"closeModal\(\);(\s*\},\s*1000\);)", r"closeModal('profile.html');\1", html)
    elif screen == 's15':
        html = wire_toast_label(html, '更换绑定', '原型演示：更换绑定需接入微信授权')
        html = wire_toast_label(html, '去绑定', '原型演示：快捷登录绑定需接入微信授权')
    elif screen == 's17':
        html = wire_toast_label(html, '添加截图', '原型演示：截图上传暂未开放')
    elif screen == 's20':
        html = wire_nav_label(html, '去逛逛（回首页）', 'index.html')
    html = inject_toast(html)
    return html


for screen, (outname, page) in PAGES.items():
    src = os.path.join(DESIGN, screen, 'code.html')
    html = open(src, encoding='utf-8').read()
    html = localize_head(html)
    html = localize_images(html)
    html = wire_tabs(html)
    html = wire_quick_access(html, screen)
    html = wire_cards(html, screen)
    html = inject_back_fallback(html, screen)
    html = wire_missing_modules(html, screen)
    dest = os.path.join(OUT, outname)
    with open(dest, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'{screen} -> {outname}  ({len(html)} chars)')
