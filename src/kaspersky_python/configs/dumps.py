from pathlib import Path

_DATA_DIR = Path(__file__).resolve().parents[3] / "data"

VULNERABILITIES_DUMP = _DATA_DIR / "vulnerabilities.json"
VERSIONS_DUMP = _DATA_DIR / "versions.json"
