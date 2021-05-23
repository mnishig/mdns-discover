"""

"""
import pyclip
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.treeview import TreeView, TreeViewLabel, TreeViewNode
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

from ServiceDiscover import ServiceDiscover

# TreeViewLabel is delivered TreeViewNode and TextLabel
class MdnsNode(TreeViewLabel):
    def on_touch_down(self, touch):
        print('node touched:', self.text)

        if touch.button == 'right':
            pyclip.copy(self.text)

class MdnsTree(TreeView):
    def __init__(self, **kwargs):
        self.hide_root = True
        super(MdnsTree, self).__init__(**kwargs)
        # self.add_node(TreeViewLabel(text ='シンカリオン E1 とき'))

    def update(self, items) -> None:
        self.depopulate()

        for item in items:
            # service_node = self.add_node(TreeViewLabel(text='name: '+item['name']))
            # self.add_node(TreeViewLabel(text='server: '+item['server']), service_node)
            # self.add_node(TreeViewLabel(text='type: '+item['type']), service_node)
            # for addr in item['addresses']:
            #     self.add_node(TreeViewLabel(text='address: '+addr), service_node)
            # self.add_node(TreeViewLabel(text='port: '+str(item['port'])), service_node)
            service_node = self.add_node(MdnsNode(text='name: '+item['name']))
            self.add_node(MdnsNode(text='server: '+item['server']), service_node)
            self.add_node(MdnsNode(text='type: '+item['type']), service_node)
            for addr in item['addresses']:
                self.add_node(MdnsNode(text='address: '+addr), service_node)
            self.add_node(MdnsNode(text='port: '+str(item['port'])), service_node)

    def depopulate(self) -> None:
        iterator = self.iterate_all_nodes()
        try:
            while True:
                node = iterator.__next__()
                self.remove_node(node)
        except StopIteration:
            return

    def on_touch_down(self, touch):
        print('btn:', touch.button)
        if touch.button == 'right':
            pass

        r = self.collide_point(*touch.pos)
        print(r)
        return super(MdnsTree, self).on_touch_down(touch)


class MainView(BoxLayout):
    tv = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.services = []
        self.update()

    def update(self) -> None:
        sd = ServiceDiscover()
        sd.browse()
        self.services = sd.services
        self.tv.update(self.services)


class BaseApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # for japanese font to display
        resource_add_path('./font')
        LabelBase.register(DEFAULT_FONT, 'ipaexg.ttf')


class MdnsDiscoverApp(BaseApp):
    # tv = ObjectProperty(None)

    def build(self) -> None:
        return MainView()


def init() -> None:
    MdnsDiscoverApp().run()


if __name__ == "__main__":
    init()
