import importlib.util
from pathlib import Path

import pytest


MODULE_PATH = Path(__file__).parents[1] / "allesfitter" / "paths.py"
SPEC = importlib.util.spec_from_file_location("allesfitter_repository_paths", MODULE_PATH)
paths = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(paths)


def test_repository_runtime_paths(monkeypatch, tmp_path):
    monkeypatch.setenv("ALLESFITTER_PATH", str(tmp_path))
    assert paths.get_repository_path() == tmp_path
    assert paths.get_data_path() == tmp_path / "data"
    assert paths.get_visuals_path() == tmp_path / "visuals"


def test_repository_path_is_required(monkeypatch):
    monkeypatch.delenv("ALLESFITTER_PATH", raising=False)
    with pytest.raises(EnvironmentError, match="ALLESFITTER_PATH"):
        paths.get_repository_path()