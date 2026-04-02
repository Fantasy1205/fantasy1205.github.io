# CLAUDE.md - Developer Guide for al-folio

## Build and Development
The recommended approach for development is using Docker.

```bash
# Start development server (runs at http://localhost:8080)
docker compose up

# Rebuild after changing dependencies or Dockerfile
docker compose up --build

# Stop containers
docker compose down
```

### Pre-Commit Checklist
Before every commit, run these steps:
1. **Format Code:** `npx prettier . --write`
2. **Build Locally & Verify:** `docker compose up --build`

## Project Structure
- `_config.yml`: Main configuration (titles, URLs, features)
- `_pages/`: Main site pages (about.md, projects.md, etc.)
- `_posts/`: Blog posts (YYYY-MM-DD-title.md)
- `_bibliography/papers.bib`: BibTeX for publications
- `_data/`: YAML data (cv.yml, socials.yml, etc.)

## Programming Guidelines
- **Template Engine:** Jekyll / Liquid
- **Styling:** SCSS (located in `_sass/`)
- **Formatting:** Use Prettier (`@shopify/prettier-plugin-liquid`) for Liquid/HTML files.
- **Environment:** Always use `JEKYLL_ENV=production` for production builds to enable minification.

## Troubleshooting
- If Docker fails, check disk space/RAM or run `docker compose down`.
- Image processing requires ImageMagick (pre-installed in Docker).
- Jupyter support requires `nbconvert`.
