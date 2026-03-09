## **Testfallentwurf (Test Case Design)**

Entwirf deine Testfälle auf Basis der Funktionen, die für das nächste Release des Online-Grocery-Shops entwickelt werden sollen\!

* Du musst die Testfälle nur entwerfen – die Testdurchführung erfolgt in einer späteren Phase.  
* Füge, wenn anwendbar, die verwendete Testentwurfs-Technik (z. B. Äquivalenzklassenbildung, Grenzwertanalyse) hinzu.

---

### **1\. Bewertungssystem für Produkte**

**Testentwurfsverfahren**: Grenzwertanalyse (BVA), Äquivalenzklassenbildung (EP),  
Fehlerermessen (Error Guessing), Anwendungsfalltest (Use Case Testing)

1. **Grenzwertanalyse:**  
     
   * **Testfall:** Bewertung mit genauer Zeichenanzahl im Feld (500).  
   * **Eingabe:** Text mit exakt 500 Zeichen.  
   * **Erwartetes Ergebnis**: Bewertung wird gespeichert.  
       
2. **Grenzwertanalyse:**  
     
* **Testfall:** Bewertung mit 501 Zeichen.  
* **Eingabe:** Text mit exakt 501 Zeichen.  
* **Erwartetes Ergebnis**: Fehlermeldung


3. ## **Äquivalenzklassenbildung:**

     
* **Testfall:** Überprüfung der Durchschnittsberechnung.  
* **Eingabe:** Drei Bewertungen für ein Produkt abgeben: 4 Sterne, 5 Sterne und 4 Sterne (4,333… Sterne)  
* **Erwartetes Ergebnis**: Die Anzeige rundet auf die nächste logische Einheit (z.B. 4,5 Sterne)  
4. **Fehlerermessen:**  
     
* **Testfall:** Bewertung absenden ohne die Auswahl von Sternen  
* **Eingabe:** Nur Text schreiben.  
* **Erwartetes Ergebnis**: Fehlermeldung.

5. **Anwendungsfalltest:**  
     
* **Testfall:** Überprüfen, dass Bewertungen nur für angemeldete Nutzer möglich ist  
* **Eingabe:** Als “Nicht-eingeloggt” Produktseite aufrufen  
* **Erwartetes Ergebnis**: Bewertungsbutton ist ausgegraut oder führt zum Login-Modal.


---

## **2\. Altersverfikation für alkoholische Produkte**

**Testentwurfsverfahren**: Grenzwertanalyse (BVA), Fehlerermessen (Error Guessing)  
Anwendungsfalltest (Use Case Testing),

### **Testfälle:**

**1\. Grenzwertanalyse:**

* **Testfall:** Nutzer ist genau heute 18 Jahre alt geworden.  
  * **Eingabe:** Geburtsdatum von heute vor exakt 18 Jahren eingeben.  
  * **Erwartetes Ergebnis**: Zugriff auf Kategorie “Alkohol” gewährt.  
      
    

**2\. Grenzwertanalyse:**

* **Testfall:** Nutzer ist einen Tag jünger als 18 Jahre.  
* **Eingabe:** Geburtstagsdatum von morgen vor 18 Jahren..  
* **Erwartetes Ergebnis**: Zugriff verweigert,Fehlermeldung


**3\. Fehlerermessen:**

* **Testfall:** Eingabe eines unrealistisches Datums.   
* **Eingabe:** Datum im Jahr 1653\.  
* **Erwartetes Ergebnis**: Fehlermeldung.


  
4\. **Anwendungsfalltest:**

* **Testfall:** Umgehen von Kategorien durch direkte Links zu den Produkten.  
* **Eingabe:** Eingabe der URL eines alkoholischen Getränkes direkt in den Browser.  
* **Erwartetes Ergebnis:** Das System erkennt fehlende Verifikation und zeigt das Modal an.


  


  


---

**3\. Berechnung der Versandkosten bei verschiedenen Warenkorb Werten (Brutto)**

**Testentwurfsverfahren**: Grenzwertanalyse (BVA), Äquivalenzklassenbildung (EP),  
 Anwendungsfalltest (Use Case Testing)

### **Testfälle:**

**1\. Grenzwertanalyse:**

* **Testfall:** Warenkorbwert auf exakten Schwellenwert (z.B. 20,00 €)  
  * **Eingabe:** Produkte im Gesamtwerk von 20,00 €.  
  * **Erwartetes Ergebnis**: Versandkosten werden mit 0,00 € angezeigt.  
    

**2\. Grenzwertanalyse:**

* **Testfall:** Warenkorbwert knapp unter dem Schwellenwert (19,99 €).  
* **Eingabe:** Produkte im Gesamtwerk von 19,99 €.  
* **Erwartetes Ergebnis**: Versandkosten werden angezeigt.  
  


## **3\. Äquivalenzklassenbildung:**

* **Testfall:** Sehr hoher Warenkorbwert.  
* **Eingabe:** Produkte im Wert von 500,00 € abgeben.  
* **Erwartetes Ergebnis**: Versandkosten werden mit 0,00 € angezeigt.

**Anwendungsfalltest:**

* **Testfall:** Automatische Neuberechnung beim Entfernen von Artikeln.  
* **Eingabe:** Warenkorb von 55, 00 € auf 45,00 € reduzieren, durch das Löschen von Artikeln.  
* **Erwartetes Ergebnis**: Versandkosten werden angezeigt.

---

