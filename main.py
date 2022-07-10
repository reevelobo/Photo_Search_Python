from kivy.app import App
from kivy.uix.screenmanager import  ScreenManager , Screen
from kivy.lang import Builder

import wikipedia
import requests


Builder.load_file('frontend.kv')
#Requrire as many screen classes as there are screens on the app

class FirstScreen(Screen):
    # The first screen will have a method
    # Search Image method
    # Below the Screen Class you will define methods that belong to that screen
    def get_image_link(self):
        # Get user Query from Text input
        query = self.manager.current_screen.ids.user_query.text

        # Get wikipedia page and the first image URL
        page = wikipedia.page(query)
        image_link = page.images[3]
        return image_link

    def download_image(self):
        # Download the image
        req = requests.get(self.get_image_link())

        # Write the content of the image to a jpg file
        imagePath = 'files/image.jpg'
        with open(imagePath, 'wb') as file:
            file.write(req.content)
        return imagePath

    def set_image(self):
        # Set the image in the image widget
        self.manager.current_screen.ids.img.source = self.download_image()

class RootWidget(ScreenManager):
    pass

class MainApp(App):
        def build(self):

            return RootWidget()

MainApp().run()