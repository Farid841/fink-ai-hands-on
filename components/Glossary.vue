<script setup lang="ts">
defineProps<{
  t: Record<string, string>
  pos?: 'right' | 'left'
}>()
</script>

<template>
  <div
    class="glossary absolute bottom-12 z-20"
    :class="pos === 'left' ? 'left-6' : 'right-6'"
  >
    <div v-for="(def, abbr) in t" :key="abbr">
      <span class="abbr">{{ abbr }}</span> {{ def }}
    </div>
  </div>
</template>

<style scoped>
.glossary {
  max-width: 330px;
  background: rgba(255, 255, 255, 0.92);
  border-left: 3px solid var(--fink-orange);
  border-radius: 6px;
  padding: 5px 10px;
  font-size: 10.5px;
  line-height: 1.45;
  color: #4a5573;
  box-shadow: 0 1px 4px rgba(21, 40, 79, 0.12);
}
.abbr {
  font-weight: 700;
  color: var(--fink-navy);
  margin-right: 2px;
}
</style>
