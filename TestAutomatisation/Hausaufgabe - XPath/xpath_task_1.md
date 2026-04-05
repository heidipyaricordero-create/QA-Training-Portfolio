# XPath Lösungen - Aufgabe 1
1. **Haupt-h1-Element finden:**
- `//h1[@id='mainTitle']` oder `//header/h1`

2. **Navigationslink "About Us" auswählen:**
- `//nav//a[text()='About Us']`

3.  **Dropdown-Link "Graphic Design" auswählen:**
- `//ul[@class='dropdown']//a[text()='Graphic Design']`

4. **Namen des Teammitglieds "Jane Smith" auswählen:**
- `//h4[text()='Jane Smith]`/p`

5. **Beschreibung der "SEO Services" auswählen:**
- `//div[h3='SEO Services']/p`

6. **Alle Service-Elemente im Abschnitt "Our Services" auswählen:**
- `//section[@id='services']//div[@class='service-item']`

7. **E-Mail-Eingabefeld im Kontaktformular auswählen:**
- `//form[@id='contactForm']//input[@id='email']`

8. **Gesamtes Kontaktformular auswählen:**
- `//form[@id='contactForm']`

9. **Footer_Absatz_Element auswählen:**
- `//footer/p`

10. **Name (h4) des ersten Teammitglieds auswäjlen:**
- `(//div[@class='team']//h4)[1]`

11. **Beschreibung des zweiten Service-Elements auswählen:**
- `(//div[@class='service-item'])[2]/p'

12. **Überschrift der Sektion "Contact Us" (h2) auswählen:**
- `//section[@id='contact']/h2'

13. **Alle Links innerhalb des Dropdowns unter "Services" auswählen:**
- `//nav//ul[@class='dropdown']//a`

14. **Erstes li_Element im Abschnitt "Our Team" auswählen:**
- `(//div[@class='team']//li)[1]`

15. **Schaltfläche "Send Message" im Kontaktformular finden:**
- `//input[@type='submit' and @value='Send Message']'

