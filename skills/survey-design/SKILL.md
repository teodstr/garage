---
name: survey-design
description: >
  Design a survey that measures something useful without biasing the answers: one
  decision to inform, the right sample, neutral questions, balanced scales, a
  pilot, and an honest analysis with margins of error. Use for market research
  questionnaires, customer satisfaction, pricing or feature preference surveys.
  Triggers: "survey", "questionnaire", "poll", "Likert", "sondage", "questionnaire
  en ligne", "étude quantitative", "enquête", "encuesta", "cuestionario", "estudio
  cuantitativo".
---

# Survey design

A survey can only measure what interviews have already uncovered, and a badly written one measures the questionnaire instead of the market. This skill builds short, neutral surveys and reads the results with the right caution.

## When to use

- After `customer-interviews`, to measure how common a problem, a habit or a preference is.
- To compare segments or track satisfaction over time.
- Not to discover new problems, and not to forecast sales: "would you buy it?" answers overstate real demand.

## Inputs

1. The decision the survey informs.
2. The target population and how to reach it.
3. Constraints: budget, deadline, survey tool.

## Method

1. **One decision, a few numbers**: write the decision and the three to five numbers needed to make it. Every question feeds one of them; cut the rest.
2. **Define the population and the sample**: who exactly, how they will be reached, and the bias of that channel (a post on the founder's social network reaches the founder's network, not the market).
3. **Compute the margin of error** for a proportion, and say that it only holds for a random sample: margin = 1.96 × √(p × (1 − p) / n). With p = 0.5, it is about ±9.8 points for 100 answers and ±4.9 points for 400.
4. **Write neutral questions**: one idea per question, no loaded words, no jargon, a "don't know" or "not applicable" option when it fits, balanced scales (as many positive as negative points), a precise time frame ("in the last 30 days").
5. **Order the questionnaire**: screening questions first, easy factual questions next, sensitive ones (income, age) last. Keep it under ten minutes and shuffle answer options when their order could matter.
6. **Ask about behavior when possible**: "What did you use last time?" beats "What would you use?". Treat purchase intent as an upper limit, never as a forecast.
7. **Pilot it** with five people from the target who think aloud while answering, then fix what confused them.
8. **Analyze honestly**: report the number of answers, the response rate, the sample's bias and the margins of error; compare segments only when each has enough answers; show the exact wording next to each result.

## Output

```markdown
### Survey plan
Decision: … | Numbers needed: … | Population: … | Channel and its bias: …
Planned sample: n = … (margin of error ±… points, random sample only)

### Questionnaire
| # | Question (exact wording) | Type and scale | Feeds which number |
|---|---|---|---|

### Results
| Number | Result | n | Margin of error | Caveat |
|---|---|---|---|---|
```

## Quality bar

- Every question maps to the decision; none is leading, double or hypothetical without a warning.
- Margins of error are computed, not guessed, and the sampling bias is stated.
- Purchase-intent answers are never presented as a sales forecast.
- The survey says how answers will be used, and personal data is kept to a minimum (GDPR in the European Union).
- Written in the user's language, with the terms below.

## Terminology

| English | Français | Español |
|---|---|---|
| Survey, questionnaire | Questionnaire, enquête | Encuesta, cuestionario |
| Sample | Échantillon | Muestra |
| Margin of error | Marge d'erreur | Margen de error |
| Response rate | Taux de réponse | Tasa de respuesta |
| Leading question | Question orientée | Pregunta sesgada |
| Likert scale | Échelle de Likert | Escala de Likert |

## Sources

- Dillman, D. A., Smyth, J. D., & Christian, L. M. (2014). *Internet, Phone, Mail, and Mixed-Mode Surveys: The Tailored Design Method* (4th ed.). Wiley.
- Saunders, M., Lewis, P., & Thornhill, A. (2019). *Research Methods for Business Students* (8th ed.). Pearson.
