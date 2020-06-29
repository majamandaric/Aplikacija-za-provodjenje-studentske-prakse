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
      <b-card header-tag="header" body-class="text-center" style="width: 600px; height:680px; margin:auto; margin-top:5px;">      
        <h3 class="naslov-form">Odaberi vrstu korisničkog računa</h3>

        <div class="img-group">
          <div class="responsive">
            <div class="gallery1">
              <a>
                <img src="@/assets/poslodavac.png"/>
              </a>
              <div class="desc">Poslodavac</div>
            </div>
          </div>

          <div class="responsive">
            <div class="gallery2">
              <a href="http://localhost:8080/">
                <img src="@/assets/student.png">
              </a>
              <div class="desc">Student</div>
            </div>
          </div>
        </div>

        <div>
          <h6 class="natpis-h6">Prijavi se kao poslodavac</h6>
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
              <b-form-input v-model="email" class="form-control" size="lg" placeholder="E-mail" type="email" required>
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
              <b-button type="submit" class="prijava-btn2">Prijavi se</b-button>
          </div>

        </form>

        <div class="zaboravljena-lozinka">
            <a href="">Zaboravili ste lozinku?</a>
        </div>

        <div class="registracija-btn">
            <b-button class="registracija-btn2" @click="toRegisterEmployer()" >Nemaš korisnički račun? Registriraj se</b-button>
        </div>

        </b-card>
      </b-container>

      <router-link class="nav-link" to="/loginprofesor">Prijava profesora</router-link>
    </div>

</template>

<script>
import axios from 'axios';

export default {
  data() {

    return {
      email: '',
      password: '',
      errorMessage: '',
    };
  },
  methods: {
    PrijavaKorisnika() {
      axios.post('http://localhost:8000/poslodavac/login', {
        email: this.email,
        lozinka: this.password,
      }).then((res) => {
        if(res.status === 200){
        localStorage.setItem('usertoken', res.data);
        this.email = '';
        this.password = '';
        this.$router.push({ name: 'Dashboard' });
        }
      }).catch((err) => {
        this.errorMessage = 'Unesena e-pošta ili lozinka ne odgovaraju nijednom računu.';
        console.log(err);
      });
      this.emitMethod();
    },
    toRegisterEmployer() {
      this.$router.push({ name: 'RegistracijaPoslodavac' });
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

  .img-group {
      margin-right: 50px;
  }

  .responsive {
    padding: 10 10 px;
    float: right;
    width: 35%;
    margin-right: 30px;
    margin-top: 30px;
  }

  div.gallery2 {
  border: 1px solid #ccc;
  }

  div.gallery2:hover {
    border: 1px solid #777;
  }

  div.gallery2 img {
    width: 100%;
    height: auto;
  }

  div.gallery1 {
    border: 1px solid #102847;
  }

  div.gallery1:hover {
    border: 1px solid #777;
  }

  div.gallery1 img {
    width: 100%;
    height: auto;
  }

  div.desc {
    padding: 15px;
    text-align: center;
    color:#636c72
  }

  * {
    box-sizing: border-box;
  }

  .clearfix:after {
    content: "";
    display: table;
    clear: both;
  }

  .natpis-h6 {
    margin-top: 280px;
    color:#636c72
  }

  .inputi{
    padding: 3 10 px;
    float: right;
    width: 70%;
    margin-right: 76px;
    margin-top: 25px;
  }

  .form-control {
    font-size:14px;
  }

  .prijava-btn {
    float: right;
    margin-right: 76px;
    margin-top: 25px;
    font-size: 10px;
  }

  .prijava-btn2 {
    font-size: 14px;
    background-color: #102847;
  }

  .zaboravljena-lozinka{
    font-size: 12px;
    margin-top: 170px;
    margin-left: 100px;
    color: gray;
  }

  a:link, a:visited {
    color: gray;
  }

  .registracija-btn {
    margin-top: 200 px;
    margin-bottom: 0px;
  }

  .registracija-btn2 {
    width: 390px;
    margin-left: 14px;
    margin-top: 25px;
    font-size: 15px;
    background-color: #102847;
  }

  .nav-link {
    font-size:10px;
    float:right;
    margin-top: -70px;
  }
</style>
