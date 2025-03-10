<!--
  2025-3-7:主页
  -->
<template>
  <div class="home">
    <AppNavbar @update:selected="handleSelection" />
    <FeaturedSection v-if="selected === 'featured'" />
    <CommunitySection v-else />
  </div>
</template>

<script>
import AppNavbar from "@/components/AppNavbar.vue";
import FeaturedSection from "@/components/FeaturedSection.vue";
import CommunitySection from "@/components/CommunitySection.vue";

export default {
  components: { AppNavbar, FeaturedSection, CommunitySection },
  data() {
    return {
      selected: "featured",
    };
  },
  methods: {
    handleSelection(option) {
      this.selected = option;
    },
  },
};
</script>
