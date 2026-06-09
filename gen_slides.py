#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter
import cairosvg, re, io

W, H = 1080, 1350
CREAM = (250, 250, 248)
INK = (26, 26, 26)
GOLD = (201, 168, 76)
DARK = (15, 17, 23)
LIGHT = (240, 237, 230)
FD = "assets/fonts/"

def F(name, size):
    path = name if name.startswith("/") else FD + name
    return ImageFont.truetype(path, size)

LIB = "/usr/share/fonts/truetype/liberation/"

# fonts
POP_XB = "Poppins-ExtraBold.ttf"
POP_B  = "Poppins-Bold.ttf"
POP_SB = "Poppins-SemiBold.ttf"
POP_M  = "Poppins-Medium.ttf"
POP_R  = "Poppins-Regular.ttf"
SER_B  = LIB + "LibreSerif-Bold.ttf" if False else "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SER_R  = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SER_I  = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"

def wrap_words(draw, words, font, max_w):
    """words: list of (text, color). returns list of lines, each line list of (text,color,w)."""
    lines, cur, cur_w = [], [], 0
    space_w = draw.textlength(" ", font=font)
    for text, color in words:
        w = draw.textlength(text, font=font)
        add = w + (space_w if cur else 0)
        if cur and cur_w + add > max_w:
            lines.append(cur); cur, cur_w = [], 0
            add = w
        cur.append((text, color, w)); cur_w += add
    if cur: lines.append(cur)
    return lines, space_w

def draw_rich(draw, x, y, lines, font, space_w, line_h, align="left", max_w=None):
    asc, desc = font.getmetrics()
    for line in lines:
        line_w = sum(w for _, _, w in line) + space_w * (len(line) - 1)
        if align == "center" and max_w:
            cx = x + (max_w - line_w) / 2
        else:
            cx = x
        for text, color, w in line:
            draw.text((cx, y), text, font=font, fill=color)
            cx += w + space_w
        y += line_h
    return y

def tokens(s, gold_set):
    return [(w, GOLD if w in gold_set else None) for w in s.split(" ")]

def pill(draw, x, y, text, font, fg, bg, pad_x=26, pad_y=14, radius=40):
    tw = draw.textlength(text, font=font)
    asc, desc = font.getmetrics()
    th = asc + desc
    draw.rounded_rectangle([x, y, x + tw + pad_x*2, y + th + pad_y*2], radius=radius, fill=bg)
    draw.text((x + pad_x, y + pad_y - 2), text, font=font, fill=fg)
    return y + th + pad_y*2

# ---------- SLIDE 1 : HOOK photo ----------
def slide1():
    photo = ImageOps.exif_transpose(Image.open("assets/robin_photo.jpeg")).convert("RGB")
    # cover crop to 1080x1350
    scale = W / photo.width
    nh = int(photo.height * scale)
    photo = photo.resize((W, nh), Image.LANCZOS)
    top = int((nh - H) * 0.42)
    photo = photo.crop((0, top, W, top + H))
    img = photo.copy()
    # top gradient scrim
    grad = Image.new("L", (1, H), 0)
    for yy in range(H):
        t = yy / H
        a = max(0, 0.52 - t*1.1)          # dark at top fading
        grad.putpixel((0, yy), int(a*255))
    grad = grad.resize((W, H))
    black = Image.new("RGB", (W, H), (0,0,0))
    img = Image.composite(black, img, grad)
    # bottom subtle scrim for safety (none, keep airy)
    d = ImageDraw.Draw(img)
    M = 90
    # pill label
    pill(d, M, 80, "CAS CONCRET", F(POP_SB, 30), CREAM, GOLD)
    # hook
    font = F(POP_B, 70)
    words = tokens("Comment mon agent IA m'a rapporté 1 400 € pendant que j'étais au sport.", {"1","400","€"})
    lines, sw = wrap_words(d, words, font, W - 2*M)
    # color non-gold white
    lines = [[(t,(c if c else (255,255,255)),w) for t,c,w in ln] for ln in lines]
    draw_rich(d, M, 210, lines, font, sw, 86)
    img.save("test_output/slide_1.png")

def arrow(d, x, y, size, color):
    d.polygon([(x, y), (x, y+size), (x+size*0.95, y+size/2)], fill=color)

def get_logo(name, hexcol, h):
    svg = open(f"assets/logos/{name}.svg").read()
    svg = re.sub(r'fill="#[0-9A-Fa-f]+"', f'fill="{hexcol}"', svg, count=1)
    png = cairosvg.svg2png(bytestring=svg.encode(), output_height=h*3)
    im = Image.open(io.BytesIO(png)).convert("RGBA")
    return im.resize((int(im.width*h/im.height), h), Image.LANCZOS)

def tracked(d, x, y, text, font, fill, sp=5):
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill)
        x += d.textlength(ch, font=font) + sp
    return x

def footer(img, d, hexcol, y, center=False):
    """Discreet 'CONSTRUIT AVEC  [Claude] · [WhatsApp]' footer."""
    lf = F(POP_SB, 23)
    label = "CONSTRUIT AVEC"
    sp = 5
    label_w = sum(d.textlength(c, font=lf)+sp for c in label) - sp
    lx = (W-label_w)//2 if center else 110
    tracked(d, lx, y, label, lf, hexcol, sp)
    h = 40
    claude = get_logo("claude", hexcol, h)
    wa = get_logo("whatsapp", hexcol, h)
    dotf = F(POP_B, 30)
    gap = 22
    dotw = d.textlength("·", font=dotf)
    row_w = claude.width + gap + dotw + gap + wa.width
    rx = int((W-row_w)//2) if center else 110
    ry = y + 46
    img.paste(claude, (rx, ry), claude); rx += claude.width + gap
    d.text((rx, ry+2), "·", font=dotf, fill=hexcol); rx += int(dotw) + gap
    img.paste(wa, (rx, ry), wa)

# ---------- generic cream content slide (vertically centered) ----------
def content_slide(idx, num, big, body, big_font=(SER_B,60), body_font=(POP_R,37)):
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    M = 110
    bf, yf = F(*big_font), F(*body_font)
    bl, bsw = wrap_words(d, [(w, INK) for w in big.split(" ")], bf, W-2*M)
    yl, ysw = wrap_words(d, [(w, (70,70,70)) for w in body.split(" ")], yf, W-2*M)
    big_lh, body_lh = int(big_font[1]*1.34), int(body_font[1]*1.5)
    num_h, rule_gap, big_gap, body_gap = 56, 40, 50, 36
    block = num_h + rule_gap + 6 + big_gap + len(bl)*big_lh + body_gap + len(yl)*body_lh
    y = (H - block)//2 - 30
    d.text((M, y), num, font=F(POP_B, 40), fill=GOLD); y += num_h + rule_gap
    d.rectangle([M, y, M+70, y+6], fill=GOLD); y += 6 + big_gap
    y = draw_rich(d, M, y, bl, bf, bsw, big_lh); y += body_gap
    draw_rich(d, M, y, yl, yf, ysw, body_lh)
    img.save(f"test_output/slide_{idx}.png")

# ---------- SLIDE 4 : DARK result (vertically centered) ----------
def slide4():
    img = Image.new("RGB", (W, H), DARK)
    d = ImageDraw.Draw(img)
    M = 110
    nf = F(POP_XB, 190)
    num = "1 400 €"
    nw = d.textlength(num, font=nf)
    sf, pf = F(SER_R, 40), F(POP_R, 38)
    sl, ssw = wrap_words(d, [(w,LIGHT) for w in "signés pendant 1h30 de sport.".split(" ")], sf, W-2*M)
    sl2, ssw2 = wrap_words(d, [(w,(150,150,150)) for w in "Sans que je touche à rien.".split(" ")], pf, W-2*M)
    label_h, gap1, num_h, gap2, sub1_h, gap3 = 40, 70, 200, 70, len(sl)*62, 24
    block = label_h + gap1 + num_h + gap2 + sub1_h + gap3 + len(sl2)*56
    y = (H - block)//2
    d.text((M, y), "L E   R É S U L T A T", font=F(POP_SB, 30), fill=(150,150,150)); y += label_h + gap1
    d.text((W/2 - nw/2, y), num, font=nf, fill=GOLD); y += num_h + gap2
    y = draw_rich(d, M, y, sl, sf, ssw, 62, align="center", max_w=W-2*M); y += gap3
    draw_rich(d, M, y, sl2, pf, ssw2, 56, align="center", max_w=W-2*M)
    footer(img, d, "#7E8590", 1170, center=True)
    img.save("test_output/slide_4.png")

# ---------- SLIDE 6 : CTA (vertically centered) ----------
def slide6():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    M = 110
    bf, yf, cf = F(SER_B, 58), F(POP_R, 38), F(POP_SB, 40)
    bl, bsw = wrap_words(d, [(w,INK) for w in "Je partage ce que je fais vraiment avec l'IA.".split(" ")], bf, W-2*M)
    yl, ysw = wrap_words(d, [(w,(70,70,70)) for w in "Pas de théorie. Que du concret.".split(" ")], yf, W-2*M)
    big_lh, body_lh = 82, 58
    block = len(bl)*big_lh + 28 + len(yl)*body_lh + 60 + 6 + 50 + 56
    y = (H - block)//2 - 20
    y = draw_rich(d, M, y, bl, bf, bsw, big_lh); y += 28
    y = draw_rich(d, M, y, yl, yf, ysw, body_lh); y += 60
    d.rectangle([M, y, M+70, y+6], fill=GOLD); y += 6 + 50
    arrow(d, M, y+8, 30, GOLD)
    d.text((M+48, y), "Abonne-toi si ça te parle.", font=cf, fill=GOLD)
    footer(img, d, "#8A8A8A", 1170, center=False)
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
