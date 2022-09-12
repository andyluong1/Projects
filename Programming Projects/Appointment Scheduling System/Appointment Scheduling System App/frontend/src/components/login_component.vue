<template>
    <div class="container">
        <div class="row vh-100 align-items-center justify-content-center">
            <div class="col-sm-8 col-md-6 col-lg-4 bg-white rounded shadow-lg">
                <div class="row justify-content-center mb-4 rounded" id="logoBackground">
                    <img src="../assets/SAOH_logo.png">
                </div>
                <div style="padding-left: 35px; padding-right: 35px;">
                    <div class="mb-4" id="heading">
                        <h1 class="display-6 text-center">Dashboard Login</h1>
                    </div>
                    <div class="mb-4">
                        <label for="username" class="form-label">Username</label>
                        <input type="text" v-model="input.username" class="form-control" id="username" aria-describedby="usernameHelp">
                    </div>
                    <div class="mb-4">
                        <label for="password" class="form-label">Password</label>
                        <input type="password" v-model="input.password" class="form-control" id="password" aria-describedby="passwordHelp">
                    </div>
                    <div class="">
                        <i v-if="this.errors.incorrectLogin == true" class="fa-solid fa-triangle-exclamation" id="errorImage"></i>
                        <p v-if="this.errors.incorrectLogin == true" id="errorText">Incorrect username or password.</p>
                    </div>
                    <div class="mb-4 form-check">
                        <input checked type="checkbox" class="form-check-input" id="remember">
                        <label class="form-check-label" for="remember">Remember Me</label>
                    </div>
                    <button @click="login()" class="btn btn-dark w-100">Login</button>
                </div>
                <div class="mt-3 mb-3 text-center"><button v-on:click="this.$parent.toggle()" class="buttonlink">Reset password</button></div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from "axios"        
    export default {
        name: 'login_component',
        data() {
            return {
                input: {
                    username: localStorage.getItem('username'),
                    password: localStorage.getItem('password')
                },
                errors: {
                    incorrectLogin: false
                }
            }
        },
        methods: {
            login() {
                if (this.input.username == '' || this.input.password == '') {
                    this.errors.incorrectLogin = true
                    return
                } 
                //let apiURL = `http://localhost:3000/login/${this.input.username}/${this.input.password}`
                let apiURL = 'http://localhost:3000/login/' + encodeURIComponent(this.input.username) + '/' + encodeURIComponent(this.input.password)
                axios.get(apiURL).then(res => {
                    if (document.getElementById('remember').checked === true) {
                        localStorage.setItem('username', this.input.username)
                        localStorage.setItem('password', this.input.password)
                    }
                    if (document.getElementById('remember').checked === false) {
                        localStorage.setItem('username', '')
                        localStorage.setItem('password', '')
                    }
                    if (res.data[0] == true) {
                        window.sessionStorage.setItem('initials', res.data[2])
                        window.sessionStorage.setItem('name', res.data[3])
                        window.sessionStorage.setItem('profile', this.input.username)
                        window.sessionStorage.setItem('authenticated', 'true')
                        if (res.data[1] == 1) {
                            window.sessionStorage.setItem('adminPrivileges', 'true')
                            window.sessionStorage.setItem('privilege', 'write')
                        }
                        if (res.data[1] == 2 || res.data[1] == 3) {
                            window.sessionStorage.setItem('adminPrivileges', 'false')
                        }
                        if (res.data[1] == 2) {
                            window.sessionStorage.setItem('privilege', 'read')
                        }
                        if (res.data[1] == 3) {
                            window.sessionStorage.setItem('privilege', 'write')
                        }
                        this.$router.replace({ name: 'dashboard'})
                    }
                    if (res.data == false) {
                        this.errors.incorrectLogin = true
                    }
                })
            }
        }
    }
</script>

<style scoped>
.buttonlink {
    background-color: transparent;
    border: 0;
    color: #0ea6ed;
    padding: 0;
}

#logoBackground {
    background: rgb(255,255,255); 
    background: linear-gradient(0deg, rgba(255,255,255,1) 0%, rgba(0,181,255,1) 48%, rgba(65,100,233,1) 100%);
}

#errorImage {
    display: inline-block;
    margin-right: .5rem;
    color: #92150c;
}
#errorText {
    display: inline-block;
    color: #92150c;
}
</style>
