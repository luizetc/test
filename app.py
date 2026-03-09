import streamlit as st
import time

# 1. EL ARCHIVADOR (Nuestra base de datos de preguntas)
preguntas = [
    {
        "texto": "¿Qué es un fármaco?",
        "opciones": [
            "Una sustancia que solo causa efectos adversos",
            "Una sustancia utilizada para prevenir, diagnosticar o tratar enfermedades",
            "Un alimento enriquecido",
            "Una vitamina"
        ],
        "correcta": "Una sustancia utilizada para prevenir, diagnosticar o tratar enfermedades"
    },
    {
        "texto": "¿Qué diferencia hay entre un fármaco genérico y uno de marca?",
        "opciones": [
            "El genérico es menos seguro",
            "El de marca tiene ingredientes activos diferentes",
            "El genérico tiene el mismo principio activo pero cuesta menos",
            "El de marca no necesita receta"
        ],
        "correcta": "El genérico tiene el mismo principio activo pero cuesta menos"
    },
    {
        "texto": "¿Qué es la farmacocinética?",
        "opciones": [
            "El estudio de cómo actúan los fármacos sobre el cuerpo",
            "El estudio de los efectos secundarios",
            "El estudio de cómo el cuerpo absorbe, distribuye, metaboliza y elimina un fármaco",
            "La preparación de medicamentos"
        ],
        "correcta": "El estudio de cómo el cuerpo absorbe, distribuye, metaboliza y elimina un fármaco"
    },
    {
        "texto": "¿Qué significa 'vía de administración' de un medicamento?",
        "opciones": [
            "El precio del medicamento",
            "El lugar del cuerpo donde actúa",
            "La forma en que el medicamento entra en el cuerpo",
            "El tiempo que tarda en hacer efecto"
        ],
        "correcta": "La forma en que el medicamento entra en el cuerpo"
    },
    {
        "texto": "¿Cuál es la diferencia entre un efecto terapéutico y un efecto secundario?",
        "opciones": [
            "No existe diferencia",
            "El efecto terapéutico es el deseado; el secundario es no deseado",
            "El secundario siempre es peligroso",
            "El terapéutico solo ocurre con dosis altas"
        ],
        "correcta": "El efecto terapéutico es el deseado; el secundario es no deseado"
    },
    {
        "texto": "¿Qué es una dosis?",
        "opciones": [
            "La marca del medicamento",
            "La cantidad de medicamento que debe administrarse",
            "El precio de un tratamiento",
            "El número de efectos adversos"
        ],
        "correcta": "La cantidad de medicamento que debe administrarse"
    },
    {
        "texto": "¿Qué órgano metaboliza principalmente los fármacos?",
        "opciones": [
            "El riñón",
            "El hígado",
            "El pulmón",
            "El estómago"
        ],
        "correcta": "El hígado"
    },
    {
        "texto": "¿Qué significa que un medicamento sea 'de venta libre'?",
        "opciones": [
            "Requiere receta",
            "Solo puede comprarlo personal médico",
            "Puede comprarse sin receta",
            "Es ilegal"
        ],
        "correcta": "Puede comprarse sin receta"
    },
    {
        "texto": "¿Qué es una contraindicación?",
        "opciones": [
            "Una dosis recomendada",
            "Situación en la que el medicamento no debe usarse",
            "Un efecto beneficioso",
            "Un sinónimo de receta"
        ],
        "correcta": "Situación en la que el medicamento no debe usarse"
    }
]

st.title("🎓 Mi Primer Examen Interactivo")
st.write("Responde a las preguntas y pulsa el botón al final para saber tu nota.")

# 2. FORMULARIO
with st.form("quiz_form"):
    respuestas_usuario = []
    for pregunta in preguntas:
        st.subheader(pregunta["texto"])
        eleccion = st.radio("Elige una opción:", pregunta["opciones"], key=pregunta["texto"])
        respuestas_usuario.append(eleccion)
        st.write("---")

    boton_enviar = st.form_submit_button("Entregar Examen")

# 3. CORRECCIÓN
if boton_enviar:
    puntos = 0
    total = len(preguntas)

    # Para el informe en Markdown
    preguntas_correctas = []
    preguntas_incorrectas = []

    for i in range(total):
        if respuestas_usuario[i] == preguntas[i]["correcta"]:
            puntos += 1
            preguntas_correctas.append(preguntas[i]["texto"])
        else:
            puntos -= 1
            preguntas_incorrectas.append(
                f"**{preguntas[i]['texto']}**  \n"
                f"❌ Tu respuesta: *{respuestas_usuario[i]}*  \n"
                f"✅ Correcta: **{preguntas[i]['correcta']}**"
            )

    # Nota (redondeada)
    nota = round((puntos / total) * 10, 2)
    
    st.divider()
    st.header(f"Resultado final: {nota} / 10")

    # FEEDBACK POR TRAMOS
    if nota < 2:
        st.error("Muy insuficiente.")
    elif nota < 5:
        st.error("Insuficiente.")
    elif nota < 6:
        st.warning("Suficiente.")
    elif nota < 7:
        with st.spinner("👏 Bien... ¡Has aprobado!"):
            time.sleep(1)
        st.success("Bien.")
    elif nota < 9:
        with st.spinner("🚀 Notable... ¡Buen trabajo!"):
            time.sleep(1)
        st.success("Notable.")
    elif nota < 10:
        with st.spinner("🌟 ¡Sobresaliente!"):
            time.sleep(1)
        st.success("Sobresaliente.")
    else:
        with st.spinner("🏆 ¡Excelente!"):
            time.sleep(1)
        st.success("Excelente")

    # TAB CON INFORME MARKDOWN
    tab_informe = st.tabs(["📄 Informe del Examen"])[0]

    with tab_informe:
        st.markdown("# 📊 Informe del Examen")
        st.markdown("## ✅ Preguntas Correctas")
        if preguntas_correctas:
            for p in preguntas_correctas:
                st.markdown(f"- **{p}**")
        else:
            st.markdown("- No acertaste ninguna 😢")

        st.markdown("---")
        st.markdown("## ❌ Preguntas Incorrectas")
        if preguntas_incorrectas:
            for p in preguntas_incorrectas:
                st.markdown(f"- {p}")
        else:
            st.markdown("- ¡No fallaste ninguna! 🎉")
