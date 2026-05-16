# APEX — Website Build Instructions
## Framer Build Guide for a Non-Developer
### Complete Day-One Launch Plan

---

## 1. PLATFORM RECOMMENDATION: WHY FRAMER

Use Framer. Not Webflow, not Squarespace, not Notion.

**Why Framer over the alternatives:**

**vs. Webflow:**
Webflow gives you more technical control but assumes you understand CSS layout concepts. The learning curve to produce a premium, typographically-led site in Webflow without prior experience is two to three weeks minimum. Framer produces the same visual output with a drag-and-drop canvas in a fraction of the time. For a solo founder launching fast, Webflow is overkill.

**vs. Squarespace:**
Squarespace templates are built for small businesses and photographers. They resist customization at the level APEX requires — you will fight the template constantly to achieve a dark, editorial, typographically-precise aesthetic. The output will look like a Squarespace site, which is not the register APEX needs.

**vs. Notion-as-website (Super, Potion):**
Appropriate for personal notes, not for a premium service studio. Immediately signals early-stage and informal. Not suitable.

**Why Framer specifically:**

- **Template quality:** Framer's template marketplace has genuinely premium, dark editorial templates designed for agency, studio, and portfolio use — the exact visual register APEX needs. Several require minimal modification to match the APEX aesthetic.
- **Design quality:** The canvas behaves like Figma. Typography control, spacing, and layout precision are significantly better than Webflow at the same experience level.
- **Speed:** A template-based Framer site can be customized and launched in one focused day. This guide is built around that timeline.
- **Custom domain:** Connect your domain (apexcommunication.ch) directly inside Framer. SSL is automatic.
- **CMS:** Framer has a built-in CMS for blog posts and case study pages — useful when you add content later. Not needed on day one.
- **Pricing:** The Pro plan (USD 30/month or approximately CHF 27/month) covers everything needed at launch: custom domain, CMS, password-protected pages, and no Framer branding. The Starter plan (free) lets you build and preview before you pay.
- **Forms:** Native Framer forms work out of the box. Connect them to your email via Framer's built-in notification system or integrate with Zapier later.

**Decision:** Start on Framer. Build on a template. Launch in a day.

---

## 2. PAGE STRUCTURE

### Pages required on Day 1 (launch):

| Page | Priority | Notes |
|------|----------|-------|
| **Home** | Essential | Full landing page — all 13 sections |
| **Services** | Essential | Expanded service descriptions and pricing |
| **Contact** | Essential | Enquiry form + call booking link |
| **Showcase** | Recommended | 3 illustrative project summaries (clearly labeled) |

### Pages to build later (not Day 1):

| Page | Timeline |
|------|----------|
| Blog / Insights | Month 2–3, once you have 2–3 articles ready |
| About | Optional — homepage credibility section may be sufficient |
| Legal / Privacy Policy | Before running paid ads or capturing email addresses |

### URL structure:
- `apexcommunication.ch` — Home
- `apexcommunication.ch/services` — Services
- `apexcommunication.ch/showcase` — Showcase
- `apexcommunication.ch/contact` — Contact

---

## 3. SECTION-BY-SECTION LAYOUT INSTRUCTIONS

### Homepage layout — section by section:

---

**HERO**
Full-bleed: 100% viewport height (100vh). Dark background (#0A0A0A).
Content centered, both horizontally and vertically.
Stack order (top to bottom, centered):
1. Small label above headline: "APEX" in letter-spaced small caps, muted gray (#6B6B6B), 11px
2. Primary headline: serif font, 56–72px on desktop, centered
3. Secondary headline: sans-serif, 18–20px, off-white, centered, max-width 600px
4. Sub-copy: sans-serif, 15–16px, muted off-white (#B0AFA9), centered, max-width 520px, 16px line height
5. CTA button: white fill, black text, 14px, letter-spaced, 48px height, 24px horizontal padding
6. Secondary text link below button: "View Services →" in muted gray

No image. No illustration. The headline carries the weight of the entire section.

Scroll indicator (optional): a single thin white line or down-arrow at the very bottom of the viewport, fading on scroll.

---

**CONTEXT STATEMENT**
White or very light off-white background (#F5F4F0).
Single column, centered.
Width: max 720px, centered in the viewport.
Top: section label in small caps, spaced, gray (#9B9A96), 11px — "THE SITUATION"
Below: one paragraph of body copy in serif or sans-serif, 18–20px, dark text (#0A0A0A), generous line height (1.75).
Padding: 120px top and bottom (sections breathe — do not compress them).

---

**THE PROBLEM**
Dark background (#0A0A0A) — this creates a visual alternation with the previous light section.
Section header centered at top: "Why most decks do not work." — serif, white, 36–42px.
Below: three problem blocks arranged in a single column, stacked, max-width 680px, centered.
Each block:
- Bold statement in white, 18–20px
- Two sentences of supporting copy below, in muted off-white (#B0AFA9), 15–16px
- A thin horizontal rule (1px, 15% white opacity) separating each block

---

**WHAT WE DO**
Light background (#F5F4F0).
Section header + 2–3 sentences of positioning copy: single column, max-width 680px, centered. Serif headline.
Below the copy: three tiles arranged in a row (desktop) or stacked (mobile).
Each tile:
- Thin top border (1px, #D0CFC9)
- Title in sans-serif, semibold, 14px, letter-spaced
- Subtitle (italic, serif, muted)
- Body copy 14–15px
- Generous internal padding: 32px
- No card shadow — the border and whitespace define the tile

---

**HOW WE WORK (PROCESS)**
Dark background (#0A0A0A) or neutral dark gray (#111111).
Section header centered at top.
Four steps in a horizontal row on desktop, stacked on mobile.
Each step:
- Step number: large, very light, almost-ghost number ("01", "02") — used as visual texture, not primary element. Approximately 80–100px, low opacity (10–15%)
- Step name: sans-serif, white, semibold, 15px, letter-spaced
- Body copy: 14px, muted off-white
- Thin vertical divider (1px) between steps on desktop

---

**CREDIBILITY**
Light background (#F5F4F0).
Single column, max-width 640px, centered.
Section header, then 3–4 sentences of body copy.
Below the copy: a blockquote — styled distinctly:
- Left border: 2px solid accent color (see Section 4 for the accent)
- Text in serif, italic, 18–20px, slightly indented
- No quotation marks — the border serves as the visual signal

---

**SERVICES / OFFERS**
White or off-white background.
Three cards in a row on desktop, stacked on mobile.
Each card:
- Clean border: 1px solid #D0CFC9
- Card header: service name, bold sans-serif, 14px, letter-spaced
- Price line: serif, 22–24px, dark
- Bullet list: 14px, generous line spacing, with thin dash (—) as bullet
- CTA text link at bottom of card: "Enquire →" in accent color
- Rounded corners: 4px maximum — keep it architectural, not bubbly
- No drop shadows

---

**FOR WHOM**
Dark background (#0A0A0A).
Three client profiles stacked in a single column, max-width 640px, centered.
Each profile:
- Bold client title in white, serif or sans-serif, 17–18px
- Supporting copy in muted off-white, 15px
- Thin horizontal rule between profiles

---

**SHOWCASE TEASER**
Light background (#F5F4F0).
Section header centered. Small NDA note directly below in muted small caps.
Three project blocks stacked (desktop: could go 2-column if space allows, but 1-column reads more premium).
Each project:
- Category label in small caps, gray, 11px
- 3–4 sentences of project description, serif body copy, 16px
- Italic note at bottom: "(Illustrative — representative of work type only)"
- Thin rule between projects

---

**FAQ**
Dark background (#0A0A0A) or white — pick whichever creates contrast with the previous section.
Accordion format (Framer supports this natively):
- Each question collapsed by default
- Question text: sans-serif, white or dark, 15–16px, medium weight
- Expand/collapse trigger: a small "+" or "→" on the right
- Answer text appears below on expansion, 14–15px, muted
- Thin rule below each item

---

**PRICING TEASER**
White or off-white background.
Single column, max-width 600px, centered.
Section header: "Investment"
One paragraph of body copy, 16–18px, generous line height.
Optional: a thin decorative horizontal rule above and below the pricing paragraph to visually separate it.

---

**FINAL CTA BLOCK**
Full-bleed dark background (#0A0A0A). High contrast.
Content centered, significant vertical padding (160px top and bottom).
Headline: serif, white, 42–52px, centered, max-width 700px.
Supporting copy: sans-serif, 16px, muted off-white, centered, max-width 520px.
Two buttons side by side (or stacked on mobile):
1. Primary: white fill, black text, "Book a Strategy Call"
2. Secondary: no fill, white border, white text, "Send an Enquiry"

---

**FOOTER**
Dark background (#0A0A0A) or very dark gray (#0F0F0F).
Two rows:
- Row 1: Navigation links left, email center (or right), LinkedIn icon right
- Row 2: Tagline left, legal note center-right, copyright right
Fine type: 12px, muted gray (#6B6B6B).
Thin top border (1px, 10% white) separates footer from content above.

---

## 4. VISUAL DIRECTION

### Color Palette

| Role | Color | Hex |
|------|-------|-----|
| Primary background (dark) | Near-black | `#0A0A0A` |
| Primary background (light) | Warm off-white | `#F5F4F0` |
| Body text on light | Deep black | `#0A0A0A` |
| Body text on dark | Off-white | `#E8E7E3` |
| Muted text (captions, labels) | Warm gray | `#9B9A96` |
| Muted body on dark | Soft gray-white | `#B0AFA9` |
| **Accent** | Warm amber-gold | `#C9A96E` |
| Card borders, dividers | Light warm gray | `#D0CFC9` |

**On the accent color:**
`#C9A96E` is a refined warm gold — not loud, not yellow. It reads as Swiss-premium: the color of quality leather, aged brass, architectural detail. Use it sparingly: CTA hover states, blockquote borders, the "Enquire →" text link on service cards, hover underlines on navigation. Never use it as a background or large block color. Less is more.

### Typography

**Headline font:** DM Serif Display
- Free on Google Fonts; import directly into Framer
- Use for: primary headlines, section headers, the blockquote
- Weights: Regular (400) only — do not use bold for this font
- It is elegant without being overwrought. Sharp, editorial, not decorative

**Body / UI font:** Inter
- Free on Google Fonts; pre-loaded in Framer
- Use for: all body copy, navigation, buttons, labels, captions
- Weights: Regular (400) for body, Medium (500) for button text, Semibold (600) for service tile titles and emphasis
- Do not use Inter Bold (700) for body text — it creates visual noise

**Type scale (desktop):**

| Element | Font | Size | Weight | Line height |
|---------|------|------|--------|-------------|
| Hero headline | DM Serif Display | 64–72px | 400 | 1.1 |
| Section headers | DM Serif Display | 36–42px | 400 | 1.2 |
| Sub-headers / tile titles | Inter | 14px | 600 | 1.4 |
| Section labels | Inter | 11px | 500 | 1.4 |
| Body copy | Inter | 15–16px | 400 | 1.75 |
| Blockquote | DM Serif Display | 19–21px | 400 italic | 1.6 |
| Small / legal | Inter | 12px | 400 | 1.5 |
| CTA button text | Inter | 13–14px | 500 | 1 |
| Price display | DM Serif Display | 22–24px | 400 | 1.2 |

Letter spacing: apply +0.08em to all Inter labels and button text in small caps. Apply +0.04em to navigation items.

### Spacing Philosophy

Sections should breathe. The minimum vertical padding for any full-width section is 100px top and bottom. Prefer 120–160px on desktop for major sections. Do not compress sections to fit more content on screen — the perceived quality of the site lives in the whitespace. When in doubt, add space, not content.

Between text elements within a section, maintain consistent vertical rhythm: 8px between related elements (label and headline), 24px between a headline and its body copy, 48px between a body block and a CTA.

Maximum content width: 1200px outer container. Content columns: 640–720px max for single-column text. Three-column grids: allow natural width within a 1200px container.

### No Stock Photography

Do not use stock photos. Do not use lifestyle images, team photos, or generic office scenes. The site communicates through typography and space alone — this is a deliberate brand decision that signals premium and confident. When a visual element is needed beyond type, use:

- Abstract architectural line textures at very low opacity (4–8%) on dark sections
- Simple geometric elements: a single horizontal rule, a thin grid overlay
- High-contrast typographic details enlarged and cropped as graphic elements (a single letter, a number)

If Framer asks you to add a hero image, leave it empty or use a solid color. The copy is the visual.

---

## 5. IMAGE AND VISUAL SUGGESTIONS

Since the site is typographic and non-photographic, visuals are used as texture, not content. Here are the specific directions:

**Option 1 — Textured paper overlay (recommended for light sections)**
A subtle, slightly rough paper texture at 3–5% opacity over the `#F5F4F0` background adds depth without being visible at a glance. Use CSS background-image with a small tiling texture, or find a high-resolution scan and set it as a background layer in Framer at very low opacity.
Unsplash search terms: `"paper texture minimal"`, `"light grain texture"`, `"off white paper grain"`

**Option 2 — Architectural photography (for Showcase section header, optional)**
One wide, desaturated architectural photograph — a Swiss building facade, a clean concrete interior, a grid of windows — used as a subtle section background at 10–15% opacity behind the Showcase header. Not as content, but as atmospheric texture.
Unsplash search terms: `"swiss architecture brutalist"`, `"concrete minimal architecture"`, `"architectural grid facade"`, `"Zurich building detail"`

**Option 3 — Abstract dark texture (for dark sections)**
On the `#0A0A0A` sections, a very subtle dark noise or grain texture at 5% opacity adds visual richness without introducing color.
Unsplash search terms: `"dark texture grain minimal"`, `"black noise texture"`, `"dark abstract minimal"`

**Option 4 — Typographic graphic element**
In the hero section or a transition section, a single large character from DM Serif Display — set to 300–400px, rotated slightly, at 4–6% opacity — can function as a decorative background element. For example: a large italicized "A" from APEX, used as ghosted texture behind the main copy. This is an APEX-specific brand element. Subtle, intentional, distinctive.

**On icons:**
Use Phosphor Icons or Feather Icons (both free, available in Framer) if any icon is needed. Use line-style icons only, at 18–20px. Never use filled icons or emoji as interface elements.

---

## 6. MOBILE CONSIDERATIONS

### Key breakpoints to configure in Framer:

| Breakpoint | Width | Key changes |
|-----------|-------|-------------|
| Desktop | 1280px | Full layout as described |
| Tablet | 768px | 3-column grids collapse to 2-column |
| Mobile | 390px | All grids collapse to single column |

### Mobile-specific rules:

**Typography:**
- Hero headline: reduce to 36–40px on mobile (max 42px)
- Section headers: 26–30px
- Body copy: 15px minimum — do not go below this on mobile
- Labels: 11px, unchanged

**Layout:**
- All three-column sections collapse to single column on mobile
- Service cards stack vertically with 24px gap between them
- The process steps stack vertically in numbered sequence
- The hero section: reduce vertical padding, headline shortens, CTA button becomes full-width

**CTA buttons:**
- Minimum touch target: 48px height
- On mobile, primary CTA becomes full-width (100% of container)
- Secondary button stacks below primary with 12px gap

**Navigation:**
- Desktop: horizontal navigation bar, links left or center, CTA button right
- Mobile: hamburger icon (three lines) opens a full-screen overlay menu
- Framer handles this automatically in most templates — verify it works before launch

**Checklist before publishing:**
- [ ] Open the site on an actual phone (not just Framer's preview)
- [ ] Verify all text is readable without zooming
- [ ] Verify CTA buttons are tappable
- [ ] Verify the FAQ accordion opens and closes correctly on touch
- [ ] Verify navigation works and hamburger menu opens

---

## 7. CTA PLACEMENT

CTAs appear at five locations across the homepage. Each has a specific role.

**CTA 1 — Hero section**
"Book a Strategy Call" (primary button)
"View Services →" (secondary text link)
Links to: Calendly booking page (new tab) / #services anchor

**CTA 2 — After the What We Do section**
Single text link: "See how it works →" scrolling to the process section
Not a button — just a lightweight directional nudge

**CTA 3 — After the Services / Offers section**
Each service card has its own "Enquire →" text link
Links to: contact@apexcommunication.ch (mailto) or the Contact page
This is where the transaction-oriented visitor exits

**CTA 4 — After the FAQ section**
A transitional sentence: "Still have questions? Book fifteen minutes."
Linked text, not a button. Lighter weight, maintains momentum.
Links to: Calendly booking page

**CTA 5 — Final CTA Block**
"Book a Strategy Call" (primary button, white fill) → Calendly
"Send an Enquiry" (secondary button, outlined) → Contact page or mailto

**Calendly setup:**
Create a free Calendly account. Set up a 30-minute "Strategy Call" event type. Set availability to match your schedule. The Calendly link goes everywhere the primary CTA appears. This removes friction — a visitor should be able to book within two clicks from anywhere on the page.

**Contact form (alternative):**
On the Contact page, use Framer's native form component. Fields: Name, Email, Company, Brief description of project, Timeline. Connect to your email via Framer's built-in form notifications (Settings → Forms in Framer). Test it before launch.

---

## 8. TRUST ELEMENTS

Since APEX is a new studio without a public client portfolio, trust is built through process transparency, professional language, and honest positioning — not through fabricated social proof.

**What to include:**

**Confidentiality statement (footer + contact page):**
One line in the footer: "All engagements conducted under mutual NDA." On the contact page, a brief note: "Enquiries are confidential. Project details are shared only as necessary for scoping." This signals professionalism and protects the client-first positioning.

**Process transparency (the How We Work section):**
A rigorous, detailed process description is itself a trust signal. It demonstrates that APEX has a methodology, not just an attitude. The four-step process description accomplishes this.

**No-guarantee disclaimer (written positively, in the FAQ):**
The FAQ answer to "Can you guarantee fundraising success?" is honest and direct: "No — no one can." This is counterintuitively more trustworthy than vague promises. It signals that APEX is operated by someone who understands the difference between what they control and what they do not.

**Showcase with clear labels:**
Labeling illustrative project summaries clearly as "(Illustrative — representative of work type only)" is more credible than presenting fictional case studies as real. It demonstrates integrity and pre-empts the question.

**No testimonials yet:**
Do not fabricate testimonials. Do not use placeholder quote blocks. Leave the testimonials section absent entirely until you have one real client willing to provide a quote. An empty testimonials section is worse than no testimonials section.

**The founder's voice:**
The blockquote in the credibility section — the founding philosophy statement — is the most authentic trust signal on the site. It communicates genuine thinking. Keep it sharp and specific.

---

## 9. FOOTER STRUCTURE

The footer is a single dark (`#0A0A0A`) strip at the bottom of every page. It does not need to be complex.

**Layout (desktop):**

Row 1 (flex row, space-between):
- Left: APEX (wordmark, small, 13px, letter-spaced)
- Center: Navigation — Home · Services · Showcase · Contact
- Right: LinkedIn icon (SVG, link to LinkedIn profile page)

Row 2 (flex row, space-between, smaller type):
- Left: Tagline — "Strategic communication, architecturally built. Zürich."
- Right: contact@apexcommunication.ch (linked)

Row 3 (centered or left-aligned, smallest type):
- Legal note (one line): "All client work conducted under NDA. Illustrative showcases do not represent actual clients. No commercial outcomes guaranteed."
- Copyright: "© 2026 APEX Strategic Communication. All rights reserved."

**Social media at launch:**
LinkedIn only. Do not add Instagram, Twitter/X, or other platforms until you have consistent content for them. An empty or rarely-updated social profile does more damage than having no link at all.

**LinkedIn setup:**
Create a LinkedIn Company Page for APEX Strategic Communication. Add the logo, tagline, and a brief description. Link to it from the footer. This can be done in 20 minutes.

---

## 10. ONE-DAY BUILD PLAN

This plan assumes you are starting fresh in Framer with no prior experience. Follow it in sequence. Total time: 7–8 focused hours.

---

### PRE-BUILD (30 minutes, the night before or that morning)

- Create a Framer account at framer.com (free plan to start)
- Create a Google Fonts account to access DM Serif Display (or note: Framer has Google Fonts built in — just search for it in the font picker)
- Have the landing-page-copy.md file open and ready
- Have your Calendly link ready (or create a free Calendly account now — takes 15 minutes)
- Have the contact email ready: contact@apexcommunication.ch
- Set up that email address (use Google Workspace for CHF ~6/month or forward from your domain registrar)

---

### HOUR 1 — Template selection and initial setup (9:00–10:00)

1. In Framer, go to Templates
2. Search for templates using these terms: "agency dark", "studio portfolio", "consulting", "minimal dark portfolio"
3. Look for templates with these characteristics:
   - Dark hero section with centered text
   - Clean section alternation (dark / light / dark)
   - Serif + sans-serif typographic hierarchy already in place
   - Simple, non-decorative layout
   - Good starting point candidates: any "Studio" or "Agency" category template rated 4+ stars
4. Select the template and click "Use this template" — this creates a copy in your workspace
5. Rename the project: "APEX Website — Launch"
6. In Framer Settings: set the page title to "APEX — Strategic Communication & Pitch Architecture"
7. In Framer Settings: add a favicon — use a simple black square with "A" in white, or the APEX wordmark. Create this in Canva (free) in 10 minutes: 512x512px, black background, white "A" in DM Serif Display.

---

### HOUR 2 — Typography and color system setup (10:00–11:00)

1. Go to Site Settings → Fonts. Add DM Serif Display and Inter from Google Fonts.
2. Open the Style panel. Update the global color tokens to match APEX palette (see Section 4). Most Framer templates have a color variable system — update these variables rather than changing colors one by one.
3. Set background colors for the alternating sections according to the layout plan above.
4. Update the base body font to Inter, size 15px, weight 400, line height 1.75.
5. Update the headline style to DM Serif Display, size variable per section.
6. Delete or hide any sections in the template that you will not need. Do not leave placeholder sections — they create confusion during build.

---

### HOUR 3 — Hero + Context + Problem sections (11:00–12:00)

1. Start with the Hero. Replace all placeholder text with the APEX copy from Section 1 of the landing-page-copy.md file. Copy exactly — do not paraphrase.
2. Update the CTA button text, link it to your Calendly URL.
3. Update the secondary link to scroll to the services anchor.
4. Move to the Context Statement section. If the template does not have this section, add a new Frame/Section below the hero. Set it to light background. Add the section label, then the paragraph.
5. Add the Problem section below. Dark background. Add three problem blocks with bold headers and supporting copy. Use horizontal rules to separate them (in Framer: add a Rectangle, set height to 1px, set background to white at 15% opacity).
6. Review at 100% scale. Check spacing. Add breathing room if sections feel compressed.

---

### HOUR 4 — What We Do + Process + Credibility (12:00–13:00)

1. Build the What We Do section. Three service tiles in a row. For each tile: add a Frame, set a top border (1px, #D0CFC9), add text layers for title, subtitle, body copy.
2. Build the Process section. Four steps. Use the ghost number technique: a large DM Serif Display number at 8% opacity as a background layer, with the step name and body copy on top.
3. Build the Credibility section. Light background. Body copy centered. Then the blockquote: add a Rectangle (2px wide, 40px tall, accent color `#C9A96E`) to the left of the quote text. Group them.
4. Save and preview at this point. Check on mobile view in Framer (toggle the breakpoint selector at the top). Note any text that overflows or elements that collide at mobile width — you will fix these in Hour 7.

---

### HOUR 5 — Services + For Whom + Showcase + FAQ (13:00–14:30)

1. Build the three service cards. Copy the card layout from the template if available, or create Frames with: border, title, price, bullet list, CTA link.
2. Build the For Whom section. Dark background. Three client profiles stacked. Use horizontal rules between them.
3. Build the Showcase section. Light background. Add the NDA note in small caps below the header. Three project blocks stacked, each with the category label, body copy, and italic illustrative note.
4. Build the FAQ using Framer's accordion component (search "accordion" in the component panel, or build manually with toggle interactions). Add all 8 questions and answers from Section 10 of the copy file.

---

### HOUR 6 — Pricing + Final CTA + Footer (14:30–15:30)

1. Build the Pricing Teaser section. Single paragraph, centered, generous padding.
2. Build the Final CTA Block. Dark full-bleed section. Large headline. Two buttons. Link primary CTA to Calendly. Link secondary to Contact page (you will build this next).
3. Build the Footer. Two-row structure as described in Section 9. Add navigation links. Link the email. Add a placeholder LinkedIn icon (link to be added once LinkedIn page is live). Add legal copy and copyright.
4. Create the Contact page (duplicate Home page, delete all sections except Footer, add a new Form section using Framer's form component). Add: Name, Email, Company, Project Brief, Timeline fields. Connect to your email in Framer Settings → Forms.
5. Create a placeholder Services page and Showcase page (can be simple at launch — one section each with the key content).

---

### HOUR 7 — Mobile optimization (15:30–16:30)

1. Switch to the mobile breakpoint (390px) in Framer's canvas view.
2. Go through every section and fix layout issues:
   - Change 3-column grids to 1-column stacks
   - Reduce headline sizes (hero: 38px, section headers: 28px)
   - Make buttons full-width
   - Ensure body text is minimum 15px
   - Ensure padding is reduced but not eliminated (40–60px per section on mobile)
3. Test the FAQ accordion on mobile.
4. Test the navigation hamburger menu.
5. Make sure the footer stacks correctly on mobile.

---

### HOUR 8 — Final review, domain connection, and publish (16:30–17:00)

1. Do a full read-through of every section on desktop. Check for typos, broken links, and layout inconsistencies.
2. Check: all CTA buttons link correctly (Calendly for primary, Contact page or mailto for secondary).
3. Check: FAQ answers are all present.
4. Check: illustrative showcase notes are visible.
5. Upgrade Framer to the Pro plan (USD 30/month).
6. Go to Framer Settings → Custom Domain. Enter `apexcommunication.ch`. Follow the DNS instructions (you will need to add a CNAME record at your domain registrar — Framer shows you exactly which records to add).
7. DNS propagation takes 10 minutes to 24 hours. Once live, visit the domain and verify the site loads correctly.
8. Send yourself a test form submission from the Contact page to verify the email notification arrives.
9. Publish. Done.

---

### Post-launch (Week 1):

- Write the LinkedIn Company Page for APEX and link it from the footer
- Set up the contact@apexcommunication.ch email if not already done
- Share the site with 3–5 trusted people and ask for honest feedback on clarity
- Book your first Calendly call

---

*Build instructions for APEX Strategic Communication. Internal reference document.*
*Last updated: May 2026.*
