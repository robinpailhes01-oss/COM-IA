#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont, ImageOps
import cairosvg, re, io

W, H = 1080, 1350
CREAM = (250, 250, 248)
INK = (26, 26, 26)
GOLD = (201, 168, 76)
DARK = (15, 17, 23)
LIGHT = (240, 237, 230)
GREY = (110, 110, 110)
FD = "assets/fonts/"

def pop(name, size):
    return ImageFont.truetype(FD + name, size)
POP_XB = lambda s: pop("Poppins-ExtraBold.ttf", s)
POP_B  = lambda s: pop("Poppins-Bold.ttf", s)
POP_SB = lambda s: pop("Poppins-SemiBold.ttf", s)
POP_R  = lambda s: pop("Poppins-Regular.ttf", s)

def serif(size, weight=700, italic=False):
    f = ImageFont.truetype(FD + ("PlayfairDisplay-Italic.ttf" if italic else "PlayfairDisplay.ttf"), size)
    try: f.set_variation_by_axes([weight])
    except Exception: pass
    return f

# ---------- token rich text (per-word font + color) ----------
def wrap_tokens(d, tokens, max_w):
    lines, cur, cur_w = [], [], 0
    for text, font, color in tokens:
        w = d.textlength(text, font=font)
        sp = d.textlength(" ", font=font)
        add = w + (sp if cur else 0)
        if cur and cur_w + add > max_w:
            lines.append(cur); cur, cur_w = [], 0; add = w
        cur.append((text, font, color, w, sp)); cur_w += add
    if cur: lines.append(cur)
    return lines

def draw_tokens(d, x, y, lines, line_h, align="left", max_w=None):
    for line in lines:
        lw = sum(w for *_, w, _ in line) + sum(line[i][4] for i in range(len(line)-1))
        cx = x + (max_w - lw)/2 if (align == "center" and max_w) else x
        for text, font, color, w, sp in line:
            d.text((cx, y), text, font=font, fill=color); cx += w + sp
        y += line_h
    return y

def wrap_words(d, words, font, max_w):
    return wrap_tokens(d, [(w, font, c) for w, c in words], max_w)

# ---------- logos ----------
def get_logo(name, hexcol, h):
    svg = open(f"assets/logos/{name}.svg").read()
    svg = re.sub(r'fill="#[0-9A-Fa-f]+"', f'fill="{hexcol}"', svg, count=1)
    png = cairosvg.svg2png(bytestring=svg.encode(), output_height=h*3)
    im = Image.open(io.BytesIO(png)).convert("RGBA")
    return im.resize((int(im.width*h/im.height), h), Image.LANCZOS)

def tracked(d, x, y, text, font, fill, sp=5):
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill); x += d.textlength(ch, font=font) + sp
    return x

def footer(img, d, hexcol, y, center=False):
    lf = POP_SB(23); label = "CONSTRUIT AVEC"; sp = 5
    lw = sum(d.textlength(c, font=lf)+sp for c in label) - sp
    lx = (W-lw)//2 if center else 110
    tracked(d, lx, y, label, lf, hexcol, sp)
    h = 40; claude = get_logo("claude", hexcol, h); wa = get_logo("whatsapp", hexcol, h)
    dotf = POP_B(30); gap = 22; dotw = d.textlength("·", font=dotf)
    row = claude.width + gap + dotw + gap + wa.width
    rx = int((W-row)//2) if center else 110; ry = y + 46
    img.paste(claude, (rx, ry), claude); rx += claude.width + gap
    d.text((rx, ry+2), "·", font=dotf, fill=hexcol); rx += int(dotw) + gap
    img.paste(wa, (rx, ry), wa)

def arrow(d, x, y, size, color):
    d.polygon([(x, y), (x, y+size), (x+size*0.95, y+size/2)], fill=color)

# ---------- SLIDE 1 : photo cover, editorial serif ----------
def slide1():
    photo = ImageOps.exif_transpose(Image.open("assets/robin_photo.jpeg")).convert("RGB")
    scale = W / photo.width
    photo = photo.resize((W, int(photo.height*scale)), Image.LANCZOS)
    top = int((photo.height - H) * 0.42); photo = photo.crop((0, top, W, top + H))
    grad = Image.new("L", (1, H), 0)
    for yy in range(H):
        grad.putpixel((0, yy), int(max(0, 0.48 - (yy/H)*1.25) * 255))
    img = Image.composite(Image.new("RGB", (W, H), (0,0,0)), photo, grad.resize((W, H)))
    d = ImageDraw.Draw(img); M = 90
    # kicker + rule
    kf = POP_SB(28)
    tracked(d, M, 86, "CAS CONCRET", kf, (255,255,255), 6)
    d.rectangle([M, 138, M+230, 141], fill=(255,255,255))
    # headline serif italic mix
    up = lambda s: serif(66, 700, False); it = lambda s: serif(66, 700, True)
    W_ = (255,255,255)
    toks = [
        ("Comment", up(0), W_), ("mon", up(0), W_), ("agent", it(0), W_), ("IA", it(0), W_),
        ("m'a", up(0), W_), ("rapporté", it(0), W_), ("1 400 €", it(0), GOLD),
        ("pendant", up(0), W_), ("que", up(0), W_), ("j'étais", up(0), W_),
        ("au", it(0), W_), ("sport", it(0), W_),
    ]
    lines = wrap_tokens(d, toks, W - 2*M)
    draw_tokens(d, M, 180, lines, 90)
    img.save("test_output/slide_1.png")

# ---------- cream content (serif headline + sans body), centered ----------
def content_slide(idx, num, big, body):
    img = Image.new("RGB", (W, H), CREAM); d = ImageDraw.Draw(img); M = 110
    bf = serif(60, 700); yf = POP_R(37)
    bl = wrap_words(d, [(w, INK) for w in big.split(" ")], bf, W-2*M)
    yl = wrap_words(d, [(w, GREY) for w in body.split(" ")], yf, W-2*M)
    big_lh, body_lh = 80, 56
    block = 56 + 40 + 6 + 50 + len(bl)*big_lh + 36 + len(yl)*body_lh
    y = (H - block)//2 - 20
    d.text((M, y), num, font=POP_B(40), fill=GOLD); y += 56 + 40
    d.rectangle([M, y, M+70, y+6], fill=GOLD); y += 6 + 50
    y = draw_tokens(d, M, y, bl, big_lh); y += 36
    draw_tokens(d, M, y, yl, body_lh)
    img.save(f"test_output/slide_{idx}.png")

# ---------- dark result ----------
def slide4():
    img = Image.new("RGB", (W, H), DARK); d = ImageDraw.Draw(img); M = 110
    nf = serif(200, 800); num = "1 400 €"; nw = d.textlength(num, font=nf)
    sf = serif(44, 600, italic=True); pf = POP_R(36)
    sl = wrap_words(d, [(w, LIGHT) for w in "signés pendant 1h30 de sport.".split(" ")], sf, W-2*M)
    sl2 = wrap_words(d, [(w, (150,150,150)) for w in "Sans que je touche à rien.".split(" ")], pf, W-2*M)
    block = 40 + 70 + 210 + 70 + len(sl)*64 + 26 + len(sl2)*54
    y = (H - block)//2 - 20
    tracked(d, M, y, "LE RÉSULTAT", POP_SB(28), (150,150,150), 6); y += 40 + 70
    d.text((W/2 - nw/2, y), num, font=nf, fill=GOLD); y += 210 + 70
    y = draw_tokens(d, M, y, sl, 64, align="center", max_w=W-2*M); y += 26
    draw_tokens(d, M, y, sl2, 54, align="center", max_w=W-2*M)
    footer(img, d, "#7E8590", 1175, center=True)
    img.save("test_output/slide_4.png")

# ---------- CTA ----------
def slide6():
    img = Image.new("RGB", (W, H), CREAM); d = ImageDraw.Draw(img); M = 110
    bf = serif(58, 700); yf = POP_R(38); cf = POP_SB(40)
    bl = wrap_words(d, [(w, INK) for w in "Je partage ce que je fais vraiment avec l'IA.".split(" ")], bf, W-2*M)
    yl = wrap_words(d, [(w, GREY) for w in "Pas de théorie. Que du concret.".split(" ")], yf, W-2*M)
    block = len(bl)*82 + 28 + len(yl)*58 + 60 + 6 + 50 + 56
    y = (H - block)//2 - 60
    y = draw_tokens(d, M, y, bl, 82); y += 28
    y = draw_tokens(d, M, y, yl, 58); y += 60
    d.rectangle([M, y, M+70, y+6], fill=GOLD); y += 6 + 50
    arrow(d, M, y+8, 30, GOLD); d.text((M+48, y), "Abonne-toi si ça te parle.", font=cf, fill=GOLD)
    footer(img, d, "#8A8A8A", 1175, center=False)
    img.save("test_output/slide_6.png")

slide1()
content_slide(2, "01", "J'étais à la salle. Téléphone dans le casier.",
              "Pendant ce temps, un agent que j'ai configuré tournait tout seul.")
content_slide(3, "02", "Un prospect m'écrit.",
              "L'agent répond, pose les bonnes questions, envoie le devis. Sans moi.")
slide4()
content_slide(5, "03", "C'est pas magique.",
              "J'ai juste pris le temps de bien le configurer une fois. Maintenant il bosse même quand je n'y suis pas.")
slide6()
print("done")
