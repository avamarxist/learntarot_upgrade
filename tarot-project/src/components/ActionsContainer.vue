<template>
    <div>
        <button v-on:click="actToggle=!actToggle"> Keywords </button>
        <Actions v-for="act in card.actions" v-bind:key="act.id" v-bind:act="act" v-if="actToggle===true" />
    </div>
</template>

<script>
import Actions from './Actions.vue';

export default {
    name:"ActionsContainer",
    components:{ 
        Actions
    },
    data(){
        return{
            actToggle: false
        }
    },
    props:['card']
}
</script>

<style scoped>

</style>
