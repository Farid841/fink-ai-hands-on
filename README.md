# Fink — Classifying the Transient Sky with AI (Slidev)

Slides en anglais, notes d'orateur en français (mode présentateur : `/presenter`).

## Lancer

```bash
npm install
npm run dev        # http://localhost:3030
```

## Structure

- `slides.md` — le contenu des slides
- `styles/index.css` — thème aux couleurs de Fink (navy `#15284F`, orange `#F5622E`)
- `global-bottom.vue` — pied de page (bandeau orange, numéro, logo Fink)
- `diagrams/*.drawio` — les 4 schémas, éditables dans draw.io / diagrams.net
- `public/img/` — logos, icônes de classes, fond, captures, et les schémas exportés en SVG

## Modifier un schéma

Ouvrir le `.drawio` dans draw.io, puis réexporter en SVG vers `public/img/` (même nom), par exemple :

```bash
drawio -x -f svg -o public/img/broker.svg diagrams/broker.drawio
```

## Exporter en PDF

```bash
npm i -D playwright-chromium
npm run export
```

## Origine des images

- Logos Fink, CNRS, LSST-France, fond « particules », icônes de classes : dépôt `astrolabsoftware/fink-science-portal` (assets)
- Capture du portail : dépôt `astrolabsoftware/fink-tutorials`
- « A real alert » : alerte ZTF18abctvau des données de test de `fink-science`, tracée avec matplotlib

## À compléter avant la présentation

- Logos Institut Pascal / IJCLab / Université Paris-Saclay : déposer dans `public/img/` et les ajouter sur la slide de titre (emplacement commenté)
- Slide de titre : vérifier nom, affiliation, date de la session
- Slide « Deep learning » : confirmer l'architecture de CATS avec l'auteur du module
- Vérifier avec l'équipe la liste des classifieurs actuellement en production
