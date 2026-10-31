# A Debt Too Great to Pay — John Tate's novel

This repository holds the working chapters of John Tate's novel. It is not software. The job here is editing prose.

## What is here
- `chapters/` holds one Markdown file per chapter, in reading order by filename (front_matter first, 35_epilogue last). File names vs printed chapters: `06a_interlude_a` = The Cabin: I; `16a_interlude_b` = The Cabin: II; `21a_interlude_c` = The Cabin: III; `34a_what_i_saw` = Ch 35; `34a2_the_four_drawers` = Ch 36; `34a3_the_key` = Ch 37; `34b_the_coal_goes_grey` = Ch 38; `35_epilogue` = Epilogue. Build order is the `L=` list in `reference/build_manuscript.sh`.
- `reference/01_story_bible.md` is the story bible. **CURRENT FACTS at the top and every dated entry at the bottom (especially 10/30/26 and 10/31/26) override everything else.** Read it before editing.
- `reference/12_rabbit_holes.md` is the back matter of documented facts readers will search.
- `reference/house_rules_brief_34.md` is the last full-panel brief; its house rules and protected list apply in full.
- `reports/` is where the readers' reports and the edit log go.

## The story in one paragraph
Fictional Martinsburg, county seat of Pedernales County (the real Fredericksburg, Texas, never named). Christmas 2026: Isaiah Mayfield, about eighty, a retired Army medic and ambulance man, tells his grandchildren Marcus (15), Lily and Ben, with Ruthie and Daniel present, the story of Ruth Vellmer (1924 to Christmas Eve 2013): a German-Texan girl, Pearl Harbor, her secret 1944 marriage to Sam Mayfield (Tuskegee airman), SOE courier in France, Avenue Foch, Ravensbrück beside Corrie and Betsie ten Boom, home to forty years as a rural mail carrier who sent anonymous R. V. money orders, and her last season in 2013. The dog man who brings her Honey is the author himself and stays unnamed.

## THE JOB: the whole-book read
John asked for every panel member to read the complete manuscript and fix every spot they see. Earlier panels each read one-sixth of the book; this pass reads it whole, so it catches what only shows across chapters.

### Phase 1: six whole-book readers (read-only, run in parallel as subagents)
Each reader reads **every chapter, cover to cover, in build order**, plus the story bible's CURRENT FACTS and 10/30 and 10/31 entries. Each writes `reports/reader_<N>_<name>.md` listing every fix as: file, the exact current text (enough to be unique in that file), the replacement, and a one-line reason. Readers do NOT edit chapter files.
1. **Continuity and timeline**: every date, age, year count, name, place, object, dog, vehicle and who-knew-what-when, checked across the whole book and against the bible. Flag a fact told twice in conflict, a name used before it is introduced, a payoff with no setup, a setup with no payoff.
2. **Grammar and house rules**: every sentence against the house grammar below, plus spelling, punctuation, tense, agreement, dialogue punctuation and unclear antecedents.
3. **Voice and dialogue**: Isaiah, Ruth, Kate, Hattie, Lena, Marcus, Lily, Ben, Ruthie and the townspeople each sound like themselves all the way through; anachronistic words; who-is-speaking confusion.
4. **The faith arc**: Ruth from the church in the Drôme, through Barracks 28 (Ch 15), Kate's card, Enchanted Rock in April 1977 (Ch 21), to Isaiah's speech by the fire in Ch 38. Every step must set up the Ch 38 speech without stating its point early. Flag repeats of the same Scripture or image that blunt it.
5. **Repetition and drag**: the same fact, image, phrase or explanation told more than once across the book (only one telling survives, unless the second is a deliberate echo); passages where a whole-book reader would skim; close repeats of words. Fixes must not cut substance.
6. **Word-craft and the two authors' seats**: (A) a bestselling inspirational novelist in the Nicholas Sparks tradition (heart, image, page-turn); (B) a bestselling WWII historical novelist in the vein of *The Nightingale* (period truth, sentence craft). Flat or vague words where a sharper, more visual word paints the picture; chapter openings and closings that could hook harder (never neon).

### Phase 2: one editor applies the fixes
After all six reports are in, ONE agent (not six at once, so edits never collide) applies them:
- Exact-string replacement in Python, `assert text.count(old) == 1` before each replace. If two readers touch the same sentence, merge them into one fix.
- Skip anything on the protected list, anything that adds a scene, fact or character, and anything that cuts substance. Say why in the log.
- **Length rule:** the book is about 151,700 words and John is watching page count. Applied edits must be word-neutral or shorter for the book overall; when two wordings are equal, take the shorter.
- Log every applied change to `reports/edit_log.md` (file, old → new, reason, which reader), with counts per chapter and the net word change. List skipped fixes in `reports/skipped.md` with the reason.
- Then a final check: grep the whole book for em dashes (—), the word "draft", sentences opening with "And " outside Scripture, and confirm every protected passage below is byte-for-byte unchanged.

### Phase 3: score and save
- `reports/panel_scores.md`: score the whole book 1 to 10 with the 22 seats in the house-rules brief plus the two authors (general-market critic kept out of the average). Last panel: 9.17 in John's market (Author A 9.32, Author B 9.09). Give each author's three best lines, three weakest, and the five pages where a reader would still skim.
- Commit and push everything. Do not build the PDF; that is done elsewhere.

## Protected: never change these
- **Ch 34, John's verbatim line**, exactly: `The old man taps the carbon. "Globalists who serve no flag, the Rothschilds among them, have held power for generations and own the seats of power that run our governments and write our history books."`
- Every letter, card and line written by or spoken by the dog man (Ch 22, Ch 23 and wherever he appears). He stays unnamed. Never invent a line for him.
- Ch 23 lawsuit facts and every quote from Adam, Peter, Amanda, the line producer, the bookkeepers and the director's lawyer. Peter, Amanda and Adam by first name only; the others unnamed.
- Scripture quoted in the King James Version, verbatim.
- Dated real-world quotes (Eisenhower, JFK, Casey, Mencken, Corrie and Betsie ten Boom, the Big Thompson coroner, and the rest).
- Lily's Cu Chi question stays unanswered, and its echo in the Epilogue stays.
- The closing lines of the Epilogue (the final bench, hand and tag sequence).
- Ch 38 (`34b_the_coal_goes_grey`), Isaiah's warfare speech from Isaiah 43:2 through Ben's question and Isaiah's Peter-and-Judas answer: the book's center. Grammar fixes only, and only if certain.
- Ch 5 the limestone and farrier's hammer line; Ch 21 "She had climbed every ladder on the homeplace by six..." (John said keep both; never propose cutting them).
- Ch 33 Hasan "by firing squad" line, Ch 26 "This courtroom happened to be honest.", and both Ch 35 (`34a_what_i_saw`) uses of "in the middle of the killing" (Pulse and Manchester, a deliberate echo): pending John; leave them.
- Lines tagged [JOHN] in the bible are his decisions.

## John's settled content rules
- The convictions in the book are the author's and settled: Islam as an ideology of conquest, globalists, the deep state, COVID, Big Pharma, Jekyll Island, Paperclip, Building Seven, the Fourth Reich, Yalta, the admiralty flag, and every conviction Ruth or Isaiah speaks. Judge writing, placement and pacing only. Never soften, hedge, balance or cut a conviction; never diminish the Islamic threat; no both-sides lines.
- Clues, not neon: the narration never tells the reader to search and never explains what is real. No author's note.
- A named source is enough. Never cite or rely on Snopes, PolitiFact, Lead Stories, Check Your Fact, CNN or MS NOW.
- Living people get only their own dated words and acts.
- Isaiah talks in long sentences (a man who talked in the back of an ambulance). Do not break them up.
- Ruth's surname is Vellmer, never Vogel. Martinsburg is the book's town; the six mentions of Fredericksburg as the real town up the road (Nimitz, the Steamboat Hotel, the Easter fires) stand as written.
- Lawsuit facts are court-established; never frame them as "John's view."
- Every true fact that sounds made up must stay as documented; any disputed part stays out.

## House grammar (every sentence you write or change, and fix existing violations)
- No sentence ends on a preposition or a particle. Phrasal verbs are NOT exempt: recast.
- No dangling verb ending.
- No sentence opens with "And" (Scripture quoted verbatim is exempt).
- No bare-pronoun subject leaning on the sentence before ("It never came." must say what never came).
- No em dashes.
- Never the word "draft."
- Write in pictures: concrete nouns, sensory detail, Nicholas Sparks warmth. Rare words are fine when they carry the true meaning better.

## Git
Commit with clear messages. Push to the branch the session gives you.
