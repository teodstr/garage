---
name: desk-research
description: >
  Run rigorous desk research on a market, an industry or a customer group: turn
  the topic into precise questions, search official statistics, filings, industry
  and academic sources, grade every source, cross-check the key numbers, and deliver
  a sourced brief with dates and confidence levels. Use for market research,
  industry overviews, finding data for a business plan, or checking a figure.
  Triggers: "market research", "desk research", "find data", "industry report",
  "statistics", "étude de marché", "recherche documentaire", "trouver des chiffres",
  "données de marché", "estudio de mercado", "investigación documental", "datos del
  sector".
---

# Desk research

The hard part of desk research is knowing how much to trust a number. This skill plans the search, goes to the sources closest to the data, grades each one, and shows the founder what is solid and what is still a guess.

## When to use

- Before interviews, to understand a market and its vocabulary.
- To fill a business plan, a grant application or a pitch deck with sourced figures.
- To check a figure someone quoted.
- Not to estimate a market size from scratch: use `market-sizing` from `boardroom` if it is installed, with the figures found here.

## Inputs

1. The questions to answer, and the decision behind them.
2. Geography, period and segment.
3. Sources the founder already has.

## Method

1. **Turn the topic into precise questions**, each with its unit, geography and year: "number of independent bakeries in France in 2024", not "the bakery market".
2. **Search in this order, closest to the data first:**
   - Official statistics: national institutes (INSEE in France, INE in Spain, their equivalents elsewhere), Eurostat, OECD, World Bank, central banks.
   - Filings and registries: annual reports, company accounts (in France, for example, Infogreffe or Pappers), stock market filings.
   - Trade associations, regulators and public agencies.
   - Academic research (for example Google Scholar) for behaviors and definitions.
   - Market research firms and the press: useful, but check how the figure was produced, and whether the article only repeats the summary of a paid report.
   - Signals: search trends, app store rankings, job postings, customer reviews, forums.
3. **Grade every source**: who produced it, with which method and sample, when, and whether the method is public. Give a confidence level: high (official or audited), medium (reputable, method partly public), low (unknown method, marketing material, unsourced summary, including summaries written by AI).
4. **Cross-check**: for each key figure, find a second independent source or a bottom-up sanity check. Explain the gaps between sources (different definitions, years or scopes).
5. **Cite precisely**: title, publisher, publication date, link and date accessed. Without web access, say which figures must be checked and where, instead of quoting from memory.
6. **Write the brief**: answers first, then the evidence, then what is still unknown and how to find it (often with `customer-interviews` or `survey-design`).

## Output

```markdown
### Research brief: <topic> (<geography>, <period>)
| Question | Answer | Source (publisher, date, link) | Accessed | Confidence |
|---|---|---|---|---|

### Cross-checks and gaps
…

### Still unknown, and how to find out
…
```

## Quality bar

- Every number has a source, a date and a confidence level; nothing is quoted from memory.
- Primary and official sources come first; a press article that quotes a study is traced back to the study.
- Definitions and years match when figures are compared.
- Unknowns are listed, not filled with guesses.
- Written in the user's language, with the terms below.

## Terminology

| English | Français | Español |
|---|---|---|
| Desk research | Recherche documentaire | Investigación documental |
| Market research | Étude de marché | Estudio de mercado |
| Primary, secondary source | Source primaire, secondaire | Fuente primaria, secundaria |
| Official statistics | Statistique publique | Estadística oficial |
| Cross-check | Recoupement | Contraste de fuentes |
| Confidence level | Niveau de fiabilité | Nivel de fiabilidad |

## Sources

- Saunders, M., Lewis, P., & Thornhill, A. (2019). *Research Methods for Business Students* (8th ed.). Pearson.
- INSEE (https://www.insee.fr), INE (https://www.ine.es) and Eurostat (https://ec.europa.eu/eurostat): official statistics portals.
