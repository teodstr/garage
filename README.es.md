<div align="center">

# garage

**Skills para tu agente de IA, de la primera idea a los primeros clientes.**

Validar una idea · Entrevistas con clientes · Investigación documental · MVP · Identidad de marca · Landing page · Pruebas de prototipo · Pitch deck · Financiación · Forma jurídica · Primeros clientes · Previsión financiera

[![Licencia: MIT](https://img.shields.io/badge/licencia-MIT-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-16-black.svg)](#las-skills)
[![Idiomas](https://img.shields.io/badge/idiomas-EN%20%7C%20FR%20%7C%20ES-green.svg)](#funciona-en-inglés-francés-y-español)
[![PR bienvenidas](https://img.shields.io/badge/PR-bienvenidas-brightgreen.svg)](CONTRIBUTING.md)

[English](README.md) · [Français](README.fr.md) · **Español**

</div>

---

Cuéntale tu idea de startup a un agente de IA y lo normal es que le parezca genial y te ayude a construirla enseguida. Pregúntale por ayudas o formas jurídicas y puede citar normas que cambiaron el año pasado.

**garage** hace que tu agente trabaje como un mentor exigente: probar la hipótesis más arriesgada antes de construir, buscar comportamientos en lugar de cumplidos, comprobar ayudas, leyes y precios en las páginas oficiales con la fecha, y producir cosas que puedes usar hoy mismo: un guion de entrevista, una landing page, un prototipo navegable, una previsión financiera.

## Instalación

**La mayoría de los agentes de programación** (Claude Code, Codex, Cursor, Windsurf, Cline y otros):

```bash
npx skills add teodstr/garage -g
```

**Claude Code**, como plugin:

```
/plugin marketplace add teodstr/garage
/plugin install garage@garage
```

**A mano:** copia las carpetas de [`skills/`](skills) en la carpeta de skills de tu agente.

## Uso

Pregunta sin más. La skill adecuada se carga sola.

```
I have an idea for a meal-prep service for students. Where do I start?
Prépare-moi un guide d'entretien pour tester mon idée de friperie en ligne.
¿Qué ayudas existen para crear una startup en Madrid?
Build me a landing page to test demand for a bike repair subscription.
Quel statut juridique choisir pour facturer mes premières missions de graphiste ?
```

## Las skills

| Skill | Qué hace |
|---|---|
| **Empezar** | |
| [`startup-roadmap`](skills/startup-roadmap/SKILL.md) | Sitúa tu proyecto, su hipótesis más arriesgada y un plan de 30 días |
| **Investigar** | |
| [`idea-validation`](skills/idea-validation/SKILL.md) | Convierte una idea en hipótesis y en pruebas baratas, con criterios fijados de antemano |
| [`customer-interviews`](skills/customer-interviews/SKILL.md) | Guiones de entrevista y resúmenes que dan hechos en lugar de cumplidos (The Mom Test) |
| [`survey-design`](skills/survey-design/SKILL.md) | Cuestionarios neutros, la muestra adecuada y márgenes de error honestos |
| [`desk-research`](skills/desk-research/SKILL.md) | Investigación documental con fuentes: estadísticas oficiales, cuentas de empresas, fuentes evaluadas |
| [`competitor-teardown`](skills/competitor-teardown/SKILL.md) | Todas las alternativas, las más fuertes analizadas a fondo, y los huecos que puedes aprovechar |
| **Diseñar** | |
| [`mvp-scoping`](skills/mvp-scoping/SKILL.md) | El producto más pequeño que pone a prueba tu hipótesis más arriesgada |
| [`brand-identity`](skills/brand-identity/SKILL.md) | Plataforma de marca, nombres con las comprobaciones que hay que hacer, colores, tipografías, bocetos de logotipo en SVG |
| [`landing-page`](skills/landing-page/SKILL.md) | Los textos y una página HTML lista para probar la demanda |
| [`prototype-testing`](skills/prototype-testing/SKILL.md) | Un prototipo HTML navegable y una prueba de usabilidad con cinco personas |
| [`pitch-deck`](skills/pitch-deck/SKILL.md) | Una historia en diez diapositivas, o la revisión de tu deck como lo leería un inversor |
| **Recursos** | |
| [`funding-options`](skills/funding-options/SKILL.md) | Subvenciones, préstamos de honor, préstamos bancarios, business angels y fondos adaptados a tu etapa y a tu país |
| [`support-programs`](skills/support-programs/SKILL.md) | Incubadoras, aceleradoras, redes, programas para estudiantes emprendedores, mentores |
| [`legal-setup`](skills/legal-setup/SKILL.md) | Las formas jurídicas comparadas y los primeros trámites, a partir de fuentes oficiales |
| **Lanzar** | |
| [`first-customers`](skills/first-customers/SKILL.md) | Los canales que hay que probar, una prospección que respeta la ley y un seguimiento semanal |
| [`financial-forecast`](skills/financial-forecast/SKILL.md) | Una previsión mensual con autonomía financiera, punto de equilibrio y tres escenarios |

## Lo que exige cada skill

- **Pruebas antes de construir.** Probar primero la hipótesis más arriesgada, con un criterio de éxito fijado antes de la prueba.
- **Comportamientos en lugar de opiniones.** Un registro, una reserva o un hábito real cuentan más que «lo compraría».
- **Fuentes oficiales, con fecha.** Ayudas, leyes, precios y umbrales se comprueban en las páginas oficiales durante la conversación, nunca de memoria.
- **Algo que puedes usar hoy.** Cada skill entrega un guion, una tabla, una página, un prototipo o un plan.
- **Honesta por principio.** Sin testimonios falsos, tracción inventada ni falsa escasez, y una prospección que respeta la ley.

## Funciona con boardroom

garage te ayuda a construir una empresa; [boardroom](https://github.com/teodstr/boardroom) te ayuda a analizarla (DAFO, Porter, BCG, tamaño de mercado, economía unitaria…). Instala las dos: las skills de garage remiten a las de boardroom cuando es útil.

## Funciona en inglés, francés y español

Pregunta en cualquiera de los tres idiomas y el agente responde con las palabras que de verdad usan quienes emprenden y las redes de apoyo: *prêt d'honneur*, *statut d'étudiant-entrepreneur*, *autónomo*, *empresa emergente*… Francia y España están cubiertas en detalle para la financiación, el acompañamiento y la forma jurídica, y añadir tu país es una de las formas más sencillas de contribuir.

## No es asesoramiento jurídico ni financiero

garage te ayuda a preparar tus decisiones y a hacer mejores preguntas. Para las decisiones jurídicas, fiscales y financieras, consulta con un gestor, un abogado o una red de apoyo al emprendimiento.

## Contribuir

garage está pensado para que cualquiera pueda contribuir, aunque nunca haya escrito una línea de código: una skill es un solo archivo Markdown.

- **Añade tu país** a `funding-options`, `support-programs` o `legal-setup`, solo con fuentes oficiales.
- **Añade una skill** de la [hoja de ruta](ROADMAP.md): pruebas de precio, pacto entre cofundadores, primera contratación, campaña de micromecenazgo…
- **Añade un idioma** a las tablas de terminología, o traduce este README.
- **Informa de una respuesta floja:** abre un issue con tu prompt y lo que produjo el agente.

Empieza por [CONTRIBUTING.md](CONTRIBUTING.md) (en inglés). Cada pull request se comprueba automáticamente.

## Licencia

[MIT](LICENSE). Mantenido por [teodstr](https://github.com/teodstr). Hecho con la ayuda de Claude.
