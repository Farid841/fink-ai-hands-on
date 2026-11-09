---
theme: default
title: "Fink: classifying the transient sky with AI"
info: |
  Paris-Saclay Astroparticle Symposium 2026, week 3: Open Alerts and Open Data
  Institut Pascal, Orsay
layout: cover
transition: slide-left
mdc: true
routerMode: hash
colorSchema: light
---

<img src="/img/Fink_PrimaryLogo_WEB.png" class="h-24 mb-8" />

# Classifying the<br/>transient sky with AI

<Glossary :t="{ 'AI': 'artificial intelligence', 'LSST': 'Legacy Survey of Space and Time (Rubin Observatory)' }" />
<Credit pos="top-right">Logos: Fink, CNRS, LSST France. Background: Fink Science Portal (github.com/astrolabsoftware/fink-science-portal, assets)</Credit>


<div class="mt-6 text-lg">

**Farid MAMAN**, DevOps at Fink

<span class="opacity-75">Paris-Saclay Astroparticle Symposium 2026 · *Open Alerts and Open Data*<br/>Institut Pascal, Orsay · November 2026</span>

</div>

<div class="absolute bottom-8 left-14 flex items-center gap-8">
  <img src="/img/cnrs.png" class="h-14" />
  <img src="/img/lsstfr.png" class="h-10" />
  <!-- Institut Pascal / IJCLab / Université Paris-Saclay : déposer les logos dans public/img/ et les ajouter ici -->
</div>

<!--
Je me présente ici, en 30 secondes : mon nom, mon rôle dans Fink (DevOps : je déploie les modèles et les pipelines qui les font tourner en temps réel).
Vérifier nom / affiliation / date exacte de la session avant de présenter.
-->

---
layout: center
class: text-center
hide: true
---

# Millions of alerts per night.
# How do we find the interesting ones?

<div class="pt-10 text-xl flex justify-center gap-6">
  <span class="pill">Who codes in Python?</span>
  <span class="pill">Who has used ZTF or Rubin alerts?</span>
  <span class="pill">Who has trained an ML model?</span>
</div>

<!--
Accroche et sondage à main levée. Adapter la suite selon les réponses :
- s'il y a peu de codeurs, rester sur les concepts et faire le TD en mode "exécuter les cellules"
- s'il y a beaucoup de gens qui font du ML, aller plus vite sur la partie 3 et insister sur la partie 5.
Demander aussi : français ou anglais ?
-->

---
layout: section
---

# 1. What is Fink?

---

# The transient sky

<Glossary :t="{ 'ZTF': 'Zwicky Transient Facility' }" />

<div class="grid grid-cols-2 gap-8 pt-2">
<div>

- Surveys image the sky every night
- Every change (a new source, a brightening, something moving) produces an alert
- ZTF: roughly 100,000 to 1 million alerts a night
- Rubin (LSST): up to about 10 million alerts a night

<div class="card orange mt-8 text-xl text-center">

Nobody can look at them all by hand.

</div>

</div>
<div class="card">

### What's in an alert?

- Position, time, brightness (flux)
- The light curve: every past measurement
- 3 image cutouts: science, reference and difference

<div class="flex justify-center pt-6">
  <img src="/img/lsstfr.png" class="h-12" />
</div>

</div>
</div>

<!--
Ordres de grandeur à garder approximatifs ("de l'ordre de").
-->

---

# What is a broker?

<Glossary :t="{ 'API': 'application programming interface' }" />
<Credit>Diagram: F. Maman, made with draw.io</Credit>


A broker sits between the telescope and the scientists.

<img src="/img/broker.svg" class="w-full pt-6" />

<div class="card mt-8">

Fink is one of the community brokers selected by Rubin, and it already processes the ZTF stream.
It runs in real time and its code is open source.

</div>

<!--
Le message : Fink reçoit, enrichit, trie et redistribue. L'étape "Enrich" (en orange) est celle qui nous intéresse aujourd'hui : c'est là que vivent les classifieurs.
-->

---

# A real alert

<Credit>ZTF alert ZTF18abctvau (ZTF public alert stream), taken from the fink-science test data (github.com/astrolabsoftware/fink-science, fink_science/data/alerts). Plot: F. Maman, matplotlib</Credit>


<img src="/img/real-alert.png" class="w-full rounded-lg shadow" />

<div class="grid grid-cols-3 gap-4 pt-4 text-sm">
<div class="card">The <i>difference</i> cutout shows what changed in the image</div>
<div class="card">The light curve shows how the brightness evolves in the g and r bands</div>
<div class="card orange">Fink adds a cross-match, scores and a final class</div>
</div>

<!--
Vraie alerte ZTF tirée des données de test de fink-science (ZTF18abctvau). Slide suivante : la même chose vue dans le portail Fink.
-->

---

# The same kind of alert in the Fink portal

<Credit>Screenshot of the Fink Science Portal, object ZTF19acnjwgm. Source: Fink tutorials, <a href="https://github.com/astrolabsoftware/fink-tutorials/blob/main/ztf/interfaces/view.png" target="_blank">https://github.com/astrolabsoftware/fink-tutorials/blob/main/ztf/interfaces/view.png</a></Credit>

<img src="/img/portal-view.png" class="h-86 mx-auto rounded-lg shadow-lg border" />

<!--
Capture du portail Fink (tutoriels Fink). Si possible, faire la démo en live à la place.
-->

---
layout: section
---

# 2. How do we classify alerts?

---

# What are we looking for?

<Glossary :t="{ 'SN': 'supernova (plural SNe)', 'SN Ia': 'type Ia supernova, the thermonuclear explosion of a white dwarf' }" />
<Credit>Class icons: Fink Science Portal (github.com/astrolabsoftware/fink-science-portal, assets/types)</Credit>


<div class="grid grid-cols-6 gap-3 pt-2 text-center text-sm icon-grid">
<div><img src="/img/SNIa.png" />SN Ia</div>
<div><img src="/img/SNCC.png" />Core-collapse SN</div>
<div><img src="/img/SLSN.png" />Superluminous SN</div>
<div><img src="/img/Variable.png" />Variable stars</div>
<div><img src="/img/MicroLens.png" />Microlensing</div>
<div><img src="/img/Asteroid.png" />Asteroids</div>
</div>

<div class="grid grid-cols-3 gap-4 pt-8">
<div class="card"><h3>Position</h3>Is something already known at this spot?</div>
<div class="card"><h3>Light curve</h3>Its shape, colour and how fast it changes</div>
<div class="card"><h3>Context</h3>The host galaxy and any earlier alerts</div>
</div>

<!--
Icônes : celles utilisées par le portail Fink pour chaque classe.
-->

---

# Science modules and filters

<Credit>Diagram: F. Maman, made with draw.io</Credit>


<img src="/img/science-module.svg" class="w-full pt-8" />

<div class="pt-10 grid grid-cols-2 gap-8">
<div class="card orange">

A science module reads a few columns of the alert and adds one column, for example a probability or a class.

</div>
<div class="card">

A filter then combines these columns, for example *"SN Ia probability > 0.5 and no known star nearby"*.

</div>
</div>

<!--
C'est la slide la plus importante pour le TD : un module ajoute une colonne, un filtre utilise les colonnes. Le TD construit exactement ça.
-->

---
layout: section
---

# 3. AI strategies: an overview

---

# The AI toolbox

<div class="text-sm">

| Strategy | Question | Everyday example | Astro example |
|---|---|---|---|
| Classification | *What is it?* | Spam filter | SN Ia or not? |
| Regression | *How much?* | House price | Photometric redshift |
| Clustering | *What looks alike?* | Customer segments | Families of variable stars |
| Anomaly detection | *What is weird?* | Credit-card fraud | Unknown transient |
| Active learning | *Which example should an expert label?* | The model asks for the labels it needs | Pick targets for spectroscopy |
| Reinforcement learning | *Which action to take?* | AlphaGo, robotics | Telescope scheduling |
| Generative AI | *Produce something new* | ChatGPT, images | Simulated light curves |

</div>

<!--
Une phrase par ligne, pas plus : c'est un panorama. Classification n'est qu'une case parmi d'autres.
-->

---

# Which model for which data?

<Glossary :t="{ 'XGBoost': 'eXtreme Gradient Boosting', 'CNN': 'convolutional neural network' }" />
<Credit pos="top-right">Diagram: F. Maman, made with draw.io</Credit>


<img src="/img/model-data.svg" class="h-80 mx-auto pt-2" />

<div class="pt-2 opacity-80 w-[62%]">

The choice depends on the type of data and on how many labelled examples we have.

</div>


---
layout: section
---

# 4. AI in Fink today

---

# An example: early type Ia supernovae

<div class="pt-3">

A ZTF module that spots a type Ia supernova from the first few points of its light curve.

</div>

<div class="flow text-lg pt-4"><span>Light curve</span><span>Sigmoid fit</span><span>a few numbers</span><span>Random Forest</span><span class="out">SN Ia score</span></div>

<div class="grid grid-cols-3 gap-6 pt-6">
<div class="card"><h3>The features</h3>A sigmoid is fitted to the rise of the light curve; its parameters become the numbers the model sees.</div>
<div class="card"><h3>The model</h3>A Random Forest: fast enough for the live stream, and we can see which features count.</div>
<div class="card orange"><h3>The training</h3>Active learning: experts labelled the alerts the model was least sure about.</div>
</div>

<div class="text-xs opacity-60 pt-6">Module <code>random_forest_snia</code>, fink-science repository</div>

<!--
Un seul exemple, puis on enchaîne sur le workflow (slide suivante) : comment ce modèle passe du notebook au flux.
-->

---

# A model's life cycle

<Credit>Diagram: F. Maman, made with draw.io</Credit>

<img src="/img/lifecycle.svg" class="w-full pt-8" />

<div class="pt-10 grid grid-cols-2 gap-6 text-center">
<div class="card">MLflow keeps every model version, so we know which one produced a score</div>
<div class="card orange">Inference runs inside the alert stream</div>
</div>

<!--
C'est mon domaine (MLOps) : 3-4 minutes max, un seul schéma. Le public scientifique s'intéresse au résultat, pas à l'infra. Garder les détails Kafka/K8s pour les questions.
-->

---
layout: center
class: text-center
---

# Wrap-up

<div class="text-xl pt-6 grid grid-cols-3 gap-6 text-left">
<div class="card"><h3>Fink</h3>Receives, enriches and filters millions of alerts in real time</div>
<div class="card"><h3>Classification</h3>Mixes rules, physics and AI</div>
<div class="card orange"><h3>From notebook to stream</h3>MLflow versions every model and takes it to the live stream</div>
</div>

<div class="pt-10 text-2xl" style="color: var(--fink-navy)">

In the hands-on session, we build a science module and a filter together

</div>

---
layout: section
---

# Thank you. Questions?

<Credit pos="top-right">Logos: Fink, CNRS, LSST France, ZTF, from the Fink Science Portal (github.com/astrolabsoftware/fink-science-portal)</Credit>

<div class="pt-6 text-lg opacity-90">

fink-broker.org · github.com/astrolabsoftware/fink-science

</div>

<div class="absolute bottom-10 right-14 bg-white rounded-xl px-5 py-3 flex items-center gap-6">
  <img src="/img/Fink_PrimaryLogo_WEB.png" class="h-12" />
  <img src="/img/cnrs.png" class="h-12" />
  <img src="/img/lsstfr.png" class="h-9" />
  <img src="/img/ztf.png" class="h-12" />
  <!-- ACME and Université Paris-Saclay: put the logos in public/img/ and add them here -->
</div>
