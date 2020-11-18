<template>
  <v-app id="login">
    <v-main class="background-login">
      <v-img src="http://legacy.fime.uanl.mx/template/images/web/cidet.jpg">
      <v-container fluid fill-height>
        <v-layout justify-center align-center>
          <v-flex xs12 sm12 md8>
            <v-layout wrap>
              <v-flex xs12 sm12 md6 class="d-flex align-content-center flex-wrap">
              </v-flex>
              <v-flex xs12 sm12 md6>
                <v-form @submit.prevent="submit">
                  <v-card class="rounded-xl" color="success" elevation="5" dark>
                    <v-card-title class="headline pl-5 font-weight-bold">Iniciar sesión</v-card-title>
                    <v-card-text>
                      <v-text-field v-model="username" :disabled="loading" prepend-icon="mdi-account" required autocomplete="off"
                      label="Correo" @input="$v.username.$touch()" @blur="$v.username.$touch()">
                      </v-text-field>
                      <v-text-field v-model="password" type="password" :disabled="loading" prepend-icon="mdi-lock" required autocomplete="off"
                      label="Contraseña" @input="$v.password.$touch()" @blur="$v.password.$touch()">
                      </v-text-field>
                      <v-btn text small :disabled="loading" style="text-transform: none !important;" @click="">¿Has olvidado tu contraseña?</v-btn>
                    </v-card-text>
                    <v-card-actions>
                      <div class="pl-3">v{{ version }}</div>
                      <v-spacer></v-spacer>
                      <v-btn type="submit" text :to="{ name: 'Revisar'}" :loading="loading">Entrar</v-btn>
                    </v-card-actions>
                  </v-card>
                </v-form>
                <v-snackbar v-model="error" color="error" :timeout="2500" bottom right>
                  {{ message }}
                </v-snackbar>
              </v-flex>
            </v-layout>
          </v-flex>
        </v-layout>
      </v-container>
          </v-img>
    </v-main>
    <main-footer/>
  </v-app>
</template>

<script>
import { mapActions } from 'vuex'


export default {
  name: 'login',
  data: () => ({
    version: process.env.VUE_APP_VERSION,
    loading: false,
    error: false,
    message: '',
    host: process.env.VUE_APP_API_SERVER,
    path: '/pub/login',
    username: '',
    password: '',
  }),
  computed: {
    usernameErrors() {
      const errors = []
      if (!this.$v.username.$dirty) return errors
      !this.$v.username.required && errors.push('El campo es obligatorio')
      !this.$v.username.maxLength && errors.push('El campo excede la longitud máxima')
      return errors
    },
    passwordErrors() {
      const errors = []
      if (!this.$v.password.$dirty) return errors
      !this.$v.password.required && errors.push('El campo es obligatorio')
      !this.$v.password.maxLength && errors.push('El campo excede la longitud máxima')
      return errors
    }
  },
  methods: {
    ...mapActions('general', [
      'newUser',
    ]),
    clear() {
      this.$v.$reset()
      this.username = ''
      this.password = ''
    },
    forgot() {
      this.$router.push('/forgot')
    },
    submit() {
      this.$v.$touch()
      if (!this.$v.$invalid) {
        this.login()
      }
      else {
        this.error = true
        this.message = 'Algunos datos del formulario son incorrectos'
      }
    },
    login() {
      this.loading = true
      setTimeout(() => {
        this.axios.post(this.host + this.path, { 
          data: {
            email: this.username, 
            password: this.password,
            dispositivo: {
              idunico: '0',
              modelo: '0',
              sistema_operativo: '0'
            }
          }
        })
          .then(response => {
            let res = response.data
            this.$session.start()
            this.$session.set('jwt', res.token)
            this.newUser({ usr_nm: this.username })
            this.$router.push('/admin/home')
          })
          .catch(error => {
            this.error = true
            this.message = 'Falta de internet /No conexión al WS'
          })
          .finally(() => {
            this.loading = false
          })
      }, 300)
    }
  }
}
</script>

<style scoped>
  .background-login {
    background-color: white !important;
  }
</style>