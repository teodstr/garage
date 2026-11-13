---
name: pitch-deck
description: >
  Build or review a startup pitch deck: a story in about ten slides (purpose,
  problem, solution, why now, market, competition, product, business model, team,
  financials and the ask), one idea per slide, simple design rules, and a review
  that flags weak or unsupported claims the way an investor or a jury would. Use
  for fundraising decks, incubator or competition applications and demo days.
  Triggers: "pitch deck", "investor deck", "pitch", "demo day", "fundraising
  presentation", "présentation investisseurs", "pitcher mon projet", "deck de
  levée de fonds", "concours de startups", "presentación para inversores", "pitch
  para inversores", "ronda de financiación".
---

# Pitch deck

A deck is often read in a few minutes, without the founder in the room. This skill builds a clear story, puts one idea on each slide, and checks every claim the way a skeptical investor would.

## When to use

- Fundraising, incubator or accelerator applications, startup competitions, demo days.
- To review an existing deck before sending it.
- Not for a detailed business plan: the deck summarizes it.

## Inputs

1. The audience (business angel, venture fund, jury, bank) and the ask: how much, for what.
2. The facts: evidence of the problem, product, traction, market figures with sources, team, financials.
3. The existing deck, for a review.

## Method

1. **Start from the audience and the ask**: the amount, the milestones it pays for, and over how long. An incubator jury looks for different things than a venture fund.
2. **Tell the story in about ten slides**, adapting the outline Sequoia Capital publishes for business plans: company purpose in one sentence, problem, solution, why now, market potential, competition and alternatives, product, business model, team, financials and the ask. Move traction to the front when it is the strongest argument.
3. **One idea per slide**: a headline that states the slide's conclusion as a full sentence, one number or one visual that proves it, and little text. Kawasaki's 10/20/30 rule is a useful check: about ten slides, twenty minutes, no text smaller than thirty points.
4. **Back every claim**: market figures with sources (`desk-research`, and `market-sizing` from `boardroom` if installed), traction with dates and definitions, competition from `competitor-teardown`, financials from `financial-forecast`.
5. **Design for reading**: one consistent layout, the brand's colors and typefaces (`brand-identity`), charts with labeled axes, strong contrast, nothing decorative that competes with the message.
6. **Review mode**: go slide by slide and flag unsupported claims, vanity metrics, "no competitors", markets sized as "1% of a huge market", numbers that differ between slides, and missing slides (team, ask). Then list the five questions an investor would ask first.
7. **Prepare the follow-up**: an appendix (detailed financials, customer data, product screens) and a short email to send with the deck.

## Output

```markdown
### Storyline
| # | Slide | Headline (its conclusion) | Proof (number, visual, source) |
|---|---|---|---|

### Review
| Slide | Problem | Why it matters to an investor | Fix |
|---|---|---|---|

### First five investor questions
1. …
```

## Quality bar

- Every slide has a headline that states its conclusion, and one proof.
- Every number has a source or is labeled as an assumption; traction metrics are defined (period, what counts as an active user).
- The ask is precise: amount, use of the money, milestones.
- No invented traction, partners, logos or testimonials.
- Written in the user's language, with the terms below.

## Terminology

| English | Français | Español |
|---|---|---|
| Pitch deck | Pitch deck, présentation investisseurs | Pitch deck, presentación para inversores |
| Traction | Traction | Tracción |
| Fundraising | Levée de fonds | Ronda de financiación |
| Use of funds | Utilisation des fonds | Uso de los fondos |
| Business angel | Business angel, investisseur providentiel | Business angel, inversor ángel |
| Demo day | Demo day | Demo day |

## Sources

- Sequoia Capital. (n.d.). *Writing a business plan*. https://www.sequoiacap.com/article/writing-a-business-plan/
- Kawasaki, G. (2004). *The Art of the Start*. Portfolio.
- Kawasaki, G. (2005, December 30). *The 10/20/30 rule of PowerPoint*. https://guykawasaki.com/the_102030_rule/
