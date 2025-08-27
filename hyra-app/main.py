from kivy.lang import Builder
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.image import Image as CoreImage
import qrcode
from io import BytesIO
from kivy.clock import Clock
Builder.load_file("hyra.kv")
class RootWidget(BoxLayout):
    fixed_costs = {
        "Larm": 486,
        "Hemförsäkring": 152
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Schedule adding fixed cost labels after KV loading
        Clock.schedule_once(self.add_fixed_costs)

    def add_fixed_costs(self, dt):
        container = self.ids.fixed_costs_container
        for name, cost in self.fixed_costs.items():
            lbl = Label(text=f"{name}: {cost} kr", size_hint_y=None)
            lbl.height = lbl.texture_size[1] + 10
            container.add_widget(lbl)

    def calculate_total(self):
        try:
            brf = float(self.ids.brf_input.text)
            interest = float(self.ids.interest_input.text)
            fixed_total = sum(self.fixed_costs.values())
            total = brf + interest + fixed_total
            self.total = total  # store total for QR generation
            self.ids.result_label.text = (
                f"Total: {total:.2f} kr\n"
                f"[color=ff0000]kr/per gubbe: {total/2:.2f} kr[/color]"
            )
        except ValueError:
            self.ids.result_label.text = "Fyll i alla fält med siffror"

    def generate_qr(self):
        try:
            per_person = self.total / 2
        except AttributeError:
            self.ids.result_label.text = "Beräkna totalen först!"
            return

        swish_number = "0703261606"  # replace with your Swish number
        ##qr_data = f"C1X:PAY:{swish_number};amount={per_person:.2f};;"
        qr_data = f"https://swish.app/pay?amount={per_person:.2f}&recipient={swish_number}"


        # Generate QR code image
        qr = qrcode.QRCode(box_size=10, border=2)
        qr.add_data(qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Convert PIL image to texture for Kivy Image widget
        buf = BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        core_image = CoreImage(buf, ext='png')

        # Set the image source to the widget
        self.ids.qr_image.texture = core_image.texture

class SwishApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    SwishApp().run()