# APEX AI Production Prompts
### 15 Immediately Usable Prompts for the APEX Workflow

---

> **How to use this file:** Each prompt is designed to be copied directly into Claude (claude.ai) or GPT-4o. Replace all `[BRACKETED PLACEHOLDERS]` with real information before running. The more specific your inputs, the sharper your outputs. Do not run prompts with placeholder text still in them.

---

## PROMPT 1: CLIENT INTAKE ANALYSIS

**Title:** Client Intake Analysis — Strategic Priority Extraction

**When to use:** Immediately after receiving the completed onboarding questionnaire, before the kickoff call.

**Purpose:** Turn a long questionnaire into a structured briefing document that identifies strategic priorities, risks, and deck focus areas.

---

**Prompt:**

```
You are a senior strategic communications analyst. I'm going to paste a client's completed onboarding questionnaire below. Your job is to analyze it and produce a structured strategic briefing.

CLIENT QUESTIONNAIRE RESPONSES:
[PASTE FULL QUESTIONNAIRE RESPONSES HERE]

Produce the following output:

1. COMPANY SNAPSHOT (3-4 sentences): What this company does, its stage, and what makes it notable or interesting.

2. STRATEGIC PRIORITIES FOR THIS DECK (numbered list of 3-5): What are the most important things this deck must accomplish, based on the client's answers? Not what they said explicitly — what does the situation actually require?

3. KEY COMMUNICATION RISKS (numbered list): What are the gaps, inconsistencies, or vulnerabilities in the narrative as currently described? What could an investor push back on?

4. WHAT THE CLIENT THINKS THE PROBLEM IS vs. WHAT IT ACTUALLY IS: Based on their answers, identify the surface problem they described and the deeper communication problem that needs to be solved.

5. AUDIENCE INTELLIGENCE: Based on the audience described, what are the top 3 things this audience will be evaluating? What are they most skeptical of at this stage?

6. RECOMMENDED DECK FOCUS AREAS (ranked by importance): Given the above, what should this deck emphasize most, and what should be given less real estate?

7. OPEN QUESTIONS (for kickoff call): What are the 3-5 questions that weren't answered clearly enough in the questionnaire that need to be resolved before work begins?

Be specific. Reference actual details from the questionnaire. Do not give generic advice — this brief should be actionable.
```

**What to do with the output:** Use this as your prep document for the kickoff call. The "open questions" section becomes your kickoff call agenda. The "communication risks" section becomes the diagnostic you share with the client to demonstrate strategic understanding.

---

## PROMPT 2: BUSINESS MODEL UNDERSTANDING

**Title:** Business Model Articulation — Investor-Ready Summary

**When to use:** Early in Phase 2 (Research + Architecture), before building the business model slide.

**Purpose:** Get a clean, precise articulation of how the business works, what the key metrics are, and what investors will focus on.

---

**Prompt:**

```
You are a former management consultant with expertise in investor relations. A founder has described their company to me. I need you to analyze it and produce an investor-relevant business model summary.

COMPANY DESCRIPTION:
[PASTE COMPANY DESCRIPTION — from questionnaire or your own notes]

ADDITIONAL CONTEXT:
- Stage: [Pre-seed / Seed / Series A / etc.]
- Revenue: [ARR or MRR if available, or "pre-revenue"]
- Business model type: [SaaS / marketplace / transactional / hardware+software / services / etc.]
- Key known metrics: [List any metrics the client has provided]

Produce the following:

1. BUSINESS MODEL IN ONE SENTENCE: How does this company make money? Be precise — not "we charge for our platform" but the actual mechanism.

2. UNIT ECONOMICS SUMMARY: What are the key unit economic metrics that matter for this model? (e.g., CAC, LTV, gross margin, payback period, take rate, ARPU — pick the ones that apply.) Fill in what's known and flag what's missing.

3. REVENUE MODEL CLARITY: Is the revenue model simple and easy for an investor to understand in 30 seconds? If not, explain what makes it complex and suggest how to simplify the explanation.

4. INVESTOR-RELEVANT METRICS TO HIGHLIGHT: Given the stage and model type, what are the 4-6 metrics an investor will want to see? Which of these does the company currently have, and which are gaps?

5. SCALE STORY: How does this business get bigger? What are the key growth levers? State this in investor terms — not "we'll grow" but the specific mechanisms.

6. BUSINESS MODEL RISK FLAGS: What are the 2-3 questions an investor is most likely to ask about the business model that the deck needs to proactively address?
```

**What to do with the output:** Use sections 1 and 5 to inform the business model and traction slides. Use section 4 to decide which metrics to feature and which to omit. Use section 6 to anticipate objections and address them in the deck.

---

## PROMPT 3: PITCH DECK DIAGNOSTIC

**Title:** Existing Deck Diagnostic — Investor Communication Audit

**When to use:** When a client has an existing deck that needs rebuilding or significant revision.

**Purpose:** Produce an itemized critique that identifies exactly what is wrong and why, before any new work begins.

---

**Prompt:**

```
You are a pitch deck strategist who has reviewed hundreds of investor presentations across seed through Series B. A client has an existing deck. I'm going to describe it to you (or paste the content). Your job is to provide an honest, expert critique.

EXISTING DECK CONTENT / DESCRIPTION:
[PASTE SLIDE CONTENT OR DESCRIBE EACH SLIDE: "Slide 1: Title — Company name and tagline. Slide 2: Problem — Three bullet points about the problem. Slide 3: Solution — Product screenshot and feature list..." etc.]

CONTEXT:
- Stage: [Seed / Series A / etc.]
- Target investor type: [VC / Angel / Family Office / Corporate / etc.]
- Sector: [Industry]
- Round size: [CHF/USD amount]

Produce the following:

1. NARRATIVE GAPS: What is the deck not saying that it needs to say? What questions does an investor have after reading this that aren't answered?

2. SLIDE ORDER ISSUES: Are slides in the wrong sequence? Does the story build properly — problem before solution, tension before resolution? Flag any slides that appear before the audience has context to care about them.

3. MISSING INVESTOR CONCERNS: What are the top concerns an investor would have about this company that this deck fails to address proactively?

4. VISUAL DENSITY PROBLEMS: Based on the content described, which slides are trying to say too much? Which slides lack a clear primary message?

5. STRUCTURAL WEAKNESSES (ranked by severity): List the 5 most significant problems with this deck, ranked from most damaging to least.

6. WHAT'S WORKING: What is this deck doing right that should be preserved in the rebuilt version?

7. RECOMMENDED REBUILD APPROACH: Given the above, what are the most important changes to make first? If you could only fix three things, which three would have the biggest impact?
```

**What to do with the output:** Share a summarized version of sections 5 and 7 with the client during the kickoff call as part of your diagnostic reframe. This demonstrates expertise immediately. Use the full output to guide your rebuild architecture.

---

## PROMPT 4: INVESTOR NARRATIVE CREATION

**Title:** Full Investor Narrative — Story Arc Construction

**When to use:** In Phase 2, after research is complete, before slide outlines are built.

**Purpose:** Produce the complete narrative logic of the deck — what happens at each story beat, what the tension is, and how the deck ends with conviction.

---

**Prompt:**

```
You are a senior narrative strategist who specializes in investor storytelling. I'm building a pitch deck for the following company. Your job is to construct the complete story arc — not slide titles, but the actual narrative logic that every slide must serve.

COMPANY OVERVIEW:
[PASTE COMPANY DESCRIPTION]

ROUND DETAILS:
- Stage: [Seed / Series A / etc.]
- Amount raising: [CHF/USD amount]
- Use of funds: [What the money is for]

TARGET INVESTOR:
[Describe the type of investor — stage preference, sector focus, what they care about]

KEY FACTS AVAILABLE:
- Traction: [Key metrics or milestones]
- Team: [Key members and relevant credentials]
- Market: [Market size estimate and source]
- Differentiation: [How this company differs from alternatives]

Produce the following:

1. THE OPENING HOOK (Slide 1 logic): What is the single most compelling way to open this deck? What is the first idea that should land in the investor's mind? Not a tagline — a strategic choice about where the story begins.

2. THE CORE TENSION: What is the central conflict of this story? What is broken in the world, and why has it stayed broken? State this in one paragraph.

3. THE NARRATIVE ARC (slide by slide story logic — not titles, but what each beat accomplishes):
   - Opening context: what world are we entering?
   - The problem: what is wrong, how big is it, why does it persist?
   - Why now: what has changed that makes this the moment?
   - The solution: how does this company resolve the tension?
   - Why this team: why are these people the ones to do it?
   - Proof: what evidence exists that this works?
   - The opportunity: what does winning look like?
   - The ask: what does the investor's involvement unlock?

4. THE RESOLUTION STATEMENT: In 2-3 sentences, what is the core conviction this deck should leave the investor with? This is the emotional and intellectual landing point.

5. THE NARRATIVE RISKS: What parts of this story are weakest? Where will a skeptical investor push back? How should the narrative address each proactively?
```

**What to do with the output:** This becomes the narrative brief that governs all slide building. Every slide headline should serve one of the story beats identified here. Share the "resolution statement" with the client to confirm alignment before building.

---

## PROMPT 5: EXECUTIVE SUMMARY CREATION

**Title:** Executive Summary — McKinsey Format, One Page

**When to use:** When a client requests a standalone one-pager, or as an add-on to any deck project.

**Purpose:** Produce a tight, one-page executive summary in the structured analytical style used by top-tier strategy firms.

---

**Prompt:**

```
You are a McKinsey-trained strategy analyst. I need you to write a one-page executive summary for the following company. The format should be clean, structured, and written in a confident, declarative style — not marketing language, not hype, not vague claims. Every sentence should carry information.

COMPANY OVERVIEW:
[PASTE FULL COMPANY DESCRIPTION, including product, customer, business model, traction, team, and round details]

Write the executive summary in the following structure:

**[COMPANY NAME] — Executive Summary**

**The Opportunity**
[2-3 sentences: What market opportunity exists, why it's significant, and why the timing is right. Cite a market size figure if available.]

**The Problem**
[2-3 sentences: What specific problem exists for which customer, and why existing solutions are insufficient.]

**Our Solution**
[2-3 sentences: What the company does, how it solves the problem, and what makes the approach distinctive.]

**Business Model**
[2-3 sentences: How the company generates revenue. Include pricing model, key metrics (ARR, margins, LTV/CAC) if available.]

**Traction**
[Bullet points or 2-3 sentences: Key milestones, customer metrics, revenue figures, growth rates — whatever is most compelling.]

**Team**
[2-3 sentences: Who the key founders are and why their background creates an unfair advantage for this specific problem.]

**The Ask**
[1-2 sentences: How much is being raised, in what structure, and what it will be used to accomplish.]

Style requirements:
- No adjectives that aren't earned (avoid "revolutionary," "game-changing," "world-class")
- Every claim should be specific and defensible
- Tone: confident and analytical, not enthusiastic and promotional
- Total length: no longer than fits on one page at normal font size
```

**What to do with the output:** Review for factual accuracy against client-confirmed data. Adjust any claims that aren't yet proven. This document can be sent standalone or attached as an appendix to the main deck. Present as a polished Word or PDF document, not as a slide.

---

## PROMPT 6: MARKET SIZING (TAM/SAM/SOM)

**Title:** Market Sizing — Three Approaches with Investor Framing

**When to use:** In Phase 2 (Research), when building the market opportunity section of the deck.

**Purpose:** Produce three credible approaches to market sizing with clear guidance on which to use and how to frame it.

---

**Prompt:**

```
You are a market research analyst with experience preparing investor-grade market analysis. I need to size the market for the following company.

COMPANY:
[Brief description of what the company does]

INDUSTRY / SECTOR:
[Industry name — e.g., B2B SaaS for logistics, consumer fintech, health tech for chronic disease management]

GEOGRAPHY:
[Target geography for market sizing — e.g., DACH region, Western Europe, Global]

TARGET CUSTOMER:
[Who the company sells to — e.g., mid-market logistics companies with 50-500 employees, individual consumers aged 25-45, etc.]

Produce the following:

1. TOP-DOWN APPROACH:
   - TAM: Total addressable market — what is the total global or relevant market for this category? Cite the logic and reference any known industry report figures.
   - SAM: Serviceable addressable market — narrowed to the geography and customer segment this company can realistically serve.
   - SOM: Serviceable obtainable market — realistic 3-5 year capture for a company at this stage.
   - Investor framing: How should these numbers be presented to make the market feel genuinely large without being obviously inflated?

2. BOTTOM-UP APPROACH:
   - Number of potential customers × average revenue per customer = market size
   - Walk through the calculation step by step, using the target customer definition above
   - Which numbers in this calculation are defensible vs. estimates that need qualification?

3. VALUE-THEORY APPROACH:
   - What value does this company create for its customer, and what % of that value could it reasonably capture as revenue?
   - What does this imply about the market opportunity?

4. RECOMMENDATION:
   - Which approach is most credible for this specific company and investor context, and why?
   - What is the single market size number to lead with, and how should it be sourced on the slide?

5. INVESTOR SKEPTICISM FLAGS:
   - What will a sophisticated investor push back on in any of these approaches?
   - How should the deck preemptively address that skepticism?
```

**What to do with the output:** Choose the approach recommended in section 4. Cross-reference the TAM/SAM/SOM numbers against available industry reports to validate. Use the skepticism flags to ensure the market slide answers, not ignores, likely objections.

---

## PROMPT 7: COMPETITOR ANALYSIS

**Title:** Competitive Positioning — Table + Differentiation Narrative

**When to use:** In Phase 2, when building the competitive landscape slide.

**Purpose:** Produce a clear competitive positioning matrix and a narrative on how this company differentiates — in investor language, not marketing language.

---

**Prompt:**

```
You are a competitive intelligence analyst preparing materials for an investor presentation. I need a rigorous competitive analysis for the following company.

OUR COMPANY:
[Company name, what it does, who it serves, how it makes money]

COMPETITORS TO ANALYZE:
1. [Competitor 1 name + brief description if you have it]
2. [Competitor 2 name + brief description]
3. [Competitor 3 name + brief description]
4. [Competitor 4 name if applicable]
5. [Competitor 5 name if applicable]

DIFFERENTIATION CLAIM (what the client believes makes them different):
[What has the client said about their differentiation? Even if rough or unsubstantiated — paste their words]

Produce the following:

1. COMPETITIVE POSITIONING TABLE:
Create a table with competitors as rows and the following dimensions as columns (select the 4-6 most relevant for this category):
- Pricing model
- Target customer segment
- Core product capability
- Key limitation or weakness
- Funding stage / scale
- One-line positioning summary

Include "Our Company" as a row for direct comparison.

2. DIFFERENTIATION NARRATIVE (3-4 sentences):
What is the genuinely defensible differentiation of this company? Separate what is real from what is marketing. Be honest about where differentiation is strong vs. where it is thin.

3. POSITIONING STATEMENT FOR THE SLIDE:
Write a 1-2 sentence competitive positioning statement that can appear on the deck — clear, specific, not generic. Avoid "we're the only company that..." unless it's truly unique.

4. COMPETITIVE RISK ASSESSMENT:
What are the top 2-3 competitive risks — i.e., moves a competitor could make that would undermine this company's positioning? Should any of these be addressed in the deck?

5. SUGGESTED SLIDE FORMAT:
Given the competitive landscape described, what is the most effective visual format for this slide — traditional comparison table, 2x2 positioning matrix, or narrative differentiation format? Explain your recommendation.
```

**What to do with the output:** Fact-check any competitor claims against public sources before using in the deck. The positioning statement goes directly on the competitive slide (refined for visual fit). Share the risk assessment with the client to ensure they have prepared responses.

---

## PROMPT 8: SLIDE OUTLINE GENERATION

**Title:** Full Deck Outline — Slide-by-Slide Structure

**When to use:** At the end of Phase 2, once narrative architecture is confirmed.

**Purpose:** Produce a complete 12–15 slide outline that specifies the purpose and key message of every slide before a single word is written.

---

**Prompt:**

```
You are a pitch deck architect. I need you to create a complete slide-by-slide outline for an investor presentation. This outline comes before any copy is written — each slide needs a title, a purpose, and a key message.

COMPANY:
[Company name + one-sentence description]

DECK TYPE:
[Seed pitch / Series A / Board presentation / Partnership deck / etc.]

ROUND:
[Amount raising + type — e.g., CHF 2M seed round / Series A of CHF 8M]

TARGET AUDIENCE:
[Investor type — e.g., Swiss-based early-stage VCs focused on B2B SaaS]

CORE NARRATIVE DIRECTION:
[Paste the narrative arc from Prompt 4, or summarize: "The story is about X problem being solved by Y approach, and the key tension is Z"]

KEY ASSETS AVAILABLE:
- Traction: [what exists — revenue, customers, growth metrics]
- Team credentials: [key founders and relevant background]
- Product: [what stage — concept, prototype, live product, scaling]

Produce a complete outline in this format for each slide:

**Slide [number]: [Title]**
- Purpose: [What job does this slide do in the narrative — what question is it answering?]
- Key message: [The single most important thing the audience should take away from this slide — in one sentence]
- Content to include: [What specific elements should appear — data points, visuals, quotes, lists]
- Transition logic: [How does this slide set up the next one?]

Build 12-15 slides. Include standard sections (problem, solution, market, business model, traction, team, ask) but sequence and title them based on the specific narrative, not a generic template. Flag if any section should be expanded to two slides.
```

**What to do with the output:** Share the outline with the client before building any slides. Get written sign-off on the structure. This is the most important alignment step — changes at the outline stage cost ten minutes; changes after slides are built cost hours.

---

## PROMPT 9: SLIDE COPY WRITING

**Title:** Slide Copy — Investor-Grade Headline + Supporting Points

**When to use:** During Phase 3 (Build), for each individual slide.

**Purpose:** Turn raw content into tight, investor-grade slide copy with a strong headline and refined supporting bullets.

---

**Prompt:**

```
You are a strategic communications writer specializing in investor presentations. I need you to write the copy for a specific slide.

SLIDE NAME:
[e.g., "The Problem" / "Market Opportunity" / "Business Model" / "Traction"]

SLIDE PURPOSE:
[What does this slide need to accomplish in the narrative — what question is it answering?]

KEY MESSAGE TO CONVEY:
[The single most important idea this slide must land — in one sentence]

RAW CONTENT (notes, data, rough bullets — paste whatever exists):
[PASTE RAW CONTENT]

COMPANY CONTEXT:
[2-3 sentences on the company so the copy is informed]

TONE:
[Bold and assertive / Data-driven and rigorous / Mission-driven / Technical and precise]

Produce the following:

1. SLIDE HEADLINE (1 option primary + 2 alternatives):
   - A declarative, specific statement — not a category label
   - Should convey the key message even if read in isolation
   - Maximum 10 words
   - Should not start with "We" or "Our"

2. SUPPORTING POINTS (3 bullets or a 2-3 sentence body):
   - Each point should add new information, not restate the headline
   - Tight and specific — no padding, no vague language
   - Investor-appropriate — factual, confident, not promotional

3. DATA CALLOUT (if applicable):
   - If there is a key number or metric to feature prominently, state it and write the 3-5 word label that accompanies it

4. COPY NOTES:
   - Any claims in the copy that need to be sourced or confirmed before publishing
   - Any language that is too strong / claims more than the data supports

Style rules:
- No "world-class," "revolutionary," "game-changing," "cutting-edge," "best-in-class" unless followed by specific evidence
- Numbers over words: "3x faster" not "significantly faster"
- Active voice throughout
- Present tense for current state; future tense only for the vision section
```

**What to do with the output:** Use option 1 headline as the primary. Place the copy in the slide. The "copy notes" section flags any claims to double-check with the client before finalizing.

---

## PROMPT 10: VISUAL DIRECTION

**Title:** Visual Language Brief — Design Direction for a Deck

**When to use:** At the start of Phase 3 (Build), before opening any design software.

**Purpose:** Produce a clear visual direction brief that informs all design decisions — color, typography, layout style.

---

**Prompt:**

```
You are a creative director specializing in investor presentation design. I need to define the visual language for a pitch deck.

COMPANY:
[Company name]

INDUSTRY / SECTOR:
[e.g., climate tech / enterprise SaaS / consumer health / fintech / deep tech]

COMPANY POSITIONING / PERSONALITY:
[How the company wants to be perceived — e.g., "rigorous and institutional," "bold and challenger," "warm and human," "precise and technical"]

TONE PREFERENCES (from client):
[What the client said about how they want it to feel — paste their exact words if available]

EXISTING BRAND ELEMENTS (if any):
- Primary color: [hex code or description, or "none"]
- Logo style: [describe the logo if no file — wordmark, icon, minimal, etc.]
- Any existing design materials: [Yes/No, brief description]

COMPANIES OR DECKS THE CLIENT ADMIRES:
[What references did they give? Any companies whose visual communication they want to be compared to?]

TARGET INVESTOR TYPE:
[Institutional VC / Angel / Family office / Corporate strategic]

Produce the following:

1. COLOR PALETTE RATIONALE:
   - Primary color recommendation (with hex code): what it signals and why it fits
   - Secondary / accent color (with hex code): when and how to use it
   - Background color (with hex code): why this choice works for this context
   - What to avoid and why

2. TYPOGRAPHY RECOMMENDATION:
   - Headline font: name + why it fits the positioning
   - Body font: name + pairing rationale
   - Where to source these fonts (Google Fonts / Adobe Fonts / system fonts)
   - Type hierarchy: recommended sizes for H1 / H2 / Body / Caption

3. LAYOUT STYLE DIRECTION:
   - Overall aesthetic direction (e.g., clean and minimal / bold and graphic / data-forward)
   - How much visual density is appropriate (text-heavy analytical vs. visual-led)
   - Grid and margin approach (tight and editorial, or open and spacious?)

4. VISUAL ELEMENTS TO USE / AVOID:
   - What types of visuals are appropriate (icons, photography, data charts, geometric shapes)
   - What to explicitly avoid for this client and context
   - Whether to use full-bleed imagery or contained visual elements

5. MOOD REFERENCE:
   - 3 companies or brands (not necessarily competitors) whose visual communication is an appropriate reference for this deck — and why each one applies
```

**What to do with the output:** This brief governs all design decisions for the project. Save it in the project folder. If the client has brand guidelines that conflict with any recommendations, defer to their brand guidelines and adjust accordingly.

---

## PROMPT 11: FUNDRAISING NARRATIVE AUDIT

**Title:** Investor Perspective Critique — Unanswered Questions and Conviction Gaps

**When to use:** After the first draft is complete, before sending to the client.

**Purpose:** Stress-test the narrative from the perspective of a skeptical, experienced investor.

---

**Prompt:**

```
You are a managing partner at a European VC firm that has reviewed over 500 decks. You are reviewing the following pitch deck narrative. Your job is not to be encouraging — your job is to identify every unanswered question, every conviction gap, and every signal that might give you pause.

DECK NARRATIVE (paste slide headlines + key content for each slide):
[PASTE COMPLETE DECK CONTENT — headlines, bullets, key data points for each slide]

COMPANY STAGE: [Seed / Series A / etc.]
SECTOR: [Industry]
ROUND SIZE: [Amount]
TARGET INVESTOR PROFILE: [Type of investor this is going to]

Produce the following:

1. UNANSWERED INVESTOR QUESTIONS (list every one):
After reading this deck, what questions does an investor still have that the deck failed to answer? List every one — minor and major. Do not filter.

2. CONVICTION GAPS:
Where does the narrative make claims that aren't sufficiently supported? Where are you being asked to take a leap of faith that most investors won't take?

3. SIGNALS THAT CONCERN YOU:
What, if anything, in this deck signals risk, inexperience, or weakness — even if unintentionally? This includes: what's missing, what's overstated, what's evasive.

4. STRONGEST PARTS OF THE NARRATIVE:
What in this deck actually works well? What would give you reason to take a follow-up meeting?

5. THE 3 MOST IMPORTANT FIXES (prioritized):
If you could make the founder fix only three things before sending this, what would they be — and specifically how?

6. WHAT WOULD MAKE YOU PASS:
What is the one thing, currently, that would most likely cause you to pass on this deal without a meeting?

Be direct. Do not soften criticism. A polite but incomplete critique is worth nothing.
```

**What to do with the output:** Go through each point in sections 1–3. For each unanswered question, decide: (a) add a slide or bullet to address it, (b) prepare a verbal answer for the meeting, or (c) acknowledge it's a known risk. Section 5 drives the final revisions before client delivery.

---

## PROMPT 12: BOARD PRESENTATION STRUCTURE

**Title:** Board Presentation Architecture — Agenda and Key Message Per Section

**When to use:** For board presentation projects, in Phase 2 (Architecture).

**Purpose:** Produce the right structure for a board presentation — different from an investor pitch, focused on governance, accountability, and decision-making.

---

**Prompt:**

```
You are a chief of staff who has prepared board materials for venture-backed companies. I need to structure a board presentation.

COMPANY CONTEXT:
[Company name, stage, what they do]

QUARTER SUMMARY:
- Revenue / ARR: [figure and YoY growth if available]
- Key wins this quarter: [list]
- Key misses or challenges: [list — be honest, this is for internal context]
- Burn rate and runway: [monthly burn + months of runway]
- Headcount: [current headcount, any changes]
- Major decisions needed from the board: [what does the CEO need the board to decide or approve?]

BOARD COMPOSITION:
[Who is on this board — investor backgrounds, independent directors, any known areas of focus or concern]

PRESENTATION LENGTH:
[How long is the board meeting total? How long is the CEO presenting vs. discussion time?]

Produce the following:

1. RECOMMENDED PRESENTATION STRUCTURE:
A full agenda with sections, timing per section, and the purpose of each section.
Format:
- Section title
- Duration
- Purpose (what decision or discussion does this section drive?)
- Key message (what is the one thing the board should take away from this section?)

2. OPENING FRAME:
How should the CEO open this board presentation? What is the single most important thing to establish in the first 2 minutes?

3. THE HONEST SIGNAL:
Board presentations that avoid bad news create distrust faster than the bad news itself. How should the CEO frame challenges or misses in a way that is honest, accountable, and forward-looking?

4. DECISIONS NEEDED (formatted clearly):
For each decision the board needs to make, provide:
- The decision question (stated precisely)
- The context the board needs to make it
- The recommendation (what the CEO is asking for)
- The alternative if the board disagrees

5. CLOSING:
How should this presentation close? What is the CEO's ask of the board after the formal presentation ends?
```

**What to do with the output:** Use the structure in section 1 as the slide outline. Section 3 informs how challenge slides are written — never defensively, always with accountability and a path forward. Section 4 becomes the "decisions required" slide, which should be one of the clearest slides in the entire deck.

---

## PROMPT 13: STORYLINE CRITIQUE

**Title:** Skeptical Investor Critique — Narrative Logic and Credibility

**When to use:** After the narrative architecture is drafted (end of Phase 2), before building slides.

**Purpose:** Find the logical gaps and credibility issues in the narrative before any production time is invested.

---

**Prompt:**

```
You are a highly skeptical Series A investor who has heard thousands of pitches. A founder is pitching to you. I'm going to give you the narrative flow of their deck — the story they intend to tell, slide by slide. I need you to critique it as if you're evaluating whether to take a follow-up meeting.

Be critical. Be precise. Do not be polite at the expense of being useful.

NARRATIVE FLOW (describe each slide's intended story beat):
[PASTE NARRATIVE ARCHITECTURE — e.g., "Slide 1 opens with a striking statistic about the problem. Slide 2 shows the scale of the market. Slide 3 explains why current solutions fail. Slide 4 introduces the product..." etc.]

COMPANY STAGE: [Seed / Series A]
SECTOR: [Industry]

Critique the following specifically:

1. WHAT DOESN'T ADD UP:
Where is the logic broken or internally inconsistent? Where does the story make a jump that a skeptic won't follow?

2. WHAT'S MISSING:
What essential element of a credible fundraising narrative is absent? What question does the story never answer?

3. WHAT CREATES DOUBT:
What in this narrative would make you trust the founder less, not more? What signals naivety, overconfidence, or evasion?

4. THE ORDER PROBLEM:
Is the narrative sequence wrong? Does the story build properly — creating tension before resolving it? Are they leading with the wrong thing?

5. WHAT WOULD MAKE YOU LEAN FORWARD:
Despite your skepticism, is there anything in this narrative that genuinely interests you? What would make you take the meeting?

6. YOUR VERDICT (before seeing the deck):
Based purely on this narrative — do you take the meeting, pass, or ask for more information first? Explain your reasoning in 3-4 sentences.
```

**What to do with the output:** Use sections 1–4 to revise the narrative architecture before any slides are built. Section 5 identifies what to amplify. Section 6 tells you the overall narrative strength — if the answer is "pass," the architecture needs significant rework.

---

## PROMPT 14: QUALITY CONTROL PASS

**Title:** Full Copy Editing Pass — Clarity, Consistency, and Investor Appropriateness

**When to use:** In Phase 4 (Quality Control), after all slide copy has been written and before design is finalized.

**Purpose:** Catch every copy issue — clarity problems, tone inconsistencies, weak language, investor-inappropriateness.

---

**Prompt:**

```
You are an executive editor specializing in investor communications. I'm going to paste the complete slide copy for a pitch deck. Your job is to edit every slide for clarity, consistency, tone, and investor-appropriateness.

For each slide, provide:
- The original copy (as I gave it)
- Your edited version (with all changes applied)
- Brief notes on what you changed and why

COMPANY CONTEXT:
[Company name, industry, stage, round — so you understand the investor audience]

TONE TARGET:
[Confident and rigorous / Bold and assertive / Data-driven / Mission-driven]

COMPLETE SLIDE COPY:
[PASTE ALL SLIDE CONTENT HERE — slide number, headline, bullets, any captions or callouts]

Editing standards to apply:

1. CLARITY: Every sentence should be immediately understandable on first read. Remove anything that requires re-reading.

2. SPECIFICITY: Replace vague language with specific claims. "Significant growth" → "3x revenue growth in 12 months." "Large market" → "$4.2B TAM in Western Europe."

3. CONFIDENCE: Remove hedging language ("we believe," "we hope," "we think," "potentially," "could be") unless specifically warranted by context.

4. INVESTOR LANGUAGE: Remove promotional language that sounds like a marketing brochure. Investors want facts, not enthusiasm. Flag any sentence that sounds like it belongs in a press release.

5. CONSISTENCY: Ensure consistent terminology throughout (product name used the same way, metrics formatted the same way, tense used consistently).

6. CONCISION: Cut every word that doesn't add information. Bullets should be tight. Headlines should be direct.

7. WEAK PHRASES TO FLAG AND REPLACE:
- "world-class" → specific evidence or remove
- "revolutionary" → specific claim about what changed
- "passionate team" → specific credential or accomplishment
- "disrupting the industry" → specific mechanism of disruption
- "unique solution" → what specifically is unique
```

**What to do with the output:** Accept all edits that improve the copy. For any edits that change meaning (not just style), verify with the client before finalizing. The "brief notes" column tells you which changes were consequential — review those specifically.

---

## PROMPT 15: FINAL POLISH

**Title:** Final Polish — Language Sharpening and Headline Optimization

**When to use:** In Phase 4, when the deck is near-final and needs the last layer of refinement.

**Purpose:** Elevate near-finished copy to the highest standard — sharper headlines, stronger language, removal of every remaining weak phrase.

---

**Prompt:**

```
You are a senior communications strategist doing a final polish on an investor presentation. The deck is nearly finished. Your job is to make every headline more compelling, every bullet tighter, and remove every phrase that weakens the overall impression.

This is not a structural review — the structure is locked. This is about language precision and impact.

NEAR-FINAL DECK COPY:
[PASTE COMPLETE SLIDE COPY — all headlines and bullets for every slide]

COMPANY: [Name and one-line description]
AUDIENCE: [Investor type / board / partners]

Produce the following for each slide:

1. HEADLINE OPTIMIZATION:
   - Current headline: [as given]
   - Optimized headline: [your version]
   - What you changed: [one sentence — why this is stronger]

2. POWER WORD SUGGESTIONS:
   - For each slide, identify 1-2 words or phrases that could be sharpened
   - Provide the current weak phrase and a stronger alternative

3. WEAK PHRASE REMOVAL:
   - Flag any remaining instances of: vague claims, hedging language, marketing-speak, redundancy
   - For each, provide the replacement

4. OPENING LINE AUDIT:
   - For the title slide and the first content slide: is the opening powerful enough to set the right tone? If not, suggest an alternative opening.

5. CLOSING LINE AUDIT:
   - For the final slide (ask / vision): does the deck end with conviction? Is the last line the investor reads the strongest possible line? If not, suggest the replacement.

6. OVERALL IMPRESSION:
   - After reading the full near-final copy: what is the single weakest slide, and what is the single strongest slide?
   - What is the one remaining change that would have the biggest impact on investor impression?

Optimization principles:
- Short words beat long words when they're equally precise
- Specific beats vague, always
- Active voice beats passive voice
- Numbers beat adjectives
- A great headline makes a skeptic want to read the next line
```

**What to do with the output:** Apply all headline optimizations — at minimum review each suggested change and accept or consciously reject it. The "overall impression" section at the end is the most valuable part: use it to identify where to spend the final 30 minutes before delivery.

---

> **Prompt Maintenance Note:** These prompts are designed to work with Claude (claude.ai) and GPT-4o as of 2025-2026. If model behavior changes significantly, revisit the prompts that produce the most critical outputs (Prompts 4, 8, 11) and adjust the instruction framing as needed.
