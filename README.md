# Bipin A Abraham — Portfolio (Flask)

A single-page portfolio site built with Flask + Jinja2, styled around a
"terminal / data-pipeline" visual theme (fits a Python/backend/automation
background): a left-hand scroll rail styled like a directory path list
(`~/experience`, `~/skills`...) that fills like a running progress bar as you
scroll, and a work-experience timeline styled like a git commit log.

## Run it

```bash
pip install -r requirements.txt
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

## Structure

```
app.py                          all resume content lives here as Python data
templates/
  base.html                     <head>, fonts, theme bootstrap script
  index.html                    page layout, loops over data via macros
  partials/
    nav_rail.html                left scroll rail + mobile topbar (dark-mode button, scroll progress)
    macros.html                  every reusable "card" (skill chip, timeline
                                  entry, education card, cert row, achievement
                                  card, strength card) — defined once, called
                                  wherever that shape repeats
static/
  css/
    variables.css                design tokens (colors, type, spacing) for
                                  both light and dark themes
    style.css                    layout and component styles
  js/
    main.js                      dark-mode toggle + persistence, scrollspy,
                                  scroll-progress fill
```

## Customizing content

Everything you'd want to change — skills, jobs, education, certifications,
achievements, contact info — is a plain Python list/dict at the top of
`app.py`. Edit the data there; the templates re-render automatically, no HTML
editing required. To add a new job, append an entry to the `EXPERIENCE` list
with the same keys as the existing ones and it will appear in the timeline
automatically (including the connecting line and "current" badge logic).

## Dark mode

Click the toggle at the bottom of the left rail (or in the top bar on
mobile). The choice is saved in `localStorage`, and until you choose
explicitly, the site follows your OS's light/dark setting.
