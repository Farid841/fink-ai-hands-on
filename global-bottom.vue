<template>
  <div
    v-if="!['cover', 'section', 'end'].includes($nav.currentLayout)"
    class="absolute bottom-0 left-0 right-0 h-10 flex items-center justify-between px-6"
    style="border-top: 3px solid #f5622e; background: #ffffff; z-index: 10"
  >
    <span class="text-xs" style="color: #15284f">
      Fink · Paris-Saclay Astroparticle Symposium 2026 · Institut Pascal
    </span>
    <div class="flex items-center gap-3">
      <span class="text-xs" style="color: #8a94ad">{{ $nav.currentPage }} / {{ $nav.total }}</span>
      <img src="/img/Fink_SecondaryLogo_WEB.png" class="h-7" />
    </div>
  </div>
</template>
