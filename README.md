# Simulacion Yahtzee — Metodo de Montecarlo

**Actividad Didactica 2-M1 | Asignatura: Simulacion**
**Institucion Universitaria Digital de Antioquia**

---

## Descripcion

Este proyecto implementa una **simulacion del juego Yahtzee** utilizando el **Metodo de Montecarlo**. Dos agentes IA se enfrentan en partidas automaticas de 13 rondas; al repetir el experimento cientos de veces se estiman empiricamente probabilidades que serian muy dificiles de calcular de forma analitica.

El flujo de ejecucion tiene dos fases:

1. **Partida de demostracion** — una sola partida con logs detallados por consola para visualizar el desarrollo del juego.
2. **Simulacion Montecarlo** — 500 partidas silenciosas que generan estadisticas agregadas: victorias, empates y puntajes promedio.

---

## Reglas del Yahtzee implementadas

El juego usa **5 dados** y se juega en **13 rondas**. En cada turno el jugador lanza los dados hasta **3 veces**, guardando los que quiera entre lanzamientos. Al final asigna la mano a una de las 13 categorias (cada categoria se usa una sola vez).

| Seccion | Categoria | Puntuacion |
|---------|-----------|------------|
| Superior | Unos — Seises | Suma de los dados del numero correspondiente |
| Superior | Bonus | +35 pts si la seccion superior suma >= 63 |
| Inferior | Trio | Suma total si hay al menos 3 iguales |
| Inferior | Poker | Suma total si hay al menos 4 iguales |
| Inferior | Full House | 25 pts (3 de un tipo + 2 de otro) |
| Inferior | Escalera Pequeña | 30 pts (4 consecutivos) |
| Inferior | Escalera Grande | 40 pts (5 consecutivos) |
| Inferior | Yahtzee | 50 pts (5 iguales) |
| Inferior | Chance | Suma total de los 5 dados |

---

## Metodo de Montecarlo

Cada dado lanza `random.randint(1, 6)`, que modela una **distribucion uniforme discreta U(1, 6)** — base del metodo de Montecarlo. Al repetir la partida N veces, la frecuencia relativa de cada resultado converge a su probabilidad real (Ley de los Grandes Numeros).

```
P(evento) ≈ numero de veces que ocurre el evento / N simulaciones
```

Las estadisticas reportadas al final incluyen:

- Porcentaje de victorias de cada IA
- Porcentaje de empates
- Puntaje promedio por jugador

---

## Estrategia de la IA

La IA utiliza una estrategia **greedy** implementada en `ai_strategy.py`:

1. Evalua la categoria disponible que da mayor puntaje con la mano actual.
2. Si el puntaje ya es alto (>= 40 pts), guarda todos los dados.
3. En caso contrario, guarda solo los dados que contribuyen a la mejor categoria objetivo.

---

## Estructura del proyecto

```
Simulacion Yazzeth/
│
├── main.py              # Punto de entrada: demo + simulacion Montecarlo
├── game.py              # Motor de una partida completa (13 rondas)
├── player.py            # Jugador IA: turnos, scorecard y puntaje total
├── dice.py              # Dado con distribucion U(1,6)
├── score_calculator.py  # Calculo de puntaje para cada categoria
├── ai_strategy.py       # Estrategia greedy de decision de dados
├── montecarlo.py        # Simulador Montecarlo y recopilacion de estadisticas
└── logger.py            # Salida en consola (verbose / silencioso)
```

---

## Requisitos

- Python 3.10 o superior (se usa `match/case` y union types `|`)
- Sin dependencias externas — solo biblioteca estandar de Python

---

## Ejecucion

```bash
python main.py
```

**Salida esperada:**

```
══════════════════════════════════════════════════════════
  SIMULACION YAHTZEE — Partida #1
══════════════════════════════════════════════════════════

  [Ronda 1/13]
  -- Turno de IA-1 --
  Lanzamiento 1: [3] [1] [3] [6] [3]
  Guarda (*):    [3*] [1] [3*] [6] [3*]
  Lanzamiento 2: [3*] [4] [3*] [2] [3*]
  IA-1         → Trio                :  9 pts
  ...

Ejecutando 500 simulaciones de Montecarlo...
  10% completado...
  ...
  100% completado...
Completado en 0.87 s.

══════════════════════════════════════════════════════════
  RESULTADOS MONTECARLO (500 simulaciones)
══════════════════════════════════════════════════════════
  IA-1 victorias  :    231  (46.2%)
  IA-2 victorias  :    234  (46.8%)
  Empates         :     35  (7.0%)
  Puntaje prom. IA-1: 183.45 pts
  Puntaje prom. IA-2: 182.91 pts
══════════════════════════════════════════════════════════
```

---

## Autor

**Maria Causil**
Estudiante — Institucion Universitaria Digital de Antioquia
`maria.causil@est.iudigital.edu.co`
