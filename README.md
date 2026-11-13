<div align="center">

# garage

**Startup skills for your AI agent, from the first idea to the first customers.**

Idea validation · Customer interviews · Desk research · MVP · Brand identity · Landing page · Prototype tests · Pitch deck · Funding · Legal setup · First customers · Forecast

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-16-black.svg)](#the-skills)
[![Languages](https://img.shields.io/badge/languages-EN%20%7C%20FR%20%7C%20ES-green.svg)](#works-in-english-french-and-spanish)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**English** · [Français](README.fr.md) · [Español](README.es.md)

</div>

---

Tell an AI agent about your startup idea and it will usually find it great, then help you build it right away. Ask it about grants or legal structures and it may quote rules that changed last year.

**garage** makes your agent work like a demanding mentor: test the riskiest assumption before building, look for behavior instead of compliments, check grants, laws and prices on official pages with the date, and produce things you can use today: an interview guide, a landing page, a clickable prototype, a forecast.

## Install

**Most coding agents** (Claude Code, Codex, Cursor, Windsurf, Cline and more):

```bash
npx skills add teodstr/garage -g
```

**Claude Code**, as a plugin:

```
/plugin marketplace add teodstr/garage
/plugin install garage@garage
```

**Manually:** copy the folders in [`skills/`](skills) into your agent's skills directory.

## Use it

Just ask. The right skill loads on its own.

```
I have an idea for a meal-prep service for students. Where do I start?
Prépare-moi un guide d'entretien pour tester mon idée de friperie en ligne.
¿Qué ayudas existen para crear una startup en Madrid?
Build me a landing page to test demand for a bike repair subscription.
Quel statut juridique choisir pour facturer mes premières missions de graphiste ?
```

## The skills

| Skill | What it does |
|---|---|
| **Start** | |
| [`startup-roadmap`](skills/startup-roadmap/SKILL.md) | Finds the stage of your project, its riskiest assumption, and a 30-day plan |
| **Research** | |
| [`idea-validation`](skills/idea-validation/SKILL.md) | Turns an idea into assumptions and cheap experiments with criteria set in advance |
| [`customer-interviews`](skills/customer-interviews/SKILL.md) | Interview guides and debriefs that get facts instead of compliments (The Mom Test) |
| [`survey-design`](skills/survey-design/SKILL.md) | Neutral questionnaires, the right sample and honest margins of error |
| [`desk-research`](skills/desk-research/SKILL.md) | Sourced market research: official statistics, company filings, graded sources |
| [`competitor-teardown`](skills/competitor-teardown/SKILL.md) | Every alternative, the strongest ones taken apart, and the gaps you can use |
| **Design** | |
| [`mvp-scoping`](skills/mvp-scoping/SKILL.md) | The smallest product that tests your riskiest assumption |
| [`brand-identity`](skills/brand-identity/SKILL.md) | Brand core, name shortlist with the checks to run, colors, typefaces, SVG logo sketches |
| [`landing-page`](skills/landing-page/SKILL.md) | The copy and a ready-to-use HTML page to test demand |
| [`prototype-testing`](skills/prototype-testing/SKILL.md) | A clickable HTML prototype and a usability test with five people |
| [`pitch-deck`](skills/pitch-deck/SKILL.md) | A ten-slide story, or a review of your deck the way an investor would read it |
| **Resources** | |
| [`funding-options`](skills/funding-options/SKILL.md) | Grants, honor loans, bank loans, angels and funds that fit your stage and country |
| [`support-programs`](skills/support-programs/SKILL.md) | Incubators, accelerators, networks, student-entrepreneur status, mentors |
| [`legal-setup`](skills/legal-setup/SKILL.md) | Legal structures compared and the first steps, from official sources |
| **Launch** | |
| [`first-customers`](skills/first-customers/SKILL.md) | Channels to test, outreach that respects the law, and a weekly funnel |
| [`financial-forecast`](skills/financial-forecast/SKILL.md) | A monthly forecast with runway, break-even and three scenarios |

## What every skill enforces

- **Evidence before building.** Test the riskiest assumption first, with a success criterion set before the test.
- **Behavior over opinions.** A sign-up, a pre-order or a past habit counts more than "I would buy it".
- **Official sources, with a date.** Grants, laws, prices and thresholds are checked on official pages during the conversation, never quoted from memory.
- **Something you can use today.** Each skill delivers a guide, a table, a page, a prototype or a plan.
- **Honest by design.** No invented testimonials, traction or scarcity, and prospecting that respects the law.

## Works with boardroom

garage helps you build a company; [boardroom](https://github.com/teodstr/boardroom) helps you analyze one (SWOT, Porter, BCG, market sizing, unit economics…). Install both: garage skills point to boardroom skills when they help.

## Works in English, French and Spanish

Ask in any of the three languages and the agent answers with the words founders and support networks actually use: *prêt d'honneur*, *statut d'étudiant-entrepreneur*, *autónomo*, *empresa emergente*… France and Spain are covered in detail for funding, support and legal setup, and adding your country is one of the easiest ways to contribute.

## Not legal or financial advice

garage helps you prepare decisions and ask better questions. For legal, tax and financial choices, check with an accountant, a lawyer or a support network.

## Contributing

garage is built so that anyone can contribute, even without ever writing code: a skill is a single Markdown file.

- **Add your country** to `funding-options`, `support-programs` or `legal-setup`, with official sources only.
- **Add a skill** from the [roadmap](ROADMAP.md): pricing experiments, cofounder agreement, first hire, crowdfunding campaign…
- **Add a language** to the terminology tables, or translate this README.
- **Report a weak output:** open an issue with your prompt and what the agent produced.

Start with [CONTRIBUTING.md](CONTRIBUTING.md). Every pull request is checked automatically.

## License

[MIT](LICENSE). Maintained by [teodstr](https://github.com/teodstr). Built with the help of Claude.
