<script setup lang="ts">
defineProps<{ pos?: 'bottom-left' | 'top-right' }>()
</script>

<template>
  <div
    class="credit absolute z-20"
    :class="pos === 'top-right' ? 'top-4 right-6 text-right' : 'bottom-12 left-6'"
  >
    <slot />
  </div>
</template>

<style scoped>
.credit {
  max-width: 55%;
  font-size: 9.5px;
  line-height: 1.35;
  color: #8a94ad;
  font-style: italic;
}
</style>
