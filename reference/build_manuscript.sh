#!/bin/bash
# Builds the coded manuscript: a .docx and a matching .pdf reading copy.
# File numbers match chapter numbers (renamed 10256-638P). Superseded chapters live in chapters/superseded/.
set -e
cd /home/claude/ruth
S=/tmp/claude-0/-home-claude/2a1d3074-161c-5db7-b3ad-f39f29b79237/scratchpad/clean
rm -rf $S; mkdir -p $S
L="front_matter 00_prologue 01_christmond 02_the_man_by_the_fire 03_the_sixth_vogel 04_the_schoolyard 05_lights_on_the_pedernales 06_honolulu 06a_interlude_a 07_december_7 08_unknowns 09_tuskegee 10_the_boy_who_lied 11_the_farm 12_baker_street 13_the_drome 14_avenue_foch 15_ravensbruck 16_the_shots 16a_interlude_b 17_the_widow_at_twenty_one 18_kate 19_hammer_and_chisel 20_the_back_row 21_the_widow_on_the_homeplace 21a_interlude_c 22_the_office_on_main_street 23_letters_to_houston 24_jezebels_paper 25_kenji 26_the_hearing 27_the_bus 28_the_vineyard 29_playoffs 30_the_nativity 31_christmas_eve 32_pallbearers 33_justice 34_the_last_thing_in_the_trunk 34a_what_i_saw 34a2_the_four_drawers 34a3_the_key 34b_the_coal_goes_grey 35_epilogue"
echo "$L" > $S/order.txt
python3 - "$S" $L <<'P'
import re,sys
S=sys.argv[1]
for n in sys.argv[2:]:
    t=open(f'chapters/{n}.md').read()
    t=re.sub(r'[ \t]*\*{0,2}\[VERIFY:?[^\]]*\]\*{0,2}','',t); t=re.sub(r'\n{3,}','\n\n',t)
    open(f'{S}/{n}.md','w').write(t)
P
F=""; for x in $L; do F="$F $S/$x.md"; done
OUT=$(python3 build_docx.py "out/A_Debt_Too_Great_to_Pay_Manuscript" "A Debt Too Great to Pay" $F | tail -1)
python3 - "$OUT" <<'P'
import sys
from docx import Document
from docx.shared import Inches
p=sys.argv[1]; d=Document(p)
for s in d.sections: s.top_margin=Inches(0.8); s.bottom_margin=Inches(0.8)
from docx.shared import Pt
idx=[i for i,q in enumerate(d.paragraphs) if q.text.startswith('Epilogue')]
if idx:
    for q in d.paragraphs[idx[-1]+1:]: q.paragraph_format.space_after=Pt(4); q.paragraph_format.line_spacing=1.15
d.save(p)
P
# Render the PDF reading copy (page numbers baked in, so every viewer shows them right).
R=$S/render; rm -rf $R; mkdir -p $R
timeout 600 soffice --headless --convert-to pdf --outdir $R "$OUT" >/dev/null 2>&1
PDF="${OUT%.docx}.pdf"
cp "$R/$(basename "${OUT%.docx}").pdf" "$PDF"
N=$(pdfinfo "$PDF" | awk '/^Pages/{print $2}')
# Store the real page total as the cached NUMPAGES value, so previewers that skip
# field updates still show the right "of N".
python3 - "$OUT" "$N" <<'P'
import sys,zipfile,shutil,re,os
p,n=sys.argv[1],sys.argv[2]; tmp=p+'.tmp'
zin=zipfile.ZipFile(p); zout=zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED)
for i in zin.infolist():
    b=zin.read(i.filename)
    if i.filename.startswith('word/footer'):
        t=b.decode()
        t=re.sub(r'(NUMPAGES</w:instrText></w:r>.*?fldCharType="separate"/></w:r><w:r>.*?<w:t>)1(</w:t>)',lambda m:m.group(1)+n+m.group(2),t,flags=re.S)
        b=t.encode()
    zout.writestr(i,b)
zout.close(); zin.close(); os.replace(tmp,p)
P
echo "$OUT"
echo "$PDF"
echo "PAGES $N"
