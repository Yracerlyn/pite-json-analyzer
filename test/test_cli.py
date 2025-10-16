"""
Tests for cli.py
"""
import sys
sys.path.append('src')
from cli import setup_config, main


def test_setup_config_default():
    """Test that setup_config returns a default configuration."""
    config = setup_config([])
    assert "path" in config
    assert "encoding" in config
    assert "threshold" in config
    assert "mode" in config


def test_setup_config_with_file():
    """Test that setup_config accepts the --file argument."""
    config = setup_config(["--file", "file.json"])
    
    assert config["path"] == "file.json"


def test_setup_config_with_all():
    """Test that setup_config accepts the --all argument."""
    config = setup_config(["--all"])
    
    assert config["mode"] == "ALL"


def test_main_runs_without_error(capsys):
    """Test that main() runs without error even if the file doesn't exist."""
    main(["--file", "file.json"])   
    captured = capsys.readouterr() 
   
    assert "Total raw records" in captured.out
    assert "Analysis Summary" in captured.out