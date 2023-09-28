from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.camera import Camera

# MATIAS SANGUINO ESMERAL.
class CameraApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # Agregar una imagen de fondo (reemplaza 'background.jpg' con tu imagen)
        self.background_image = Image(source='178.jpg')
        self.layout.add_widget(self.background_image)

        # Botón para abrir la cámara
        self.camera_button = Button(
            text='Abrir Cámara',
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5}
        )
        self.camera_button.bind(on_release=self.open_camera)
        self.layout.add_widget(self.camera_button)

        return self.layout

    def open_camera(self, instance):
        # Eliminar la imagen de fondo y el botón
        self.layout.remove_widget(self.background_image)
        self.layout.remove_widget(self.camera_button)

        # Agregar la cámara a la interfaz
        self.camera = Camera(play=True)
        self.layout.add_widget(self.camera)

if __name__ == '__main__':
    CameraApp().run()
