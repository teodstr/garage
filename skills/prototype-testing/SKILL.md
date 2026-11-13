---
name: prototype-testing
description: >
  Build a clickable prototype of a product as a single HTML file and test it with
  five users: realistic tasks, a think-aloud session script, a findings grid with
  counts and severity, and the changes to make before building for real. Use to
  test a product idea, an app flow or a website before coding it. Triggers:
  "prototype", "clickable prototype", "usability test", "user testing", "mockup",
  "wireframe", "prototype cliquable", "test utilisateur", "maquette", "test
  d'utilisabilité", "prototipo", "prueba de usabilidad", "test con usuarios",
  "maqueta".
---

# Prototype testing

Watching a handful of people use a prototype reveals problems that would otherwise appear after launch, when they cost much more to fix. Nielsen's research suggests that about five users per round uncover most usability problems, so small rounds repeated often beat one large study. This skill builds the prototype, which an agent can do in minutes, and runs a light usability test with it.

## When to use

- Before building the interface of an MVP (`mvp-scoping`), or to compare two flows.
- After a `landing-page` has shown interest, to check that people can use what they asked for.
- Not to measure demand or prices: a usability test shows whether people can use something, not whether they will pay for it.

## Inputs

1. The core job and the two or three tasks a user must complete.
2. The target users and how to recruit five of them.
3. Brand elements if they exist.

## Method

1. **Choose the tasks** that matter for the core job (sign up, find something, complete a purchase) and write them as scenarios that do not give away the answer: "You want to… Show me how you would do it."
2. **Build the prototype as one HTML file**: realistic content instead of placeholder text, clickable links between the screens, the paths of the tasks working, and the rest clearly marked "not part of this test". Keep the polish light, so that people feel free to criticize it.
3. **Recruit five users** from the target, not colleagues. Plan a second round of five new users after the fixes.
4. **Run each session** (about 30 minutes, in person or by video): ask for consent, explain that the prototype is being tested, not them, and ask them to think aloud. Do not help or explain. Note where they hesitate, make mistakes or give up, and what they say.
5. **Log the findings** in a grid: task, what happened, how many of the five users hit the problem, severity (blocks the task, slows it down, cosmetic) and the likely cause.
6. **Fix and test again**: change the prototype for the severe problems and run the next round.
7. **Report**: the main problems with evidence (quotes and counts), the decisions taken, and what is still unknown.

## Output

```markdown
### Test plan
Tasks: 1. … 2. … 3. … | Users: five people matching <profile> | Success: task completed without help

### Findings
| Task | What happened | Users (out of 5) | Severity | Fix |
|---|---|---|---|---|

### Prototype
<one HTML file, screens linked, realistic content>
```

## Quality bar

- Tasks are scenarios that do not reveal the answer.
- Findings give counts out of five and real quotes; no conclusion about demand or price comes from a usability test.
- The prototype uses realistic content and is accessible enough for the people tested.
- Participants gave their consent, and recordings are kept only as long as needed.
- Written in the user's language, with the terms below.

## Terminology

| English | Français | Español |
|---|---|---|
| Prototype | Prototype, maquette | Prototipo, maqueta |
| Usability test | Test d'utilisabilité | Prueba de usabilidad |
| Think-aloud | Pensée à voix haute | Pensamiento en voz alta |
| Wireframe | Wireframe, maquette fil de fer | Wireframe, esquema de pantalla |
| Task success rate | Taux de réussite des tâches | Tasa de éxito de las tareas |
| Severity | Gravité | Gravedad |

## Sources

- Nielsen, J. (2000). *Why you only need to test with 5 users*. Nielsen Norman Group. https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/
- Krug, S. (2010). *Rocket Surgery Made Easy*. New Riders.
