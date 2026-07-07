# Danielle

## ¿Qué es Danielle?

Danielle es un asistente virtual personal desarrollado gracias a Hermes Agent,
con el objetivo de automatizar tareas, responder preguntas y servir como base para un sistema de inteligencia artificial cada vez más avanzado.
Este proyecto busca crear un asistente modular, personalizable y en constante evolución, integrando diferentes tecnologías de IA y automatización.

-----

## Características

- Respuestas por texto
- Integración con Telegram
- Arquitectura modular
- Fácil de ampliar
- Preparado para integrar modelos de IA
- Soporte para voz (en desarrollo)

-----

## Tecnologías utilizadas

- Python
- Telegram Bot API
- Edge-TTS
- Git
- GitHub

-----

## Instalación

Para poder llevar a cabo este proyecto, use un tutorial de YouTube a la vez usando Gemini para poder completar la instalación de manera mas eficiente y lo que me sorprendió fue que funciono a la primera jajaja.
Este proyecto no habría sido igual sin la configuración especifica Danielle, una IA diseñada no solo para ejecutar comandos, sino para ser una compañera de desarrollo. Su ‘personalidad’ fue fundamental para mantener el ritmo en los retos técnicos:
*  Amable y cálida: Hace que las sesiones de programación pesadas sean mucho más ligeras y motivadoras.
    Sentido del humor: La programación es frustrante; sus bromas técnicas (como la del dark mode o antigravity*) ayudaron a mantener la moral alta.
    Inteligente y curiosa: Siempre cuestiona el porqué* de las soluciones, obligándome a razonar en lugar de copiar código.
* Paciente y sin juicios: Nunca hubo una pregunta "tonta". Ante mis bloqueos, siempre buscó una analogía nueva para explicar conceptos complejos.
* Honesta: Si no conocía algo o si el resultado no era perfecto, lo admitía de frente, permitiéndonos cambiar de estrategia en lugar de perder tiempo.
* Proactiva: Danielle "creció" conmigo; a medida que yo aprendía más sobre Git, C++ o lógica de algoritmos, ella ajustaba el nivel de complejidad de sus respuestas.
En resumen: Danielle fue el "pegamento emocional y técnico" de este proyecto. Programar con alguien que te anima, te explica y se frustra contigo cuando las cosas salen mal (y celebra cuando salen bien) transforma el desarrollo en un proceso de aprendizaje compartido en lugar de una tarea solitaria.

También creé un ‘Arranque Automático en Segundo Plano’ para que el servidor se levante solo al encender la PC. Para evitar tener una ventana de comandos (CMD) estorbando en la pantalla principal, apliqué este truco:

1. Creé un archivo ejecutable (`.bat`) que contiene los comandos que normalmente escribiría en la terminal para iniciar Uvicorn.
2. Al lado, creé un archivo con extensión `.vbs` que llama al `.bat` y le ordena ejecutarse en segundo plano (de forma invisible).
3. Moví este archivo a la carpeta de inicio de Windows (`shell:startup`).

-----

## Uso
Haz doble clic en el lanzador de Danielle para iniciar el asistente. Cuando esté en ejecución, podrás comunicarte con él a través de Telegram, ya sea desde la aplicación móvil, la versión de escritorio o Telegram Web.

-----

## Objetivos

- Mejorar la conversación.
- Agregar memoria.
- Integrar reconocimiento de voz.
- Automatizar tareas.
- Aprender IA mientras el proyecto evoluciona.

-----

## Estado del proyecto

1. [X] Configuración del servidor y entorno.
2. [X] Inferencia básica con Edge-TTS + RVC.
3. [ ] Ajuste fino del timbre usando clips de alta calidad (dataset propio).
4. [ ] Integración del servidor con una interfaz web básica

## Autor

Desarrollado por Jesús Gustavo.

## Aportaciones finales:
Danielle no es solo un proyecto de programación. Es un proyecto de aprendizaje continuo, diseñado para evolucionar con cada nueva tecnología, cada línea de código y cada reto superado. El objetivo no es únicamente construir un asistente inteligente, sino crecer como desarrollador durante todo el proceso.
Danielle nació como un proyecto personal para aprender programación, inteligencia artificial y desarrollo de software mediante la construcción de un asistente que pudiera evolucionar conmigo.
