<template>
  <v-app id="inspire">
    <Header v-model="expandOnHover"></Header>
    <SidebarStudent :expand-on-hover.sync="expandOnHover"></SidebarStudent>
    <v-content>
      <v-container class="fill-height" fluid>
        <router-view />
      </v-container>
    </v-content>
    <Footer></Footer>
  </v-app>
</template>

<script>
import Header from "./header/Header";
import SidebarStudent from "./sidebar/SidebarStudent";
import Footer from "./footer/Footer";
import { mapState, mapMutations } from "vuex";
export default {

  name: "Layout",

  components: {
    Header,
    SidebarStudent,
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
