<template>
  <div class="pixel-crab-sprite" :class="`state-${state}`" :style="spriteStyle" />
</template>

<script setup>
import { computed } from 'vue'

// Real sprite sheet (public/spritesheet.webp): 8 cols x 9 rows, each cell 192x208.
// Row usage (0-indexed):
//   0 = idle (slow blink)          1 = walk cycle (8 frames)
//   8 = thinking pose / "typing"   3 = wave / "holding something out" (4 frames)
// Note: row 8 is a slow "thinking" gesture — keep its playback speed slow,
// otherwise it reads as a fast punch instead of a thoughtful pause.
const props = defineProps({
  size: { type: Number, default: 48 }, // display width in px
  state: { type: String, default: 'idle' }, // idle | walk | typing | report
})

const COLS = 8
const ROWS = 9
const CELL_W = 192
const CELL_H = 208

const ROW_MAP = {
  idle: { row: 0, frames: 6 },
  walk: { row: 1, frames: 8 },
  typing: { row: 8, frames: 6 },
  report: { row: 3, frames: 4 },
}

const displayW = computed(() => props.size)
const displayH = computed(() => props.size * (CELL_H / CELL_W))

const spriteStyle = computed(() => {
  const cfg = ROW_MAP[props.state] || ROW_MAP.idle
  const w = displayW.value
  const h = displayH.value
  return {
    width: `${w}px`,
    height: `${h}px`,
    backgroundImage: "url('/spritesheet.webp')",
    backgroundRepeat: 'no-repeat',
    backgroundSize: `${w * COLS}px ${h * ROWS}px`,
    backgroundPositionY: `-${cfg.row * h}px`,
    '--sprite-x-end': `-${cfg.frames * w}px`,
  }
})
</script>

<style scoped>
.pixel-crab-sprite {
  background-position-x: 0;
  image-rendering: pixelated;
  flex-shrink: 0;
}
.state-idle { animation: sprite-x 1.8s steps(6) infinite; }
.state-walk { animation: sprite-x 0.7s steps(8) infinite; }
.state-typing { animation: sprite-x 1.5s steps(6) infinite ease-in-out; }
.state-report { animation: sprite-x 0.8s steps(4) infinite; }

@keyframes sprite-x {
  from { background-position-x: 0; }
  to { background-position-x: var(--sprite-x-end); }
}
</style>
