<template>
    <div>
        <Actions v-for="act in card.actions" v-bind:key="act.id" v-bind:act="act"/>
    </div>
</template>

<script>
import Actions from '.\\Actions.vue';

export default {
    name:"ActionsContainer",
    components:{
        Actions
    },
    props:['card']
}
</script>

<style scoped>

</style>
