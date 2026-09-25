"""Lightweight diagnostics built from Allesfitter's time-series utilities."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from .exoworlds_rdx.lightcurves.lightcurve_tools import phase_fold


def load_light_curve(input_path):
    """Read an Allesfitter time, flux, and flux-uncertainty CSV file."""

    input_path = Path(input_path)
    print("Reading from %s..." % input_path)
    data = np.loadtxt(input_path, delimiter=",", comments="#")
    if data.ndim != 2 or data.shape[1] != 3:
        raise ValueError("Light-curve input must contain time, flux, and flux error columns.")
    return data


def generate_phase_folded_figure(
    input_path,
    output_path,
    period_days=3.4,
    epoch_days=1.1,
    phase_bin_width=0.02,
):
    """Phase-fold an Allesfitter light curve and write its diagnostic figure."""

    output_path = Path(output_path)
    if output_path.suffix not in (".png", ".pdf"):
        raise ValueError("Output format must be 'png' or 'pdf'.")

    data = load_light_curve(input_path)
    phase, binned_flux, binned_error, _, raw_phase = phase_fold(
        data[:, 0],
        data[:, 1].copy(),
        period_days,
        epoch_days,
        dt=phase_bin_width,
        ferr_style="sem",
    )
    finite = np.isfinite(binned_flux)

    figure, axis = plt.subplots(figsize=(6.5, 4.0), facecolor="white")
    axis.scatter(
        raw_phase,
        data[:, 1],
        color="0.65",
        alpha=0.35,
        s=9,
        linewidths=0,
        label="Simulated exposures",
    )
    axis.errorbar(
        phase[finite],
        binned_flux[finite],
        yerr=binned_error[finite],
        color="#006C67",
        marker="o",
        markersize=4,
        linewidth=1.2,
        capsize=2,
        label="Phase-bin mean",
    )
    axis.set_xlabel("Orbital phase")
    axis.set_ylabel("Relative flux")
    axis.set_title("Simulated 3.4-day transit")
    axis.grid(False)
    axis.legend(frameon=True, fancybox=True, framealpha=1.0)
    figure.tight_layout()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    print("Writing to %s..." % output_path)
    figure.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(figure)
    return {
        "phase": phase[finite],
        "flux": binned_flux[finite],
        "flux_error": binned_error[finite],
        "output_path": output_path,
    }
