#!/usr/bin/env python3
"""Phase-fold Allesfitter's bundled simulated transit light curve."""

import argparse
from pathlib import Path

from allesfitter import generate_phase_folded_figure


def main():
    """Generate the simulated transit diagnostic."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--typefileplot", choices=("png", "pdf"), default="png")
    arguments = parser.parse_args()
    example_directory = Path(__file__).resolve().parent
    input_path = (
        example_directory
        / "crash_course"
        / "allesfit_Leonardo"
        / "Leonardo.csv"
    )
    output_path = example_directory / (
        "simulated_transit_phase_fold.%s" % arguments.typefileplot
    )
    generate_phase_folded_figure(
        input_path,
        output_path,
        period_days=3.4,  # [day]
        epoch_days=1.1,  # [day]
    )


if __name__ == "__main__":
    main()
