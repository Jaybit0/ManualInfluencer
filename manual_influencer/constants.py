GCP_PROJECT_ID = "manualinfluencer"
BUCKET_NAME = "manual-influencer-manuals"
PDF_FILE_NAME = "StaubMeister_DustPro2000_Bedienungsanleitung.pdf"
GCP_REGION = "europe-west10"
TEXT_TO_SCENES_PROMPT = """Schaltmeister Kompaktregler"""
TEXT_TO_SCENES_SYSTEM_INSTRUCTION = """
Erstelle ein Skript für ein TikTok Video über das gegebene Produkt. Es sollen unerwartete Dinge 
passieren, aber man soll der Geschichte trotzdem folgen können. Es gibt nur einen Sprecher. Gib nur den gesprochenen 
Text in das "audio" Feld aus. Eine Szene besteht aus nicht viel mehr als einem Bild. Alle Handlungen müssen über die Stimme 
beschrieben werden. 

Das Video ist insgesamt sehr kurz, so 10-20s, 2-4 szenen. Jede Szene hat 1-3 Sätze, also wenig Text. Der Sprecher kann seine Stimme nicht 
verstellen. Der erste Satz ist der wichtigste. Er soll catchy sein und direkt in die Situation einsteigen. Es gibt keine 
Einleitung und kein Schluss. Höchstens zwei Worte für Kontext. Oder ein einleitender Satz wie aus einer Fernsehwerbung.
Manchmal verwendest du Phrasen, wie "Kennen Sie das auch?", "Oha", "Oh nein", "Nicht schon wieder", "Oh oh" oder ähnliches.
Aber nicht immer.
Der erste satz darf nicht den produktnamen enthalten. Sei kreativ und benutze nicht immer aber manchmal die Beispielwörter.

Das Bild ("visual") passt meistens zu dem gesprochenen. Beschreibe die Szene. Sie sollen absurd und unterhaltend sein.

Merkmale dieses Stils:

- Bürokratie-Faszination
- Humor mit Kultcharakter
- Post-Ironie und Surrealität
- Ästhetik der Tristesse
- Übertriebene Spezifität"""
