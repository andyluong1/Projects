<template>
    <div class="bg-image" style="height: 100vh; width: 100vw;" id="loginBackground">
        <component :is="component" />
    </div>
</template>

<script>
import login_component from '../components/login_component.vue'
import account_component from '../components/account_component.vue'

export default {
    components: {
        login_component,
        account_component
    },
    data() {
        return {
            component: 'login_component'
        }
    },
    methods: {
        toggle() {
            if (this.component === 'login_component') {
                this.component = 'account_component'
            }
            else {
                this.component = 'login_component'
            }
        }
    } 
}
</script>

<style scoped>
#loginBackground {
    background-image: url("../assets/login_background.png");
    background-repeat: no-repeat;
    background-size: cover;
};
</style>