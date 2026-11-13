<div align="center">

# garage

**Des skills pour votre agent IA, de la première idée aux premiers clients.**

Valider une idée · Entretiens clients · Recherche documentaire · MVP · Identité de marque · Landing page · Tests de prototype · Pitch deck · Financements · Statut juridique · Premiers clients · Prévisionnel

[![Licence : MIT](https://img.shields.io/badge/licence-MIT-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-16-black.svg)](#les-skills)
[![Langues](https://img.shields.io/badge/langues-EN%20%7C%20FR%20%7C%20ES-green.svg)](#fonctionne-en-anglais-en-français-et-en-espagnol)
[![PR bienvenues](https://img.shields.io/badge/PR-bienvenues-brightgreen.svg)](CONTRIBUTING.md)

[English](README.md) · **Français** · [Español](README.es.md)

</div>

---

Parlez de votre idée de startup à un agent IA : le plus souvent, il la trouve excellente et vous aide aussitôt à la construire. Interrogez-le sur les aides ou les statuts juridiques : il risque de citer des règles qui ont changé l'an dernier.

**garage** fait travailler votre agent comme un mentor exigeant : tester l'hypothèse la plus risquée avant de construire, chercher des comportements plutôt que des compliments, vérifier aides, lois et prix sur les sites officiels avec la date, et produire des choses utilisables tout de suite : un guide d'entretien, une landing page, un prototype cliquable, un prévisionnel.

## Installation

**La plupart des agents de code** (Claude Code, Codex, Cursor, Windsurf, Cline et d'autres) :

```bash
npx skills add teodstr/garage -g
```

**Claude Code**, sous forme de plugin :

```
/plugin marketplace add teodstr/garage
/plugin install garage@garage
```

**À la main :** copiez les dossiers de [`skills/`](skills) dans le dossier de skills de votre agent.

## Utilisation

Posez simplement votre question. Le bon skill se charge tout seul.

```
I have an idea for a meal-prep service for students. Where do I start?
Prépare-moi un guide d'entretien pour tester mon idée de friperie en ligne.
¿Qué ayudas existen para crear una startup en Madrid?
Build me a landing page to test demand for a bike repair subscription.
Quel statut juridique choisir pour facturer mes premières missions de graphiste ?
```

## Les skills

| Skill | Ce qu'il fait |
|---|---|
| **Démarrer** | |
| [`startup-roadmap`](skills/startup-roadmap/SKILL.md) | Situe votre projet, son hypothèse la plus risquée et un plan sur 30 jours |
| **Rechercher** | |
| [`idea-validation`](skills/idea-validation/SKILL.md) | Transforme une idée en hypothèses et en tests peu coûteux, avec des critères fixés à l'avance |
| [`customer-interviews`](skills/customer-interviews/SKILL.md) | Guides d'entretien et comptes rendus qui donnent des faits plutôt que des compliments (The Mom Test) |
| [`survey-design`](skills/survey-design/SKILL.md) | Questionnaires neutres, bon échantillon et marges d'erreur honnêtes |
| [`desk-research`](skills/desk-research/SKILL.md) | Recherche documentaire sourcée : statistiques publiques, comptes des entreprises, sources notées |
| [`competitor-teardown`](skills/competitor-teardown/SKILL.md) | Toutes les alternatives, les plus fortes passées au crible, et les failles à exploiter |
| **Concevoir** | |
| [`mvp-scoping`](skills/mvp-scoping/SKILL.md) | Le plus petit produit qui teste votre hypothèse la plus risquée |
| [`brand-identity`](skills/brand-identity/SKILL.md) | Plateforme de marque, noms avec les vérifications à faire, couleurs, typographies, esquisses de logo en SVG |
| [`landing-page`](skills/landing-page/SKILL.md) | Les textes et une page HTML prête à l'emploi pour tester la demande |
| [`prototype-testing`](skills/prototype-testing/SKILL.md) | Un prototype HTML cliquable et un test d'utilisabilité avec cinq personnes |
| [`pitch-deck`](skills/pitch-deck/SKILL.md) | Une histoire en dix slides, ou la relecture de votre deck comme le ferait un investisseur |
| **Ressources** | |
| [`funding-options`](skills/funding-options/SKILL.md) | Subventions, prêts d'honneur, prêts bancaires, business angels et fonds adaptés à votre stade et à votre pays |
| [`support-programs`](skills/support-programs/SKILL.md) | Incubateurs, accélérateurs, réseaux, statut d'étudiant-entrepreneur, mentors |
| [`legal-setup`](skills/legal-setup/SKILL.md) | Les statuts juridiques comparés et les premières démarches, à partir des sources officielles |
| **Lancer** | |
| [`first-customers`](skills/first-customers/SKILL.md) | Les canaux à tester, une prospection qui respecte la loi et un suivi chaque semaine |
| [`financial-forecast`](skills/financial-forecast/SKILL.md) | Un prévisionnel mensuel avec autonomie financière, point mort et trois scénarios |

## Ce que chaque skill impose

- **Des preuves avant de construire.** Tester d'abord l'hypothèse la plus risquée, avec un critère de réussite fixé avant le test.
- **Des comportements plutôt que des avis.** Une inscription, une précommande ou une habitude passée comptent plus que « je l'achèterais ».
- **Des sources officielles, datées.** Aides, lois, prix et seuils sont vérifiés sur les sites officiels pendant la conversation, jamais cités de mémoire.
- **Un livrable utilisable tout de suite.** Chaque skill produit un guide, un tableau, une page, un prototype ou un plan.
- **Honnête par principe.** Pas de faux témoignages, de traction inventée ni de fausse rareté, et une prospection qui respecte la loi.

## Fonctionne avec boardroom

garage aide à construire une entreprise ; [boardroom](https://github.com/teodstr/boardroom) aide à en analyser une (SWOT, Porter, BCG, taille de marché, économie unitaire…). Installez les deux : les skills de garage renvoient à ceux de boardroom quand c'est utile.

## Fonctionne en anglais, en français et en espagnol

Posez votre question dans l'une des trois langues et l'agent répond avec les mots qu'emploient vraiment les créateurs d'entreprise et les réseaux d'accompagnement : *prêt d'honneur*, *statut d'étudiant-entrepreneur*, *autónomo*, *empresa emergente*… La France et l'Espagne sont couvertes en détail pour les financements, l'accompagnement et le statut juridique, et ajouter votre pays est l'une des façons les plus simples de contribuer.

## Pas un conseil juridique ou financier

garage aide à préparer ses décisions et à poser les bonnes questions. Pour les choix juridiques, fiscaux et financiers, faites valider par un expert-comptable, un avocat ou un réseau d'accompagnement.

## Contribuer

garage est pensé pour que tout le monde puisse contribuer, même sans avoir jamais écrit une ligne de code : un skill tient dans un seul fichier Markdown.

- **Ajoutez votre pays** aux skills `funding-options`, `support-programs` ou `legal-setup`, avec des sources officielles uniquement.
- **Ajoutez un skill** de la [feuille de route](ROADMAP.md) : tests de prix, pacte entre cofondateurs, premier recrutement, campagne de financement participatif…
- **Ajoutez une langue** aux tableaux de terminologie, ou traduisez ce README.
- **Signalez une réponse faible :** ouvrez une issue avec votre prompt et ce que l'agent a produit.

Commencez par [CONTRIBUTING.md](CONTRIBUTING.md) (en anglais). Chaque pull request est vérifiée automatiquement.

## Licence

[MIT](LICENSE). Maintenu par [teodstr](https://github.com/teodstr). Réalisé avec l'aide de Claude.
