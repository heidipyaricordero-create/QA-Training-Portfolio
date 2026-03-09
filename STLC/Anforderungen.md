# **Anforderungen**

Der erste Teil des Projektes ist es, die Anforderungen richtig zu verstehen. Überleg dir Fragen und beantworte sie mithilfe der Webiste. Schreib eine kurze Zusammenfassung aller Informationen, die du gefunden hast.

### **Die Software:**

[https://grocerymate.masterschool.com/](https://grocerymate.masterschool.com/)

Webshop mit folgenden Grundfunktionen:

* Registrierung und Login  
* Produktsuche mit Sortierfunktion (z. B. nach Preis), Kategorisierung von Produkten  
* Produkte zu Favoriten hinzufügen  
* Produkte in den Warenkorb legen  
* Bestellabschluss: Eingabe von Rechnungs- und Versandinformationen, Auswahl der Zahlungsmethode, Preisberechnung (Gesamtsumme)

---

## **Neue Funktionen (Features)**

---

### 1\. Bewertungssystem für Produkte

### Ursprünglich vage formulierte Anforderung:

### Nutzer sollen Produkte mit einem 5-Sterne-System bewerten und zusätzlich schriftliches Feedback hinterlassen können.

### 2\. Altersverifikation für alkoholische Produkte

### Ursprünglich vage formulierte Anforderung:

### Alkoholische Produkte erfordern eine Altersverifikation. Beim Aufrufen der Kategorie soll ein Modal erscheinen, in dem Nutzer ihr Alter angeben müssen (18+), bevor sie Zugriff erhalten.

### 3\. Änderungen bei den Versandkosten

### Ursprünglich vage formulierte Anforderung:1

### Versandkosten entfallen ab einem bestimmten Bestellwert. Darunter fallen Versandkosten an.

## **Bewertungs Grundlage**

* ### Mindestens 3 Fragen pro neuem Feature

* ### Fragen müssen für das Verständnis des Testings relevant sein

\----------------------------------------------------------------------------------------------------------------------------

### **1\. Bewertungssystem für Produkte**

**Ursprünglich vage formulierte Anforderung:**

Nutzer sollen Produkte mit einem 5-Sterne-System bewerten und zusätzlich schriftliches Feedback hinterlassen können.

**Fragen:**

1\.  Ist Rich-Text (Fett, Kursiv, Links) erlaubt oder nur Plain Text?

2\. Kann die Gesamtzeichenlänge  (500 Zeichen) unter- oder überschritten werden?

3\. Sind halbe Sterne erlaubt, oder nur ganze Sterne?

4\.  Kann eine Sterne-Bewertung ohne Text abgegeben werden (und umgekehrt)?

**Detaillierte Anforderung:**

Kunden erhalten die Möglichkeit, Produkte zu bewerten. Dies umfasst sowohl eine quantitative Bewertung mittels eines Sternensystems als auch eine qualitative Bewertung durch ein Textfeld für schriftliches Feedback.

### **2\. Altersverifikation für alkoholische Produkte**

**Ursprünglich vage formulierte Anforderung:**

Alkoholische Produkte erfordern eine Altersverifikation. Beim Aufrufen der Kategorie soll ein Modal erscheinen, in dem Nutzer ihr Alter angeben müssen (18+), bevor sie Zugriff erhalten.

**Fragen:**

1. Was, wenn ein Nutzer über eine Suchmaschine oder einen Direktlink direkt auf die Alokohol \- Produktseite gelangt, anstatt über die Kategorie \- Seite?  
     
2.  Muss der Inhalt der Seite hinter dem Modal komplett ausgeblendet sein, oder darf man die Produkte im Hintergrund schon "erahnen"?  
     
3. Was, wenn ein Nutzer ein ungültiges Datum eingibt: z.B. 1654?  
     
4. Wie lange soll das berechnete Ergebnis gespeichert werden? Session-cookie oder Persistent- Cookie (30 Tage)?  
   

**Detaillierte Anforderung:**

Um auf die Produktseite Alkohol zu gelangen, muss der Benutzer sein Geburtsdatum eingeben, das mit dem aktuellen Datum validiert wird. Dies dient der rechtlichen Absicherung, dass das Mindestalter von 18 Jahren für diese Kategorie erreicht sein muss.

### 

### **3\. Änderungen bei den Versandkosten**

**Ursprünglich vage formulierte Anforderung:**

Versandkosten entfallen ab einem bestimmten Bestellwert. Darunter fallen Versandkosten an.

**Fragen:**

1. Bezieht sich der Mindestbestellwert auf den Brutto- oder Nettobetrag?  
     
2. Was passiert exakt bei dem Wert  20,00 €? Ist es dann Versandkostenfrei oder erst ab 20,01 €?  
     
3. Was passiert, wenn ein Artikel hinzu kommt oder entfernt wurde?

**Detaillierte Anforderung:**

Das System berechnet die Versandkosten automatisch basierend auf dem aktuellen Wert der Produkte im Warenkorb. Es wird ein Schwellenwert definiert, ab dem die Lieferung zu versandkostenfrei  freigeschaltet wird.


