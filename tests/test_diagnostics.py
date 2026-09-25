from pathlib import Path

import matplotlib.image as mpimg
import numpy as np
import pytest

import allesfitter


DATA_PATH = (
    Path(__file__).resolve().parents[1]
    / "examples"
    / "crash_course"
    / "allesfit_Leonardo"
    / "Leonardo.csv"
)


def test_package_import_does_not_require_optional_samplers():
    assert callable(allesfitter.generate_phase_folded_figure)


def test_generate_phase_folded_figure(tmp_path, capsys):
    output_path = tmp_path / "simulated_transit_phase_fold.png"

    result = allesfitter.generate_phase_folded_figure(DATA_PATH, output_path)

    image = mpimg.imread(output_path)
    assert image.shape[0] > 100
    assert image.shape[1] > 100
    assert image[..., :3].min() < 0.8
    assert len(result["phase"]) == 50
    assert np.nanmin(result["flux"]) == pytest.approx(0.9887, abs=1e-4)
    output = capsys.readouterr().out
    assert "Reading from %s..." % DATA_PATH in output
    assert "Writing to %s..." % output_path in output
