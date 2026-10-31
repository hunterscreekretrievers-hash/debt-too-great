# Brief 34: Full panel + line-by-line edit on manuscript 10306-835P (406 pages, ~147,000 words)

John, Oct 30, 2026, 8:40 p.m.: "run another full analysis, and add some additional readers, and a couple who are authors to review, page by page, line by line and word by word, take your time to notice any issues, correct grammar or wordsmith, and improve for ranking and readability."

You own ONE segment of the book (named in your prompt). Two jobs, in this order.

## Job 1: Line-by-line edit, applied in place (your segment's chapter files ONLY)
Read every line of every file in your segment in /home/claude/ruth/chapters/. A full pre-edit backup of all chapters is at /home/claude/ruth/backups/pre_fullpanel_1793410824/. Read /home/claude/ruth/01_story_bible.md first: CURRENT FACTS at the top and every dated entry from 10/30/26 at the bottom. They govern facts and John's decisions.

Fix, word by word:
- Grammar, punctuation, spelling, tense slips, agreement, dialogue punctuation, repeated words in close range ("wind... wind" -> "wind... gusts"), unclear antecedents, flat or vague words where a vivid, exact one paints the picture (Nicholas Sparks warmth, highly visual, concrete nouns, sensory detail). Rare words are fine when they carry the true meaning better.
- Readability: a sentence that trips the ear, an unclear who-is-speaking, a time jump with no anchor, a name the reader can't place. Chapter openings and closings that could hook harder (a stronger first or last line, never neon).
- Ranking: clarity, page-turn pull, emotional beats landing, searchable facts stated cleanly.
- Every house grammar rule below, on every sentence in your segment (fix existing violations too, not only your new ones).
Limits: light hand. No new scenes, no new facts, no new characters, no cuts of substance, no merged or deleted paragraphs. Never touch: the John verbatim line in Ch 34 ("Globalists who serve no flag..."), any dog-man letter or line, the Ch 23 lawsuit facts and every quote from Adam, Peter, Amanda, the line producer or the bookkeepers, Scripture (KJV), dated real-world quotes, [JOHN]-tagged lines, documented facts woven in today, Lily's unanswered Cu Chi question. Edit by exact-string replacement in Python with assert count==1. Log every change (old -> new, one-line reason) to /home/claude/ruth/audit/fullpanel_10306/edits_<segment>.md with a count per chapter. Do not rebuild the manuscript. Do not edit the story bible, back matter or any file outside your segment.

## Job 2: The panel scores your segment (after your edits)
Seats (score each 1-10 for your segment, one or two sentences each, quote the line that moved them most):
- The 15 standing perspectives from earlier panels: conservative Christian reader, pastor, Hill Country rancher, WWII historian, skeptic/"do your own research" reader, book-club leader, Black church reader, veteran, nurse, teacher, teenager (15), grandmother, acquisitions editor at a Christian house, faith-film producer, general-market literary critic (general-market score kept OUT of the average).
- New readers: a Gold Star mother; a homeschooling mom of five; a retired Army chaplain; a San Antonio paramedic; a German-Texan from Fredericksburg whose family came over in the 1840s; an audiobook narrator (reading for the ear).
- Two author seats: (A) a bestselling inspirational novelist in the Nicholas Sparks tradition, reading for heart, image and page-turn; (B) a bestselling WWII historical novelist in the vein of *The Nightingale* and *All the Light We Cannot See*, reading for period truth, structure and sentence craft. Each author names the three best lines in the segment and the three weakest, and says what they would change.
Report: average in John's market (general-market critic separate), tears and laughs moments you notice, the pages where a reader would skim, and "Suggestions to improve," ranked by impact, each naming the chapter and quoting the passage, that you did NOT apply because they exceed a light hand. Baseline for comparison: Panel 7 on 10306-313P scored 8.57 in John's market (/home/claude/ruth/audit/panels_7/matrix_rescore_10306-313P.md).
Write it to /home/claude/ruth/audit/fullpanel_10306/panel_<segment>.md.

File names vs printed chapters: `21a_interlude_c` prints as The Cabin: III; `34a_what_i_saw` = Ch 35, `34a2_the_four_drawers` = Ch 36, `34a3_the_key` = Ch 37, `34b_the_coal_goes_grey` = Ch 38, `35_epilogue` = Epilogue. Cabin I = 06a, Cabin II = 16a.

## John's settled rules (every seat obeys)
Content: the convictions are the author's and settled (Islam as an ideology of conquest, globalists, deep state, COVID, Big Pharma, Jekyll Island, Paperclip, Building Seven, Fourth Reich, Yalta, admiralty flag, every conviction Ruth or Isaiah speaks). Judge writing, placement, pacing, reader reaction. Never recommend softening, hedging, balancing or cutting a conviction; never diminish the Islamic threat; no both-sides lines. Clues, not neon; no author's note. A named source is enough; never cite Snopes, PolitiFact, Lead Stories, Check Your Fact, CNN or MS NOW. The dog man (John Tate) stays unnamed; his letters are his verbatim words; never invent lines for him. Peter, Amanda, Adam first names only; the financier unnamed; the director's daughter, line producer and bookkeepers unnamed. Living people get only their own dated words and acts. KJV verbatim. Dates less important than facts. Isaiah's long sentences fit him (a man who talks in the back of an ambulance); do not break them. Nazi comparisons that fit are fine. Never suggest shortening at the cost of substance. Never suggest a lawyer. Business Table guards anything that makes John, his dogs or kennel look bad to puppy clients; earlier holds cleared.
House grammar for every proposed line: no sentence ends on a preposition or particle (phrasal verbs NOT exempt); no dangling verb ending; no "And" openers (KJV exempt); no bare-pronoun subjects leaning on the prior sentence; no em dashes; never the word "draft."
Market: John's market is conservative, faith-and-family, independent and Christian publishing, faith film, and the skeptic reader. General-market view separately, out of the averages.


Ruth's surname is Vellmer (never Vogel, except Jan Vogel in back matter). Lawsuit facts are court-established; never frame them as "John's view."

## Reply
Reply with: edits count per chapter, your segment's John's-market average, the two author scores, the top five unapplied suggestions (one line each), and both file paths.
