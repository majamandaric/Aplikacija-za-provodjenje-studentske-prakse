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
      <b-card header-tag="header" body-class="text-center" style="width: 600px; height:350px; margin:auto; margin-top:5px; top:100px;">

        <div>
            <h6 class="naslov-form">Prijava profesora</h6>
        </div>
        <form @submit.prevent="PrijavaKorisnika">
          <b-alert class="alert-sm" variant="dark" style="width: 392px; left: 90px; margin-bottom: 0px; margin-right: 0px; top: 6px; font-size:11px;" :show="!!errorMessage">
            {{errorMessage}}
          </b-alert>

          <div class="inputi">
            <b-input-group>
              <b-input-group-prepend>
                <span class="input-group-text"> <b-icon-envelope-fill></b-icon-envelope-fill></span>
              </b-input-group-prepend>
              <b-form-input v-model="email" class="form-control" size="lg" type="email" placeholder="E-mail" required>
              </b-form-input>
          </b-input-group>
          </div>

          <div class="inputi">
            <b-input-group>
              <b-input-group-prepend>
                <span class="input-group-text"><b-icon-lock-fill></b-icon-lock-fill></span>
              </b-input-group-prepend>
              <b-form-input v-model="password" class="form-control" size="lg" type="password" placeholder="Lozinka" required>
              </b-form-input>
            </b-input-group>
          </div>

          <div class="prijava-btn">
              <b-button class="odustani-btn" @click="toOdustani()">Odustani</b-button>
              <b-button type="submit" class="prijava-btn2">Prijavi se</b-button>
          </div>
        </form>

      </b-card>
    </b-container>
  </div>

</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      signUp: false,
      email: '',
      password: '',
      errorMessage: '',
    };
  },
  methods: {
    PrijavaKorisnika() {
      axios.post('http://localhost:8000/profesor/login', {
        email: this.email,
        lozinka: this.password,
      }).then((res) => {
        if(res.status === 200){
        localStorage.setItem('usertoken', res.data);
        this.email = '';
        this.password = '';
        this.$router.push({ name: 'Dashboard3' });
        }
      }).catch((err) => {
        this.errorMessage = 'Unesena e-pošta ili lozinka ne odgovaraju nijednom računu.';
        console.log(err);
      });
      this.emitMethod();
    },
    toOdustani() {
      this.$router.push({ name: 'PrijavaStudent' });
    },
  },
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
    width: 70%;
    margin-right: 76px;
    margin-top: 25px;
  }

  .form-control {
      font-size:14px;
  }

  .prijava-btn{
      float: right;
      margin-right: 76px;
      margin-top: 35px;
      font-size: 10px;
  }

  .odustani-btn{
      font-size: 14px;
      background-color: #102847;
      margin-right: 215px;
  }

  .prijava-btn2{
      font-size: 14px;
      background-color: #102847;
  }
</style>
