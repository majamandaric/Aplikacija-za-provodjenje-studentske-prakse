<template>
  <v-container fluid class="down-top-padding">
    <v-row>
      <v-col cols="12" sm="12">
        <BaseCard heading="Popis studenata s odabranim prioritetima studentskih praksi">
            <TableSimpleFixHeight></TableSimpleFixHeight>
        </BaseCard>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

export default {

  name: "BasicDashboard",

  components: {
      TableSimpleFixHeight: () => import('@/components/tables-simple/TableSimpleFixHeight')
  },
  data() {
    return {
    };
  } ,
  created() {
  },

  computed: {
  },

  methods: {
  },
};

</script>

<style lang="scss" scoped>
</style>
