"""The science module: Fink calls processor(alerts, model) on each batch of alerts."""
import pandas as pd

import preprocessing as pp


def processor(alerts, model):
    """Return one score per alert: the probability that it is an active galaxy.

    Alerts removed by the filter get a score of 0.
    """
    scores = pd.Series(0.0, index=alerts.index)
    kept = pp.make_cut(alerts)
    if len(kept) > 0:
        X = pp.make_X(kept)
        scores[kept.index] = model.predict_proba(X)[:, 1]
    return scores
