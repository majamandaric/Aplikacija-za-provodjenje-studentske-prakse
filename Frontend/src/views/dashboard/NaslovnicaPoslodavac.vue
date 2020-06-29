<template>
  <v-container fluid class="down-top-padding">
    <v-row style="margin-bottom: 180px;">
      <v-col class="projekti" cols="12" lg="6" v-for="post of pageOfItems" v-bind:key="post.id">
        <v-card>
          <v-card-text class="pa-5">
            <a data-toggle="modal" data-target="#modal1" @click="UrediProjekt(post)"> 
              <img border="0" class="projekt-detalji-img" src="https://cdn4.iconfinder.com/data/icons/pictype-free-vector-icons/16/more-512.png" width="22" height="22">
            </a>
            <h1 class="zadatak-studenta-h1">{{post.zadatak_studenta}}</h1>
            <div class="d-flex align-center justify-center border-top pt-4">
              <v-sparkline :fill="fill" height="145px" :gradient="gradient" :line-width="width" :padding="padding" :smooth="radius || false" :value="value" auto-draw></v-sparkline>
            </div>
            <h6 class="subtitle-2 font-weight-light"><b>Naziv poduzeća: </b>{{post.naziv_poduzeca}} </h6>
            <h6 class="subtitle-2 font-weight-light"><b>Tehnologije: </b>{{post.preferirane_tehnologije}}</h6>
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
                  <b-button v-b-popover.hover.top="'Izmjeni'" type="button" variant="secondary" size="sm" class="izmjeni-btn" data-toggle="modal" data-target="#modal2" @click="UrediProjekt(post)">
                    <b-icon-pencil-square></b-icon-pencil-square>
                  </b-button>
                  <b-button v-b-popover.hover.top="'Arhiviraj'" type="button" variant="secondary" size="sm" class="arhiviraj-btn" @click="Arhiviraj(post); ObrisiProjekt(post.id)">
                    <b-icon-files></b-icon-files>
                  </b-button>
                </div>
              </b-col>
            </b-row>
          </v-card-text>
        </v-card>
      </v-col>

      <div class="pagination">
        <jw-pagination :items="projekti" @changePage="onChangePage" :styles="customStyles" ></jw-pagination>
      </div>
    </v-row>

    <div class="modal fade bd-example-modal-lg" id="modal2" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Izmijeni projekt</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <b-form @submit="onSubmitUpdate" class="w-100">
            <div class="modal-body">
              <!--  -->
              <b-form-group id="form-title-edit-group1" label-for="form-title-edit-input">
                <label>Naziv poduzeća</label><label class="zvjezdica-lbl">*</label>
                <b-form-input id="form-title-edit-input1" type="text" v-model="editForm.naziv_poduzeca" required placeholder="">
                </b-form-input>
              </b-form-group>
              <!--  -->
              <b-form-group id="form-title-edit-group" label-for="form-title-edit-input">
                <label>Kontakt osoba (+mail, telefon)</label><label class="zvjezdica-lbl">*</label>
                <b-form-input id="form-title-edit-input" type="text" v-model="editForm.kontakt_osoba" required >
                </b-form-input>
              </b-form-group>
              <!--  -->
              <b-form-group id="form-title-edit-group1" label-for="form-title-edit-input">
                <label>Zadatak studenta</label><label class="zvjezdica-lbl">*</label>
                <b-form-input id="form-title-edit-input1" type="text" v-model="editForm.zadatak_studenta" required placeholder="">
                </b-form-input>
              </b-form-group>
              <!--  -->
              <b-form-group id="form-title-edit-group2" label-for="form-title-edit-input">
                <label>Preferirane tehnologije</label>
                <b-form-input id="form-title-edit-input2" type="text" v-model="editForm.preferirane_tehnologije" required placeholder="">
                </b-form-input>
              </b-form-group>
              <!--  -->
              <b-form-group id="form-title-edit-group3" label-for="form-title-edit-input">
                <label>Broj studenata</label><label class="zvjezdica-lbl">*</label>
                <b-form-input id="form-title-edit-input3" type="text" v-model="editForm.broj_studenta" required placeholder="">
                </b-form-input>
              </b-form-group>
              <!--  -->
              <b-form-group id="form-title-edit-group4" label-for="form-title-edit-input">
                <label>Preferencije pri odabiru studenta</label>
                <b-form-input id="form-title-edit-input4" type="text" v-model="editForm.preferencije" required placeholder="">
                </b-form-input>
              </b-form-group>
              <!--  -->
              <b-form-group id="form-title-edit-group5" label-for="form-title-edit-input">
                <label>Potrebna infrastruktura koju student mora posjedovati</label>
                <b-form-input id="form-title-edit-input5" type="text" v-model="editForm.potrebna_infrastruktura" required placeholder="">
                </b-form-input>
              </b-form-group>
              <!--  -->
              <b-form-group id="form-title-edit-group6" label-for="form-title-edit-input">
                <label>Željeno trajane prakse</label><label class="zvjezdica-lbl">*</label>
                <b-form-input id="form-title-edit-input6" type="text" v-model="editForm.broj_sati" required placeholder="">
                </b-form-input>
              </b-form-group>
              <!--  -->
              <b-form-group id="form-title-edit-group7" label-for="form-title-edit-input">
                <label>Lokacija održavanja studentske prakse</label><label class="zvjezdica-lbl">*</label>
                <b-form-input id="form-title-edit-input7" type="text" v-model="editForm.lokacija" required placeholder="">
                </b-form-input>
              </b-form-group>
              <!--  -->
              <b-form-group id="form-title-edit-group8" label-for="form-title-edit-input">
                <label>Željeno okvirno vrijeme početka</label>
                <b-form-input id="form-title-edit-input8" type="text" v-model="editForm.vrijeme_pocetka" required placeholder="">
                </b-form-input>
              </b-form-group>
              <!--  -->
              <b-form-group id="form-title-edit-group9" label-for="form-title-edit-input">
                <label>Angažman nastavnika s FIPU</label>
                <b-form-input id="form-title-edit-input9" type="text" v-model="editForm.angazman_nastavnika" required placeholder="">
                </b-form-input>
              </b-form-group>
              <!--  -->
              <b-form-group id="form-title-edit-group10" label-for="form-title-edit-input">
                <label>Dodatna napomena:</label>
                <b-form-input id="form-title-edit-input10" type="text" v-model="editForm.dodatna_napomena" required placeholder="">
                </b-form-input>
              </b-form-group>
              <div class="modal-footer">
                <b-button type="button" class="odustani-btn" data-dismiss="modal">Odustani</b-button>
                <b-button type="submit" class="izmjeni-btn2" variant="secondary">Izmjeni</b-button>
              </div>
            </div>
          </b-form>
        </div>
      </div>
    </div>

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
              <b-button type="button" class="nazad-btn" data-dismiss="modal">Nazad</b-button>
            </div>
          </div>
        </div>
      </div>
    </div>

  </v-container>
</template>


<script>
import axios from 'axios';
import jwtDecode from 'jwt-decode';

const customStyles = {
    ul: {
        background: '#102847',
    },
};

export default {

  name: "BasicDashboard",

  data() {
    const token = localStorage.usertoken;
    const decoded = jwtDecode(token);
    return {
      customStyles,
      token: localStorage.usertoken,
      projekti: [],
      id: decoded.identity.id,
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

      pageOfItems: []
    };
  },

  created() {
    this.DohvatiProjekte();
  },

  computed: {
  },

  methods: {
    onChangePage(pageOfItems) {
            this.pageOfItems = pageOfItems;
    },
    Arhiviraj(arhivaID) {
      this.editForm = arhivaID;
      axios.post('http://localhost:8000/arhiva', {
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
        poslodavac_id: this.id,
      }).then((res) => {
        console.log(res);
      }).catch((err) => {
        console.log(err);
      });
    },
    DohvatiProjekte() {
    axios.get(`http://localhost:8000/poslodavac/${this.id}/projekt`).then((response) => {
      this.projekti = response.data;
    })
    .catch((e) => {
      console.error(e);
    });
    },
    ObrisiProjekt(projektID) {
      const path = `http://localhost:8000/poslodavac/${this.id}/projekt/${projektID}`;
      axios.delete(path)
      .then(() => {
        this.DohvatiProjekte();
      })
      .catch((error) => {
        console.error(error);
      });
    },
    UrediProjekt(projektID) {
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
      this.AzurirajProjekt(payload, this.editForm.id);
    },
    AzurirajProjekt(payload, projektID) {
      const path = `http://localhost:8000/poslodavac/${this.id}/projekt/${projektID}`;
      axios.put(path, payload)
        .then(() => {
          this.$router.go();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  }
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

  .izmjeni-btn {
    margin-right:10px;
    background-color: #102847;
  }

  .arhiviraj-btn {
    background-color: #102847;
  }

  .pagination {
    margin-left:380px; 
    margin-top:30px;
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

   .form-group {
    margin-bottom: 25px;
    font-size: 16px;
  }

  .zvjezdica-lbl {
    color: red;
  }

  .modal-footer {
    padding-right:0px;
    padding-left:0px;
    padding-top:20px;
    padding-bottom:15px;
  }

  .odustani-btn {
  margin-right:0px;
  background-color: #102847;
  }

  .izmjeni-btn2 {
  margin-right:0px;
  background-color: #102847;
  }

  .podaci-lbl {
    font-size:14px;
  }

  .nazad-btn {
  margin-right:0px;
  background-color: #102847;
  }
</style>
