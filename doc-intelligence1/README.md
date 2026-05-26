**Doc Intelligence — Project Summary**

A multi-stage AI pipeline built with React and the Anthropic Claude API. The app accepts any plain text document, runs it through three parallel Claude API calls to extract a structured summary, topic tags, and key facts — all returned as typed JSON. A fourth stage opens a stateful Q&A chat grounded strictly in the uploaded document, maintaining full conversation history across turns.

**Stack:** React + Vite (frontend), Anthropic Claude Sonnet (inference), Vite dev proxy (CORS handling), `.env` for key management.

**Key engineering concepts demonstrated:**
- **Prompt engineering for structured outputs** — system prompts constrain Claude to respond only in JSON with a defined schema, making responses programmatically parseable
- **Parallel API calls** — the three analysis stages run simultaneously via `Promise.all()`, cutting latency roughly by two-thirds versus sequential calls
- **Multi-turn conversation state** — full message history is passed with every Q&A request, simulating memory across a stateless API
- **Pipeline architecture** — each stage is a discrete function with a single responsibility, making the system modular and easy to extend

**Practical use case:** Rapid document intelligence for research, legal, finance, or knowledge management workflows — drop in a report and instantly get a structured brief plus an interactive Q&A layer on top of it.

# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Oxc](https://oxc.rs)
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/)

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.
