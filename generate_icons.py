from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(size, output_path):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Outer squircle / rounded rectangle with gradient effect
    radius = int(size * 0.22)
    padding = int(size * 0.04)
    
    # Base gradient background simulation
    steps = 100
    for i in range(steps):
        ratio = i / float(steps)
        r = int(56 + (192 - 56) * ratio)
        g = int(189 + (132 - 189) * ratio)
        b = int(248 + (252 - 248) * ratio)
        color = (r, g, b, 255)
    
    # Draw rounded rectangle background
    # Gradient simulation from top-left to bottom-right
    bg_img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    bg_draw = ImageDraw.Draw(bg_img)
    
    # Draw smooth gradient in background
    for y in range(size):
        for x in range(size):
            dist = (x + y) / (2.0 * size)
            # from #0ea5e9 (14, 165, 233) to #8b5cf6 (139, 92, 246)
            r = int(14 + (139 - 14) * dist)
            g = int(165 + (92 - 165) * dist)
            b = int(233 + (246 - 233) * dist)
            bg_draw.point((x, y), fill=(r, g, b, 255))
            
    # Mask rounded rectangle
    mask = Image.new("L", (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([padding, padding, size - padding, size - padding], radius=radius, fill=255)
    
    # Composite background
    final_img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    final_img.paste(bg_img, (0, 0), mask=mask)
    draw_final = ImageDraw.Draw(final_img)
    
    # Draw inner symbol: Stylized Markdown 'M' and Annotation Speech Bubble / Pen
    # Dark obsidian central badge
    inner_pad = int(size * 0.18)
    inner_mask = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    inner_draw = ImageDraw.Draw(inner_mask)
    inner_draw.rounded_rectangle([inner_pad, inner_pad, size - inner_pad, size - inner_pad], radius=int(radius * 0.7), fill=(10, 13, 18, 230))
    final_img.paste(inner_mask, (0, 0), mask=inner_mask)
    
    # Draw 'A' / Antigravity icon + comment dots in white/cyan
    draw_final = ImageDraw.Draw(final_img)
    w = size
    # Draw Markdown / Antigravity shape
    # Antigravity stylized "A" / delta symbol
    p1 = (w * 0.5, w * 0.28)
    p2 = (w * 0.32, w * 0.68)
    p3 = (w * 0.68, w * 0.68)
    
    line_w = max(3, int(w * 0.055))
    draw_final.line([p1, p2], fill=(56, 189, 248, 255), width=line_w)
    draw_final.line([p1, p3], fill=(192, 132, 252, 255), width=line_w)
    draw_final.line([(w * 0.38, w * 0.55), (w * 0.62, w * 0.55)], fill=(255, 255, 255, 255), width=line_w)
    
    # Draw speech bubble dot / annotation badge at top-right
    bubble_r = int(w * 0.09)
    bx = int(w * 0.72)
    by = int(w * 0.28)
    draw_final.ellipse([bx - bubble_r, by - bubble_r, bx + bubble_r, by + bubble_r], fill=(250, 204, 21, 255))
    # Little inner dot in bubble
    draw_final.ellipse([bx - int(bubble_r*0.4), by - int(bubble_r*0.4), bx + int(bubble_r*0.4), by + int(bubble_r*0.4)], fill=(10, 13, 18, 255))
    
    final_img.save(output_path, "PNG")
    print(f"Generated: {output_path} ({size}x{size})")

create_icon(192, "icon-192.png")
create_icon(512, "icon-512.png")
create_icon(180, "apple-touch-icon.png")
create_icon(64, "favicon.png")
