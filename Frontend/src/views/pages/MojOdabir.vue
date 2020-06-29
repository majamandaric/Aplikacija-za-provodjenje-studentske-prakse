<template>
  <v-container fluid class="down-top-padding" style="height:746px;">
    <div>
      <img v-if="korak1==1" style="width:650px; margin-left:210px;" src="@/assets/1.png"/>
      <img v-if="korak2==1" style="width:650px; margin-left:210px;" src="@/assets/2.png"/>
      <img v-if="korak3==1" style="width:650px; margin-left:210px;" src="@/assets/3.png"/>
    </div>

    <div v-if="korak1==1">
      <v-row >
        <v-col class="projekti" cols="12" lg="6" v-for="post of projekti" v-bind:key="post.id">
          <v-card>
            <v-card-text class="pa-5">
              <a data-toggle="modal" data-target="#modal1" @click="Detalji(post)"> 
              <img border="0" class="projekt-detalji-img" src="https://cdn4.iconfinder.com/data/icons/pictype-free-vector-icons/16/more-512.png" width="22" height="22"></a>
              <h1 class="zadatak-studenta-h1">{{post.zadatak_studenta}}</h1>
              <div class="d-flex align-center justify-center border-top pt-4">
                <v-sparkline :fill="fill" height="145px" :gradient="gradient" :line-width="width" :padding="padding" :smooth="radius || false" :value="value" auto-draw></v-sparkline>
              </div>
              <h6 class="subtitle-2 font-weight-light"><b>Ime poduzeća:</b> {{post.naziv_poduzeca}}</h6>
              <h6 class="subtitle-2 font-weight-light"><b>Tehnologije: </b> {{post.preferirane_tehnologije}}</h6>
              <h6 class="subtitle-2 font-weight-light pb-2"><b>Trajanje prakse: </b>{{post.broj_sati}}</h6>
              <div class="d-flex align-left justify-left border-top pt-1">
              </div>
              <b-row>
                <b-col cols="9">
                  <div class="d-flex align-left justify-left pt-1">
                    <div class="d-flex align-left px-3">
                      <span class="success--text">
                        <b-img src="https://image.flaticon.com/icons/png/512/33/33308.png" class="person-icon" fluid alt="Responsive image"></b-img>
                        <span class="font-weight-regular">{{post.broj_studenta}}</span>
                      </span>
                    </div>
                    <div class="d-flex align-left px-5">
                      <span class="success--text">
                        <b-img src="https://image.freepik.com/free-icon/calendar-icon-black_318-9776.jpg" class="calendar-icon" fluid alt="Responsive image"></b-img>
                        <span class="font-weight-regular">{{post.vrijeme_pocetka}}</span>
                      </span>
                    </div>
                    <div class="d-flex align-left px-2">
                      <span class="success--text">
                        <b-img src="https://image.flaticon.com/icons/png/512/67/67872.png" class="time-icon" fluid alt="Responsive image"></b-img>
                        <span class="font-weight-regular">{{post.lokacija}}</span>
                      </span>
                    </div>
                  </div>
                </b-col>

                <b-col>
                  <div class="d-flex align-left justify-left px-6">
                    <b-button v-b-popover.hover.top="'Obriši'" type="button" variant="secondary" size="sm" class="izmjeni-btn" style="background-color: #102847; margin-left: 43px;" @click="ObrisiFavorita(post.id)">
                      <b-icon-trash></b-icon-trash>
                    </b-button>
                  </div>
                </b-col>
              </b-row>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>

      <div class="modal fade bd-example-modal-lg" id="modal1" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-lg">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel">Detalji projektnog zadatka</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
            <list-group>
              <list-group-item><b>Naziv poduzeća</b></list-group-item><br>
              <label class="podaci-lbl">{{editForm.naziv_poduzeca}}</label><br><hr>
              <list-group-item><b>Kontakt osoba (+mail, telefon)</b></list-group-item><br>
              <label class="podaci-lbl">{{editForm.kontakt_osoba}}</label><br><hr>
              <list-group-item><b>Zadatak studenata</b></list-group-item><br>
              <label class="podaci-lbl">{{editForm.zadatak_studenta}}</label><br><hr>
              <list-group-item ><b>Preferirane tehnologije</b></list-group-item><br>
              <label class="podaci-lbl">{{editForm.preferirane_tehnologije}}</label><br><hr>
              <list-group-item><b>Broj studenata</b></list-group-item><br>
              <label class="podaci-lbl">{{editForm.broj_studenta}}</label><br><hr>
              <list-group-item><b>Preferencije pri odabiru studenta</b></list-group-item><br>
              <label class="podaci-lbl">{{editForm.preferencije}}</label><br><hr>
              <list-group-item><b>Potrebna infrastruktura koju student mora posjedovati</b></list-group-item><br>
              <label class="podaci-lbl">{{editForm.potrebna_infrastruktura}}</label><br><hr>
              <list-group-item><b>Željeno trajane prakse</b></list-group-item><br>
              <label class="podaci-lbl">{{editForm.broj_sati}}</label><br><hr>
              <list-group-item><b>Lokacija održavanja studentske prakse</b></list-group-item><br>
              <label class="podaci-lbl">{{editForm.lokacija}}</label><br><hr>
              <list-group-item><b>Željeno okvirno vrijeme početka</b></list-group-item><br>
              <label class="podaci-lbl">{{editForm.vrijeme_pocetka}}</label><br><hr>
              <list-group-item><b>Angažman nastavnika s FIPU</b></list-group-item><br>
              <label class="podaci-lbl">{{editForm.angazman_nastavnika}}</label><br><hr>
              <list-group-item><b>Dodatna napomena</b></list-group-item><br>
              <label class="podaci-lbl">{{editForm.dodatna_napomena}}</label><br><hr>
            </list-group>
            <div>
              <b-button type="button" class="nazad-izmjeni" data-dismiss="modal">Nazad</b-button>
            </div>
          </div>
        </div>
      </div>
        
      </div>
        <b-button class="dalje-btn" style="float:right; background-color: #102847; width:100px; bottom:45px; margin-top:10px;" size="md" variant="secondary" @click="prebaci();">Dalje</b-button>
      </div>
     
      <v-col v-if="korak2==1" style="top: 19px; width: 800px; left:125px;">
        <v-card style="height: 510px; top: 19px;" >
          <form @submit.prevent="DodajOdabir();korak1=0;korak2=0;korak3=1;">
            <v-card-text>
              <h3 class="title color-#102847 text--darken-2 font-weight-regular">Moji prioriteti</h3>
              <p class="font-weight-light" style="font-size:13px; margin-bottom: -20px;">Odaberi poslodavca i projekt na koji se želiš prijaviti</p>
            </v-card-text>
            <v-divider></v-divider>
            <v-card-text style="width: 600px; margin-left: 90px; margin-top: 20px;">
              <b-alert class="alert-sm" variant="danger" style="bottom:5px;" :show="!!errorMessage">
                {{errorMessage}}
              </b-alert>
              <b-select v-model="odabir1" required class="form-control no-border" style="margin-bottom:20px;"> 
                <b-form-select-option :value="null" disabled>-- Odaberite prioritet 1 --</b-form-select-option>
                <b-form-select-option v-for="team of projekti" v-bind:key="team.id" v-bind:value="team.zadatak_studenta + ' - ' + team.naziv_poduzeca" v-bind:disabled="odabir2==team.zadatak_studenta + ' - ' + team.naziv_poduzeca || odabir3==team.zadatak_studenta + ' - ' + team.naziv_poduzeca " >
                {{ team.zadatak_studenta }} - {{ team.naziv_poduzeca }}
                </b-form-select-option>
              </b-select>
            
              <b-select v-model="odabir2" required class="form-control no-border" style="margin-bottom:20px;" > 
                <b-form-select-option :value="null" disabled>-- Odaberite prioritet 2 --</b-form-select-option>
                <b-form-select-option v-for="team of projekti" v-bind:key="team.id" v-bind:value="team.zadatak_studenta + ' - ' + team.naziv_poduzeca" v-bind:disabled="odabir1==team.zadatak_studenta + ' - ' + team.naziv_poduzeca || odabir3==team.zadatak_studenta + ' - ' + team.naziv_poduzeca ">
                {{ team.zadatak_studenta }} - {{ team.naziv_poduzeca }}
                </b-form-select-option>
              </b-select>
            
              <b-select v-model="odabir3" required class="form-control no-border" style="margin-bottom:30px;" > 
                <b-form-select-option :value="null" disabled>-- Odaberite prioritet 2 --</b-form-select-option>
                <b-form-select-option v-for="team of projekti" v-bind:key="team.id" v-bind:value="team.zadatak_studenta + ' - ' + team.naziv_poduzeca" v-bind:disabled="odabir1==team.zadatak_studenta + ' - ' + team.naziv_poduzeca ||  odabir2==team.zadatak_studenta + ' - ' + team.naziv_poduzeca" >
                {{ team.zadatak_studenta }} - {{ team.naziv_poduzeca }}
                </b-form-select-option>
              </b-select>

              <div class="mt-3">Prioritet 1: <strong>{{ odabir1 }}</strong></div>
              <div class="mt-3">Prioritet 2: <strong>{{ odabir2 }}</strong></div>
              <div class="mt-3">Prioritet 3: <strong>{{ odabir3 }}</strong></div>

              <div class="d-flex">
                <v-btn style="margin-left: -87px; margin-right:580px; top:25px;" @click="korak1=1; korak2=0"  class="text-capitalize mt-5 element-0" color="success">Nazad</v-btn>
                <v-btn style="top:25px;" type="submit" class="text-capitalize mt-5 element-0" color="success">Dalje</v-btn>
              </div>
            </v-card-text>
          </form>
        </v-card>
      </v-col>
 
      <v-col v-if="korak3==1" >
        <v-card style="top: 40px; width: 800px; left:125px">
          <v-card-text>
            <h3 class="title blue-grey--text text--darken-2 font-weight-regular">Vaši odabiri su poslani.</h3>
            <h6 class="subtitle-2 font-weight-light">Profesor će Vam konačni odabir poslati na e-mail adresu.</h6>
          </v-card-text>
        </v-card>
      </v-col>

  </v-container>
</template>

<script>
import axios from 'axios';
import jwtDecode from 'jwt-decode';
import jspdf from 'jspdf';

export default {
  name: "MojOdabir",

  data() {
    const token = localStorage.usertoken;
    const decoded = jwtDecode(token);
    return{
      id: decoded.identity.id,
      ime: decoded.identity.ime,
      prezime: decoded.identity.prezime,
      email: decoded.identity.email,
      godina: decoded.identity.godina,
      smjer: decoded.identity.smjer,
      jmbag: decoded.identity.jmbag,
      vrsta_studija: decoded.identity.vrsta_studija,
      odabir1: '',
      odabir2: '',
      odabir3: '',
      editForm: {
        id: '',
        kontakt_osoba: '',
        naziv_poduzeca: '',
        zadatak_studenta: '',
        preferirane_tehnologije: '',
        broj_studenta: '',
        preferencije: '',
        potrebna_infrastruktura: '',
        broj_sati: '',
        lokacija: '',
        vrijeme_pocetka: '',
        angazman_nastavnika: '',
        dodatna_napomena: '',
      },
      poslodavac: [],
      projekti: [],
      selected: [],
      clicked: 0,
      alert: 0,
      korak1: 1,
      korak2: 0,
      korak3: 0,

      errorMessage: '',
    }
  },
  methods: {

    generatePDF(){
      //this.tryer = 's';
      
      const logo = require('@/assets/unipu.jpg')

      var imgLogo = new Image()
      imgLogo.src = logo

      let doc = new jspdf();
      
      doc.addImage(imgLogo, 'PNG', 0, 40, 24, 8)
      doc.text('Natjecanje: ' + this.odabir1, 10, 20);
      doc.text('Ekipa B: ', 15, 150);

      doc.save("export77.pdf");
    },

    ObrisiFavorita(favoritID) {
      const path = `http://localhost:8000/favoriti/${favoritID}`;
      axios.delete(path)
      .then(() => {
        this.DohvatiProjekte();
      })
      .catch((error) => {
        console.error(error);
      });
    },
    prebaci(){
      this.korak1 = 0;
      this.korak2 = 1;
    },
    DohvatiProjekte() {
    axios.get(`http://localhost:8000/favoriti/${this.id}`).then((response) => {
      this.projekti = response.data;
    })
    .catch((e) => {
      console.error(e);
    });
    },
    DodajOdabir() {
      axios.post('http://localhost:8000/odabir', {
        ime: this.ime,
        prezime: this.prezime,
        email: this.email,
        godina: this.godina,
        smjer: this.smjer,
        jmbag: this.jmbag,
        vrsta_studija: this.vrsta_studija,
        odabir1_ime_projekta: this.odabir1,
        odabir2_ime_projekta: this.odabir2,
        odabir3_ime_projekta: this.odabir3,
      }).then((res) => {
        this.clicked = 1;
        this.alert = 1;
        console.log(res);
      }).catch((err) => {
        this.errorMessage = 'Vaš odabir je zaprimljen, profesor će vam odgovoriti u najkraćem roku.';
        this.korak3=0;
        this.korak2=1;
        console.log(err);
      });
    },
    Detalji(projektID) {
      this.editForm = projektID;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      const payload = {
        kontakt_osoba: this.editForm.kontakt_osoba,
        naziv_poduzeca: this.editForm.naziv_poduzeca,
        zadatak_studenta: this.editForm.zadatak_studenta,
        preferirane_tehnologije: this.editForm.preferirane_tehnologije,
        broj_studenta: this.editForm.broj_studenta,
        preferencije: this.editForm.preferencije,
        potrebna_infrastruktura: this.editForm.potrebna_infrastruktura,
        broj_sati: this.editForm.broj_sati,
        lokacija: this.editForm.lokacija,
        vrijeme_pocetka: this.editForm.vrijeme_pocetka,
        angazman_nastavnika: this.editForm.angazman_nastavnika,
        dodatna_napomena: this.editForm.dodatna_napomena,
      };
      this.updateBook(payload, this.editForm.id);
    },
  },
   created() {
    this.DohvatiProjekte();
  },
  
};
</script>
<style lang="scss" scoped>

  .projekti {
    bottom: 0px;
    margin-top: 20px;
  }

  .pa-5 {
    height: 235px;
  }

  .projekt-detalji-img {
    float:right;
  }

  .zadatak-studenta-h1 {
    font-size:16px;
    font-weight: regular;
    color: #102847;
    padding-bottom: 10px;
  }

  .person-icon {
    width: 20px;
    margin-right: 5px;
  }

  .calendar-icon {
    width: 20px;
    margin-right: 8px;
  }

  .time-icon {
    width: 18px;
    margin-right: 2px;
  }

  .modal-content {
    width: 650px;
    left: 100px;
  }

  .modal-body {
    padding-top: 50px;
    padding-left: 90px;
    padding-right: 90px;
    padding-bottom: 10px;
    bottom: 15px;
  }

  .podaci-lbl {
    font-size:14px;
  }
</style>