<template>
  <v-container fluid class="down-top-padding">
    <v-row>
      <v-col cols="12" lg="4">
        <v-card>
          <v-card-text class="text-center pa-7">
            <img
              src="https://img.pngio.com/computer-icons-user-profile-male-my-profile-icon-png-1490051-male-icon-png-920_960.png"
              alt="user"
              width="150px"
              class="img-fluid rounded-circle shadow-sm"
            />
            <h4 class="mt-2 title blue-grey--text text--darken-2 font-weight-regular">{{poslodavac.ime}} {{poslodavac.prezime}}</h4>
            <h6 class="subtitle-2 font-weight-light">{{poslodavac.email}}</h6>
          </v-card-text>
        </v-card>
      </v-col>

      <v-col cols="12" lg="8">
        <v-card>
          <v-card-text>
            <h3 class="title blue-grey--text text--darken-2 font-weight-regular">Profil</h3>
            <h6 class="subtitle-2 font-weight-light">Uredi svoje podatke</h6>
          </v-card-text>
          <v-divider></v-divider>
          <form v-on:submit.prevent="PromijeniPodatke">
            <v-card-text>
              <v-text-field
                v-model="poslodavac.ime"
                label="Ime"
                filled
                background-color="transparent"
                :rules="[rules.required]"
              ></v-text-field>
              <v-text-field
                v-model="poslodavac.prezime"
                label="Prezime"
                filled
                background-color="transparent"
                :rules="[rules.required]"
              ></v-text-field>
              <v-text-field
                type="email"
                v-model="poslodavac.email"
                label="E-mail"
                filled
                background-color="transparent"
                :rules="[rules.required]"
              ></v-text-field>
              <v-text-field
                v-model="poslodavac.lozinka"
                filled
                background-color="transparent"
                :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                :rules="[rules.required, rules.min]"
                :type="show1 ? 'text' : 'password'"
                name="input-10-1"
                label="Password"
                hint="At least 8 characters"
                counter
                @click:append="show1 = !show1"
              ></v-text-field>
              <v-text-field
                type="text"
                v-model="poslodavac.naziv_poduzeca"
                label="Naziv poduzeća"
                filled
                background-color="transparent"
                :rules="[rules.required]"
              ></v-text-field>
              <v-text-field
                type="text"
                v-model="poslodavac.oib_poduzeca"
                label="OIB poduzeća"
                filled
                background-color="transparent"
                :rules="[rules.required]"
              ></v-text-field>
              <v-text-field
                type="text"
                v-model="poslodavac.mjesto"
                label="Mjesto"
                filled
                background-color="transparent"
                :rules="[rules.required]"
              ></v-text-field>
              <v-text-field
                type="text"
                v-model="poslodavac.web"
                label="Web"
                filled
                background-color="transparent"
                :rules="[rules.required]"
              ></v-text-field>
              <v-btn type="submit" class="text-capitalize mt-5 element-0" color="success">Uredi</v-btn>
            </v-card-text>
          </form>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import jwtDecode from 'jwt-decode';
import axios from 'axios';

export default {
  name: "ProfilPoslodavac",

  data() {
    const token = localStorage.usertoken;
    const decoded = jwtDecode(token);
    return{
      poslodavac: [],
      id: decoded.identity.id,
      rules: {
        required: value => !!value || "Required.",
        min: v => v.length >= 8 || "Min 8 characters",
        emailMatch: () => "The email and password you entered don't match"
      },
    }
  },
  components: {},
  created() {
    this.DohvatiPoslodavca();
  },
  methods: {
    DohvatiPoslodavca() {
    axios.get(`http://localhost:8000/poslodavac/${this.id}`).then((response) => {
      this.poslodavac = response.data;
    })
    .catch((e) => {
      console.error(e);
    });
    },
  PromijeniPodatke() {
      axios.put(`http://localhost:8000/poslodavac/${this.id}`, {
        ime: this.poslodavac.ime,
        prezime: this.poslodavac.prezime,
        email: this.poslodavac.email,
        lozinka: this.poslodavac.lozinka,
        naziv_poduzeca: this.poslodavac.naziv_poduzeca,
        oib_poduzeca: this.poslodavac.oib_poduzeca,
        mjesto: this.poslodavac.mjesto,
        web: this.poslodavac.web,
      }).then((res) => {
        this.$router.go();
        console.log(res);
      }).catch((err) => {
        console.log(err);
      });
    },
  },
};
</script>
