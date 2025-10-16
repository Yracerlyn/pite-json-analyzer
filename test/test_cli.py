"""
Tests simples pour cli.py
"""
import sys
sys.path.append('src')
from cli import setup_config, main


def test_setup_config_default():
    """Test que setup_config retourne une configuration par défaut."""
    config = setup_config([])
    assert "path" in config
    assert "encoding" in config
    assert "threshold" in config
    assert "mode" in config


def test_setup_config_with_file():
    """Test que setup_config accepte l'argument --file."""
    config = setup_config(["--file", "mon_fichier.json"])
    
    assert config["path"] == "mon_fichier.json"


def test_setup_config_with_all():
    """Test que setup_config accepte l'argument --all."""
    config = setup_config(["--all"])
    
    assert config["mode"] == "ALL"


def test_main_runs_without_error(capsys):
    """Test que main() s'exécute sans erreur même si le fichier n'existe pas."""
    main(["--file", "fichier_inexistant.json"])   
    captured = capsys.readouterr() 
   
    assert "Total raw records" in captured.out
    assert "Analysis Summary" in captured.out