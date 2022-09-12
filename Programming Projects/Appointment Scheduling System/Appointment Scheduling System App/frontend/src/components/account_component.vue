<template>
    <div class="container">
        <div class="row vh-100 align-items-center justify-content-center">
            <div class="col-sm-8 col-md-6 col-lg-4 bg-white rounded shadow-lg">
                <div class="row justify-content-center mb-4 rounded" id="logoBackground">
                    <img src="../assets/SAOH_logo.png">
                </div>
                <div style="padding-left: 35px; padding-right: 35px;">
                    <div class="mb-4" id="heading">
                        <h1 class="display-6 text-center">Password Reset</h1>
                    </div>
                    <div class="">
                        <i v-if="this.noUser == true" class="fa-solid fa-triangle-exclamation" id="errorImage"></i>
                        <p v-if="this.noUser == true" id="errorText">Incorrect username or password.</p>
                    </div>
                    <div class="mb-4">
                        <label for="username" class="form-label">Username</label>
                        <input v-model="this.resetData.username" type="username" class="form-control" id="username">
                    </div>
                    <div class="mb-4">
                        <label for="password" class="form-label">Current Password</label>
                        <input v-model="this.resetData.currentPassword" type="password" class="form-control" id="password">
                    </div>
                    <div class="mb-4">
                        <label for="confirmPassword" class="form-label">New password</label>
                        <input v-model="this.resetData.newPassword" type="password" class="form-control">
                    </div>
                    <div class="mb-4">
                        <label for="confirmPassword" class="form-label">Confirm password</label>
                        <input v-model="this.resetData.confirmNewPassword" type="password" class="form-control">
                        <small v-if="this.resetData.confirmNewPassword != '' && this.resetData.confirmNewPassword != this.resetData.newPassword" id="phoneHelpBlock" class="form-text text-muted">
                                passwords must match
                        </small>
                    </div>
                    <button v-if="this.resetData.newPassword == this.resetData.confirmNewPassword && this.resetData.username != '' && this.resetData.currentPassword != '' &&  this.resetData.newPassword != '' && this.resetData.confirmNewPassword != ''" type="submit" @click="resetPassword()" class="mt-2 btn btn-dark w-100">Reset</button>
                    <button v-else type="submit" class="mt-2 btn btn-dark w-100" disabled>Reset</button>
                </div>
                <div class="mt-3 mb-3 text-center"><button v-on:click="this.$parent.toggle()" class="buttonlink">Return to login</button></div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'account_component',
    data() {
            return {
                resetData: {
                    username: '',
                    currentPassword: '',
                    newPassword: '',
                    confirmNewPassword: ''
                },
                noUser: false,
            }
        },
    methods: {
        resetPassword() {
            let apiURL = 'http://localhost:3000/login/passwordReset'
            axios.put(apiURL, this.resetData).then(res => {
                if (res.data == 'no user found') {
                    this.noUser = true
                }
                if (res.data == 'reset success') {
                    this.noUser = false
                    alert('Password reset successful. You may now login with your new credentials.')
                    this.$parent.toggle()
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
