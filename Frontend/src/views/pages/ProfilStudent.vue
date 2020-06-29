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
            <h4 class="mt-2 title blue-grey--text text--darken-2 font-weight-regular">{{student.ime}} {{student.prezime}}</h4>
            <h6 class="subtitle-2 font-weight-light">{{student.email}}</h6>
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
                v-model="student.ime"
                label="Ime"
                filled
                background-color="transparent"
                :rules="[rules.required]"
              ></v-text-field>
              <v-text-field
                v-model="student.prezime"
                label="Prezime"
                filled
                background-color="transparent"
              ></v-text-field>
              <v-text-field
                type="email"
                v-model="student.email"
                label="E-mail"
                filled
                background-color="transparent"
              ></v-text-field>
              <v-text-field
                v-model="student.lozinka"
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
                v-model="student.jmbag"
                label="JMBAG"
                filled
                background-color="transparent"
              ></v-text-field>
              <v-text-field
                v-model="student.grad"
                label="Grad"
                filled
                background-color="transparent"
              ></v-text-field>
              <v-text-field
                v-model="student.sveuciliste"
                label="Sveuciliste"
                filled
                background-color="transparent"
              ></v-text-field>
              <v-text-field
                v-model="student.vrsta_studija"
                label="Vrsta studija"
                filled
                background-color="transparent"
              ></v-text-field>
              <v-text-field
                v-model="student.smjer"
                label="Smjer"
                filled
                background-color="transparent"
              ></v-text-field>
              <v-text-field
                v-model="student.godina"
                label="Godina"
                filled
                background-color="transparent"
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
  name: "ProfilStudent",

  data() {
    const token = localStorage.usertoken;
    const decoded = jwtDecode(token);
    return{
      student: [],
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
    this.DohvatiStudenta();
  },
  methods: {
    DohvatiStudenta() {
    axios.get(`http://localhost:8000/student/${this.id}`).then((response) => {
      this.student = response.data;
    })
    .catch((e) => {
      console.error(e);
    });
    },
    PromijeniPodatke() {
        axios.put(`http://localhost:8000/student/${this.id}`, {
          ime: this.student.ime,
          prezime: this.student.prezime,
          email: this.student.email,
          lozinka: this.student.lozinka,
          grad: this.student.grad,
          sveuciliste: this.student.sveuciliste,
          smjer: this.student.smjer,
          godina: this.student.godina,
          vrsta_studija: this.student.vrsta_studija,
          jmbag: this.student.jmbag,
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
