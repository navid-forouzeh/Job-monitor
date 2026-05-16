# APEX — Notion Workspace Structure
**Strategic Communication & Pitch Architecture Studio**
*Navid Forouzeh · Zürich*

> This document defines the complete Notion operating system for APEX. Build each database exactly as specified. The system is designed to run the full business cycle: lead generation → client management → project delivery → invoicing → content → knowledge base.

---

## HOW TO BUILD THIS IN NOTION

1. Create a new Notion page titled **"APEX OS"** — this is your master workspace.
2. Create each database as a **Full-page database** (not inline) so it can be linked across the workspace.
3. Use **Relations** to connect Leads → Clients → Projects → Invoices.
4. Build a **Home dashboard** page that pulls widgets from each database.
5. Keep the sidebar clean: only the Home page and the 11 databases visible at top level.

---

## DATABASE 1 — LEADS
**Icon:** 🎯

**Purpose:** Track every potential client from first touch to conversion — the top of your entire business pipeline.

### Properties

| Property Name | Type | Options / Notes |
|---|---|---|
| Name | Title | Full name of the contact |
| Company | Text | Company or organization |
| Role | Select | Founder / CEO / CFO / CTO / Investor / Partner / Other |
| Industry | Select | Fintech / Deeptech / SaaS / Healthcare / Real Estate / Consulting / VC / Other |
| Source | Select | LinkedIn / Cold Email / Referral / Event / Inbound / Other |
| Status | Select | New / Contacted / Replied / Called / Proposal Sent / Won / Lost |
| Priority | Select | High / Medium / Low |
| LinkedIn URL | URL | Direct profile link |
| Email | Email | |
| Last Contact Date | Date | |
| Notes | Text | Free-form notes from conversations |
| Related Project | Relation | → Projects database |

### Status Options (with color coding)
- **New** — Gray
- **Contacted** — Blue
- **Replied** — Yellow
- **Called** — Orange
- **Proposal Sent** — Purple
- **Won** — Green
- **Lost** — Red

### Views to Create

**View 1: Pipeline Board** (Board view, grouped by Status)
- Show: Name, Company, Priority, Last Contact Date
- Sort: Priority descending
- Filter: Status is not Lost

**View 2: Active Leads Table** (Table view)
- Filter: Status is not Won AND Status is not Lost
- Sort: Last Contact Date ascending (oldest first = needs attention)
- Show all properties

**View 3: Follow-up Needed** (List view)
- Filter: Status = Contacted OR Replied, AND Last Contact Date is before 5 days ago
- Show: Name, Company, Status, Last Contact Date
- Sort: Last Contact Date ascending

### Example Entries

**Entry 1**
- Name: Lukas Brenner
- Company: Alchemist Ventures
- Role: Founder
- Industry: Fintech
- Source: LinkedIn
- Status: Proposal Sent
- Priority: High
- LinkedIn URL: linkedin.com/in/lukasbrenner
- Last Contact Date: 2026-05-10
- Notes: Met at Impact Hub event. Raising Series A Q3. Said current deck "needs a full overhaul." Warm intro from Miriam K. Sent COMMAND offer proposal.

**Entry 2**
- Name: Dr. Petra Vogel
- Company: NordLogic GmbH
- Role: CEO
- Industry: SaaS
- Source: Cold Email
- Status: Replied
- Priority: Medium
- Email: p.vogel@nordlogic.de
- Last Contact Date: 2026-05-13
- Notes: Replied to cold email sequence. Interested in board presentation work. Asked for portfolio samples. Send case studies and book a call.

### Weekly Use (Monday Ritual)
Every Monday morning, Navid opens the Pipeline Board view and scans left to right. He identifies every lead in "Contacted" or "Replied" that hasn't been touched in 5+ days and moves them to a follow-up queue. He updates the Status for any leads that moved forward or went cold over the week. New leads added from the weekend's LinkedIn activity get entered here first. The goal: the board is never stale. Takes 5 minutes maximum.

---

## DATABASE 2 — CLIENTS
**Icon:** 🤝

**Purpose:** Centralize all client relationships — active, past, and potential — with full contact info and revenue history.

### Properties

| Property Name | Type | Options / Notes |
|---|---|---|
| Company Name | Title | |
| Contact Person | Text | Primary point of contact |
| Email | Email | |
| Phone | Phone | |
| Industry | Select | Fintech / Deeptech / SaaS / Healthcare / Real Estate / Consulting / VC / Other |
| Stage | Select | Startup / Scale-up / KMU / Enterprise |
| Status | Select | Active / Past / Potential |
| Total Revenue (CHF) | Number | Format: CHF, running total across all projects |
| Start Date | Date | Date of first project |
| Notes | Text | Relationship notes, preferences, communication style |
| Related Projects | Relation | → Projects database |

### Status Options
- **Active** — Green (currently on a project)
- **Past** — Gray (completed, no active project)
- **Potential** — Blue (not yet converted, stronger than a lead — e.g., intro made)

### Views to Create

**View 1: All Clients Table** (Table view)
- Show all properties
- Sort: Total Revenue descending

**View 2: Active Clients** (Table view)
- Filter: Status = Active
- Show: Company Name, Contact Person, Email, Related Projects, Notes
- This is the view Navid checks during active project weeks

### Example Entries

**Entry 1**
- Company Name: Alchemist Ventures AG
- Contact Person: Lukas Brenner
- Email: lukas@alchemistventures.ch
- Industry: Fintech
- Stage: Startup
- Status: Active
- Total Revenue: 4,800 CHF
- Start Date: 2026-05-15
- Notes: Prefers short async updates via WhatsApp. Very decisive. Does not need hand-holding. Deadline-sensitive. Has a co-founder who may review final deck — include her in delivery email.

**Entry 2**
- Company Name: NordLogic GmbH
- Contact Person: Dr. Petra Vogel
- Email: p.vogel@nordlogic.de
- Industry: SaaS
- Stage: Scale-up
- Status: Past
- Total Revenue: 2,400 CHF
- Start Date: 2026-04-01
- Notes: Completed SIGNAL package for board presentation. Very satisfied. Left a LinkedIn testimonial. May return for investor narrative in Q4. Keep warm with monthly check-in.

### Weekly Use (Monday Ritual)
Navid checks Active Clients view every Monday to confirm all ongoing projects have a next action assigned. He reviews the Notes column for communication preferences before reaching out. Once a project is delivered and invoice is paid, Status moves from Active to Past. Total Revenue updates automatically via a formula or manual entry after each invoice is marked Paid.

---

## DATABASE 3 — PROJECTS
**Icon:** 📁

**Purpose:** Manage every client engagement from intake to delivery — the operational heart of APEX.

### Properties

| Property Name | Type | Options / Notes |
|---|---|---|
| Project Name | Title | e.g., "Alchemist Ventures — Series A Deck" |
| Client | Relation | → Clients database |
| Offer Type | Select | CLARITY / SIGNAL / COMMAND |
| Status | Select | Intake / Architecture / Build / Review / Delivered |
| Start Date | Date | |
| Deadline | Date | |
| Final Price (CHF) | Number | Format: CHF |
| Hours Spent | Number | Log manually or via toggle |
| Deliverables | Text | List what's included (e.g., "12-slide deck, narrative script, speaker notes") |
| Notes | Text | Internal notes, client requests, version history |
| Invoice Sent | Checkbox | |
| Paid | Checkbox | |

### Offer Type Definitions
- **CLARITY** — Starter tier: diagnosis + strategic brief
- **SIGNAL** — Core tier: full deck or executive narrative
- **COMMAND** — Premium tier: end-to-end pitch system

### Status Options (with color coding)
- **Intake** — Gray (questionnaire received, kick-off pending)
- **Architecture** — Blue (narrative structure and outline)
- **Build** — Yellow (slides / document being built)
- **Review** — Orange (client feedback round)
- **Delivered** — Green (final files sent)

### Views to Create

**View 1: Active Board** (Board view, grouped by Status)
- Filter: Status is not Delivered
- Show: Project Name, Client, Deadline, Offer Type
- This is the daily operational view

**View 2: Deadline Calendar** (Calendar view, by Deadline)
- Show all projects
- Color: by Offer Type
- Critical for spotting deadline collisions

**View 3: All Projects Table** (Table view)
- Show all properties
- Sort: Start Date descending

### Example Entries

**Entry 1**
- Project Name: Alchemist Ventures — Series A Pitch System
- Client: Alchemist Ventures AG
- Offer Type: COMMAND
- Status: Architecture
- Start Date: 2026-05-15
- Deadline: 2026-05-29
- Final Price: 4,800 CHF
- Hours Spent: 6
- Deliverables: 14-slide investor deck, founder narrative script, Q&A prep sheet, speaker notes
- Notes: Client wants dark theme. Benchmark: Stripe's Series B deck aesthetic. Co-founder review on day 7.
- Invoice Sent: ✓ (deposit invoice)
- Paid: ✓ (deposit received)

**Entry 2**
- Project Name: NordLogic — Q2 Board Presentation
- Client: NordLogic GmbH
- Offer Type: SIGNAL
- Status: Delivered
- Start Date: 2026-04-01
- Deadline: 2026-04-14
- Final Price: 2,400 CHF
- Hours Spent: 11
- Deliverables: 18-slide board deck, executive summary (1-pager)
- Notes: Delivered on time. Client requested one extra revision (covered in scope). Final files sent via WeTransfer. Testimonial received.
- Invoice Sent: ✓
- Paid: ✓

### Weekly Use (Monday Ritual)
The Active Board is the first thing Navid opens after the Leads pipeline. He checks which stage each project is in, identifies what needs to happen this week per project, and confirms no deadline is approaching without a clear plan. He updates Hours Spent weekly to track efficiency. If a project is stuck in Review for more than 3 days, he follows up with the client proactively.

---

## DATABASE 4 — OFFERS
**Icon:** 📦

**Purpose:** Define, track, and refine APEX's service offerings — a single source of truth for what you sell.

### Properties

| Property Name | Type | Options / Notes |
|---|---|---|
| Offer Name | Title | e.g., "COMMAND — Full Pitch System" |
| Type | Select | Starter / Core / Retainer |
| Price Range | Text | e.g., "CHF 4,500 – 6,000" |
| Status | Select | Active / Paused / Testing |
| Last Updated | Date | |
| Notes | Text | What's included, ideal client, positioning notes |

### Status Options
- **Active** — Currently selling this offer
- **Paused** — Temporarily not selling (refining or seasonal)
- **Testing** — Running a trial price or format

### Views to Create

**View 1: Active Offers** (Table view)
- Filter: Status = Active
- Show: Offer Name, Type, Price Range, Notes

**View 2: All Offers** (Table view)
- Show all properties, all statuses

### Example Entries

**Entry 1**
- Offer Name: COMMAND — Full Pitch System
- Type: Core
- Price Range: CHF 4,500 – 6,000
- Status: Active
- Last Updated: 2026-05-01
- Notes: Includes full investor deck (up to 16 slides), founder narrative, speaker notes, Q&A prep. Target: founders raising Seed to Series A. Delivery: 10 business days. 2 revision rounds included. Deposit: 50% upfront.

**Entry 2**
- Offer Name: CLARITY — Strategic Brief
- Type: Starter
- Price Range: CHF 800 – 1,200
- Status: Active
- Last Updated: 2026-05-01
- Notes: 90-min intake call + written strategic brief (positioning, narrative spine, 3 core messages). Entry point for founders not ready for full deck. Often upsells to SIGNAL or COMMAND. Delivery: 3 business days.

### Weekly Use
Navid reviews this database whenever he's writing a proposal — he copies the offer details directly into the proposal template. When pricing or scope evolves based on client feedback, he updates the Notes field immediately. At the end of each month, he reviews whether any offers should be tested at a different price point.

---

## DATABASE 5 — OUTREACH TRACKER
**Icon:** 📤

**Purpose:** Track every individual outreach message sent — prevent double-messaging and ensure systematic follow-up.

### Properties

| Property Name | Type | Options / Notes |
|---|---|---|
| Name | Title | Full name of person contacted |
| Company | Text | |
| Platform | Select | LinkedIn / Email / Phone |
| Message Type | Select | Cold / Follow-up 1 / Follow-up 2 / Warm |
| Date Sent | Date | |
| Response | Select | Yes / No / Pending |
| Notes | Text | What was sent, any reply context |
| Related Lead | Relation | → Leads database |

### Response Options
- **Yes** — Responded positively (reply, call booked, interest expressed)
- **No** — No response after full sequence, or explicitly declined
- **Pending** — Awaiting response

### Views to Create

**View 1: Response Board** (Board view, grouped by Response)
- Shows at a glance where conversations stand
- Filter: none (show all active outreach)

**View 2: Outreach Calendar** (Calendar view, by Date Sent)
- Track outreach cadence and avoid messaging clusters on the same day

**View 3: No Response + Older Than 5 Days** (Table view)
- Filter: Response = Pending AND Date Sent is before 5 days ago
- Sort: Date Sent ascending
- This is the follow-up queue — action this every Monday

### Example Entries

**Entry 1**
- Name: Marc Hofmann
- Company: Alpine Capital Partners
- Platform: LinkedIn
- Message Type: Cold
- Date Sent: 2026-05-12
- Response: Pending
- Notes: Sent cold DM referencing his post about Series A pipeline. Mentioned APEX's DACH positioning. Short and specific. Follow-up due May 17.
- Related Lead: Marc Hofmann (→ Leads)

**Entry 2**
- Name: Sabine Kühn
- Company: Kühn & Partner Strategy
- Platform: Email
- Message Type: Follow-up 1
- Date Sent: 2026-05-09
- Response: Yes
- Notes: Followed up on cold email from May 2. She replied and asked for a portfolio sample. Sent case study PDF. Booking call via Calendly.
- Related Lead: Sabine Kühn (→ Leads)

### Weekly Use (Monday Ritual)
Navid opens the "No Response + Older Than 5 Days" view and sends follow-up messages to everyone who hasn't replied. He logs each follow-up as a new entry (Message Type: Follow-up 1 or 2) rather than editing the original. This creates a full history. After two follow-ups with no response, he marks Response = No and stops. He tracks weekly outreach volume (aim: 10–15 new contacts/week).

---

## DATABASE 6 — CONTENT CALENDAR
**Icon:** 📅

**Purpose:** Plan, draft, and track LinkedIn content — ensuring consistent posting without scrambling for ideas.

### Properties

| Property Name | Type | Options / Notes |
|---|---|---|
| Post Title | Title | Working title or hook line |
| Platform | Select | LinkedIn (only, for now) |
| Format | Select | Text / Image / Carousel |
| Status | Select | Idea / Drafting / Scheduled / Published |
| Publish Date | Date | |
| Topic Tag | Select | Pitch Education / Strategic Communication / Founder Mistakes / Swiss Ecosystem / Behind the Scenes |
| Impressions | Number | Fill after publishing |
| Likes | Number | Fill after publishing |
| Comments | Number | Fill after publishing |
| Notes | Text | Draft copy, ideas, links to inspiration |

### Status Options
- **Idea** — Just a concept or hook saved
- **Drafting** — Being written
- **Scheduled** — Finalized, set to post
- **Published** — Live on LinkedIn

### Views to Create

**View 1: Content Calendar** (Calendar view, by Publish Date)
- Shows the full posting schedule visually
- Color: by Topic Tag

**View 2: Production Board** (Board view, grouped by Status)
- Shows pipeline from Idea → Published
- Filter: Platform = LinkedIn

**View 3: Performance Table** (Table view)
- Filter: Status = Published
- Sort: Impressions descending
- Use this to identify top-performing content and double down

### Example Entries

**Entry 1**
- Post Title: "The 3 slides every investor reads first"
- Platform: LinkedIn
- Format: Text
- Status: Scheduled
- Publish Date: 2026-05-20
- Topic Tag: Pitch Education
- Notes: Educational post. Hook: "Before they read your problem slide, they've already formed an opinion." End with soft CTA. No image needed. Aim for 600–700 words.

**Entry 2**
- Post Title: "A 28-slide deck is not a strategy"
- Platform: LinkedIn
- Format: Text
- Status: Published
- Publish Date: 2026-05-13
- Topic Tag: Founder Mistakes
- Impressions: 2,340
- Likes: 67
- Comments: 14
- Notes: Strong performer. Contrarian take worked well. Comments mostly from founders agreeing. Consider a follow-up post on deck length guidelines.

### Weekly Use (Monday Ritual)
Navid opens the Production Board and checks that at least 3 posts are in "Scheduled" for the upcoming week. If any slot is empty, he moves the best "Idea" into "Drafting" and writes it that same Monday morning. He updates performance metrics for all published posts from the prior week. Strong performers get flagged for repurposing or expansion into carousel format.

---

## DATABASE 7 — PORTFOLIO EXAMPLES
**Icon:** 🗂️

**Purpose:** Curate a library of showcase-ready work — real (masked) and fictional — for use in proposals and the website.

### Properties

| Property Name | Type | Options / Notes |
|---|---|---|
| Project Title | Title | Descriptive title without revealing client |
| Type | Select | Fictional / Real (Masked) |
| Client | Text | "Fintech Startup, Zürich" — masked description |
| Industry | Select | Fintech / Deeptech / SaaS / Healthcare / Real Estate / Other |
| Deliverable Type | Select | Pitch Deck / Board Presentation / Executive Narrative / Strategy Brief |
| Showcase Text | Text | 2–3 sentence description of the challenge, approach, and outcome |
| Visuals | Files & Media | Upload slide screenshots or PDF exports |
| Status | Select | Draft / Ready to Show / NDA Required |

### Status Options
- **Draft** — Work in progress, not yet polished enough to show
- **Ready to Show** — Cleared to share in proposals and on website
- **NDA Required** — Real client work, only show after signing NDA

### Views to Create

**View 1: Gallery** (Gallery view)
- Filter: Status = Ready to Show
- Show: Project Title, Industry, Deliverable Type, Visuals
- Use this view when sharing the portfolio link with prospects

**View 2: All Work Table** (Table view)
- Show all properties and all statuses
- Internal reference only

### Example Entries

**Entry 1**
- Project Title: Series A Pitch — Climate Fintech (Zürich)
- Type: Real (Masked)
- Client: Climate Fintech Startup, Zürich, 12 employees
- Industry: Fintech
- Deliverable Type: Pitch Deck
- Showcase Text: The founder had a compelling product but a deck that buried the business model on slide 9. We restructured the narrative to lead with market urgency, moved the business model to slide 4, and rewrote the problem statement in investor language. Result: the deck was used in 6 investor meetings within 30 days of delivery.
- Status: Ready to Show

**Entry 2**
- Project Title: Board Presentation — B2B SaaS Scale-up (Berlin)
- Type: Fictional
- Client: Fictional B2B SaaS company, 45 employees, post-Series A
- Industry: SaaS
- Deliverable Type: Board Presentation
- Showcase Text: Fictional case demonstrating APEX's approach to board-level communication. Shows how we structure performance data into a narrative arc — not a data dump — with clear decisions the board needs to make. Built as a portfolio anchor for scale-up positioning.
- Status: Ready to Show

### Weekly Use
Navid reviews this database whenever a proposal is going out. He selects 2–3 relevant examples (matching the prospect's industry or deliverable type) and links to the Gallery view or attaches screenshots. He adds new work here immediately after delivery — while it's fresh — and marks it NDA Required if it's real client work. He builds at least one new fictional example per month to fill industry gaps in the portfolio.

---

## DATABASE 8 — TEMPLATES
**Icon:** 📋

**Purpose:** Store every reusable document — proposals, invoices, outreach messages, call scripts — in one organized library.

### Properties

| Property Name | Type | Options / Notes |
|---|---|---|
| Template Name | Title | Descriptive name |
| Type | Select | Onboarding / Proposal / Invoice / Outreach / Call Script / Questionnaire / Other |
| File Link | URL | Google Docs, Notion page, or file link |
| Last Updated | Date | |
| Notes | Text | When to use, any version notes |

### Views to Create

**View 1: By Type** (Table view, grouped by Type)
- Shows all templates organized by category
- Default view for finding what you need

**View 2: Recently Updated** (Table view)
- Sort: Last Updated descending
- Use to find the most current version of any template

### Example Entries

**Entry 1**
- Template Name: COMMAND Proposal v3
- Type: Proposal
- File Link: [Notion page link]
- Last Updated: 2026-05-01
- Notes: Standard proposal for the COMMAND package. Includes scope, timeline, deliverables, payment terms, and confidentiality notice. Customize: client name, project context, and deadline before sending. Always attach a relevant portfolio example.

**Entry 2**
- Template Name: Cold LinkedIn DM — Founder (Fundraising Context)
- Type: Outreach
- File Link: [Notion page link]
- Last Updated: 2026-04-20
- Notes: Short DM for founders who've posted about fundraising in the last 7 days. Keep under 80 words. Personalize line 1. Do not include pricing in first message. Version A/B tested — Version B has 22% higher reply rate.

### Weekly Use
Navid opens this database whenever he's starting a new outreach sequence, writing a proposal, or preparing for a client call. Templates are never sent as-is — always personalized. When Navid notices a template underperforming (low reply rate, clients asking the same clarifying questions), he revises the template and updates the Last Updated date. This database is also where all AI prompts live before they graduate to the AI Prompt Library.

---

## DATABASE 9 — INVOICES
**Icon:** 🧾

**Purpose:** Track all financial transactions — what's been invoiced, what's been paid, and what's overdue.

### Properties

| Property Name | Type | Options / Notes |
|---|---|---|
| Invoice Number | Title | Format: APEX-2026-001 |
| Client | Relation | → Clients database |
| Amount (CHF) | Number | Format: CHF |
| Status | Select | Draft / Sent / Paid / Overdue |
| Issue Date | Date | |
| Due Date | Date | |
| Payment Date | Date | Leave blank until paid |
| Notes | Text | Project reference, payment method, partial payment notes |
| Project | Relation | → Projects database |

### Status Options
- **Draft** — Not yet sent to client
- **Sent** — Delivered to client, awaiting payment
- **Paid** — Payment confirmed, date logged
- **Overdue** — Past due date, no payment received

### Views to Create

**View 1: All Invoices Table** (Table view)
- Sort: Issue Date descending
- Show all properties
- Full financial history

**View 2: Unpaid Invoices** (Table view)
- Filter: Status = Sent OR Overdue
- Show: Invoice Number, Client, Amount, Issue Date, Due Date, Status
- This is the weekly cashflow check

### Example Entries

**Entry 1**
- Invoice Number: APEX-2026-003
- Client: Alchemist Ventures AG
- Amount: 2,400 CHF (50% deposit of 4,800 CHF total)
- Status: Paid
- Issue Date: 2026-05-15
- Due Date: 2026-05-25
- Payment Date: 2026-05-17
- Notes: Deposit invoice for COMMAND package. Final invoice (APEX-2026-004) to be issued upon delivery.
- Project: Alchemist Ventures — Series A Pitch System

**Entry 2**
- Invoice Number: APEX-2026-002
- Client: NordLogic GmbH
- Amount: 2,400 CHF
- Status: Paid
- Issue Date: 2026-04-14
- Due Date: 2026-04-24
- Payment Date: 2026-04-22
- Notes: Final invoice for SIGNAL package — Q2 Board Presentation. Paid via bank transfer. Ref: INV-2026-002.
- Project: NordLogic — Q2 Board Presentation

### Weekly Use (Monday Ritual)
Navid opens the Unpaid Invoices view every Monday and checks: (1) Has any invoice crossed its due date? If yes, send a polite payment reminder same day. (2) Are any invoices still in Draft? Send them. He also checks that every delivered project has a corresponding final invoice sent. At month end, he totals Paid invoices for the month and logs it in a simple monthly revenue tracker (a separate Notion page or spreadsheet).

---

## DATABASE 10 — FEEDBACK / TESTIMONIALS
**Icon:** ⭐

**Purpose:** Collect and curate client feedback for use in proposals, the website, and LinkedIn content.

### Properties

| Property Name | Type | Options / Notes |
|---|---|---|
| Client Name | Title | First name + last initial, or company name |
| Date | Date | When feedback was received |
| Quote | Text | Verbatim quote — do not edit |
| Rating | Select | ⭐ / ⭐⭐ / ⭐⭐⭐ / ⭐⭐⭐⭐ / ⭐⭐⭐⭐⭐ |
| Type | Select | Email / LinkedIn / Verbal |
| Permission to Publish | Checkbox | Only publish if checked |
| Platform Used | Select | Website / LinkedIn Proposal / Pitch Deck / All |

### Views to Create

**View 1: Showcase Gallery** (Gallery view)
- Filter: Permission to Publish = Yes
- Show: Client Name, Quote, Rating
- Share this view link in proposals as a "what clients say" section

**View 2: All Feedback Table** (Table view)
- Show all, including unpermissioned feedback
- Useful for identifying patterns and improving service

### Example Entries

**Entry 1**
- Client Name: Lukas B. (Alchemist Ventures)
- Date: 2026-05-30
- Quote: "Navid completely transformed how we present our company. We went into investor meetings with a deck we were actually proud of. The narrative was sharper than anything we'd built ourselves."
- Rating: ⭐⭐⭐⭐⭐
- Type: LinkedIn
- Permission to Publish: ✓
- Platform Used: Website, LinkedIn, Proposal

**Entry 2**
- Client Name: Dr. Petra V. (NordLogic)
- Date: 2026-04-15
- Quote: "The board presentation was clear, well-structured, and received well. Navid understood the context quickly and delivered without needing excessive briefing. Would work with him again."
- Rating: ⭐⭐⭐⭐
- Type: Email
- Permission to Publish: ✓
- Platform Used: Proposal

### Weekly Use
After every project delivery, Navid sends a short feedback request — a 2-question email or a direct ask on LinkedIn. He logs every response here, even if it's not permission-granted. Over time, this database becomes a conversion asset. He updates the Platform Used field when he places a testimonial somewhere new. He reviews this database monthly to identify which testimonials are strongest and whether any existing clients should be asked for an updated quote.

---

## DATABASE 11 — AI PROMPT LIBRARY
**Icon:** 🤖

**Purpose:** Store, rate, and refine every AI prompt Navid uses — turning one-time experiments into repeatable intellectual infrastructure.

### Properties

| Property Name | Type | Options / Notes |
|---|---|---|
| Prompt Name | Title | Short descriptive name |
| Category | Select | Intake / Narrative / Research / Slides / QC / Outreach |
| Prompt Text | Text (Long) | Full prompt, copy-paste ready |
| Last Updated | Date | |
| Effectiveness | Select | ⭐ / ⭐⭐ / ⭐⭐⭐ / ⭐⭐⭐⭐ / ⭐⭐⭐⭐⭐ |
| Notes | Text | What it's best for, what to watch out for, iteration history |

### Category Definitions
- **Intake** — Prompts used to process client questionnaires and extract key positioning elements
- **Narrative** — Prompts for building story structure, investor narrative arcs, executive messaging
- **Research** — Prompts for competitive landscape, market sizing, investor persona research
- **Slides** — Prompts for slide-by-slide content generation and headline writing
- **QC** — Quality control prompts — reviewing drafts, checking clarity, stress-testing logic
- **Outreach** — Prompts for writing and personalizing outreach messages

### Views to Create

**View 1: By Category** (Table view, grouped by Category)
- Show: Prompt Name, Effectiveness, Notes
- Default view — find the right prompt for the task at hand

**View 2: Top-Rated Gallery** (Gallery view)
- Filter: Effectiveness = ⭐⭐⭐⭐ or ⭐⭐⭐⭐⭐
- Show: Prompt Name, Category, Notes
- The "greatest hits" — go here first

### Example Entries

**Entry 1**
- Prompt Name: Investor Narrative Spine Builder
- Category: Narrative
- Prompt Text: "You are a senior partner at a top-tier VC firm reviewing a pitch. Based on the following company information [paste intake data], identify: (1) The single most compelling reason this company exists right now. (2) The moment in the market that makes this opportunity time-sensitive. (3) The one risk an investor will identify in the first 3 minutes. Then write an opening narrative arc for a pitch deck — 3 short paragraphs — that leads with urgency, establishes credibility, and pre-empts the primary objection. Do not use startup clichés. Write in clear, precise English."
- Last Updated: 2026-05-01
- Effectiveness: ⭐⭐⭐⭐⭐
- Notes: Best prompt in the library. Use after completing the intake questionnaire. Often produces the narrative spine with minimal editing needed. Watch: sometimes too VC-US in tone — adjust for German/Swiss audiences by asking for a "more measured, data-grounded tone."

**Entry 2**
- Prompt Name: Cold Outreach Personalizer
- Category: Outreach
- Prompt Text: "Write a LinkedIn DM under 75 words for [NAME] who is the [ROLE] at [COMPANY]. They recently [RECENT ACTIVITY — e.g., posted about fundraising / announced a round / spoke at an event]. I am Navid from APEX, a Zürich-based pitch architecture studio. The message should: reference their specific context, not use generic flattery, make one clear value statement, and end with a low-friction question. Do not mention pricing. Sound like a human, not a template."
- Last Updated: 2026-04-28
- Effectiveness: ⭐⭐⭐⭐
- Notes: Strong performer. Works best when the recent activity is specific (an actual post or event). Generic context = generic output. Always edit the first line manually before sending.

### Weekly Use (Monday Ritual)
When starting a new project, Navid opens By Category view and pulls the relevant prompts for that project phase. After any new prompt experiment, he adds it here immediately — good or bad — with notes on what happened. He rates prompts after 3+ uses to ensure the rating reflects real-world performance. Once a month, he archives prompts with ⭐ or ⭐⭐ effectiveness by moving them to a sub-page called "Archive" to keep the library clean.

---

## WEEKLY REVIEW RITUAL — THE 15-MINUTE MONDAY PROTOCOL

> Run this every Monday morning before you start any client work. It keeps the entire business system current.

**Step 1 — Leads Pipeline (3 min)**
Open the Leads Pipeline Board. Move any leads that changed status over the weekend. Identify follow-ups needed (use the "Follow-up Needed" view). Add new leads from LinkedIn/email activity.

**Step 2 — Active Projects (3 min)**
Open the Projects Active Board. Confirm each project has a clear next action. Check the Deadline Calendar — any collisions or tight turnarounds this week?

**Step 3 — Outreach Queue (2 min)**
Open the "No Response + Older Than 5 Days" Outreach Tracker view. Send follow-ups to everyone on that list before 10am.

**Step 4 — Unpaid Invoices (2 min)**
Open the Unpaid Invoices view. Send reminders for anything overdue. Check if any delivered projects are missing their final invoice.

**Step 5 — Content Pipeline (2 min)**
Open the Content Calendar Production Board. Confirm 3 posts are scheduled for the week. If not, move one Idea to Drafting and write it this morning.

**Step 6 — Quick Wins (3 min)**
Any testimonial to request from a recent delivery? Any portfolio example to add? Any prompt to log from last week's project work?

**Total: 15 minutes. Then close Notion and start the work.**

---

## THE 5 HOME DASHBOARD WIDGETS

Build these on your APEX OS Home page using Notion's linked database views and callout blocks.

**Widget 1 — Active Pipeline**
Linked database: Leads (Pipeline Board view, filtered to Active)
Shows all leads from Contacted → Proposal Sent at a glance.

**Widget 2 — This Week's Projects**
Linked database: Projects (filtered to Status ≠ Delivered, grouped by Status)
The operational heartbeat — what's being worked on right now.

**Widget 3 — Content This Week**
Linked database: Content Calendar (filtered to Publish Date = this week, Status = Scheduled or Published)
Confirms the posting schedule is in order.

**Widget 4 — Unpaid Invoices**
Linked database: Invoices (filtered to Status = Sent or Overdue)
Cash flow at a glance. Should usually be empty or close to it.

**Widget 5 — Quick Stats Callout Block**
A manually updated callout block (refresh monthly):
- Total clients served: [X]
- Revenue this month: CHF [X]
- Active projects: [X]
- LinkedIn followers: [X]

---

## DAILY TASK FORMAT

Use a simple recurring Notion page titled **"Daily — [DATE]"** inside a "Daily Notes" section. Keep it minimal.

```
## TODAY — [DATE]

### Must Do (max 3)
- [ ] 
- [ ] 
- [ ] 

### Client Work
- [ ] [Project name] — [specific next action]
- [ ] [Project name] — [specific next action]

### Outreach
- [ ] Send [X] LinkedIn DMs
- [ ] Follow up with [NAME]

### Content
- [ ] Draft / schedule post: [title]

### Admin
- [ ] 

---
Notes:
```

Keep task lists to one page per day. Archive at end of day. Never carry more than 3 "must do" items — if everything is a priority, nothing is.
