# Fink hands-on: a science module with MLflow, on your laptop

We train a model that tells active galaxies from stars, using real ZTF alerts processed by Fink, then use it the way Fink does in production. No account and no remote server are needed.

*On entraîne un modèle qui distingue les galaxies actives des étoiles, à partir de vraies alertes ZTF traitées par Fink, puis on l'utilise comme Fink en production. Tout tourne en local.*

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# terminal 1, keep it running
mlflow server --host 127.0.0.1 --port 6969

# terminal 2
jupyter notebook
```

## Files

| File | What it does |
|---|---|
| `00_get_the_data.ipynb` | where the alerts come from and how `data/alerts.parquet` was made |
| `01_train_and_track.ipynb` | look at an alert, train a model, compare runs in MLflow |
| `02_register_and_serve.ipynb` | register the best model as `champion`, run it on a stream, write a filter |
| `preprocessing.py` | the filter, the features and the labels: the file you edit |
| `processor.py` | `processor(alerts, model)`, the function Fink calls on each batch |
| `prepare_data.py` | joins the 4 downloaded files into `data/alerts.parquet` |
| `images/` | screenshots of what you should see |

## Data

`data/alerts.parquet` comes from the test data of [fink-science](https://github.com/astrolabsoftware/fink-science) (`fink_science/data/alerts/datatest`, Apache 2.0 licence). The labels come from the SIMBAD class that Fink adds to each alert (`cdsxmatch`).

## Notes for the trainer

- Tested with MLflow 3.18 and scikit-learn 1.9 on Python 3.13. The screenshots come from MLflow 3.18: older versions look a bit different.
- Models are saved with `serialization_format="cloudpickle"`, because recent MLflow versions refuse to save random forests in their default format (skops).
- To start again from zero, stop the server and delete the `mlruns/` and `mlartifacts/` folders.
