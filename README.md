# FastAPI Blog

A small FastAPI + Jinja + Tailwind CSS project.

## Stack

- FastAPI for the backend
- Jinja2 templates for server-side rendering
- Tailwind CSS compiled with the Tailwind CLI
- Static files served by FastAPI

## Project Structure

- `main.py` - FastAPI app and routes
- `templates/` - Jinja templates
- `static/src/input.css` - Tailwind source CSS
- `static/css/main.css` - compiled Tailwind output

## Requirements

- Python 3.11+
- Node.js 22+
- npm

## Setup

Clone the repository on any machine and install the Python and Node dependencies:

```bash
uv sync
npm install
```

## Build Tailwind CSS

Generate the compiled stylesheet once:

```bash
npm run build:css
```

During development, keep Tailwind watching for changes:

```bash
npm run watch:css
```

## Run the App

Start FastAPI with reload enabled:

```bash
uv run uvicorn main:app --reload
```

If port `8000` is already in use, choose another port:

```bash
uv run uvicorn main:app --reload --port 8001
```

## Working From Office and Home

This repo is set up so you can pull the same code on both machines and keep working:

1. Commit and push changes from one machine.
2. Pull the latest changes on the other machine.
3. Run `uv sync` if Python dependencies changed.
4. Run `npm install` if Node dependencies changed.
5. Rebuild CSS with `npm run build:css` or keep `npm run watch:css` running.

## Notes

- `node_modules/`, `.venv/`, and other local caches are ignored.
- The generated Tailwind CSS is checked into the project so the app works after a pull.
- If you edit templates or add Tailwind classes, rebuild CSS before testing.
