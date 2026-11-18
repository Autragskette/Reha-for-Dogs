#!/usr/bin/env python3
"""Erzeugt alle Seiten von Reha for Dogs aus gemeinsamen Bausteinen (Kopf, Fuß, Seitenleiste)."""
import os

AUS = os.path.join(os.path.dirname(__file__), "public")
TEL = "0172 474 08 08"
TEL_LINK = "tel:+491724740808"
MAIL = "liane.schlesiger@arcor.de"
ADRESSE = "Schonnebeckhöfe 51, 45309 Essen"
ROUTE = "https://www.google.com/maps/dir/?api=1&destination=Schonnebeckh%C3%B6fe+51%2C+45309+Essen"

I = {
 "pfote": '<path d="M12 21c-3 0-5.5-1.6-5.5-4 0-2.3 2.4-4.6 5.5-4.6s5.5 2.3 5.5 4.6c0 2.4-2.5 4-5.5 4z"/><ellipse cx="5" cy="10" rx="2" ry="2.6"/><ellipse cx="19" cy="10" rx="2" ry="2.6"/><ellipse cx="9" cy="5.5" rx="2" ry="2.6"/><ellipse cx="15" cy="5.5" rx="2" ry="2.6"/>',
 "physio": '<path d="M4 20c2-6 5-9 8-9s6 3 8 9"/><circle cx="12" cy="5" r="2.5"/><path d="M12 11v4M8.5 14.5 12 15l3.5-.5"/>',
 "hand": '<path d="M7 11V6.5a1.5 1.5 0 0 1 3 0V10M10 10V4.5a1.5 1.5 0 0 1 3 0V10M13 10V5.5a1.5 1.5 0 0 1 3 0V12M16 9.5a1.5 1.5 0 0 1 3 0V14a7 7 0 0 1-7 7h-1a6 6 0 0 1-5-2.7L3.6 14.6a1.6 1.6 0 0 1 2.5-2L7 13.5V11"/>',
 "puls": '<path d="M3 12h4l2-6 4 12 2-6h6"/>',
 "tropfen": '<path d="M12 3s6 6.4 6 11a6 6 0 0 1-12 0c0-4.6 6-11 6-11z"/><path d="M9.5 15a2.5 2.5 0 0 0 2.5 2.5"/>',
 "herz": '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
 "bluete": '<circle cx="12" cy="12" r="2.4"/><path d="M12 9.6C10.5 6.5 10.8 4 12 3c1.2 1 1.5 3.5 0 6.6zM12 14.4c1.5 3.1 1.2 5.6 0 6.6-1.2-1-1.5-3.5 0-6.6zM9.6 12C6.5 13.5 4 13.2 3 12c1-1.2 3.5-1.5 6.6 0zM14.4 12c3.1-1.5 5.6-1.2 6.6 0-1 1.2-3.5 1.5-6.6 0z"/>',
 "geraet": '<rect x="3" y="7" width="18" height="11" rx="2"/><path d="M7 11h4M7 14h2M15 12.5a1.5 1.5 0 1 0 0 .01M8 7V5h8v2"/>',
 "person": '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
 "stern": '<path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>',
 "regenbogen": '<path d="M3 17a9 9 0 0 1 18 0M6.5 17a5.5 5.5 0 0 1 11 0M10 17a2 2 0 0 1 4 0"/>',
 "link": '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
 "tel": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
 "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
 "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
 "uhr": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
 "check": '<path d="M20 6 9 17l-5-5"/>',
 "pfeil": '<path d="M5 12h14M13 6l6 6-6 6"/>',
 "runter": '<path d="m6 9 6 6 6-6"/>',
 "menue": '<path d="M4 7h16M4 12h16M4 17h16"/>',
 "zu": '<path d="M6 6l12 12M18 6 6 18"/>',
 "info": '<circle cx="12" cy="12" r="10"/><path d="M12 16v-5M12 8h.01"/>',
 "akte": '<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6M8 13h8M8 17h5"/>',
 "extern": '<path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/>',
 "euro": '<path d="M18 7a7 7 0 1 0 0 10M4 10h10M4 14h10"/>',
}
def ic(n, fill=False):
    if fill:
        return f'<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">{I[n]}</svg>'
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{I[n]}</svg>'

# Leistungen: Datei, Titel, Kurztext, Icon
LEISTUNGEN = [
 ("physiotherapie.html", "Hunde-Physiotherapie", "Schmerzlinderung, Beweglichkeit und Muskelaufbau – nach Operationen, bei Lähmungen und Gelenkerkrankungen.", "physio"),
 ("massage.html", "Massage & Akupunktur", "Gezielte Massagetechniken und Akupunktur gegen Verspannungen und Schmerzen am Bewegungsapparat.", "hand"),
 ("erkrankungen.html", "Erkrankungen", "Arthrose, Cauda equina, Spondylose und weitere Krankheitsbilder, die ich behandle – mit typischen Anzeichen.", "puls"),
 ("homoeopathie.html", "Homöopathie", "Den Hund im Ganzen sehen: Ursachen suchen statt nur Symptome zu behandeln.", "tropfen"),
 ("psychologie.html", "Hunde-Psychologie", "Verhalten verstehen, Zusammenhänge zwischen Verhalten und Erkrankungen erkennen.", "herz"),
 ("bachblueten.html", "Bachblüten", "Eine sanfte Methode bei Angst, Unsicherheit, Stress oder Trauer – nach genauer Analyse.", "bluete"),
 ("geraete.html", "Geräte & Methoden", "Stepper, Trampolin, Interferenz- und Low-Level-Lasertherapie in meiner Praxis.", "geraet"),
]

def kopf(titel, beschreibung, aktiv=""):
    dd = "".join(f'<a href="{d}"><span class="ic">{ic(i)}</span><span><b>{t}</b><small>{k.split("–")[0].split(":")[0][:58]}</small></span></a>' for d, t, k, i in LEISTUNGEN)
    mob = "".join(f'<a href="{d}">{ic(i)}{t}</a>' for d, t, k, i in LEISTUNGEN)
    def a(href, txt, key):
        return f'<a href="{href}"{" class=\"aktiv\"" if aktiv == key else ""}>{txt}</a>'
    return f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{titel}</title>
<meta name="description" content="{beschreibung}">
<meta name="theme-color" content="#26384d">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Crect width='24' height='24' rx='6' fill='%2326384d'/%3E%3Cg fill='%23fff' transform='translate(4 4) scale(.66)'%3E%3Cpath d='M12 21c-3 0-5.5-1.6-5.5-4 0-2.3 2.4-4.6 5.5-4.6s5.5 2.3 5.5 4.6c0 2.4-2.5 4-5.5 4z'/%3E%3Cellipse cx='5' cy='10' rx='2' ry='2.6'/%3E%3Cellipse cx='19' cy='10' rx='2' ry='2.6'/%3E%3Cellipse cx='9' cy='5.5' rx='2' ry='2.6'/%3E%3Cellipse cx='15' cy='5.5' rx='2' ry='2.6'/%3E%3C/g%3E%3C/svg%3E">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<div class="topbar"><div class="wrap"><span class="weg">Termine nach Vereinbarung · telefonisch Mo–Fr 9:00–18:00 Uhr</span><span>Mobil: <a href="{TEL_LINK}">{TEL}</a></span></div></div>
<header class="kopf"><div class="wrap">
  <a class="logo" href="index.html" aria-label="Reha for Dogs – zur Startseite"><span class="zeichen">{ic("pfote", True)}</span><span><b>Reha for Dogs</b><small>Hundephysiotherapie · Liane Schlesiger</small></span></a>
  <nav class="haupt" aria-label="Hauptmenü">
    {a("index.html", "Start", "start")}
    <div class="dd"><button type="button" aria-haspopup="true" aria-expanded="false">Leistungen {ic("runter")}</button><div class="dd-menu">{dd}</div></div>
    {a("ueber-mich.html", "Über mich", "ueber")}
    {a("referenzen.html", "Referenzen", "ref")}
    {a("index.html#kontakt", "Kontakt", "kontakt")}
    <a class="btn btn-p cta" href="{TEL_LINK}">{ic("tel")}Termin vereinbaren</a>
  </nav>
  <button class="burger" type="button" aria-label="Menü öffnen" aria-expanded="false" onclick="menue()">{ic("menue")}</button>
</div></header>
<div class="mobil" id="mobil">
  <a href="index.html">{ic("pfote")}Start</a>
  <div class="gruppe">Leistungen</div>
  {mob}
  <div class="gruppe">Praxis</div>
  <a href="ueber-mich.html">{ic("person")}Über mich</a>
  <a href="referenzen.html">{ic("stern")}Referenzen</a>
  <a href="regenbogenbruecke.html">{ic("regenbogen")}Regenbogenbrücke</a>
  <a href="index.html#kontakt">{ic("pin")}Kontakt & Anfahrt</a>
  <a class="btn btn-p" href="{TEL_LINK}">{ic("tel")}{TEL} anrufen</a>
</div>
<main>
'''

def fuss():
    lst = "".join(f'<li><a href="{d}">{t}</a></li>' for d, t, k, i in LEISTUNGEN)
    return f'''</main>
<footer><div class="wrap">
  <div class="raster">
    <div><a class="logo" href="index.html"><span class="zeichen">{ic("pfote", True)}</span><span><b>Reha for Dogs</b><small>Hundephysiotherapie · Liane Schlesiger</small></span></a>
      <p>Physiotherapie, Massage, Akupunktur, Psychologie, Homöopathie und Bachblüten für Hunde in Essen-Schonnebeck.</p></div>
    <div><h4>Leistungen</h4><ul>{lst}</ul></div>
    <div><h4>Praxis</h4><ul><li><a href="ueber-mich.html">Über mich</a></li><li><a href="referenzen.html">Referenzen</a></li><li><a href="regenbogenbruecke.html">Regenbogenbrücke</a></li><li><a href="links.html">Empfehlungen & Links</a></li></ul></div>
    <div><h4>Kontakt</h4><ul><li>Schonnebeckhöfe 51<br>45309 Essen</li><li><a href="{TEL_LINK}">{TEL}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li><li>Telefonisch Mo–Fr 9:00–18:00 Uhr</li></ul></div>
  </div>
  <div class="unten"><span>© <span id="jahr">2026</span> Liane Schlesiger · Reha for Dogs</span><span><a href="impressum.html">Impressum</a> · <a href="datenschutz.html">Datenschutz</a></span></div>
</div></footer>
<nav class="aktion" aria-label="Schnellkontakt"><a href="{TEL_LINK}">{ic("tel")}Anrufen</a><a href="{ROUTE}" target="_blank" rel="noopener">{ic("pin")}Route</a></nav>
<script src="assets/main.js"></script>
</body>
</html>
'''

def seitenleiste(aktiv):
    nav = "".join(f'<a href="{d}"{" class=\"aktiv\"" if d == aktiv else ""}>{ic(i)}{t}</a>' for d, t, k, i in LEISTUNGEN)
    return f'''<aside class="seite">
  <div class="karte"><h3>Alle Leistungen</h3><nav aria-label="Leistungen">{nav}</nav></div>
  <div class="karte dunkel"><h3>Termin vereinbaren</h3><p>Termine nach Vereinbarung, damit jeder Hund die Behandlung in Ruhe genießen kann. Telefonisch erreichbar Mo–Fr von 9:00 bis 18:00 Uhr.</p>
    <a class="btn btn-w" href="{TEL_LINK}">{ic("tel")}{TEL}</a><a class="btn btn-g" href="mailto:{MAIL}">{ic("mail")}E-Mail schreiben</a></div>
</aside>'''

def seitenkopf(titel, lead, icon, krumen):
    k = '<li><a href="index.html">Start</a></li>' + "".join(f"<li>{x}</li>" for x in krumen)
    return f'''<section class="seitenkopf" style="padding-bottom:40px"><div class="wrap">
  <ol class="krumen">{k}</ol>
  <div class="titel"><span class="ic">{ic(icon)}</span><h1>{titel}</h1></div>
  {f'<p class="lead">{lead}</p>' if lead else ''}
</div></section>'''

def unterseite(datei, titel, meta, lead, icon, inhalt, mit_leiste=True, krumen=None):
    kr = krumen if krumen is not None else ['<a href="index.html#leistungen">Leistungen</a>', titel]
    html = kopf(f"{titel} | Reha for Dogs – Liane Schlesiger, Essen", meta, "")
    html += seitenkopf(titel, lead, icon, kr)
    html += f'<section class="inhalt"><div class="wrap"{"" if mit_leiste else " style=\"grid-template-columns:minmax(0,820px)\""}><div class="text">{inhalt}</div>{seitenleiste(datei) if mit_leiste else ""}</div></section>'
    html += fuss()
    open(os.path.join(AUS, datei), "w", encoding="utf-8").write(html)

def liste(punkte, eins=False):
    return f'<ul class="liste{" eins" if eins else ""}">' + "".join(f"<li>{ic('check')}<span>{p}</span></li>" for p in punkte) + "</ul>"

def chips(punkte):
    return '<ul class="chips">' + "".join(f"<li>{p}</li>" for p in punkte) + "</ul>"

TIERARZT = f'<p class="anmerkung">{ic("info")}<span>Die Behandlung ersetzt nicht den Tierarzt. Eine Zusammenarbeit mit der behandelnden Tierarztpraxis ist mir wichtig.</span></p>'

# ---------------- Startseite ----------------
def startseite():
    karten = ""
    for n, (d, t, k, i) in enumerate(LEISTUNGEN):
        if n == 0:
            karten += f'<li class="rv" style="grid-column:span 2;display:contents"></li>'
    karten = ""
    for n, (d, t, k, i) in enumerate(LEISTUNGEN):
        breit = n == 6
        if breit:
            karten += f'<li class="rv breit-li"><a class="leistung breit" href="{d}"><span class="ic">{ic(i)}</span><span class="txt"><h3>{t}</h3><p>{k}</p><span class="mehr">Mehr erfahren {ic("pfeil")}</span></span></a></li>'
        else:
            karten += f'<li class="rv"><a class="leistung" href="{d}"><span class="ic">{ic(i)}</span><h3>{t}</h3><p>{k}</p><span class="mehr">Mehr erfahren {ic("pfeil")}</span></a></li>'
    galerie = "".join(f'<li class="rv"><img src="bilder/{b}.jpg" alt="{a}" loading="lazy"></li>' for b, a in [
        ("asco", "Zwei weiße Schäferhunde im Garten"), ("frodo", "Französische Bulldogge auf einer Rutsche"), ("motte", "Schäferhund am Meer"),
        ("havaneser", "Kleiner schwarz-weißer Hund im Behandlungsraum"), ("bexx", "Junger Hund entspannt im Sand"), ("lab", "Schwarzer Labrador im Behandlungsraum")])
    html = kopf("Reha for Dogs – Hundephysiotherapie Liane Schlesiger in Essen-Schonnebeck",
                "Hundephysiotherapie, Massage, Akupunktur, Hunde-Psychologie, Homöopathie und Bachblüten für Hunde in Essen-Schonnebeck. Termine nach Vereinbarung: 0172 474 08 08.", "start")
    html += f'''
<section class="hero" style="padding:0"><div class="wrap">
  <div>
    <span class="kicker">Hundephysiotherapie in Essen-Schonnebeck</span>
    <h1>Mehr Beweglichkeit und Lebens&shy;qualität für <em>Ihren Hund</em></h1>
    <p class="lead">Physiotherapie, Massage und Akupunktur – ergänzt durch Hunde-Psychologie, Homöopathie und Bachblüten. Mit Zeit, Ruhe und einem Blick auf den ganzen Hund.</p>
    <div class="knoepfe"><a class="btn btn-p" href="{TEL_LINK}">{ic("tel")}Termin vereinbaren</a><a class="btn btn-s" href="#leistungen">Leistungen ansehen {ic("pfeil")}</a></div>
    <ul class="punkte"><li>{ic("check")}Hundephysiotherapie seit 2012</li><li>{ic("check")}Termine in Ruhe, nach Vereinbarung</li><li>{ic("check")}In Zusammenarbeit mit Ihrem Tierarzt</li></ul>
  </div>
  <div class="hero-bild">
    <div class="rahmen"><img src="bilder/eragon-strand.jpg" alt="Brauner Labrador sitzt am Strand und schaut aufs Meer" width="790" height="982"></div>
    <div class="karte"><span class="ic">{ic("uhr")}</span><span><b>Telefonisch Mo–Fr 9–18 Uhr</b><small>Termine nach Vereinbarung</small></span></div>
  </div>
</div></section>

<section id="leistungen"><div class="wrap">
  <div class="kopfzeile rv"><span class="kicker">Leistungen</span><h2>Behandlung und Begleitung, die zu Ihrem Hund passt</h2><p>Wählen Sie einen Bereich, um mehr über Ablauf, Einsatzgebiete und Methoden zu erfahren.</p></div>
  <ul class="leistungen">{karten}</ul>
</div></section>

<section class="ablauf"><div class="wrap">
  <div class="kopfzeile rv"><span class="kicker">Ablauf</span><h2>So kommen Sie zu einem Termin</h2></div>
  <ol class="schritte">
    <li class="rv"><h3>Anrufen</h3><p>Sie erreichen mich Mo–Fr von 9:00 bis 18:00 Uhr unter {TEL}. Wir sprechen kurz über Ihren Hund und vereinbaren einen Termin.</p></li>
    <li class="rv"><h3>Unterlagen mitbringen</h3><p>Bitte bringen Sie vorhandene Befunde mit, etwa Röntgenbilder oder einen CT-Befund. So kann ich die Behandlung gezielt planen.</p></li>
    <li class="rv"><h3>Behandlung in Ruhe</h3><p>Jeder Termin ist so geplant, dass auch ein kranker Hund die Behandlung in Ruhe genießen kann.</p></li>
  </ol>
  <p class="hinweis rv">{ic("euro")}<span><b>Kosten:</b> Die Kosten richten sich nach Art und Umfang meines Einsatzes. Sprechen Sie mich gern darauf an.</span></p>
</div></section>

<section><div class="wrap person">
  <div class="bild rv"><img src="bilder/moira.jpg" alt="Hündin Moira am Strand" loading="lazy" width="900" height="900"><div class="schild"><b>seit 2012</b>Hundephysiotherapie</div></div>
  <div class="rv">
    <span class="kicker">Über mich</span>
    <h2>Liane Schlesiger</h2>
    <p>Von 2007 bis 2011 habe ich Tierpsychologie (Hund, Katze, Pferd) studiert, mich zur Hundeheilpraktikerin ausbilden lassen und die Homöopathie für Hunde sowie Massage und Akupunktur erlernt. 2012 kam die Hundephysiotherapie dazu.</p>
    <p class="zitat">„Man kann wirklich sagen, dass meine Hunde mir genau den Weg gezeigt haben, den ich gehen musste.“</p>
    <ul class="daten"><li><b>2007</b><span>Beginn Studium Tierpsychologie</span></li><li><b>2011</b><span>Hundeheilpraktikerin</span></li><li><b>2012</b><span>Hunde&shy;physiotherapie</span></li></ul>
    <a class="btn btn-s" href="ueber-mich.html">Mehr über mich {ic("pfeil")}</a>
  </div>
</div></section>

<section style="background:var(--blau-xl)"><div class="wrap">
  <div class="kopfzeile mitte rv"><span class="kicker">Referenzen</span><h2>So viele, die wieder laufen und spielen können</h2><p>Ich freue mich immer wieder, wenn ich sehe, wie gut den Hunden die Behandlung bekommt.</p></div>
  <ul class="galerie">{galerie}</ul>
  <p class="danke rv">Vielen Dank für das Vertrauen.</p>
  <p style="text-align:center;margin-top:22px"><a class="btn btn-s" href="referenzen.html">Alle Referenzen {ic("pfeil")}</a></p>
</div></section>

<section class="kontakt" id="kontakt"><div class="wrap">
  <div class="kopfzeile rv"><span class="kicker">Kontakt</span><h2>Vereinbaren Sie einen Termin</h2><p>Am einfachsten telefonisch. Ich nehme mir Zeit für Ihre Fragen und finde mit Ihnen einen passenden Termin.</p></div>
  <div class="kontakt-raster">
    <div class="kbox rv"><span class="ic">{ic("tel")}</span><h3>Telefon</h3><a class="gross" href="{TEL_LINK}">{TEL}</a><p>Mo–Fr von 9:00 bis 18:00 Uhr</p><span class="status" id="status"><i></i><span>Telefonzeiten Mo–Fr 9–18 Uhr</span></span></div>
    <div class="kbox rv"><span class="ic">{ic("pin")}</span><h3>Praxis</h3><p>Liane Schlesiger<br>Schonnebeckhöfe 51<br>45309 Essen-Schonnebeck</p><p style="margin-top:10px"><a href="{ROUTE}" target="_blank" rel="noopener">Route planen →</a></p></div>
    <div class="kbox rv"><span class="ic">{ic("mail")}</span><h3>E-Mail</h3><a href="mailto:{MAIL}" style="word-break:break-all">{MAIL}</a><p style="margin-top:10px">Termine nach Vereinbarung. Die Kosten richten sich nach Art und Umfang der Behandlung.</p></div>
  </div>
  <div class="knoepfe"><a class="btn btn-w" href="{TEL_LINK}">{ic("tel")}Jetzt anrufen</a><a class="btn btn-g" href="mailto:{MAIL}">{ic("mail")}E-Mail schreiben</a></div>
</div></section>
'''
    html += fuss()
    open(os.path.join(AUS, "index.html"), "w", encoding="utf-8").write(html)

# ---------------- Leistungsseiten ----------------
def leistungsseiten():
    unterseite("physiotherapie.html", "Hunde-Physiotherapie",
        "Hunde-Physiotherapie in Essen-Schonnebeck: Rehabilitation, Lähmungen, Arthrose, HD, ED, Spondylose, vor und nach Operationen.",
        "Die Physiotherapie bewirkt eine Schmerzlinderung, eine Verbesserung der Gelenkbeweglichkeit, Muskelaufbau und Muskelerhalt – die Lebensqualität unserer Hunde wird verbessert.", "physio", f'''
<h2>Einsatzgebiete</h2>
{liste(["Rehabilitation", "Nervenerkrankungen und Lähmungen", "Erkrankungen am Bewegungsapparat wie ED, HD, Arthrose, Cauda equina, Spondylose usw.", "Vor und nach Operationen", "Muskelerkrankungen", "Neurologische Erkrankungen"])}
<h2>Therapieformen</h2>
<p>Die Physiotherapie besteht aus vielen einzelnen Therapieformen, die ich je nach Hund und Krankheitsbild kombiniere:</p>
{chips(["Massage", "Passives Bewegen", "Elektrotherapie", "Gerätetherapie", "Thermotherapie", "Isometrische Übungen"])}
<div class="bilder2"><figure><img src="bilder/trampolin.jpg" alt="Trampolin für die Bewegungstherapie" loading="lazy"><figcaption>Trampolin für die Gerätetherapie</figcaption></figure><figure><img src="bilder/stepper.jpg" alt="Stepper für die Bewegungstherapie" loading="lazy"><figcaption>Stepper für gezielte Übungen</figcaption></figure></div>
<div class="box blau"><h3>Bitte mitbringen</h3><p>Bringen Sie bitte vorhandene Unterlagen wie Röntgenbilder, CT-Befunde usw. mit.</p></div>
<p class="anmerkung">{ic("info")}<span>Die Physiotherapie kann den Tierarzt nicht ersetzen – eine Zusammenarbeit ist wichtig.</span></p>
<p><a class="btn btn-s" href="geraete.html">Geräte & Methoden ansehen {ic("pfeil")}</a></p>''')

    unterseite("massage.html", "Massage & Akupunktur",
        "Hunde-Massage und Akupunktur in Essen-Schonnebeck bei Muskelverspannungen, Arthrose, Spondylose, Cauda equina sowie Bänder- und Sehnenerkrankungen.",
        "Mit gezielter Massage und Akupunktur können viele Erkrankungen behandelt werden.", "hand", f'''
<p>Der Hund hat Spaß an Bewegung: rennen, toben – und am liebsten würde er uns den ganzen Tag begleiten. Durch Erkrankungen am Bewegungsapparat kann das sehr schnell eingeschränkt sein. Lahmheiten und Schmerzen schränken unseren Hund ein.</p>
<h2>Massage</h2>
<p>Eine Massage, die aus vielen Techniken besteht, wirkt dem Schmerz entgegen und fördert die Durchblutung. Eingesetzt werden kann die Massage unter anderem bei:</p>
{chips(["Muskelverspannungen", "Cauda equina", "Arthrose", "Spondylose", "Bänder- und Sehnenerkrankungen"])}
<figure class="bild-breit"><img src="bilder/massage.jpg" alt="Massagehilfsmittel wie Igelbälle und Massageroller" loading="lazy" style="aspect-ratio:16/8"></figure>
<h2>Akupunktur</h2>
<p>Die Akupunktur wird ebenfalls bei Erkrankungen des Bewegungsapparates sowie bei Erkrankungen der Organe eingesetzt.</p>
{TIERARZT}''')

    erk = [
     ("Arthrose", "Eine degenerative Gelenkerkrankung, die schmerzhaft ist und die Gelenkfunktion einschränkt. Sie entsteht durch einen normalen Alterungsprozess sowie durch Wachstumsstörungen beim Junghund.",
      ["Lahmheiten", "Wetterfühligkeit", "Anlaufbeschwerden", "Schonhaltungen", "Bewegungseinschränkungen", "Der Hund möchte keine Treppen mehr steigen, nicht mehr springen und spielt nicht mehr"]),
     ("Cauda equina", "Eine Kompression der Nerven am Ende des Rückenmarks.",
      ["Der Hund kann nicht mehr gerade sitzen", "Beschwerden beim Aufstehen, Treppensteigen oder Springen", "Harn- und Kotabsatz können gestört sein", "Die Rute wird nicht mehr nach oben getragen", "Der Hund schleift mit den Krallen der Hinterläufe"]),
     ("Spondylose", "Auch die Spondylose ist eine chronische Erkrankung des Bewegungsapparates. Knöcherne Zubildungen an der Wirbelsäule verursachen eine Versteifung einzelner Abschnitte.",
      ["Lahmheiten", "Die Hinterhand knickt ein", "Der Hund schleift mit den Krallen der Hinterläufe", "Harn- und Kotabsatz können gestört sein", "Schmerzen beim Aufstehen, Spielen oder bei Berührung des Rückens"]),
    ]
    teile = "".join(f'<div class="erk"><h3>{t}</h3><p>{b}</p><div class="zeichen">Mögliche Anzeichen</div>{liste(z, True)}</div>' for t, b, z in erk)
    unterseite("erkrankungen.html", "Erkrankungen",
        "Arthrose, Cauda equina, Spondylose, ED, HD, Kreuzbandriss, Patellaluxation, Bandscheibenvorfall – Erkrankungen, die mit Physiotherapie begleitet werden können.",
        "Viele Erkrankungen des Bewegungsapparates zeigen sich zunächst durch kleine Veränderungen im Alltag. Hier finden Sie typische Krankheitsbilder und ihre Anzeichen.", "puls", f'''
{teile}
<h2>Weitere Erkrankungen</h2>
{chips(["Ellenbogengelenksdysplasie (ED)", "Hüftgelenksdysplasie (HD)", "Kreuzbandriss", "Patellaluxation", "Bandscheibenvorfall", "Wobbler-Syndrom", "Degenerative Myelopathie"])}
<p class="anmerkung">{ic("info")}<span>Diese Übersicht ersetzt keine Diagnose. Bitte lassen Sie Beschwerden immer tierärztlich abklären und bringen Sie vorhandene Befunde zum Termin mit.</span></p>''')

    unterseite("homoeopathie.html", "Homöopathie",
        "Homöopathie für Hunde in Essen-Schonnebeck: den Hund ganzheitlich betrachten und nach der Ursache suchen.",
        "Entwickelt von Samuel Hahnemann (1755–1843). Das Tier im Ganzen zu sehen, ist die Grundvoraussetzung für eine ganzheitliche Behandlung.", "tropfen", f'''
<p>Dazu gehören eine gute Beobachtungsgabe und viel Einfühlungsvermögen. Alle Erkrankungen haben eine Ursache. Diese Ursache herauszufinden und nicht nur die Symptome zu behandeln, ist die Aufgabe eines Homöopathen.</p>
<div class="box"><h3>Leitsätze der Homöopathie</h3><p style="font-family:var(--serif);font-size:20px;font-style:italic;color:var(--navy-d)">„Ähnliches werde durch Ähnliches geheilt.“</p><p>Es kann nur geheilt werden, was gestört ist, nicht was zerstört ist.</p></div>
<h2>Grenzen der Homöopathie</h2>
<p>Auch die Homöopathie hat Grenzen, zum Beispiel:</p>
{liste(["Fortgeschrittene Organschädigung", "Wenn ein operativer Eingriff nötig ist", "Wenn die Lebenskraft des Hundes zu schwach ist", "Wenn keine artgerechte Haltung gegeben ist", "Lebensbedrohliche Zustände"])}
<p>Eine Abklärung bzw. Zusammenarbeit mit der behandelnden Tierarztpraxis kann durchaus erforderlich sein.</p>
<p class="anmerkung">{ic("info")}<span>Die Homöopathie ist wissenschaftlich umstritten und wird von der Lehrmedizin nicht anerkannt.</span></p>''')

    unterseite("psychologie.html", "Hunde-Psychologie",
        "Hunde-Psychologie in Essen-Schonnebeck: Verhalten ganzheitlich verstehen, Zusammenhänge zwischen Verhalten und Krankheiten erkennen.",
        "Die Sprache des Hundes ist sehr vielfältig. In ihrem Verhalten sind Hunde uns Menschen ähnlicher, als man denkt.", "herz", f'''
<h2>Hunde …</h2>
{liste(["mögen nicht jeden – und zeigen das auch", "haben Angst und reagieren sehr verschieden darauf", "spielen und toben", "haben Freundschaften und Feindschaften"])}
<p>Um einen Hund analysieren zu können, muss man ihn – genau wie in der Homöopathie – ganzheitlich betrachten, also von der Nase bis zur Schwanzspitze.</p>
<div class="box blau"><h3>Weiterbildung</h3><p>Die vielen Seminare und persönlichen Gespräche mit Günther Bloch (Kynologe) haben mir aufgezeigt, was in Bezug auf die Kommunikation der Hunde wichtig ist. Um mehr über den Zusammenhang zwischen Verhalten und Krankheiten zu lernen, habe ich zahlreiche Seminare bei PD Dr. Udo Gansloßer besucht.</p></div>
<h2>Hunde werden zu dem, was wir aus ihnen machen?</h2>
<p>Ja und nein. Denn wir Hundehalter werden durch Gesetze sehr eingeschränkt und können unseren Hunden nicht mehr all das bieten, was früher möglich war. Toben und einfach mal Hund sein ist heute oft nur auf sogenannten Hundewiesen möglich.</p>
<p>Das Resultat nicht artgerechter Haltung – insbesondere durch Leinenzwang – äußert sich bei einigen Hunden in Verhaltensauffälligkeiten. Bei anderen Hunden kann es zu starken Verspannungen am Bewegungsapparat kommen, da die natürliche Bewegungsfolge an der Leine gestört wird.</p>
<p class="zitat">Die Psychologie und die Homöopathie bilden eine Einheit.</p>''')

    bl = [("Mimulus", "wenn Ihr Hund ängstlich ist"), ("Rock Rose", "wenn Ihr Hund unter Angst und Panik leidet"), ("Olive", "wenn Ihr Hund nervös, ungeduldig und leicht reizbar ist"),
          ("Larch", "wenn Ihr Hund wenig Selbstvertrauen hat"), ("Star of Bethlehem", "wenn Ihr Hund einen Schock erlitten hat"),
          ("Crab Apple", "wenn Ihr Hund auf Stress mit übertriebener Reinlichkeit reagiert"), ("Honeysuckle", "wenn Ihr Hund trauert")]
    unterseite("bachblueten.html", "Bachblüten",
        "Bachblüten für Hunde in Essen-Schonnebeck: sanfte Methode bei Angst, Panik, Unsicherheit, Schock oder Trauer – nach persönlicher Analyse.",
        "Entwickelt von Dr. Edward Bach (1886–1936). Zur Verfügung stehen 38 Bachblüten sowie die Notfalltropfen „Rescue“.", "bluete", f'''
<p>Das Verhalten eines Hundes ist sehr vielfältig, deshalb ist eine genaue Analyse unumgänglich. In einem persönlichen Gespräch werden die Verhaltensauffälligkeiten – wie Angst, Panik, Selbstverstümmelung, Aggression und vieles mehr – genau besprochen.</p>
<div class="box"><p style="font-family:var(--serif);font-size:20px;font-style:italic;color:var(--navy-d)">Eine sanfte Methode, die Blockaden löst und den Weg für die Selbstheilung in Gang setzt. Wenn die Seele leidet, leidet auch der Körper.</p></div>
<h2>Beispiele aus den 38 Bachblüten</h2>
<ul class="bluete">{"".join(f"<li><b>{n}</b><span>{t[0].upper() + t[1:]}.</span></li>" for n, t in bl)}</ul>
<p class="anmerkung">{ic("info")}<span>Die Bachblütentherapie ist wissenschaftlich nicht belegt und schulmedizinisch nicht anerkannt. Sie ersetzt keine tierärztliche Behandlung.</span></p>''')

    unterseite("geraete.html", "Geräte & Methoden",
        "Geräte in der Hundephysiotherapie: Stepper, Trampolin, Interferenztherapie und Low-Level-Lasertherapie.",
        "Je nach Krankheitsbild ergänze ich die Behandlung durch gezielte Übungen an Geräten und durch physikalische Therapieformen.", "geraet", f'''
<ul class="geraete">
  <li><img src="bilder/stepper.jpg" alt="Stepper" loading="lazy"><div><b>Stepper</b><span>Gezielte Übungen für Koordination, Muskelaufbau und Beweglichkeit.</span></div></li>
  <li><img src="bilder/trampolin.jpg" alt="Trampolin" loading="lazy"><div><b>Trampolin</b><span>Arbeiten mit dem Hund auf instabilem Untergrund.</span></div></li>
  <li><img src="bilder/geraet.jpg" alt="Gerät für die Interferenztherapie" loading="lazy"><div><b>Interferenztherapie</b><span>Eine spezielle Form der Elektrotherapie.</span></div></li>
  <li><img src="bilder/massage.jpg" alt="Massagehilfsmittel" loading="lazy"><div><b>Massagehilfsmittel</b><span>Igelbälle, Roller und Bürsten für die Massage.</span></div></li>
</ul>
<h2>Low-Level-Lasertherapie</h2>
<p>Zusätzlich setze ich die Low-Level-Lasertherapie ein.</p>
{TIERARZT}''')

# ---------------- Weitere Seiten ----------------
def weitere():
    unterseite("ueber-mich.html", "Über mich", "Liane Schlesiger – Hundephysiotherapeutin, Hundeheilpraktikerin und Tierpsychologin in Essen-Schonnebeck.",
      "", "person", f'''
<div class="person klein"><div class="bild"><img src="bilder/moira.jpg" alt="Hündin Moira am Strand" width="900" height="900"></div>
<div><h2 style="margin-top:0">Liane Schlesiger</h2><p>Mein Name ist Liane Schlesiger, geboren 1967. Mein Leben teile ich mit meinem Ehemann, meiner Hündin Moira und meinem Rüden Eragon.</p>
<p>Meine beiden Hunde Angi († 07.04.2015) und Gismo († 13.06.2013) haben mir den Weg gezeigt, den ich gehen musste.</p></div></div>
<h2>Mein Weg</h2>
<ul class="daten lang"><li><b>2007–2011</b><span>Tierpsychologie (Hund, Katze, Pferd), Ausbildung zur Hundeheilpraktikerin</span></li><li><b>2007–2011</b><span>Homöopathie für Hunde, Massage und Akupunktur</span></li><li><b>2012</b><span>Ausbildung Hundephysiotherapie</span></li></ul>
<p>Mein Rüde Gismo bekam sehr früh die Diagnose Ellenbogendysplasie, sodass eine Operation nach der anderen folgte. Also musste ich mir etwas einfallen lassen und entschloss mich, meinen Weg zu gehen. So erlernte ich 2012 die Hundephysiotherapie.</p>
<p class="zitat">„Man kann wirklich sagen, dass meine Hunde mir genau den Weg gezeigt haben, den ich gehen musste. Ich bin meinen beiden sehr dankbar dafür, denn heute weiß ich, dass diese Entscheidung richtig war.“</p>
<p>Das bedeutet aber nicht, dass meine Fellnasen nicht mehr zum Tierarzt gehen. Es gibt immer Situationen, in denen der Rat eines Mediziners eingeholt werden muss.</p>
<figure class="bild-breit"><img src="bilder/eragon-weit.jpg" alt="Rüde Eragon am Strand" loading="lazy"><figcaption>Mein Rüde Eragon</figcaption></figure>
<p><a class="btn btn-s" href="regenbogenbruecke.html">{ic("regenbogen")}In Erinnerung an Gismo und Angi</a></p>''', krumen=["Über mich"])

    gal = "".join(f'<li><img src="bilder/{b}.jpg" alt="{a}" loading="lazy"></li>' for b, a in [
        ("asco", "Zwei weiße Schäferhunde"), ("frodo", "Französische Bulldogge"), ("motte", "Schäferhund am Meer"), ("bexx", "Junger Hund im Sand"),
        ("lab", "Schwarzer Labrador"), ("havaneser", "Kleiner schwarz-weißer Hund")])
    unterseite("referenzen.html", "Referenzen", "Referenzen von Reha for Dogs – Hunde, die nach der Behandlung wieder laufen und spielen können.",
      "So viele, die wieder laufen und spielen können – ich freue mich immer wieder, wenn ich sehe, wie gut ihnen die Behandlung bekommt.", "stern", f'''
<ul class="galerie" style="grid-template-columns:repeat(2,1fr)">{gal}</ul>
<p class="danke">Vielen Dank für das Vertrauen.</p>''', krumen=["Referenzen"])

    unterseite("regenbogenbruecke.html", "Regenbogenbrücke", "In Erinnerung an Gismo und Angi.",
      "In Erinnerung an meine beiden Seelenhunde, die mir den Weg gezeigt haben.", "regenbogen", f'''
<div class="erinnerung"><img src="bilder/gismo.jpg" alt="Gismo" loading="lazy"><div><span class="jahre">18.05.2005 – 13.06.2013</span><h2>Gismo</h2>
<p>Lieber Gismo, für immer wirst Du in meinem Herzen sein. Du warst ein großer Kämpfer und dennoch haben wir verloren. Ich weiß, dass Du im Regenbogenland viele Deiner Freunde sehen wirst. Die Schmerzen sind vorbei und Du bist endlich frei. Es wird der Tag kommen, an dem wir uns wiedersehen, ich glaube ganz fest daran. Du fehlst mir so sehr. Ich liebe Dich.</p></div></div>
<div class="erinnerung"><img src="bilder/angi.jpg" alt="Angi" loading="lazy" style="object-position:40% 50%"><div><span class="jahre">† 07.04.2015 · 12,5 Jahre</span><h2>Angi</h2>
<p>12,5 Jahre ist ein stolzes Alter, aber dennoch musste ich Dich viel zu früh gehen lassen. Du kannst jetzt wieder spielen, rennen und schwimmen ohne Schmerz. Ich vermisse Dich und irgendwann werden wir uns wiedersehen.</p></div></div>''', mit_leiste=False, krumen=["Regenbogenbrücke"])

    links = ["sannis-dog-shots.de", "westfalenstammhunde.de", "hundefarm-eifel.de", "hundezentrum-teamwork.net", "hunde-in-essen.de",
             "hundetraining-nau.de", "friendlydog.de", "hundeschule-casacanis.de"]
    li = "".join(f'<li><a href="https://www.{l}" target="_blank" rel="noopener">{l}{ic("extern")}</a></li>' for l in links)
    unterseite("links.html", "Empfehlungen & Links", "Empfehlungen und Links rund um den Hund.", "Hundeschulen, Fotografie und weitere Adressen rund um den Hund, die ich empfehlen kann.", "link",
      f'<ul class="links">{li}</ul><p>Außerdem: Mammut-Zoofachhandel und AmberSheen.</p><p class="anmerkung">{ic("info")}<span>Für die Inhalte externer Seiten sind ausschließlich deren Betreiber verantwortlich.</span></p>',
      mit_leiste=False, krumen=["Empfehlungen & Links"])

    unterseite("impressum.html", "Impressum", "Impressum von Reha for Dogs – Liane Schlesiger.", "", "akte", f'''
<h2>Angaben gemäß § 5 DDG</h2>
<p>Liane Schlesiger<br>Reha for Dogs – Hundephysiotherapie<br>Schonnebeckhöfe 51<br>45309 Essen</p>
<h2>Kontakt</h2>
<p>Telefon: <a href="{TEL_LINK}">{TEL}</a><br>E-Mail: <a href="mailto:{MAIL}">{MAIL}</a></p>
<h2>Steuerliche Angaben</h2>
<p>Steuernummer: 111/5258/1502, Finanzamt Essen-Ost</p>
<h2>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</h2>
<p>Liane Schlesiger, Anschrift wie oben</p>
<h2>Hinweis zu den Therapien</h2>
<p>Die von mir angebotenen Therapien sind Teil der alternativen Medizin, die nicht wissenschaftlich belegt und nicht schulmedizinisch anerkannt sind. Sie ersetzen keine tierärztliche Untersuchung und Behandlung.</p>
<h2>Haftung für Inhalte</h2>
<p>Die Inhalte dieser Seiten wurden mit größter Sorgfalt erstellt. Für die Richtigkeit, Vollständigkeit und Aktualität der Inhalte kann ich jedoch keine Gewähr übernehmen.</p>
<h2>Haftung für Links</h2>
<p>Diese Website enthält Links zu externen Websites Dritter, auf deren Inhalte ich keinen Einfluss habe. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter oder Betreiber verantwortlich.</p>
<h2>Urheberrecht</h2>
<p>Die auf diesen Seiten erstellten Inhalte und Werke unterliegen dem deutschen Urheberrecht. Jede Vervielfältigung, Veröffentlichung oder sonstige Verwendung bedarf der vorherigen schriftlichen Zustimmung von Liane Schlesiger.</p>''', mit_leiste=False, krumen=["Impressum"])

    unterseite("datenschutz.html", "Datenschutz", "Datenschutzerklärung von Reha for Dogs – Liane Schlesiger.", "", "akte", f'''
<h2>1. Verantwortliche</h2>
<p>Liane Schlesiger, Schonnebeckhöfe 51, 45309 Essen<br>Telefon: {TEL} · E-Mail: <a href="mailto:{MAIL}">{MAIL}</a></p>
<h2>2. Allgemeines</h2>
<p>Diese Website setzt keine Cookies, keine Analyse- oder Tracking-Werkzeuge und keine externen Schriftarten ein. Es gibt kein Kontaktformular. Personenbezogene Daten werden nur verarbeitet, wenn Sie mich selbst per Telefon oder E-Mail kontaktieren.</p>
<h2>3. Hosting und Server-Logfiles</h2>
<p>Beim Aufruf der Website werden durch den Hosting-Anbieter technisch notwendige Daten verarbeitet (z.&nbsp;B. IP-Adresse, Datum und Uhrzeit des Abrufs, aufgerufene Seite, Browsertyp). Dies dient der sicheren und stabilen Bereitstellung der Website (Art. 6 Abs. 1 lit. f DSGVO). <strong>[Hosting-Anbieter und Speicherdauer werden vor Veröffentlichung ergänzt.]</strong></p>
<h2>4. Kontakt per Telefon oder E-Mail</h2>
<p>Wenn Sie mich kontaktieren, verarbeite ich Ihre Angaben zur Bearbeitung Ihrer Anfrage und zur Terminvereinbarung (Art. 6 Abs. 1 lit. b DSGVO). Die Daten werden gelöscht, sobald sie nicht mehr erforderlich sind und keine gesetzlichen Aufbewahrungspflichten bestehen.</p>
<h2>5. Externe Links</h2>
<p>Der Link „Route planen“ führt zu Google Maps. Erst beim Anklicken werden Daten an Google übertragen. Gleiches gilt für Links zu anderen externen Websites.</p>
<h2>6. Ihre Rechte</h2>
<p>Sie haben das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch (Art. 15–21 DSGVO) sowie das Recht auf Beschwerde bei einer Datenschutz-Aufsichtsbehörde, z.&nbsp;B. der Landesbeauftragten für Datenschutz und Informationsfreiheit NRW.</p>''', mit_leiste=False, krumen=["Datenschutz"])

if __name__ == "__main__":
    startseite(); leistungsseiten(); weitere()
    print("fertig:", sorted(f for f in os.listdir(AUS) if f.endswith(".html")))
