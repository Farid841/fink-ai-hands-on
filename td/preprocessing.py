"""Turn raw ZTF alerts into a table of numbers (X) and labels (y).

This is the file you edit during the hands-on session.
"""
import pandas as pd

# SIMBAD classes of active galaxies (label 1)
AGN_CLASSES = ["QSO", "QSO_Candidate", "AGN", "AGN_Candidate", "Seyfert", "Seyfert_1",
               "Seyfert_2", "BLLac", "Blazar", "Blazar_Candidate", "LINER"]


def make_labels(alerts):
    """1 for an active galaxy, 0 for a star, None for everything else.

    In SIMBAD, the name of every star type ends with "*" (for example "RRLyr*").
    """
    def label(simbad_class):
        if simbad_class in AGN_CLASSES:
            return 1
        if simbad_class.endswith("*"):
            return 0
        return None

    return alerts["cdsxmatch"].apply(label)


def light_curve(alert):
    """All the measurements of one alert: time, magnitude, error and band (1 = g, 2 = r)."""
    points = list(alert["prv_candidates"]) + [alert["candidate"]]
    rows = [[p["jd"], p["magpsf"], p["sigmapsf"], p["fid"]] for p in points if p["magpsf"] is not None]
    return pd.DataFrame(rows, columns=["jd", "mag", "err", "band"])


def make_cut(alerts, min_points=3):
    """The filter: keep alerts with at least `min_points` measurements."""
    n_points = alerts.apply(lambda alert: len(light_curve(alert)), axis=1)
    return alerts[n_points >= min_points]


def make_X(alerts):
    """The features: a few numbers per band that describe the light curve."""
    rows = []
    for _, alert in alerts.iterrows():
        lc = light_curve(alert)
        g = lc[lc["band"] == 1]["mag"]
        r = lc[lc["band"] == 2]["mag"]
        rows.append({
            "mean_g": g.mean(), "std_g": g.std(), "amplitude_g": g.max() - g.min(),
            "mean_r": r.mean(), "std_r": r.std(), "amplitude_r": r.max() - r.min(),
            "color_gr": g.mean() - r.mean(),
        })
    return pd.DataFrame(rows, index=alerts.index)
