<template>
  <div class="auth-page">
    <v-app-bar app clipped-left clipped-right color="#102847" dark>
      <v-toolbar-title class="align-center d-flex">
        <h5 class="naslov-aplikacije">Aplikacija za provođenje studentske prakse</h5>
      </v-toolbar-title>
      <v-app-bar-nav-icon
        class="d-block d-md-none"
        @click="$vuetify.breakpoint.smAndDown ? setSidebarDrawer(!Sidebar_drawer) : $emit('input', !value)"
      />
      <v-spacer />
    </v-app-bar>

    <b-container>
      <b-card header-tag="header" body-class="text-center" style="width: 600px; height:1080px; margin:auto; margin-top:5px;">
        <h3 class="naslov-form">Registracija poslodavca</h3>
        <form v-on:submit.prevent="RegistracijaKorisnika">
          
          <div class="inputi">
            <label for="ime" class="podaci-poslodavac-lbl">Ime</label>
            <label class="zvjezdica-lbl">*</label>
            <b-input-group>
              <b-form-input
                v-model="ime"
                class="form-control"
                type="text"
                size="lg"
                name="ime"
                placeholder="Unesite ime"
                required
              ></b-form-input>
            </b-input-group>
          </div>

          <div class="inputi">
            <label for="prezime" class="podaci-poslodavac-lbl">Prezime</label>
            <label class="zvjezdica-lbl">*</label>
            <b-input-group>
              <b-form-input
                v-model="prezime"
                class="form-control"
                type="text"
                size="lg"
                name="prezime"
                placeholder="Unesite prezime"
                required
              ></b-form-input>
            </b-input-group>
          </div>

          <div class="inputi">
            <label for="email" class="podaci-poslodavac-lbl">E-mail</label>
            <label class="zvjezdica-lbl">*</label>
            <b-input-group>
              <b-form-input
                v-model="email"
                class="form-control"
                type="email"
                size="lg"
                name="email"
                placeholder="Unesite email"
                required
              ></b-form-input>
            </b-input-group>
          </div>

          <div class="inputi">
            <label for="lozinka" class="podaci-poslodavac-lbl">Lozinka</label>
            <label class="zvjezdica-lbl">*</label>
            <b-input-group>
              <b-form-input
                v-model="lozinka"
                class="form-control"
                type="password"
                size="lg"
                name="lozinka"
                placeholder="Unesite lozinku"
                required
              ></b-form-input>
            </b-input-group>
          </div>

          <div class="inputi">
            <label for="lozinka2" class="podaci-poslodavac-lbl">Ponovite lozinku</label>
            <label class="zvjezdica-lbl">*</label>
            <b-input-group>
              <b-form-input
                class="form-control"
                type="password"
                v-model="ponovite_lozinku"
                size="lg"
                name="lozinka2"
                placeholder="Ponovite lozinku"
                required
              ></b-form-input>
            </b-input-group>
          </div>

          <label
            class="podaci-poslodavac-lbl2"
            v-if="ponovite_lozinku!=lozinka"
            show
            variant="danger"
          >* Lozinke moraju biti iste.</label>

          <div class="inputi">
            <label for="naziv-poduzeca" class="podaci-poslodavac-lbl">Naziv poduzeća</label>
            <label class="zvjezdica-lbl">*</label>
            <b-input-group>
              <b-form-input
                v-model="naziv_poduzeca"
                class="form-control"
                type="text"
                size="lg"
                name="naziv_poduzeca"
                placeholder="Unesite naziv poduzeća"
                required
              ></b-form-input>
            </b-input-group>
          </div>

          <div class="inputi">
            <label for="oib-poduzeca" class="podaci-poslodavac-lbl">OIB poduzeća</label>
            <label class="zvjezdica-lbl">*</label>
            <b-input-group>
              <b-form-input
                v-model="oib_poduzeca"
                class="form-control"
                type="text"
                size="lg"
                name="oib_poduzeca"
                placeholder="Unesite OIB poduzeća"
                required
              ></b-form-input>
            </b-input-group>
          </div>

          <div class="inputi">
            <label for="mjesto" class="podaci-poslodavac-lbl">Mjesto</label>
            <label class="zvjezdica-lbl">*</label>
            <b-input-group>
              <b-form-input
                v-model="mjesto"
                class="form-control"
                type="text"
                size="lg"
                name="mjesto"
                placeholder="Unesite mjesto"
                required
              ></b-form-input>
            </b-input-group>
          </div>

          <div class="inputi">
            <label for="web" class="podaci-poslodavac-lbl">Web</label>
            <label class="zvjezdica-lbl">*</label>
            <b-input-group>
              <b-form-input
                v-model="web"
                class="form-control"
                type="text"
                size="lg"
                name="web"
                placeholder="Unesite web"
                required
              ></b-form-input>
            </b-input-group>
          </div>

          <div class="group-btn">
            <b-button class="odustani-btn" @click="toOdustani()">Odustani</b-button>
            <b-button class="registracija-btn" type="submit">Registriraj se</b-button>
          </div>
          
        </form>
      </b-card>
    </b-container>
  </div>
</template>

<script>
import axios from "axios";
import { required, sameAs, minLength } from "vuelidate/lib/validators";

export default {
  name: "FormValidation",
  data() {
    return {
      ime: "",
      prezime: "",
      email: "",
      lozinka: "",
      ponovite_lozinku: "",
      naziv_poduzeca: "",
      oib_poduzeca: "",
      mjesto: "",
      web: ""
    };
  },
  validations: {
    lozinka: {
      required,
      minLength: minLength(6)
    },
    ponovite_lozinku: {
      sameAsPassword: sameAs("lozinka")
    }
  },
  methods: {
    RegistracijaKorisnika() {
      axios
        .post("http://localhost:8000/poslodavac/register", {
          ime: this.ime,
          prezime: this.prezime,
          email: this.email,
          lozinka: this.lozinka,
          naziv_poduzeca: this.naziv_poduzeca,
          oib_poduzeca: this.oib_poduzeca,
          mjesto: this.mjesto,
          web: this.web
        })
        .then(res => {
          this.$router.push({ name: "PrijavaPoslodavac" });
          console.log(res);
        })
        .catch(err => {
          console.log(err);
        });
    },
    toOdustani() {
      this.$router.push({ name: "PrijavaPoslodavac" });
    }
  }
};
</script>

<style lang="scss" scoped>
  .auth-page {
    padding-top: 10vh;
    height: 100vh;
  }

  .naslov-aplikacije {
    font-size: 17px;
    margin-top: 10px;
    margin-left: 10px;
  }

  .naslov-form {
    color: black;
    font-size: 18px;
    margin-top: 10px;
    color:#636c72
}

  .inputi {
    padding: 3 10 px;
    float: right;
    width: 75%;
    margin-right: 70px;
    margin-top: 30px;
  }

  .podaci-poslodavac-lbl {
    float:left;
    font-size:15px;
  }

  .zvjezdica-lbl {
  float: left;
  color: red;
  padding-left: 1px;
  }

  .form-control {
    font-size:14px;
  }

  .podaci-poslodavac-lbl2 {
    margin-right: 280px;
    font-size:11px;
    color: red;
    margin-bottom: 0px;
  }

  .group-btn {
    float: right;
    margin-right: 70px;
    margin-top: 35px;
    font-size: 10px;
  }

  .odustani-btn {
    font-size: 14px;
    background-color: #102847;
  }

  .registracija-btn {
    font-size: 14px;
    background-color: #102847;
    margin-left: 215px;
}

</style>
