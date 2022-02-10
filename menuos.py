from kivy.lang import Builder
#from kivy.app import App
from kivymd.app import MDApp

from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty
from kivy.animation import Animation
from kivymd.uix.card import MDCard
from kivymd.uix.card import MDCardSwipe




KV = '''
#:import C kivy.utils.get_color_from_hex
<SwipeButton@Carousel>:
    text: ''
    size_hint_y: None
    #on_press: app.press(root.data_index)
    height: 48
    ignore_perpendicular_swipes: True
    data_index: 0
    min_move: 20 / self.width
    on__offset: app.update_index(root.data_index, self.index)
    canvas.before:
        Color:
            rgba: C('FFFFFF33')
        Rectangle:
            pos: self.pos
            size: self.size
        Line:
            rectangle: self.pos + self.size
    Button:
        text: 'delete ({}:{})'.format(root.text, root.data_index)
        on_press: app.delete(root.data_index)
    Label:
        text: root.text
        
    Button:
        text: 'archive'
        on_press: app.archive(root.data_index)
<MD3Card>:
    color: .2, .2, .2, .8
    MDIconButton:
        icon: "dots-vertical"
    
    MDLabel:
        
        text: root.text
<SwipeToDeleteItem>:
RecycleView:
    data: app.data
    #viewclass: 'SwipeToDeleteItem'
    #viewclass: 'MDCard'
    viewclass: 'SwipeToDeleteItem'
    do_scroll_x: False
    scroll_timeout: 100
    RecycleBoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: self.minimum_height
        default_size_hint: 1, None
'''
import create_cache
import libparse

create_cache.createcache('')
xxx=libparse.parse('','','')


print (xxx)
class ListApp(MDApp):
    data = ListProperty()

    def build(self):
        self.data = [{
            'data_index': i,
            'index': 1,
            'height': 48,
            'text': str(xxx[i][0])
            }
            for i in range(len(xxx))
        ]
        return Builder.load_string(KV)

    def update_index(self, data_index, index):
        print('update data index: {}: {}'.format(data_index, index))
        self.data[data_index]['index'] = index

    def delete(self, data_index):
        print("delete {}".format(data_index))
        self._remove(data_index)
    def press(self, data_index):
        print ('lol')

    def archive(self, data_index):
        print("archive {}".format(data_index))
        #self._remove(data_index)
        print (xxx[data_index][0])
        (xxx[data_index][0])='shitty'
        print (xxx[data_index][0])


    def _remove(self, data_index):
        self.data.pop(data_index)
        self.data = [{
            'data_index': i,
            'index': d['index'],
            'height': d['height'],
            'text': d['text']
            }
            for i, d in enumerate(self.data)
        ]


if __name__ == '__main__':
    ListApp().run()