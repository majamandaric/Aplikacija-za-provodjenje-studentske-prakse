<template>
  <v-app id="inspire">
    <HeaderPoslodavac v-model="expandOnHover"></HeaderPoslodavac>
    <SidebarPoslodavac :expand-on-hover.sync="expandOnHover"></SidebarPoslodavac>
    <v-content>
      <v-container class="fill-height" fluid>
        <router-view />
      </v-container>
    </v-content>
    <Footer></Footer>
  </v-app>
</template>

<script>
import HeaderPoslodavac from "./header/HeaderPoslodavac";
import SidebarPoslodavac from "./sidebar/SidebarPoslodavac";
import Footer from "./footer/Footer";
import { mapState, mapMutations } from "vuex";

export default {
  name: "Layout",

  components: {
    HeaderPoslodavac,
    SidebarPoslodavac,
    Footer
  },

  props: {
    source: String
  },

  data: () => ({
    expandOnHover: false
  }),
  
  computed: {
    ...mapState(["Customizer_drawer"])
  },

  methods: {
    ...mapMutations({
      setCustomizerDrawer: "SET_CUSTOMIZER_DRAWER"
    })
  }
};
</script>
