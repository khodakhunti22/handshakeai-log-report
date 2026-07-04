import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")


def load_report():
    assert REPORT_PATH.exists(), "no report.json found"
    with REPORT_PATH.open() as report_file:
        return json.load(report_file)


def test_report_is_valid_json_object():
    """Verifies instruction criterion 1: /app/report.json is a valid JSON object."""
    report = load_report()
    assert isinstance(report, dict), "report.json must contain a JSON object"


def test_report_schema_exact_keys():
    """Verifies instruction criterion 2: the report has exactly the required keys."""
    report = load_report()
    assert set(report) == {"total_requests", "unique_ips", "top_path"}


def test_report_request_and_ip_counts():
    """Verifies instruction criterion 3: request and unique IP counts are correct."""
    report = load_report()
    assert report["total_requests"] == 6
    assert report["unique_ips"] == 3


def test_report_top_path():
    """Verifies instruction criterion 4: top_path is the most requested path."""
    report = load_report()
    assert report["top_path"] == "/index.html"
