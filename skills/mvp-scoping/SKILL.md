---
name: mvp-scoping
description: >
  Define the smallest product that tests the riskiest assumption: the one job it
  must do, the type of MVP, a story map with a clear cut line, features sorted with
  the Kano model, what to fake or do by hand, a success criterion and a build plan
  in weeks. Use when a founder is about to build a first version, has a long
  feature list, or asks what an MVP should include. Triggers: "MVP", "minimum
  viable product", "first version", "feature list", "prioritize features",
  "produit minimum viable", "première version", "prioriser les fonctionnalités",
  "producto mínimo viable", "primera versión", "priorizar funcionalidades".
---

# MVP scoping

An MVP exists to learn, as cheaply as possible, whether customers want something. This skill cuts a feature list down to what the riskiest assumption requires, and finds what can be faked or done by hand.

## When to use

- After the problem is validated (`customer-interviews`, `idea-validation`) and before building.
- When the feature list keeps growing and the launch keeps moving.
- Not for technical architecture or choosing a tech stack.

## Inputs

1. The riskiest assumption to test.
2. The target customer and the job the product does for them.
3. The feature wish list.
4. The team's skills, budget and weekly hours.

## Method

1. **Write the one job** the MVP does for one type of customer, in one sentence.
2. **Choose the type of MVP** that tests the assumption at the lowest cost: concierge (the service is done by hand for a few customers), Wizard of Oz (customers see a product, people do the work behind it), single-feature product, no-code or spreadsheet version, landing page with pre-orders (`landing-page`), clickable prototype (`prototype-testing`).
3. **Draw a story map** (Patton): the steps of the user's journey from left to right, the features under each step, and a cut line. Above the line goes only what the user needs to complete the journey once.
4. **Sort the features with the Kano model**: must-be (expected; their absence makes users unhappy), one-dimensional (the more, the better), attractive (delight that nobody expected), indifferent. The MVP keeps the must-be features of the core job and at most one attractive feature that carries the promise.
5. **Fake or do by hand** what the test does not need: payment by bank transfer, onboarding by phone, admin in a spreadsheet. Stay honest with users: if people do the work behind the scenes, never claim the opposite (for example, a "fully automatic" service).
6. **Define success before launch**: the behavior that proves the assumption (activation, repeat use, payment), its target and its deadline.
7. **Plan the build in weeks** with the team's real capacity. A first test that needs more than four to eight weeks is a warning sign (a rule of thumb, not a law).

## Output

```markdown
### MVP: <one job> for <customer>
Assumption tested: … | Type of MVP: … | Success if … by <date>

### Story map
| Step 1 | Step 2 | Step 3 |
|---|---|---|
| feature (must-be) | … | … |
| --- cut line: everything below waits --- | | |
| later | … | … |

### Fake it or do it by hand
…

### Build plan
| Week | Deliverable | Who |
|---|---|---|
```

## Quality bar

- The MVP tests one named assumption with one measurable success criterion.
- Every feature above the line is justified by the core job; features cut are listed, not forgotten.
- Manual and fake parts are explicit, and users are never misled about them.
- The build time fits the team's real capacity.
- Written in the user's language, with the terms below.

## Terminology

| English | Français | Español |
|---|---|---|
| Minimum viable product (MVP) | Produit minimum viable (MVP) | Producto mínimo viable (PMV) |
| Concierge MVP | MVP concierge | MVP concierge |
| Wizard of Oz MVP | MVP « magicien d'Oz » | MVP «mago de Oz» |
| User story map | Story map, carte des parcours utilisateur | Mapa de historias de usuario |
| Must-be, attractive quality (Kano) | Qualité obligatoire, attractive (Kano) | Calidad obligatoria, atractiva (Kano) |
| Feature | Fonctionnalité | Funcionalidad |

## Sources

- Ries, E. (2011). *The Lean Startup*. Crown Business.
- Patton, J. (2014). *User Story Mapping: Discover the Whole Story, Build the Right Product*. O'Reilly.
- Kano, N., Seraku, N., Takahashi, F., & Tsuji, S. (1984). Attractive quality and must-be quality. *Journal of the Japanese Society for Quality Control*, 14(2), 147–156.
