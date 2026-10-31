#!/usr/bin/env python3
"""Build a coded .docx from Markdown with John's footer rule.

Usage: build_docx.py OUT_BASENAME TITLE INPUT.md [INPUT2.md ...]
The save code is computed from the America/Chicago clock at run time and goes in
exactly two places: the filename and the bottom-left footer (Page X of Y right).
"""
import subprocess, sys, os, tempfile
from datetime import datetime
from zoneinfo import ZoneInfo
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def save_code():
    now = datetime.now(ZoneInfo("America/Chicago"))
    hour = now.strftime("%I").lstrip("0")
    ampm = "A" if now.strftime("%p") == "AM" else "P"
    return f"{now.month}{now.strftime('%d')}{str(now.year)[-1]}-{hour}{now.strftime('%M')}{ampm}"

def add_field(paragraph, instr, size):
    parts = [("begin", None), ("instr", instr), ("separate", None), ("text", "1"), ("end", None)]
    for tag, text in parts:
        r = paragraph.add_run(); r.font.size = size; r.font.color.rgb = RGBColor(0x80, 0x80, 0x80)
        if tag == "instr":
            el = OxmlElement("w:instrText"); el.set(qn("xml:space"), "preserve"); el.text = text
        elif tag == "text":
            el = OxmlElement("w:t"); el.text = text
        else:
            el = OxmlElement("w:fldChar"); el.set(qn("w:fldCharType"), tag)
        r._r.append(el)

def main():
    base, title, inputs = sys.argv[1], sys.argv[2], sys.argv[3:]
    code = save_code()
    outdir = os.path.dirname(base) or "."
    out = f"{base}-{code}.docx"
    with tempfile.TemporaryDirectory() as td:
        combined = os.path.join(td, "all.md")
        with open(combined, "w") as f:
            for i, p in enumerate(inputs):
                if i:
                    f.write("\n\n```{=openxml}\n<w:p><w:r><w:br w:type=\"page\"/></w:r></w:p>\n```\n\n")
                f.write(open(p).read())
        tmp = os.path.join(td, "tmp.docx")
        subprocess.run(["pandoc", combined, "-f", "markdown+raw_attribute", "-o", tmp,
                        "--metadata", f"pagetitle={title}"], check=True)
        doc = Document(tmp)
    # Base styles: book-like
    st = doc.styles["Normal"]; st.font.name = "Georgia"; st.font.size = Pt(12)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "Georgia")
    bystyle = {x.name.lower(): x for x in doc.styles if x.name}
    for name in ("body text", "first paragraph", "compact"):
        s = bystyle.get(name)
        if s is not None:
            s.font.name = "Georgia"; s.font.size = Pt(12)
            s.paragraph_format.space_after = Pt(8); s.paragraph_format.line_spacing = 1.25
    for name, size in (("title", 26), ("heading 1", 20), ("heading 2", 15), ("heading 3", 13)):
        s = bystyle.get(name)
        if s is not None:
            s.font.name = "Georgia"; s.font.size = Pt(size)
            s.font.color.rgb = RGBColor(0x22, 0x30, 0x26)
            rf = s.element.rPr.rFonts
            for a in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
                rf.set(qn(a), "Georgia")
            for a in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
                if rf.get(qn(a)) is not None:
                    del rf.attrib[qn(a)]
    fs = bystyle.get("footer")
    if fs is not None:
        fs.font.size = Pt(8)
    for sec in doc.sections:
        sec.page_width = Inches(8.5); sec.page_height = Inches(11)
        sec.left_margin = sec.right_margin = Inches(1)
        sec.top_margin = sec.bottom_margin = Inches(1)
        footer = sec.footer
        p = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
        p.text = ""
        usable = sec.page_width - sec.left_margin - sec.right_margin
        p.paragraph_format.tab_stops.add_tab_stop(usable, WD_TAB_ALIGNMENT.RIGHT)
        r = p.add_run(code); r.font.size = Pt(8); r.font.color.rgb = RGBColor(0x80, 0x80, 0x80)
        r = p.add_run("\tPage "); r.font.size = Pt(8); r.font.color.rgb = RGBColor(0x80, 0x80, 0x80)
        add_field(p, "PAGE", Pt(8))
        r = p.add_run(" of "); r.font.size = Pt(8); r.font.color.rgb = RGBColor(0x80, 0x80, 0x80)
        add_field(p, "NUMPAGES", Pt(8))
    if os.path.exists(out):
        raise SystemExit(f"refusing to overwrite {out}")
    doc.save(out)
    print(out)

if __name__ == "__main__":
    main()
