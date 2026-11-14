---
name: funding-options
description: >
  Map the funding options that fit a project's stage, country and founder profile
  (savings and friends and family, grants and public aid, honor loans, bank loans,
  crowdfunding, business angels, venture capital), check their current conditions
  on official pages, and plan the applications. Use this skill whenever someone
  asks which grants, aid, subsidies, loans or investors exist to start or grow a
  business in a country, region or city (for example "what aid is there for
  startups in Madrid?"), even when the question looks simple: these programs
  change often, so the answer must come from official pages checked today, not
  from memory. Not financial advice. Triggers: "funding", "grants", "startup
  loan", "raise money", "investors", "financement", "quelles aides", "aides à la
  création", "subventions", "prêt d'honneur", "lever des fonds", "financiación",
  "qué ayudas hay", "ayudas para emprender", "ayudas para startups",
  "subvenciones", "préstamo participativo".
---

# Funding options

The right money depends on the stage of the project and on what the founder is ready to give in return: time, a share of the company, or a personal guarantee. This skill maps the options for the founder's country, checks their current conditions on official pages, and builds an application plan.

Amounts, rates, deadlines and eligibility rules change often. The agent looks them up on the official page during the conversation and gives the link and the date of the check. Without web access, it names the programs and the pages to check, and gives no figures.

## When to use

- When the founder needs money for a next milestone, or wonders whether to raise funds.
- Before choosing between a loan, a grant and selling shares.
- Not for structuring a fundraising round or a shareholder agreement: that needs a lawyer.

## Inputs

1. Stage, country and region, and whether the company already exists.
2. The founder's profile (student, employee, job seeker, age bracket when a program depends on it).
3. The amount needed, what it pays for, and the milestone it should reach.
4. Revenue, team, and the share of the company the founders are ready to sell.

## Method

1. **Start from the need**: the amount, its use, and the milestone it buys (for example, six months to reach paying customers). Selling shares early for a small amount is rarely a good deal.
2. **Map the families of funding** and what each one costs the founder: savings and friends and family; non-dilutive public support (grants, innovation aid, tax schemes); honor loans (personal loans at zero interest that often help obtain a bank loan); bank loans (sometimes with a public guarantee); crowdfunding (rewards, loans or shares); business angels; venture capital (only for projects that can grow very fast and very big).
3. **List the programs to check for the country:**
   - France: Bpifrance (bpifrance.fr, with guides on bpifrance-creation.fr), honor loans from Initiative France and Réseau Entreprendre, France Active, the start-up exemption on social contributions (ACRE, on urssaf.fr), the schemes for job seekers on francetravail.fr, regional aid, and the French Tech programs (lafrenchtech.gouv.fr).
   - Spain: ENISA participative loans (enisa.es), CDTI for technology projects (cdti.es), regional agencies, and the startup law (Ley 28/2022, on boe.es) with its tax measures.
   - European Union: the EIC Accelerator for deep tech (eic.ec.europa.eu).
   - Elsewhere: the national innovation agency, the chambers of commerce and the government's business portal. Contributions for more countries are welcome.
4. **Check each program on its official page**: who can apply, stage, amount range, conditions (own contribution, co-financing, company already registered or not), timing. Write down the date of the check.
5. **Sequence them**: what to apply for first (public support and honor loans often come before a bank loan, and help obtain it) and what comes later (angels, funds) once there is traction.
6. **Plan the applications**: documents (business plan, forecast from `financial-forecast`, deck from `pitch-deck`), deadlines, contacts and the next step for each.
7. **Explain the trade-offs** in plain words: dilution, personal guarantees, reporting duties, and what happens if the project fails.

## Output

```markdown
### Need
Amount: … | Use: … | Milestone: …

### Options that fit
| Option | Type | Why it fits | Conditions (checked on <date>) | Official link |
|---|---|---|---|---|

### Application plan
| Order | Program | Documents | Deadline | Next step |
|---|---|---|---|---|

### Trade-offs
…
```

## Quality bar

- No amount, rate, deadline or eligibility rule comes from memory: each one comes from an official page, with its link and the date of the check.
- The options match the stage and the profile; venture capital is not suggested to a project that does not need it.
- Trade-offs (dilution, guarantees, obligations) are explained in plain words.
- The answer says it is not financial or legal advice, and suggests an accountant or a support network for the final choice (`support-programs`).
- Written in the user's language, with the terms below.

## Terminology

| English | Français | Español |
|---|---|---|
| Grant, subsidy | Subvention | Subvención |
| Honor loan | Prêt d'honneur | Préstamo de honor |
| Participative loan | Prêt participatif | Préstamo participativo |
| Friends and family money | Love money | Dinero de amigos y familia |
| Dilution | Dilution | Dilución |
| Non-dilutive funding | Financement non dilutif | Financiación no dilutiva |

## Sources

- Feld, B., & Mendelson, J. (2019). *Venture Deals: Be Smarter Than Your Lawyer and Venture Capitalist* (4th ed.). Wiley.
- Official portals: Bpifrance Création (https://bpifrance-creation.fr), Initiative France (https://www.initiative-france.fr), Réseau Entreprendre (https://www.reseau-entreprendre.org), France Active (https://www.franceactive.org), ENISA (https://www.enisa.es), CDTI (https://www.cdti.es), European Innovation Council (https://eic.ec.europa.eu).
- Ley 28/2022, de 21 de diciembre, de fomento del ecosistema de las empresas emergentes. *Boletín Oficial del Estado*. https://www.boe.es/eli/es/l/2022/12/21/28
