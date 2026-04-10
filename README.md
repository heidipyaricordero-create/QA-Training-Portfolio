# QA-Training-Portfolio

Dieses Repository ist ein praxisorientiertes Portfolio für Quality Assurance und Testautomatisierung. Es dokumentiert sowohl den Software Testing Life Cycle (STLC) als auch konkrete Automatisierungsübungen mit Python, Pytest, Selenium und XPath.

## Projektübersicht

- **Testdokumentation & STLC:** Anforderungsanalyse, Testplanung, Testfalldesign, Testdurchführung und Testberichterstattung.
- **Automatisierung:** Python-basierte Tests mit Pytest, Browserautomatisierung mit Selenium und XPath-Lösungen für Web-Datenextraktion.
- **Qualitätssicherung:** Fokus auf reproduzierbare Tests, negative Testfälle, edge case-Tests und klare Ergebnisdokumentation.

## Struktur

- `STLC/` - Vollständige Testdokumentation
  - `Anforderungen.md`
  - `Testplan.md`
  - `Testfallentwurf (Test Case Design).md`
  - `Testdurchführung`
  - `Testdurchführung ohne screenshots.md`
  - `Hausaufgabe - Testdurchführung & Testberichterstattung (2).pdf`
- `TestAutomatisation/` - Automatisierung und praktische Testaufgaben
  - `1_Hausaufgabenpytest/` - Pytest-Übungen mit parametrisierten und negativen Tests
  - `Hausaufgabe - XPath/` - XPath-Lösungen inklusive Referenz-HTML
  - `hausaufgabe_selenium/` - Selenium-Testskripte für Web-Automation
  - `sample.py`, `test_sample.py` - Einstieg in Pytest

## Fähigkeiten & Tools

- Testmethoden: Blackbox-Testing, Whitebox-Testing, Grenzwertanalyse, Regressionstests
- Testdesign: Testfallentwurf, Testplanerstellung, Anforderungsabgleich
- Automatisierung: Python, Pytest, Selenium, XPath
- Dokumentation: strukturierte Testpläne, Testdurchführung, Testergebnisse

## Projekthighlights

- Aufbau eines vollständigen STLC von der Anforderung bis zur Testausführung
- Implementierung parametrischer Tests mit `pytest.mark.parametrize`
- Entwicklung robuster negativer Tests zur Absicherung gegen ungültige Eingaben
- Praxis mit Selenium zur Automatisierung browserbasierter Abläufe
- XPath-Training zur zuverlässigen Identifikation von Web-Elementen

## So nutzen Sie das Portfolio

1. Virtuelle Umgebung erstellen:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
2. Abhängigkeiten installieren:
   ```powershell
   pip install pytest selenium
   ```
3. Tests ausführen:
   ```powershell
   pytest
   ```
4. Alternativ gezielt ausführen:
   ```powershell
   pytest TestAutomatisation\1_Hausaufgabenpytest
   ```

## Bewerbungsrelevanz

Dieses Projekt ist ideal für Bewerbungen im Bereich QA, Testautomation und Softwarequalität. Es demonstriert Fähigkeit zur strukturierten Testplanung, fundierte Testerstellung und praktische Umsetzung von Automatisierungslösungen.
