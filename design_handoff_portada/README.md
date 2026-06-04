# Handoff: Portada Web — systec hub

## Overview
Hero / landing page principal de **systec hub**. La sección comunica la promesa central del producto: implementar un sistema operativo interno en 6 semanas, dejando atrás el "caos" operativo.

Composición editorial a dos columnas:
- **Izquierda**: eyebrow + headline grande + lede + CTA primario/secundario + 3 promesas con iconos.
- **Derecha**: narrativa visual "Caos → 6 semanas → Sistema" usando dos tarjetas + una píldora central + el isotipo de marca.

## About the Design Files
Los archivos de este bundle son **referencias de diseño hechas en HTML** — prototipos que muestran el look & feel y la composición intencionada, **no código de producción para copiar tal cual**. La tarea es **recrear estos diseños en el entorno del codebase** (React/Next, Vue, Astro, etc.) siguiendo sus patrones y librerías existentes. Si no hay codebase aún, elegí el framework que mejor encaje (recomendado: **Next.js + Tailwind** o **Astro**, dado el peso editorial y estático de la portada).

Las clases CSS del HTML son una guía visual; en producción conviene reescribirlas con la estrategia del proyecto (Tailwind, CSS Modules, styled-components, etc.) pero **manteniendo los tokens** de `design-system.css`.

## Fidelity
**Alta fidelidad (hifi).** Colores, tipografía, escalas, espaciados, sombras y radios son finales. Recrear pixel-perfect usando los tokens del sistema.

## Screens / Views

### 1. Portada (Hero)

**Layout — Desktop (≥1024px)**
- Container global `max-width: 1280px`, padding horizontal `48px`.
- Nav sticky arriba (z-index 10) con borde inferior `1px solid #ECE4D4`.
- Hero: grid de 2 columnas `1.05fr 0.95fr`, gap `72px`, padding vertical `80px / 96px`.
- Trust strip: borde superior hairline, padding `28px 48px`.

**Layout — Tablet (≤1024px)**
- Hero pasa a 1 columna, gap `56px`, padding `56px 32px 72px`.
- Visual centrado, max-width `480px`.
- Nav: solo logo + CTA visible.

**Layout — Mobile (≤640px)**
- Headline baja a `40px`, lede a `16px`.
- Botones full-width.
- Promesas en columna única.
- Visual altura fija `360px`, max-width `360px`.

#### Componentes — columna izquierda

**1.1 Nav**
- Altura ~`64px`, fondo `#FBF7F0`, hairline inferior `#ECE4D4`.
- Brand: isotipo `28×28` + wordmark "systec hub" en Montserrat Medium 18px, color `#5BA7DD`.
- Links: Montserrat Medium 14px, color negro. Hover → `#6B5FE8`.
- CTA "Empezar ahora →": fondo `#2C27B8`, texto `#F9F1E3`, padding `10px 18px`, radius `8px`, font 14px/600.

**1.2 Eyebrow**
- "MÉTODO SYSTEC · Implementación en 6 semanas"
- Caps, tracking `0.12em`, 12px/600, color `#2C27B8`.
- Estructura: punto violeta `6px` + texto + divisor horizontal de `24×1px` negro 40% + texto.

**1.3 Headline (h1)**
- Texto: `Del Caos a tu Sistema Operativo en 6 semanas`
- Font Montserrat Bold 700, line-height `1.02`, letter-spacing `-0.025em`.
- Tamaño responsive `clamp(44px, 5.4vw, 76px)`.
- text-wrap: balance.
- Tratamientos por palabra:
  - **"Caos"** → `font-weight: 300; font-style: italic; color: rgba(0,0,0,0.55)` (representa lo viejo).
  - **"Sistema Operativo"** → `color: #2C27B8` (azul profundo).
  - **"6 semanas"** → `color: #6B5FE8; font-weight: 900` + resaltado: pseudo-elemento `::after` `height: 10px; background: rgba(107,95,232,0.12); bottom: 4px; z-index: -1` (efecto highlighter sutil).

**1.4 Lede (párrafo)**
- 18px, line-height `1.55`, color `rgba(0,0,0,0.72)`, max-width `560px`.
- Texto: `En menos de seis semanas, tu equipo deja de perder tiempo, centraliza todo en un solo sistema y toma decisiones con datos reales.`
- Las frases "deja de perder tiempo" y "datos reales" en `<strong>` con `color: #000; font-weight: 600`.

**1.5 CTA row**
- Gap `20px`.
- **Primario** "Agendar diagnóstico →":
  - Fondo `#2C27B8`, texto `#F9F1E3`, radius `10px`, padding `16px 26px`, 15px/600.
  - Sombra: `0 4px 12px rgba(44,39,184,0.12), 0 16px 32px rgba(44,39,184,0.08)`.
  - Hover: fondo `#24208F`, `translateY(-1px)`, sombra intensificada, ícono flecha `translateX(3px)`.
- **Ghost** "Ver el método":
  - Transparente, border `1px solid rgba(0,0,0,0.18)`, color negro.
  - Hover: fondo `rgba(107,95,232,0.08)`, border `#6B5FE8`.

**1.6 Promesas (3 columnas)**
- Border-top hairline, padding-top `32px`, max-width `620px`.
- Grid 3 col, gap `28px`.
- Cada item: icono outline Lucide-style `22×22` color `#6B5FE8`, título 14px/600, descripción 13px/1.45 color `rgba(0,0,0,0.6)`.
- Contenido:
  1. **Recuperá tu tiempo** — icono `clock` — "Tu equipo deja de apagar incendios y se enfoca en lo importante."
  2. **Todo en un solo lugar** — icono `grid-2x2` — "Procesos, datos y personas conectados en un sistema único."
  3. **Decidí con datos** — icono `line-chart` — "Indicadores en vivo. Sin planillas dispersas ni suposiciones."

#### Componentes — columna derecha (visual)

Container `position: relative`, aspect-ratio `1/1`, max-width `540px`, justificado a la derecha.

**1.7 Tarjeta "Caos" (top-left)**
- `position: absolute; top: 0; left: 0; width: 232px; transform: rotate(-3.5deg)`.
- Fondo blanco, border `1px solid #ECE4D4`, radius `14px`, padding `18px 20px`, sombra `0 1px 2px rgba(0,0,0,0.04), 0 12px 28px rgba(0,0,0,0.06)`.
- Label: `HOY · CAOS` (11px/600, tracking 0.12em, color rgba(0,0,0,0.5)).
- Cinco "bloques" en grises variados (opacidad 0.14–0.22) con rotaciones aleatorias (-15° a +20°) — representan el desorden actual.

**1.8 Flecha conectora**
- SVG `200×200`, posicionado `left: 24%, top: 34%`, opacidad `0.55`, color `#6B5FE8`.
- Path curvo con `stroke-dasharray: 4 7`, `stroke-width: 1.5`.

**1.9 Píldora central "6 semanas"**
- Centrada (`left: 50%; top: 50%; translate(-50%,-50%) rotate(-2deg)`), z-index 2.
- Fondo `#2C27B8`, texto `#F9F1E3`, padding `14px 22px`, radius `999px`.
- Sombra `0 8px 24px rgba(44,39,184,0.22)`.
- Contenido: número grande **"6"** (36px/900, letter-spacing -0.02em) + texto a la derecha "SEMANAS / DE IMPLEMENTACIÓN" (12px/600, caps, tracking 0.1em).

**1.10 Tarjeta "Sistema" (bottom-right)**
- Mismas reglas de card que Caos, width `282px`, `transform: rotate(2.5deg)`.
- Label con dot violeta delante: `SEMANA 6 · SISTEMA OPERATIVO` (color `#6B5FE8`).
- Adentro: el **isotipo de systec hub** a tamaño grande (los 5 bloques violetas ordenados que forman la "S").

**1.11 Chips flotantes**
- Pill blancas con border hairline, sombra suave, font 12px/500.
- Chip 1 (top-right): icono `clock` + "Semana 0 · Diagnóstico", rotación `4deg`.
- Chip 2 (bottom-left): icono `check` + "Equipo alineado", rotación `-5deg`.

#### Componentes — Trust strip

**1.12 Strip de confianza**
- Border-top hairline, fondo `#FBF7F0`, padding `28px 48px`.
- Label izquierda: "MÁS DE 40 EQUIPOS YA LO IMPLEMENTARON" (12px/600, tracking 0.14em, caps, gris 50%).
- Logos derecha: 5 nombres tipográficos (18px/500, gris 55%), algunos en itálica para variar el ritmo.
- **Nota dev**: reemplazar por logos reales de clientes cuando estén disponibles. Por ahora son placeholders tipográficos (decisión deliberada — no usar logos genéricos).

## Interactions & Behavior

- **Sticky nav**: queda fija arriba al scrollear, mantiene fondo `#FBF7F0` con hairline.
- **Smooth scroll** a las anclas (`#metodo`, `#resultados`, `#precios`, `#empezar`, `#agenda`).
- **Hover botón primario**: `translateY(-1px)` + intensifica sombra + flecha desplaza `3px` a la derecha. Duración `200ms`, easing `cubic-bezier(0.2, 0.8, 0.2, 1)`.
- **Hover botón ghost**: border y border-bottom se tiñen de violeta, fondo `rgba(107,95,232,0.08)`.
- **Hover links nav**: color a `#6B5FE8`, sin underline.
- **Focus visible** en todo elemento interactivo: `box-shadow: 0 0 0 3px rgba(107,95,232,0.24)`.
- **Sin animaciones de entrada** por ahora (la marca prefiere sobriedad). Si se quisieran, fade + translate `8px` con duración `320ms`, escalonado `60ms` por elemento. Respetar `prefers-reduced-motion`.

## State Management

Página estática. No requiere estado.

CTAs deberían disparar:
- **"Agendar diagnóstico"** → abrir modal con formulario o redirigir a página de booking (Cal.com / Calendly / form interno).
- **"Empezar ahora"** → ruta de signup o misma página de booking.
- **"Ver el método"** → scroll a sección de método (no incluida en este handoff).

## Design Tokens

Todos los tokens están en `design-system.css`. Resumen:

### Colors
| Token | Hex | Uso |
|---|---|---|
| `--page-bg` | `#FBF7F0` | Fondo de página (override del crema del DS, pedido por cliente) |
| `--crema` | `#F9F1E3` | Crema del sistema (texto sobre fondos oscuros) |
| `--negro` | `#000000` | Texto principal |
| `--violeta-sistema` | `#6B5FE8` | Acento primario, isotipo, "6 semanas" en el headline |
| `--azul-medio` | `#5BA7DD` | Wordmark, links |
| `--azul-profundo` | `#2C27B8` | CTA primario, "Sistema Operativo" en headline |
| `--azul-claro` | `#B6D4FB` | Surface alternativo (no usado en esta portada) |
| `--hairline` | `#ECE4D4` | Bordes sutiles sobre crema |
| `--negro-64` | `rgba(0,0,0,0.64)` | Texto secundario |
| `--negro-40` | `rgba(0,0,0,0.40)` | Texto terciario |
| `--violeta-12` | `rgba(107,95,232,0.12)` | Wash hover, highlight detrás de "6 semanas" |

### Typography
- **Familia única**: Montserrat (self-hosted, OTF, weights 200–900).
- Body: 16px / 1.55 / weight 400.
- Headline display: `clamp(44px, 5.4vw, 76px)` / 1.02 / weight 700 / letter-spacing -0.025em.
- Lede: 18px / 1.55 / weight 400.
- Eyebrow + overline: 12px / 600 / tracking 0.12em / UPPERCASE.
- Botones: 15px / 600.
- Promesa título: 14px / 600. Descripción: 13px / 1.45.

### Spacing scale
4 / 8 / 12 / 16 / 20 / 24 / 32 / 40 / 48 / 64 / 80 / 96 px.

### Radii
4 / 6 / 8 / 10 / 12 / 14 / 16 / 999 px (pill).

### Shadows
- **Card resting**: `0 1px 2px rgba(0,0,0,0.04), 0 12px 28px rgba(0,0,0,0.06)`.
- **CTA primario**: `0 4px 12px rgba(44,39,184,0.12), 0 16px 32px rgba(44,39,184,0.08)`.
- **Píldora 6 semanas**: `0 8px 24px rgba(44,39,184,0.22)`.
- **Chip flotante**: `0 2px 8px rgba(0,0,0,0.05)`.

### Motion
- Duración base: `200ms`.
- Easing enter: `cubic-bezier(0.2, 0.8, 0.2, 1)`.
- Easing exit: `cubic-bezier(0.4, 0, 1, 1)`.

## Assets

Carpeta `assets/`:
- `isotipo.svg` — 5 bloques violetas formando la "S" de systec. Marca visual principal.
- `wordmark.svg` — "systec hub" en azul medio.
- `logo-horizontal.svg` — isotipo + wordmark lockup horizontal.
- `isotipo-cream.svg` — variante mono crema (para uso sobre azul profundo / negro).

Carpeta `fonts/` — Montserrat OTF weights 200/300/400/500/600/700/800/900. Self-hosted via `@font-face` en `design-system.css`. Para producción considerá:
- Convertir a WOFF2 (mucho más liviano).
- Subsetting latin-ext si solo se usa español.
- O usar Google Fonts si el proyecto lo permite (familia "Montserrat" en weights 400, 500, 600, 700, 900).

### Iconografía
Iconos inline SVG estilo **Lucide** (https://lucide.dev). `stroke-width 1.5–1.8`, `stroke-linecap round`, `stroke-linejoin round`, color heredado (`currentColor`).

Iconos usados:
- `arrow-right` (CTAs)
- `clock` (promesa 1, chip "Semana 0")
- `grid-2x2` (promesa 2)
- `line-chart` (promesa 3)
- `check` (chip "Equipo alineado")

En producción recomiendo importar `lucide-react` y usar los componentes directos en vez de inline SVG.

## Files

Incluidos en este bundle:
- `Portada Web.html` — el prototipo completo.
- `design-system.css` — tokens del sistema SysteC (78 custom properties + `@font-face` + reset).
- `assets/` — logos y marcas.
- `fonts/` — Montserrat self-hosted.

## Implementation Notes

- El fondo de la página es `#FBF7F0` (un crema ligeramente más cálido que el crema del DS `#F9F1E3`). Es un override solicitado por el cliente — mantenelo así.
- El visual de la derecha es una **composición posicionada en absoluto** dentro de un contenedor cuadrado. Si lo trasladás a un componente React, considerá usar `position: absolute` con valores relativos (`top: 0; left: 0`) o variantes de Tailwind (`absolute top-0 left-0`).
- El **highlighter detrás de "6 semanas"** se hace con `position: relative` en el span + `::after` absoluto con `z-index: -1`. El padre necesita un stacking context o asegurar que el `::after` no se esconda detrás del fondo de la página — funciona porque `body` no tiene z-index.
- **Accesibilidad**: el visual de la derecha usa `aria-hidden="true"` porque la historia narrativa ya está en el headline + lede. No agregues texto alt redundante.
- **Performance**: el SVG del isotipo se inline-a dos veces (nav + visual). Para reducir peso, considerá un `<symbol>` + `<use>` o un componente React reutilizable.
