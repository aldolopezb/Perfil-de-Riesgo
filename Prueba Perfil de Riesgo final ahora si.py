import tkinter as tk
from PIL import Image, ImageTk


class PerfilRiesgo:
    def __init__(self):
        # Preguntas, opciones y puntajes específicos
        self.questions = [
            {
                "text": "Planeo comenzar a retirar dinero de mis inversiones en:",
                "options": ["Menos de 3 años", "De 3 a 5 años", "De 6 a 10 años", "11 años o más"],
                "scores": [1, 3, 7, 10]
            },
            {
                "text": "Una vez que comience a retirar dinero de mis inversiones, planeo gastar todo el dinero en:",
                "options": ["Menos de 2 años", "De 2 a 5 años", "De 6 a 10 años", "11 años o más"],
                "scores": [0, 1, 4, 8]
            },
            {
                "text": "Describiría mi conocimiento de inversiones como:",
                "options": ["Nulo", "Limitado", "Bueno", "Amplio"],
                "scores": [0, 2, 4, 6]
            },
            {
                "text": "¿Qué cantidad de riesgo financiero estás dispuesto a asumir cuando inviertes?",
                "options": [
                    "Riesgo bajo, buscando rendimiento menor al promedio",
                    "Riesgo moderado, buscando rendimiento promedio",
                    "Riesgo alto, buscando rendimiento superior al promedio"
                ],
                "scores": [0, 4, 8]
            },
            {
                "text": "Selecciona las inversiones que actualmente posees o has tenido:",
                "options": [
                    "Ninguna",
                    "Bonos y/o fondos de bonos",
                    "Acciones y/o fondos de acciones",
                    "Activos y/o fondos fuera de EEUU"
                ],
                "scores": [0, 3, 6, 8]
            },
            {
                "text": "Considera el siguiente escenario: Imagina que en los últimos 3 meses, el mercado de valores en su conjunto perdió el 25% de su valor. Una inversión en acciones individuales que posees también perdió el 25% de su valor. ¿Qué harías?",
                "options": [
                    "Vender todas mis acciones",
                    "Vender algunas de mis acciones",
                    "No haría nada",
                    "Comprar más acciones"
                ],
                "scores": [0, 2, 5, 8]
            },
            {
                "text": "Revisa la siguiente tabla: Proyecciones más probables de mejores y peores rendimientos anuales de 5 planes de inversión hipotéticos. ¿Cuál rango de resultados posibles es más aceptable para ti?",
                "options": ["Plan A", "Plan B", "Plan C", "Plan D", "Plan E"],
                "scores": [0, 3, 6, 8, 10]
            }
        ]

        # Tabla de perfiles
        self.perfil_tabla = [
            {"rango_a": (3, 4), "rango_b": (0, 18), "perfil": "Conservador"},
            {"rango_a": (3, 4), "rango_b": (19, 31), "perfil": "Moderadamente Conservador"},
            {"rango_a": (3, 4), "rango_b": (32, 40), "perfil": "Moderado"},
            #-----------------------------------------------------------------------------------
            {"rango_a": (5, 5), "rango_b": (0, 15), "perfil": "Conservador"},
            {"rango_a": (5, 5), "rango_b": (16, 24), "perfil": "Moderadamente Conservador"},
            {"rango_a": (5, 5), "rango_b": (25, 35), "perfil": "Moderado"},
            {"rango_a": (5, 5), "rango_b": (36, 40), "perfil": "Moderadamente Agresivo"},
            #-----------------------------------------------------------------------------------
            {"rango_a": (7, 9), "rango_b": (0, 12), "perfil": "Conservador"},
            {"rango_a": (7, 9), "rango_b": (13, 20), "perfil": "Moderadamente Conservador"},
            {"rango_a": (7, 9), "rango_b": (21, 28), "perfil": "Moderado"},
            {"rango_a": (7, 9), "rango_b": (29, 37), "perfil": "Moderadamente Agresivo"},
            {"rango_a": (7, 9), "rango_b": (38, 40), "perfil": "Agresivo"},
            #-----------------------------------------------------------------------------------
            {"rango_a": (10, 12), "rango_b": (0, 11), "perfil": "Conservador"},
            {"rango_a": (10, 12), "rango_b": (12, 18), "perfil": "Moderadamente Conservador"},
            {"rango_a": (10, 12), "rango_b": (19, 26), "perfil": "Moderado"},
            {"rango_a": (10, 12), "rango_b": (27, 34), "perfil": "Moderadamente Agresivo"},
            {"rango_a": (10, 12), "rango_b": (35, 40), "perfil": "Agresivo"},
            #-----------------------------------------------------------------------------------
            {"rango_a": (14, 18), "rango_b": (0, 10), "perfil": "Conservador"},
            {"rango_a": (14, 18), "rango_b": (11, 17), "perfil": "Moderadamente Conservador"},
            {"rango_a": (14, 18), "rango_b": (18, 24), "perfil": "Moderado"},
            {"rango_a": (14, 18), "rango_b": (25, 31), "perfil": "Moderadamente Agresivo"},
            {"rango_a": (14, 18), "rango_b": (32, 40), "perfil": "Agresivo"},
        ]

        self.scores = [0] * len(self.questions)
        self.current_question_index = 0
        self.seccion_a_score = 0
        self.seccion_b_score = 0

        # Configuración de la ventana principal
        self.root = tk.Tk()
        self.root.title("Evaluación de Perfil de Riesgo de Inversión")
        self.root.geometry("700x550")

        self.font_large = ("Arial", 16, "bold")
        self.font_medium = ("Arial", 14)

        self.question_label = tk.Label(self.root, text="", wraplength=600, font=self.font_large)
        self.question_label.pack(pady=20)

        self.options_var = tk.StringVar(value="")
        self.options_frame = tk.Frame(self.root)
        self.options_frame.pack(pady=10)

        self.image_label = None
        self.next_button = tk.Button(self.root, text="Siguiente", command=self.siguiente_pregunta, font=self.font_medium)
        self.next_button.pack(pady=20)

        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        for widget in self.options_frame.winfo_children():
            widget.destroy()

        question = self.questions[self.current_question_index]
        self.question_label.config(text=f"Pregunta {self.current_question_index + 1}: {question['text']}")

        # Mostrar imagen para la pregunta 7
        if self.current_question_index == 6:  # Índice 6 corresponde a la pregunta 7
            try:
                img = Image.open("Tabla_de_Rendimientos.png")
                img = img.resize((800, 450), Image.LANCZOS)
                img_tk = ImageTk.PhotoImage(img)

                if not self.image_label:
                    self.image_label = tk.Label(self.root, image=img_tk)
                    self.image_label.image = img_tk
                    self.image_label.pack(pady=10)
                else:
                    self.image_label.config(image=img_tk)
                    self.image_label.image = img_tk

                self.root.geometry("1000x1000")
            except FileNotFoundError:
                if not self.image_label:
                    self.image_label = tk.Label(self.root, text="Imagen no encontrada.", font=self.font_medium)
                    self.image_label.pack(pady=10)
                else:
                    self.image_label.config(text="Imagen no encontrada.")
        else:
            if self.image_label:
                self.image_label.pack_forget()
            self.root.geometry("700x550")

        for idx, option in enumerate(question["options"], start=1):
            tk.Radiobutton(
                self.options_frame,
                text=option,
                variable=self.options_var,
                value=str(idx),
                font=self.font_medium,
                anchor="w",
                wraplength=600
            ).pack(fill="x", pady=5)

    def siguiente_pregunta(self):
        if not self.options_var.get():
            tk.messagebox.showwarning("Advertencia", "Por favor selecciona una opción antes de continuar.")
            return

        question = self.questions[self.current_question_index]
        selected_option = int(self.options_var.get()) - 1
        self.scores[self.current_question_index] = question["scores"][selected_option]

        if self.current_question_index == 1:
            self.seccion_a_score = sum(self.scores[:2])
            if self.seccion_a_score < 3:
                self.mostrar_perfil_conservador()
                return
            self.mostrar_puntaje_seccion("Sección A", self.seccion_a_score)
        elif self.current_question_index == 6:
            self.seccion_b_score = sum(self.scores[2:])
            self.mostrar_puntaje_seccion("Sección B", self.seccion_b_score)

        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.mostrar_pregunta()
        else:
            self.mostrar_resultado()

    def mostrar_puntaje_seccion(self, seccion, puntaje):
        seccion_window = tk.Toplevel(self.root)
        seccion_window.title(f"Puntaje {seccion}")
        seccion_window.geometry("400x200")
        seccion_label = tk.Label(
            seccion_window,
            text=f"Puntaje total de {seccion}: {puntaje}",
            font=self.font_large,
            wraplength=300
        )
        seccion_label.pack(pady=50)

    def mostrar_perfil_conservador(self):
        resultado_window = tk.Toplevel(self.root)
        resultado_window.title("Resultado Final")
        resultado_window.geometry("600x400")
        result_text = "Una puntuación menor a 3 indica un horizonte de inversión muy corto. Para un Horizonte Temporal tan breve, se sugiere un portafolio o cartera relativamente baja en riesgo, compuesto por 40% en bonos o fondos de bonos a corto plazo (con un vencimiento promedio de cinco años o menos) y 60% en inversiones en efectivo, ya que las inversiones en acciones pueden ser significativamente más volátiles a corto plazo. "
        result_label = tk.Label(resultado_window, text=result_text, wraplength=500, font=self.font_large)
        result_label.pack(pady=20)

    def mostrar_resultado(self):
        resultado_window = tk.Toplevel(self.root)
        resultado_window.title("Resultado Final")
        resultado_window.geometry("800x700")

        result_text = (
            f"Puntaje Horizonte Temporal (Sección A): {self.seccion_a_score}\n"
            f"Puntaje Tolerancia al Riesgo (Sección B): {self.seccion_b_score}\n"
        )
        result_label = tk.Label(resultado_window, text=result_text, wraplength=600, font=self.font_large)
        result_label.pack(pady=20)

        perfil = self.determinar_perfil()
        perfil_label = tk.Label(resultado_window, text=f"Tu perfil de riesgo es: {perfil}", font=self.font_large)
        perfil_label.pack(pady=10)

        self.mostrar_imagen_por_perfil(perfil)
        self.mostrar_imagen_activos(perfil)

        try:
            img = Image.open("Cuadro_Perfil.png")
            img = img.resize((750, 500), Image.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)
            img_label = tk.Label(resultado_window, image=img_tk)
            img_label.image = img_tk
            img_label.pack(pady=10)
        except FileNotFoundError:
            tk.Label(resultado_window, text="Imagen del cuadro no encontrada.", font=self.font_medium).pack(pady=10)

    def mostrar_imagen_por_perfil(self, perfil):
        # Diccionario de imágenes por perfil
        imagenes_perfil = {
            "Conservador": "Conservador.png",
            "Moderadamente Conservador": "Moderadamente_Conservador.png",
            "Moderado": "Moderado.png",
            "Moderadamente Agresivo": "Moderadamente_Agresivo.png",
            "Agresivo": "Agresivo.png"
        }

        # Texto repetido para todos los perfiles
        texto_repetido = (
            "Este portafolio muestra como el inverionista puede asignar su dinero entre inversiones en diversas categorías. "

            "Ten en cuenta que estos ejemplos no se basan en pronósticos de mercado, sino que simplemente reflejan un enfoque establecido para invertir, que consiste en distribuir el dinero entre diferentes categorías de inversión."
        )

        imagen_window = tk.Toplevel(self.root)
        imagen_window.title(f"Imagen para el perfil: {perfil}")
        imagen_window.geometry("800x500")

        try:
            # Cargar la imagen
            img_path = imagenes_perfil.get(perfil, "default.png")
            img = Image.open(img_path)
            img = img.resize((750, 300), Image.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)

            # Mostrar la imagen
            img_label = tk.Label(imagen_window, image=img_tk)
            img_label.image = img_tk
            img_label.pack(pady=20)

            # Mostrar el texto repetido
            texto_label = tk.Label(
                imagen_window,
                text=texto_repetido,
                wraplength=750,
                font=self.font_medium,
                justify="center"
            )
            texto_label.pack(pady=10)

        except FileNotFoundError:
            tk.Label(imagen_window, text="Imagen no encontrada.", font=self.font_medium).pack(pady=20)



    def mostrar_imagen_activos(self, perfil):
        # Diccionario de imágenes por perfil
        imagenes_activos = {
            "Conservador": "Activos.png",
            "Moderadamente Conservador": "Activos.png",
            "Moderado": "Activos.png",
            "Moderadamente Agresivo": "Activos.png",
            "Agresivo": "Activos.png"
        }


        imagen_window = tk.Toplevel(self.root)
        imagen_window.title(f"Tipos de Activos")
        imagen_window.geometry("800x850")

        try:
            img_path = imagenes_activos.get(perfil, "default.png")
            img = Image.open(img_path)
            img = img.resize((750, 700), Image.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)

            img_label = tk.Label(imagen_window, image=img_tk)
            img_label.image = img_tk
            img_label.pack(pady=20)
        except FileNotFoundError:
            tk.Label(imagen_window, text="Imagen no encontrada.", font=self.font_medium).pack(pady=20)


    def determinar_perfil(self):
        for regla in self.perfil_tabla:
            rango_a = regla["rango_a"]
            rango_b = regla["rango_b"]
            if rango_a[0] <= self.seccion_a_score <= rango_a[1] and rango_b[0] <= self.seccion_b_score <= rango_b[1]:
                return regla["perfil"]
        return "No definido"

    def iniciar(self):
        self.root.mainloop()


# Ejecutar el sistema
sistema = PerfilRiesgo()
sistema.iniciar()
