<template>
  <div>
    <v-app-bar app clipped-left clipped-right color="#102847" dark>    
      <v-toolbar-title class="align-center d-flex">
        <h5 class="naslov-aplikacije">Aplikacija za provođenje studentske prakse</h5>
      </v-toolbar-title>
      <v-app-bar-nav-icon class="d-block d-md-none" @click="$vuetify.breakpoint.smAndDown ? setSidebarDrawer(!Sidebar_drawer) : $emit('input', !value)"/>
      <v-spacer />
      <b-button data-toggle="modal" data-target="#modal3" class="dodaj-projekt-btn" variant="outline-light">Dodaj projekt</b-button>
    </v-app-bar>

    <div class="modal fade bd-example-modal-lg" id="modal3" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Obrazac za objavu projekta</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form v-on:submit.prevent="DodajProjekt">
              <div class="form-group">
                <label for="naziv-poduzeca">Naziv poduzeća </label>
                <label class="zvjezdica-lbl">*</label>
                <input type="text" v-model="naziv_poduzeca" class="form-control" name="ime" placeholder="" required>
              </div>
              <div class="form-group">
                <label for="kontakt-osoba">Kontakt osoba (+mail, telefon) </label>
                <label class="zvjezdica-lbl">*</label>
                <p class="projekt-podatci-p">Osoba kojoj će se student obratiti pri započinjanju studentske prakse oko dogovora. Ne mora nužno biti budući mentor.</p>
                <input type="text" v-model="kontakt_osoba" class="form-control" name="ime" placeholder="" required>
              </div>
              <div class="form-group">
                <label for="zadatak-studenta">Zadatak studenta</label>
                <label class="zvjezdica-lbl">*</label>
                <p class="projekt-podatci-p">Opis zadatka koji bi student izvršavao. Može biti: mala (web, mobilna, desktop) aplikacija, program za obradu podataka,
                analiza podataka, poboljšanje postojećeg koda (engl. code refactoring), pomoć pri održavanju računalne ili aplikacijske
                infrastrukture - DevOps poslovi, ... Preporuča se što detaljniji opis kako bi mogli alocirati idealnog kandidata. </p>
                <textarea type="text" v-model="zadatak_studenta" class="form-control" name="prezime" placeholder="" required></textarea>
              </div>
              <div class="form-group">
                <label for="preferirane-tehnologije">Preferirane tehnologije</label>
                <p class="projekt-podatci-p">Što sve koristi vaša tvrtka? Npr. PHP, Laravel, Python, Django, JavaScript, Vue.js, Unity, WordPress, TensorFlow, ...</p>
                <textarea type="text" v-model="preferirane_tehnologije" class="form-control" name="email" placeholder=""></textarea>
              </div>
              <div class="form-group">
                <label for="broj-studenta">Broj studenata</label>
                <label class="zvjezdica-lbl">*</label>
                <p class="projekt-podatci-p">Koliko studenata možete primiti u rješavanju ovog zadatka? Studenti mogu raditi odvojeno ili u timu. Ako imate više zadataka,
                možete ponovno popuniti  formu za svaki zadatak posebno.</p>
                <input type="text" v-model="broj_studenta" class="form-control" name="lozinka" placeholder="" required>
              </div>
              <div class="form-group">
                <label for="preferencije">Preferencije pri odabiru studenta</label>
                <p class="projekt-podatci-p">Ukoliko smatrate važnim, opišite odlike poželjnog kandidata na praksi.</p>
                <textarea type="text" v-model="preferencije" class="form-control" name="naziv_poduzeca" placeholder=""></textarea>
              </div>
              <div class="form-group">
                <label for="potrebna-infrastruktura">Potrebna infrastruktura koju student mora posjedovati</label>
                <input type="text" v-model="potrebna_infrastruktura" class="form-control" name="oib_poduzeca" placeholder="">
              </div>
              <div class="form-group">
                <label for="broj-sati">Željeno trajane prakse</label>
                <label class="zvjezdica-lbl">*</label>
                <p class="projekt-podatci-p">Preporučeno trajanje studentske prakse je između 90 i 150 radnih sati. U dogovoru sa studentom može se kasnije taj angažman produljiti.
                Dogovor kako će se izvršiti tih 90-150 sati je između vas i studenta (npr. koncentrirano u 2-3 tjedna ili par puta tjedno kroz dulje vrijeme).</p>
                <input type="text" v-model="broj_sati" class="form-control" name="mjesto" placeholder="" required>
              </div>
              <div class="form-group">
                <label for="lokacija">Lokacija održavanja studentske prakse </label>
                <label class="zvjezdica-lbl">*</label>
                <input type="text" v-model="lokacija" class="form-control" name="web" placeholder="" required>
              </div>
              <div class="form-group">
                <label for="vrijeme-pocetka">Željeno okvirno vrijeme početka</label>
                <p class="projekt-podatci-p">Praksa se mora obaviti do kraja 8. mjeseca 2020. godine.</p>
                <input type="text" v-model="vrijeme_pocetka" class="form-control" name="web" placeholder="">
              </div>
              <div class="form-group">
                <label for="angazman-nastavnika">Angažman nastavnika s FIPU</label>
                <p class="projekt-podatci-p">Po želji, nastavno  osoblje FIPU-a može pomoći pri izvođenju prakse na način da oni dijelom (ili u potpunosti) mentoriraju studenta.
                Moguće je čak da student u našem laboratoriju  obavlja s praksom, te povremeno dolazi prezentirati učinjeno.
                Ukoliko Vam je takva opcija interesantna, molimo da navedete Vaše potrebe.</p>
                <textarea type="text" v-model="angazman_nastavnika" class="form-control" name="web" placeholder=""></textarea>
              </div>
              <div class="form-group">
                <label for="dodatna-napomena">Dodatna napomena</label>
                <textarea type="text" v-model="dodatna_napomena" class="form-control" name="web" placeholder=""></textarea>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" style="background-color: #102847;" data-dismiss="modal">Odustani</button>
                <button type="submit" class="btn btn-secondary" style="background-color: #102847;">Dodaj projekt</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div> 
  </div>
</template>


<script>
import { mapState, mapMutations } from "vuex";
import axios from 'axios';
import jwtDecode from 'jwt-decode';

export default {
  name: "HeaderPoslodavac",

  components: {},

  props: {
    value: {
      type: Boolean,
      default: false
    }
  },

  data() {
    const token = localStorage.usertoken;
    const decoded = jwtDecode(token);
      return {
        id: decoded.identity.id,
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
    DodajProjekt() {
      axios.post('http://localhost:8000/projekt', {
        kontakt_osoba: this.kontakt_osoba,
        naziv_poduzeca: this.naziv_poduzeca,
        zadatak_studenta: this.zadatak_studenta,
        preferirane_tehnologije: this.preferirane_tehnologije,
        broj_studenta: this.broj_studenta,
        preferencije: this.preferencije,
        potrebna_infrastruktura: this.potrebna_infrastruktura,
        broj_sati: this.broj_sati,
        lokacija: this.lokacija,
        vrijeme_pocetka: this.vrijeme_pocetka,
        angazman_nastavnika: this.angazman_nastavnika,
        dodatna_napomena: this.dodatna_napomena,
        poslodavac_id: this.id,
      }).then((res) => {
        this.$router.go();
        console.log(res);
      }).catch((err) => {
        console.log(err);
      });
    },
  }
};
</script>

<style lang="scss" scoped>
  .naslov-aplikacije {
      font-size: 17px;
      margin-top: 10px;
      margin-left: 10px;
  }

  .dodaj-projekt-btn {
    font-size: 13px;
    margin-right: 10px;
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

  .projekt-podatci-p {
    font-size:11px;
    top: 20px;
  }

  .modal-footer {
    padding-right:0px;
    padding-left:0px;
    padding-top:20px;
    padding-bottom:15px;
  }
</style>