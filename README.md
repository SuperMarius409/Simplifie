# Simplifique [1.0.0](https://github.com/SuperMarius409/Simplifie)

<img align="right" height="340" src="https://github.com/SuperMarius409/Simplifie/blob/main/files/project/computer/images/icon.png"/>

Does school really expect you to remember when and where every class is, AND what’s due at what time?
Staying organized is harder now than ever, so even if you were a super computer you’d still struggle.
Don’t worry, we’ve got an app that will help even the laziest students stay organized, productive, and, dare we say, ON TIME!

Our `all-in-one organizational app` is designed to cater to the diverse needs of students, offering a range of functionalities to keep you on track and productive throughout your academic journey.

First and foremost, our `Note Taking App` provides a seamless and intuitive interface for capturing and organizing your notes, lectures, videos, and other important resources. You can easily create, edit, and categorize your notes into customized notebooks or folders, ensuring that all your academic materials are neatly arranged and easily accessible.

But the note-taking feature is just the tip of the iceberg. Our app goes beyond that to offer a powerful `AI Assistant`, leveraging the capabilities of artificial intelligence to provide personalized support and guidance. The AI Assistant can help you with a variety of tasks, such as setting reminders for upcoming assignments and exams, suggesting study resources based on your subjects, and even offering study tips and techniques tailored to your learning style.

Furthermore, our app includes a comprehensive task management system. You can create to-do lists, set deadlines, and receive notifications to stay on top of your assignments, projects, and extracurricular activities. The app's intuitive interface allows you to prioritize tasks, track progress, and ensure you never miss a deadline again.

To make studying more engaging and interactive, our app features a `built-in quiz game`. You can create custom quizzes based on your course materials, enabling you to reinforce your learning and assess your knowledge in a fun and gamified manner. Challenge yourself, compete with classmates, or simply use it as a self-assessment tool to gauge your understanding of the subject matter.

With our app, you'll have a comprehensive suite of tools at your disposal, enabling you to stay organized, manage your tasks effectively, access personalized support, and make learning an enjoyable and engaging experience.

So, what do you think? Are you ready to install our app and revolutionize the way you stay organized and productive as a student?

[![PyPI version](https://img.shields.io/pypi/v/kivymd.svg)](https://pypi.org/project/kivymd)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/kivymd.svg)](#Installation)
[![Repository size](https://img.shields.io/github/repo-size/kivymd/kivymd.svg)](https://github.com/SuperMarius409)

## About

Team Name: Simplifie

App Name: Simplifique

## Installation

```bash
git clone https://github.com/SuperMarius409/Simplifie.git
```

### Dependencies:

- [Kivy](https://github.com/kivy/kivy) >= 2.2.0 ([Installation](https://kivy.org/doc/stable/gettingstarted/installation.html))
- [KivyMD](https://github.com/kivymd/KivyMD) >= 1.1.1 
- [Python 3.7+](https://www.python.org/)
- [Pillow](https://github.com/python-pillow/Pillow/)
- [Wikipedia](https://pypi.org/project/wikipedia/)
- [Python-Docx](https://pypi.org/project/python-docx/)
- [Urllib3](https://pypi.org/project/urllib3/)

## Documentation & Credits

- See documentation at https://kivymd.readthedocs.io
- Wiki with examples of using KivyMD widgets: https://github.com/kivymd/KivyMD/wiki
- All the icons are taken from : https://icons8.com/
- Some designs of the app are taken from [Dribble](https://dribbble.com/) and stored in `files\ideeas`
- We are using [PlatformTools](https://developer.android.com/tools/releases/platform-tools) for debugging the app
- We used [Buildozer](https://buildozer.readthedocs.io/en/latest/) for converting the app into `.apk` file
- The sites that we used for gething information is [NewsAPI](https://newsapi.org/), [TheMealDB](https://www.themealdb.com/) and [OpenWeatherAPI](https://openweathermap.org/api)
- We used random tutorials from youtube to make the apps here are some chanels: [KivyMD](https://www.youtube.com/@KivyMD), [Codemy](https://www.youtube.com/@Codemycom) and [BuildWithPython](https://www.youtube.com/@buildwithpython)

## Watch Our App Demo

<p align="left">
  <a href="https://www.youtube.com/watch?v=Wv9xPJrNvbw">
    <img 
        width="600" 
        src="https://github.com/SuperMarius409/Simplifie/blob/main/files/project/video.png" 
        title="Click to watch demo application of our app"
    >
  </a>
</p>

## Web-Powered App Integration

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

This essential function serves as the **backbone** for all our apps. It utilizes an `API` to retrieve `JSON` data and dynamically updates the app's text based on the received information. In this example we use [OpenWeatherAPI](https://openweathermap.org/api) to get the json data and update it to our app. We rely on this function across our apps to seamlessly integrate real-time data and provide users with **up-to-date** and relevant content.
