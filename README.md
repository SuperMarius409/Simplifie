# Simplifique [1.0.0](https://github.com/SuperMarius409/Simplifie)

<img align="right" height="340" src="https://github.com/SuperMarius409/Simplifie/blob/main/files/project/computer/images/icon.png"/>

Școala chiar se așteaptă ca tu să-ți amintești când și unde este fiecare curs și ce trebuie să faci și când?

Menținerea organizării este mai grea acum decât oricând, deci chiar dacă ai fi un supercomputer, tot ai avea dificultăți.

Nu-ți face griji, avem o aplicație care te va ajuta chiar și pe cei mai leneși elevi să rămână organizați, productivi și, îndrăznesc să spun, LA TIMP!

Aplicația noastră `all-in-one` este concepută pentru a răspunde nevoilor diverse ale elevilor, oferind o gamă de funcționalități pentru a te menține pe drumul cel bun și productiv pe parcursul călătoriei tale academice.

În primul rând, aplicația noastră de `task-uri` oferă o interfață fluidă și intuitivă pentru capturarea și organizarea notelor tale, a lecturilor, a videoclipurilor și a altor resurse importante. Poți crea, edita și categoriza cu ușurință `notitele` tale în caiete personalizate sau în foldere, asigurându-te că toate materialele tale academice sunt aranjate ordonat și accesibile cu ușurință.

Dar caracteristica de luare a notițelor este doar vârful aisbergului. Aplicația noastră merge dincolo de asta pentru a oferi un `Asistent AI` puternic, valorificând capacitățile inteligenței artificiale pentru a oferi suport și îndrumare personalizate. Asistentul AI te poate ajuta într-o varietate de sarcini, cum ar fi stabilirea de mementouri pentru sarcinile și examenele viitoare, sugestii de resurse de studiu bazate pe materiile tale și chiar oferirea de sfaturi și tehnici de învățare adaptate stilului tău de învățare.

În plus, aplicația noastră include un sistem cuprinzător de gestionare a sarcinilor. Poți crea liste de sarcini, stabili termene limită și primi notificări pentru a rămâne la curent cu temele, proiectele și activitățile extracurriculare. Interfața intuitivă a aplicației îți permite să prioritizezi sarcinile, să urmărești progresul și să te asiguri că nu mai ratezi niciodată o termen limită.

Pentru a face studiul mai captivant și interactiv, aplicația noastră dispune de un `joc de quiz încorporat`. Poți crea teste personalizate pe baza materialelor cursului tău, permițându-ți să-ți consolidezi învățarea și să-ți evaluezi cunoștințele într-un mod distractiv și gamificat. Provocă-te pe tine însuți, concurează cu colegii de clasă sau pur și simplu folosește-l ca un instrument de autoevaluare pentru a măsura înțelegerea ta a materiei.

Cu aplicația noastră, vei avea la dispoziție o suită cuprinzătoare de instrumente, care îți vor permite să rămâi organizat, să-ți gestionezi sarcinile eficient, să beneficiezi de suport personalizat și să faci din învățare o experiență plăcută și captivantă.

Deci, ce părere ai? Ești gata să instalezi aplicația noastră și să revoluționezi modul în care rămâi `organizat și productiv ca student?`

[![PyPI version](https://img.shields.io/pypi/v/kivymd.svg)](https://pypi.org/project/kivymd)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/kivymd.svg)](#Installation)
[![Repository size](https://img.shields.io/github/repo-size/kivymd/kivymd.svg)](https://github.com/SuperMarius409)

## Despre

Echipa: Simplifie

Numele aplicației: Simplifique

Membri: Radulescu Marius (partea tehnică), Vacaru Stefania (ideea și designul)

Școala: Colegiul Național Militar "Tudor Vladimirescu" 

## Instalare

```bash
git clone https://github.com/SuperMarius409/Simplifie.git
```

### Dependente:

- [Kivy](https://github.com/kivy/kivy) >= 2.2.0 ([Installation](https://kivy.org/doc/stable/gettingstarted/installation.html))
- [KivyMD](https://github.com/kivymd/KivyMD) >= 1.1.1 
- [Python 3.7+](https://www.python.org/)
- [Pillow](https://github.com/python-pillow/Pillow/)
- [Wikipedia](https://pypi.org/project/wikipedia/)
- [Python-Docx](https://pypi.org/project/python-docx/)
- [Urllib3](https://pypi.org/project/urllib3/)

## Documentație și Credite

- Vezi documentatia la https://kivymd.readthedocs.io
- Toate iconitele sunt luate de pe : https://icons8.com/
- Cateva design-uri sunt luate de pe [Dribble](https://dribbble.com/) si stocate in `files\ideeas`
- Folosim [PlatformTools](https://developer.android.com/tools/releases/platform-tools) pentru a depana aplicația
- Folosim [Buildozer](https://buildozer.readthedocs.io/en/latest/) pentru a converti aplicatia intrun fisier `.apk`
- Site-urile din care am luat datele sunt [NewsAPI](https://newsapi.org/), [TheMealDB](https://www.themealdb.com/) si [OpenWeatherAPI](https://openweathermap.org/api)
- Am folosit tutorialele si modelele aplicatiilor unora dintre cele mai cunoscute canale de youtube: [KivyMD](https://www.youtube.com/@KivyMD), [Codemy](https://www.youtube.com/@Codemycom) si [BuildWithPython](https://www.youtube.com/@buildwithpython)

## Vizionati Demo-ul

<p align="left">
  <a href="https://www.youtube.com/watch?v=4er9b6TH_TA">
    <img 
        width="600" 
        src="https://github.com/SuperMarius409/Simplifie/blob/main/files/project/video.png" 
        title="Da-ti click pentru a viziona demo-ul"
    >
  </a>
</p>

## Integrarea aplicației bazate pe web

```python
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={self.api_key}"
    x = requests.get(url).json()
    screen6 = self.root.get_screen("screen6")
    if x["cod"] != "404":
      temperature = str(round(x["main"]["temp"]-273.15))
      temperature = f"[b]{temperature}[/b]°"
      humidity = x["main"]["humidity"]
      weather = x["weather"][0]["main"]
      id = str(x["weather"][0]["id"])
      wind_speed = round(x["wind"]["speed"]*18/5)
      location = x["name"] + ", " + x["sys"]["country"]
```

Această funcție esențială servește ca model pentru toate aplicațiile noastre. Utilizează un `API` pentru a obține date în format `JSON` și actualizează dinamic textul aplicației pe baza informațiilor primite. În acest exemplu, folosim [OpenWeatherAPI](https://openweathermap.org/api) pentru a obține datele JSON și pentru a le actualiza în aplicația noastră. Ne bazăm pe această funcție în toate aplicațiile noastre pentru a integra fără probleme date în timp real și a oferi utilizatorilor conținut actualizat și relevant.