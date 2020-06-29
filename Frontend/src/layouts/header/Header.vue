<template>
  <v-app-bar app clipped-left clipped-right color="#102847" dark>    
    <v-toolbar-title class="align-center d-flex">
      <h5 class="naslov-aplikacije">Aplikacija za provođenje studentske prakse</h5>
    </v-toolbar-title>
  </v-app-bar>
</template>

<script>
import { mapState, mapMutations } from "vuex";

export default {
  name: "Header",

  components: {},

  props: {
    value: {
      type: Boolean,
      default: false
    }
  },

  data() {
    return{
      userprofile: [
      { title: "My Profile" },
      { title: "My Balance" },
      { title: "Inbox" },
      { title: "Account Setting" },
      { title: "Logout" }
    ],
    };
  },

  computed: {
    ...mapState(["Sidebar_drawer"])
  },

  methods: {
    ...mapMutations({
      setSidebarDrawer: "SET_SIDEBAR_DRAWER"
    }),
  }
};
</script>

<style lang="scss" scoped>
.naslov-aplikacije {
  font-size: 17px;
  margin-top: 10px;
  margin-left: 10px;
}
</style>