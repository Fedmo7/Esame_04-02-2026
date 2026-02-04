import flet as ft

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model



    def take_ruoli(self):
        self.lista_ruoli = self._model.take_all_ruoli()
        self._view.popola_dropdown_ruolo(self.lista_ruoli)



    def handle_crea_grafo(self, e):


        ruolo_scelto=self._view.dd_ruolo.value

        if ruolo_scelto is None:
            self._view.show_alert("Errore: selezionare un ruolo.")
            return


        num_nodi,num_archi=self._model.build_graph(ruolo_scelto)
        self._view.list_risultato.controls.clear()
        self._view.list_risultato.controls.append(ft.Text(f'Nodi: {num_nodi}| Archi: {num_archi}'))

        self._view.update()


        self._view.btn_classifica.disabled = False





    def handle_classifica(self, e):



        nodes=list(self._model.dizionario_nodi.values())

        nodes.sort(reverse=True,key=lambda x: x.num_objects)

        for n in nodes:
            self._view.list_risultato.controls.append(ft.Text(f'{n.name} {n.num_objects}'))

        self._view.update()



