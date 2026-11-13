---
name: financial-forecast
description: >
  Build a startup financial forecast from explicit assumptions: revenue drivers,
  costs, hiring, a monthly profit and cash plan for the first year, burn rate,
  runway, break-even and three scenarios, in a table that pastes into a
  spreadsheet. Use for business plans, loan or grant applications, pitch decks, or
  to know how long the money will last. Triggers: "financial forecast", "financial
  model", "runway", "burn rate", "cash flow", "business plan financials",
  "prévisionnel financier", "plan de trésorerie", "budget prévisionnel", "seuil de
  rentabilité", "plan financiero", "previsión de tesorería", "proyecciones
  financieras".
---

# Financial forecast

A forecast is a model of the business: its value lies in the assumptions it makes visible. This skill builds it from drivers the founder can defend, month by month for the first year, and shows how long the cash will last.

## When to use

- For a business plan, a loan, grant or incubator application, or the financial slide of a `pitch-deck`.
- To plan cash every month and decide when to raise money (`funding-options`).
- Not to value a company. For the economics of one customer, use `unit-economics` from `boardroom` if it is installed.

## Inputs

1. The business model and the prices.
2. Sales assumptions (volumes, conversion, cancellations) and their evidence.
3. Costs: fixed (rent, tools, salaries), variable (per unit sold), one-off investments.
4. Planned funding (shares, loans, grants) and its dates.
5. The country: employer contributions and VAT are checked on official sources.

## Method

1. **List the drivers, not the totals**: revenue = customers × price × purchase frequency; new customers = leads × conversion rate; costs split into fixed, variable per unit and one-off. Each driver has a source or is labeled as an assumption, with its reason.
2. **Build the first twelve months month by month**, then years two and three by year: revenue, variable costs, gross margin, fixed costs (salaries with employer contributions taken from official simulators), and the result before tax.
3. **Build the cash plan separately**: when customers really pay, when suppliers are paid, VAT timing, loan repayments, money raised. Startups run out of cash before they run out of profit, so this plan matters most.
4. **Compute the key numbers and show the formulas**:
   - net burn = cash out − cash in, per month;
   - runway (months) = cash available ÷ net burn;
   - break-even volume = fixed costs ÷ contribution margin per unit;
   - funding need = the lowest cash balance of the plan, plus a safety buffer chosen with the founder.
5. **Run three scenarios** (low, base, high) by changing the two or three drivers that matter most, and show the runway in each one.
6. **Sanity-check**: growth against comparable companies or the founder's own data, salaries against market sources, conversion rates against cited benchmarks. Flag the assumptions that carry the whole forecast.
7. **Deliver it ready to use**: a table in CSV or Markdown that pastes into a spreadsheet, the formulas explained, and the list of assumptions to compare with real figures every month.

## Output

```markdown
### Assumptions
| Driver | Value | Source or reason |
|---|---|---|

### Year 1, month by month
| Month | Customers | Revenue | Variable costs | Fixed costs | Result | Cash in | Cash out | Cash balance |
|---|---|---|---|---|---|---|---|---|

### Key numbers
Net burn: … per month | Runway: … months | Break-even: month … | Funding need: …

### Scenarios
| | Low | Base | High |
|---|---|---|---|
| Runway | | | |
```

## Quality bar

- Every figure comes from a driver with a source or a labeled assumption; no growth curve without an explanation.
- Profit and cash are shown separately, with VAT and payment delays where they apply.
- Tax and contribution rates come from official sources or simulators, with the date; none from memory.
- Formulas are shown, and the table pastes into a spreadsheet.
- The forecast is presented as an estimate, with the list of figures to monitor every month.
- Written in the user's language, with the terms below.

## Terminology

| English | Français | Español |
|---|---|---|
| Financial forecast | Prévisionnel financier | Previsión financiera, plan financiero |
| Cash flow plan | Plan de trésorerie | Previsión de tesorería |
| Burn rate | Consommation de trésorerie (burn rate) | Consumo de caja (burn rate) |
| Runway | Autonomie financière | Autonomía financiera |
| Break-even point | Seuil de rentabilité, point mort | Punto de equilibrio |
| Gross margin | Marge brute | Margen bruto |

## Sources

- Rogers, S., & Makonnen, R. (2014). *Entrepreneurial Finance: Finance and Business Strategies for the Serious Entrepreneur* (3rd ed.). McGraw-Hill Education.
- URSSAF simulators (France): https://www.urssaf.fr
