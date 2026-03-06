# **1\. Hausaufgabe: Testplan & Testfallentwurf**

## Testobjekt (System unter Test):

# \*\*Webshop: [https://grocerymate.masterschool.com/\*\*](https://grocerymate.masterschool.com/**)

# ---

## **Testplan**

# Erstelle deinen eigenen Testplan für die neuen Funktionen des Webshops\!

# Indem du die Fragen in der untenstehenden Vorlage beantwortest, erstellst du den Testplan für das Produkt, das du testen wirst:

# Der Testplan sollte enthalten:

1. # Analyse des Produkts

2. # Entwurf der Teststrategie

3. # Definition der Testziele

4. # Festlegung der Testkriterien (z. B. Abnahmekriterien, Abbruchkriterien, Fortsetzungskriterien)

5. # Ressourcenplanung

6. # Planung der Testumgebung

7. # Zeitplan und Aufwandsschätzung

8. # Festlegung der Testliefergegenstände (Test-Deliverables)

# Nutze deine Anforderungen aus den vorherigen Aufgaben als Grundlage für den Testplan.

## **Testfallentwurf (Test Case Design)**

# Entwirf deine Testfälle auf Basis der Funktionen, die für das nächste Release des Online-Grocery-Shops entwickelt werden sollen\!

* # Du musst die Testfälle nur entwerfen – die Testdurchführung erfolgt in einer späteren Phase.

* # Füge, wenn anwendbar, die verwendete Testentwurfs-Technik (z. B. Äquivalenzklassenbildung, Grenzwertanalyse) hinzu.

## **Bewertungskriterien:**

### **Testplan**

# Der Testplan sollte folgende Informationen enthalten:

1. # Zielsetzung (Testziele)

2. # Nutzerbasis (Zielgruppen)

3. # Produktfunktionen

4. # Testumfang (Scope)

5. # Testarten (z. B. funktionale Tests, nicht-funktionale Tests, Regressionstests, Abnahmetests)

# Die Studierenden können kreativ sein und überlegen, wie es in der Praxis wäre.

# Der Inhalt sollte als Leitfaden für den Testprozess dienen.

# Wichtig: Der Testplan muss sich auf die neuen Funktionen von Market Mate beziehen\!

# ---

### **Testfallentwurf**

* # Die Testfälle sollen die drei neuen Funktionen prüfen.

* # Pro Funktion müssen mindestens 3 Testfälle entworfen werden.

* # Falls eine Testentwurfs-Technik anwendbar ist, muss sie angegeben werden.

* # Außerdem muss ergänzt werden, welche Testfälle automatisiert würden – und warum.

# ---

# **Testplan:** 

# **GroceryMate-Webshop, Erweiterungen**

1. # **Produktanalyse**

**Zielsetzung:** 

Erweiterung des GroceryMate-Webshops um ein Bewertungssystem, eine rechtssichere Atersverifikation für alkoholische Produkte und eine dynamische Versandkostenbewertung.

**Zielgruppe:** 

Endverbraucher, die Lebensmittel online bestellen.

**Hardware- und Software-Spezifikationen**

* **Hardwareanforderungen:**  
  * Geräte: PCs, Laptops, Smartphones, Tablets  
  * Spezifikationen: Standardkonfigurationen für Android- und iOS-Geräte; Desktops mit mindestens 4 GB RAM und 2 GHz Prozessor  
* **Softwareanforderungen:**  
  * Betriebssysteme: Windows, macOS, Android, iOS  
  * Browser: Chrome, Firefox, Safari, Edge  
  * Abhängigkeiten: Backend-Dienste, Drittanbieter-Werbeanbieter, Zahlungsschnittstellen  
    

**Funktionalität des Produkts:**

* Registrierung & Login  
* Produktsuche & Filter  
* Favoritenliste & Warenkorb  
* Neu: 5-Sterne Bewertungssystem, Textfeedback  
* Neu: Altersverifikation für Alkohol Kategorie  
* Neu: Dynamische Versandkostenberechnung mit Schwellenwert

---

## **2\. Teststrategie entwerfen**

## **Testumfang (Scope of Testing)**

* ## **Im Umfang enthalten:**

1. Validierung der Altersprüfung inklusive Direct Links  
2. Berechnung der Versandkosten bei verschiedenen Warenkorb Werten (Brutto)  
3. Abgabe und Anzeige von \-sterne \- und Textbewertungen  
4. Produktsuche  
5. Login- und Registrierungsprozess

   

* **Nicht im Umfang enthalten:**   
1. Bank Transaktionen  
2. Lieferungen  
3. Informationen Drittanbieter

**Geplante Testarten**

Funktionstests

Regressions-Tests

Performancetest

Sicherheitstests

Usability-tests

**Risiken und Gegenmaßnahmen**

* **Entwicklungsverzögerungen**  
  * Maßnahme: Pufferzeit einplanen  
* **Fehlende Testdaten**  
  * Maßnahme: Erzeugung von Mock-Daten  
* **Ressourcenengpässe**  
  * Maßnahme: Ersatzressourcen identifizieren


  


**Testlogistik (Testverantwortlichkeiten)**

* Testmanager – Jane Smith  
* QA Engineer (Funktion & Regression) – John Doe  
* QA Engineer (Performance & Sicherheit) – Alice Johnson  
* QA Engineer (Usability) – Robert Brown  
* Endanwender für UAT (User Acceptance Test) – Maria Garcia  
  

---

## **3\. Testziele definieren**

## **Ziele**

* ## Funktionalität: Versandkosten werden ab dem Schwellenwert  (20,00 €) auf 0 gesetzt.

* ## Sicherheit: Das Alters-Modal lässt sich nicht durch Schließen oder URL-Manipulation umgehen.

* ## Qualität: Bewertungen sind nach einem Kauf möglich und werden korrekt gerundet (Sterne).


## **Erwartete Ergebnisse**

* ## Alle Funktionen verhalten sich gemäß Spezifikation

* ## Testfälle zur Altersvalidierung erfolgreich

* ## Testfälle zur Versandkostenberechnung erfolgreich

* ## Es bestehen keine sicherheitsrelevanten Schwachstellen

* ## Die Anwendung ist leicht bedienbar für Endnutzer

    
    
  


---

**4\. Testkriterien definieren**

**Aussetzungskriterien (Suspension Criteria)**

* Kritische Fehler blockieren die Fortsetzung der Tests  
* Fehlende Ressourcen oder Ausfall der Testumgebung


**Abnahmekriterien (Exit Criteria)**

* Alle geplanten Tests wurden ausgeführt  
* **Ausführungsrate:** Mindestens 95 % aller Testfälle wurden ausgeführt  
* **Bestehensquote:** Mindestens 90 % der ausgeführten Testfälle bestanden  
* Alle kritischen und hochpriorisierten Defekte sind geschlossen  
* Es bestehen keine offenen Fehler der Schweregrade 1 oder 2  
* Performanzanforderungen wurden erfüllt  
* Sicherheitslücken wurden behoben  
* Der Abnahmetest (UAT) wurde abgeschlossen und freigegeben


---

## **5\. Ressourcenplanung**

* **Personelle Ressourcen:** QA-Team, Entwicklerteam, Endanwender für UAT  
* **Hardware:** PCs, Laptops, Smartphones, Tablets  
* **Software:** Aktuelle Browser (Chrome, Firefox, Safari, Edge), Betriebssysteme (Windows, macOS, Android, iOS)  
* **Infrastruktur:** Testumgebungen, Automatisierungs-Tools, Performanztest-Werkzeuge

---

## **6\. Testumgebung planen**

* **Testgeräte:** Echte Endgeräte mit real installierten Betriebssystemen und Browsern zur realitätsnahen Simulation  
* **Umgebungen:**  
  * Entwicklung (DEV)  
  * Test (TEST)  
  * Abnahme (ACC – Acceptance)  
    

---

**7\. Zeitplan und Aufwandsschätzung**

| Aktivität | Startdatum | Enddatum | Umgebung | Verantwortlich | Geplanter Aufwand |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Testplanung | 04.03.2026 | 08.03.2026 | Alle | Testmanager | 20 Stunden |
| Testfalldesign | 04.03.2026 | 13.03.2026 | Alle | QA-Team | 40 Stunden |
| Unittest | 11.03.2026 | 20.08.2024 | DEV | Entwickler-Team | 60 Stunden |
| Integrationstest | 18.03.2026 | 23.08.2024 | TEST | QA-Team | 30 Stunden |
| Systemtest | 23.03.2026 | 02.04.2026 | TEST | QA-Team | 80 Stunden |
| Regressions-Test | 06.04.2026 | 10.04.2026 | TEST | QA-Team | 40 Stunden |
| Performanztest | 09.04.2026 | 11.04.2026 | TEST | QA-Team | 20 Stunden |
| Sicherheitstest | 12.03.2026 | 14.03.2026 | TEST | QA-Team | 20 Stunden |
| Abnahmetest (UAT) | 16.03.2026 | 24.03.2026 | ACC | Endanwender | 50 Stunden |
| Release/ Golive | 10.04.2026 | 10.03.2026 | PROD | DevOps-Team | 10 Stunden |

---

## 

## **8\. Testartefakte (Test-Deliverables)**

Folgende Dokumente und Werkzeuge werden im Rahmen des Testprozesses erstellt und bereitgestellt:

* Testplandokument  
* Testfälle und Testskripte  
* Testdaten  
* Testberichte  
* Fehlerberichte (Defect Reports)  
* UAT-Freigabedokumentation (Sign-off)  
    
    
    
  


