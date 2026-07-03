import os
import webbrowser

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.metrics import dp

def ordner(icon=None, **unterordner_oder_sites):
    return {"type": "folder", "icon": icon, "items": unterordner_oder_sites}


def sites(*eintraege, icon=None):
    return {"type": "sites", "icon": icon, "items": list(eintraege)}


DATA = ordner(
    **{
        "Filme & Serien": ordner(
            icon="images/imagefilme.png",
            **{
                "Animes": sites(
                    ("aniworld", "images/aniworld.png", "https://aniworld.to/"),
                    icon="images/animeord.png",
                ),
                "Filme Deutsch": sites(
                    ("hdfilme", "images/imagehd.png", "https://hdfilme.my/"),
                    ("Megakino", "images/imagemega.png", "https://megakino9.com/"),
                    ("Topstreamfilme", "images/imagetopstream.png", "https://www.topstreamfilm.live/"),
                    icon="images/filmd.png",
                
                ),
                "Serien": sites(
                    ("Serienstream", "images/ser.png", "http://186.2.175.5/"),
                    ("Serienstream2", "images/ser.png", "https://s.to/"),
                    icon="images/serd.png",
                
                ),
                "Filme Englisch": sites(
                    ("Popcornmovie", "images/imagepop.png", "https://popcornmovies.io/trending"),
                    ("Streamx", "images/imagestreamx.png", "https://streamex.sh/"),
                    ("MovieBox", "images/imagemoviebox.png", "https://moviebox.ph/"),
                    ("MovieNova","images/imagemovienova.png", "https://movienova.sc/"),
                    icon="images/moveord.png",
                ),
                "K-Drama": sites(
                    ("kissasian", "images/imageskissasian.png", "https://wwv19.kissasian.com.lv/"),
                    ("kisskh", "images/imageskiss.png", "https://kisskh.do/"),
                    ("Dramacool", "images/drama.png", "https://myasiantvy.top/"),
                    ("Asiaflix", "images/imagesasia.png", "https://asiaflix.net/home"),
                    ("Drama Day", "images/imagesday.png", "https://dramaday.me/?__cf_chl_f_tk=U8jmRdHxq5GkuyB9oU3UIr7ap_qTtpdq5zoI5cF7tzw-1783101419-1.0.1.1-ZWWVUQyPfVV47ty4wqCeGuEgTvTCSb.QlmxaYsKhQIg"),
                    ("OneTouchTV", "images/imagetouch.png", "https://onetouchtv.xyz/"),
                    ("MKVDrama", "images/imagemkv.png", "https://mkvdrama.net/"),
                    icon="images/dramaord.png",
                ),
            },
        ),
        "KI": ordner(
            icon="images/aid.png",
            **{
                "Chatbots": sites(
                    ("ChatGPT", "images/chat.png", "https://chat.openai.com/"),
                    ("Claude", "images/claudp.png", "https://claude.ai/"),
                    ("Gemini", "images/gem.png", "https://gemini.google.com/"),
                    ("Grok", "images/grok2.png", "https://grok.com/"),
                    ("Copilot", "images/cop.png", "https://copilot.microsoft.com/"),
                    ("Deepseek", "images/Deepseek.png", "https://www.deepseek.com/"),
                    ("Sider", "images/Sider.png", "https://sider.ai/de?landing"),
                    ("Mistral", "images/Mistral.png", "https://chat.mistral.ai/chat"),
                    ("Perplexity", "images/perp.png", "https://www.perplexity.ai/"),
                ),
                "Videos": sites(
                    ("Runway", "images/Runaway.png", "https://runwayml.com/"),
                    ("Synthesia", "images/synthesia.png", "https://www.synthesia.io/de"),
                    ("Vizard", "images/vizard.png", "https://vizard.ai/workspace"),
                    ("Sora", "images/sora.png", "https://sora.chatgpt.com/login?next=%2Fexplore%2Fvideos"),
                ),
                "Images": sites(
                    ("Midjourney", "images/midjourney.png", "https://www.midjourney.com/"),
                    ("Deepai", "images/deep.png", "https://deepai.org/machine-learning-model/text2img"),
                ),
                "Coding": sites(
                    ("Cursor", "images/Cursor.png", "https://cursor.sh/"),
                    ("Bubble", "images/bub.png", "https://bubble.io/"),
                    ("Bolt", "images/bolt.png", "https://bolt.new/"),
                    ("Emergent", "images/emerg.png", "https://app.emergent.sh/landing/"),
                    ("Lovable", "images/Lovable.png", "https://lovable.dev/login?redirect=%2Fdashboard"),
               
                ),
                "Presentation": sites(
                    ("Gamma", "images/Gamma.png", "https://gamma.app/"),
                ),
                "Music": sites(
                    ("Suno", "images/suno.png", "https://suno.com/"),
                    ("Mixaudio", "images/mix.png", "https://mix.audio/"),
                    ("Topmedia", "images/topmedia.png", "https://www.topmediai.com/app/ai-music/"),
                    ("Music Tool", "images/voc.png", "https://vocalremover.org/key-bpm-finder"),
                    ("Musicfy", "images/musicfy.png", "https://create.musicfy.lol/create/voice"),
                    ("MusicGPT", "images/muskgpt.png", "https://musicgpt.com/"),
                    ("Treblo", "images/treb.png", "https://treblo.com/"),
                ),
                "RVC": sites(
                    ("Voiceai", "images/voce.png", "https://voice.ai/tools/reverb-remover"),
                    ("Elevenlabs", "images/el.png", "https://elevenlabs.io/app/sign-in?redirect=%2Fapp%2Fspeech-synthesis%2Fspeech-to-speech"),
                ),
                "Multiple Models": sites(
                    ("Poe", "images/poe.png", "https://poe.com/"),
                    ("Arena", "images/arena.png", "https://arena.ai/"),
                    ("Dubao", "images/duabo.png", "https://www.doubao.com/security/doubao-region-ban?source=1"),
                    ("Aixploria", "images/aix.png", "https://www.aixploria.com/en/"),
                    ("Arcade", "images/arcade.png", "https://arcade.la/"),

                ),
                "Games": sites(
                    ("Tesana", "images/tesa.png", "https://tesana.ai/en"),
                    ("Codewisp", "images/codewisp.png", "https://codewisp.ai/"),
                 

                ),
            },
        ),
    }
)


def kurzname(url):
    return url.split("//")[1].split("/")[0].replace("www.", "")


class KlickbaresBild(ButtonBehavior, Image):
    def __init__(self, on_click=None, **kwargs):
        super().__init__(**kwargs)
        self.on_click = on_click
        self.allow_stretch = True
        self.keep_ratio = True

    def on_press(self):
        if self.on_click:
            self.on_click()


def mach_icon_widget(icon_path, on_click, fallback_text):
    if icon_path and os.path.exists(icon_path):
        return KlickbaresBild(source=icon_path, on_click=on_click)
    else:
        btn = Button(text=fallback_text, background_color=(0.2, 0.2, 0.2, 1))
        btn.bind(on_press=lambda *_: on_click())
        return btn


class BrowserScreen(Screen):
    def __init__(self, root_data, **kwargs):
        super().__init__(**kwargs)
        self.stack = [("Noflix", root_data)]

        self.root_layout = BoxLayout(orientation="vertical")
        self.add_widget(self.root_layout)
        self.render()

    def push(self, name, node):
        self.stack.append((name, node))
        self.manager.transition = SlideTransition(direction="left")
        self.render()

    def pop(self, *args):
        if len(self.stack) > 1:
            self.stack.pop()
            self.manager.transition = SlideTransition(direction="right")
            self.render()

    def render(self):
        self.root_layout.clear_widgets()
        title, node = self.stack[-1]

        header = BoxLayout(orientation="horizontal", size_hint_y=None, height=dp(50))
        if len(self.stack) > 1:
            back_btn = Button(text="< Zurueck", size_hint_x=None, width=dp(120))
            back_btn.bind(on_press=self.pop)
            header.add_widget(back_btn)
        header.add_widget(Label(text=title, font_size="18sp"))
        self.root_layout.add_widget(header)

        scrollview = ScrollView(do_scroll_x=False, do_scroll_y=True)
        grid = GridLayout(cols=2, spacing=25, padding=25, size_hint_y=None)
        grid.bind(minimum_height=grid.setter("height"))

        if node["type"] == "folder":
            for name, child in node["items"].items():
                grid.add_widget(self._folder_box(name, child))
        else:
            for display_name, icon, url in node["items"]:
                grid.add_widget(self._site_box(display_name, icon, url))

        scrollview.add_widget(grid)
        self.root_layout.add_widget(scrollview)

    def _folder_box(self, name, child_node):
        box = BoxLayout(orientation="vertical", size_hint_y=None, height=dp(180))
        icon_widget = mach_icon_widget(
            child_node.get("icon"),
            on_click=lambda: self.push(name, child_node),
            fallback_text="📁",
        )
        box.add_widget(icon_widget)
        label_btn = Button(
            text=name, size_hint_y=None, height=dp(35),
            background_color=(0.1, 0.5, 0.9, 1),
        )
        label_btn.bind(on_press=lambda *_: self.push(name, child_node))
        box.add_widget(label_btn)
        return box

    def _site_box(self, display_name, icon, url):
        box = BoxLayout(orientation="vertical", size_hint_y=None, height=dp(180))
        icon_widget = mach_icon_widget(
            icon,
            on_click=lambda: webbrowser.open(url),
            fallback_text=display_name,
        )
        box.add_widget(icon_widget)
        text_btn = Button(
            text=display_name or kurzname(url), size_hint_y=None, height=dp(35),
            background_color=(0.1, 0.5, 0.9, 1),
        )
        text_btn.bind(on_press=lambda *_: webbrowser.open(url))
        box.add_widget(text_btn)
        return box


class MyApp(App):
    def build(self):
        self.title = "Noflix"
        sm = ScreenManager()
        sm.add_widget(BrowserScreen(DATA, name="browser"))
        return sm


if __name__ == "__main__":
    MyApp().run()
