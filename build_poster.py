#!/usr/bin/env python3
"""Draw the 24 November 2026 world-news poster (1024x1024 PNG).

One-day newspaper front page: navy masthead, six flat-pictogram story
cards in a 2x3 grid, navy footer ticker. Pure Pillow, no network.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 231)
NAVY = (20, 33, 61)
GOLD = (233, 196, 106)
WHITE = (255, 255, 255)
INK = (30, 30, 30)
GREY = (90, 88, 82)
CARD_LINE = (214, 208, 194)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def centre(draw, y, text, fnt, fill, cx=W // 2):
    draw.text((cx, y), text, font=fnt, fill=fill, anchor="ma")


def draw_globe(d, cx, cy):
    r = 34
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(42, 157, 143))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(20, 33, 61), width=3)
    d.arc([cx - r * 0.45, cy - r, cx + r * 0.45, cy + r], 90, 270,
          fill=(233, 196, 106), width=4)
    d.arc([cx - r * 0.45, cy - r, cx + r * 0.45, cy + r], 270, 90,
          fill=(233, 196, 106), width=4)
    d.line([cx - r, cy, cx + r, cy], fill=(233, 196, 106), width=4)
    crack = [(cx - 8, cy - r + 6), (cx + 10, cy - r * 0.4), (cx - 6, cy),
             (cx + 12, cy + r * 0.45), (cx - 2, cy + r - 6)]
    d.line(crack, fill=(214, 48, 49), width=5, joint="curve")


def draw_warning(d, cx, cy):
    s = 36
    d.polygon([(cx, cy - s), (cx + s, cy + s * 0.75), (cx - s, cy + s * 0.75)],
              fill=(214, 48, 49), outline=(20, 33, 61))
    d.rectangle([cx - 4, cy - s * 0.45, cx + 4, cy + s * 0.25], fill=WHITE)
    d.ellipse([cx - 5, cy + s * 0.4, cx + 5, cy + s * 0.55], fill=WHITE)


def draw_ship(d, cx, cy):
    d.rectangle([cx - 52, cy - 26, cx - 18, cy + 2], fill=(42, 157, 143))
    d.rectangle([cx - 14, cy - 26, cx + 20, cy + 2], fill=(233, 196, 106))
    d.rectangle([cx + 24, cy - 26, cx + 52, cy + 2], fill=(214, 48, 49))
    d.polygon([(cx - 62, cy + 2), (cx + 62, cy + 2), (cx + 48, cy + 26),
               (cx - 48, cy + 26)], fill=(38, 84, 124))
    for i, x in enumerate(range(cx - 56, cx + 52, 22)):
        d.line([x, cy + 36, x + 12, cy + 36],
               fill=(38, 84, 124), width=4)


def draw_train(d, cx, cy):
    d.rounded_rectangle([cx - 56, cy - 30, cx + 56, cy + 28], radius=14,
                        fill=(230, 126, 34))
    d.rounded_rectangle([cx - 44, cy - 20, cx + 44, cy + 2], radius=6,
                        fill=(20, 33, 61))
    d.line([cx, cy - 20, cx, cy + 2], fill=(230, 126, 34), width=4)
    d.ellipse([cx - 34, cy + 10, cx - 18, cy + 24], fill=(233, 196, 106))
    d.ellipse([cx + 18, cy + 10, cx + 34, cy + 24], fill=(233, 196, 106))
    d.line([cx - 70, cy + 34, cx + 70, cy + 34], fill=(90, 88, 82), width=4)
    d.line([cx - 70, cy + 42, cx + 70, cy + 42], fill=(90, 88, 82), width=4)


def draw_factory(d, cx, cy):
    d.rectangle([cx - 56, cy - 6, cx + 56, cy + 30], fill=(70, 70, 78))
    d.rectangle([cx - 46, cy - 30, cx - 28, cy - 6], fill=(70, 70, 78))
    d.rectangle([cx - 10, cy - 40, cx + 8, cy - 6], fill=(70, 70, 78))
    for x in (-40, -2, 36):
        d.rectangle([cx + x, cy + 6, cx + x + 12, cy + 18], fill=(233, 196, 106))
    flame = [(cx + 34, cy - 34), (cx + 46, cy - 12), (cx + 56, cy - 30),
             (cx + 62, cy - 8), (cx + 48, cy + 2), (cx + 36, cy - 10)]
    d.polygon(flame, fill=(230, 126, 34))


def draw_crowd(d, cx, cy):
    for dx, dy, col in [(-38, 8, (106, 90, 205)), (-12, -2, (142, 68, 173)),
                        (14, 8, (106, 90, 205)), (40, -2, (142, 68, 173))]:
        d.ellipse([cx + dx - 11, cy + dy - 11, cx + dx + 11, cy + dy + 11],
                  fill=col)
        d.pieslice([cx + dx - 16, cy + dy + 8, cx + dx + 16, cy + dy + 40],
                   180, 360, fill=col)
    d.rectangle([cx - 52, cy - 42, cx - 22, cy - 20], fill=(20, 33, 61))
    d.line([cx - 37, cy - 20, cx - 37, cy + 4], fill=(20, 33, 61), width=4)
    d.rectangle([cx + 22, cy - 42, cx + 52, cy - 20], fill=(214, 48, 49))
    d.line([cx + 37, cy - 20, cx + 37, cy + 4], fill=(214, 48, 49), width=4)


STORIES = [
    ("NO DEAL AT COP31",
     "Climate talks in Antalya end in deadlock as a fossil-fuel deal stalls.",
     (42, 157, 143), draw_globe),
    ("MOSCOW WARNS ESTONIA",
     "\u201cOpen war\u201d threat as Estonia plans to close its border with Russia.",
     (214, 48, 49), draw_warning),
    ("25 SEAFARERS KILLED",
     "UN counts the dead after attacks near the Strait of Hormuz.",
     (38, 84, 124), draw_ship),
    ("$1.6BN FOR NEPAL",
     "India pledges rebuild aid; a new Ayodhya\u2013Janakpur train opens.",
     (230, 126, 34), draw_train),
    ("FACTORY FIRE IN BANTEN",
     "Rescue under way in Indonesia after a deadly blaze.",
     (214, 48, 49), draw_factory),
    ("LISBON PROTESTS",
     "Thousands march against the rising cost of living.",
     (142, 68, 173), draw_crowd),
]


def build(path):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Masthead
    d.rectangle([0, 0, W, 148], fill=NAVY)
    d.rectangle([0, 148, W, 152], fill=GOLD)
    centre(d, 16, "TUESDAY, 24 NOVEMBER 2026", font(BOLD, 40), WHITE)
    centre(d, 66, "THE WORLD IN ONE DAY", font(BOLD, 34), GOLD)
    centre(d, 112, "SIX STORIES THAT DEFINED THE DAY",
           font(BOLD, 17), (200, 210, 225))
    centre(d, 164, "Six stories that defined the day \u2014 from Antalya to Lisbon",
           font(REG, 21), GREY)

    # Grid: 2 cols x 3 rows
    gx, gy, gap = 24, 196, 16
    cw = (W - 2 * gx - gap) // 2
    ch = (938 - gy - 2 * gap) // 3
    hl_font = font(BOLD, 26)
    cap_font = font(REG, 19)
    for i, (head, cap, accent, icon) in enumerate(STORIES):
        x = gx + (i % 2) * (cw + gap)
        y = gy + (i // 2) * (ch + gap)
        d.rounded_rectangle([x, y, x + cw, y + ch], radius=10, fill=WHITE,
                            outline=CARD_LINE, width=2)
        d.rectangle([x, y, x + cw, y + 8], fill=accent)
        icon(d, x + cw // 2, y + 60)
        # headline, centred, up to 2 lines
        lines = wrap(d, head, hl_font, cw - 36)
        ty = y + 108
        for ln in lines[:2]:
            centre(d, ty, ln, hl_font, INK, cx=x + cw // 2)
            ty += 30
        # caption
        clines = wrap(d, cap, cap_font, cw - 44)
        ty = y + 108 + 30 * min(len(lines), 2) + 4
        for ln in clines[:3]:
            centre(d, ty, ln, cap_font, GREY, cx=x + cw // 2)
            ty += 23

    # Footer ticker (auto-fit so the full line stays on screen)
    d.rectangle([0, 952, W, H], fill=NAVY)
    d.rectangle([0, 952, W, 956], fill=GOLD)
    ticker = ("ALSO TODAY: Pant hits 128 in the Wellington Test \u2022 "
              "Verstappen wins the Las Vegas Grand Prix \u2022 Ferrari unveils "
              "two new 296 models")
    tsize = 18
    while d.textlength(ticker, font=font(BOLD, tsize)) > W - 24 and tsize > 10:
        tsize -= 1
    centre(d, 970, ticker, font(BOLD, tsize), WHITE)

    img.save(path, "PNG", optimize=True)
    return path


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    build(out)
    print(out, os.path.getsize(out), "bytes")
