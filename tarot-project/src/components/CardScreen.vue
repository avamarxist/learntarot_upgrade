<template>
    <div>
        <h2> {{card.title}} </h2>
        <ActionsContainer v-bind:card="card" />
        <br>
        <DescriptionContainer v-bind:card="card" />
        
    </div>
</template>

<script>
import ActionsContainer from ".\\ActionsContainer.vue";
import DescriptionContainer from ".\\DescriptionContainer.vue";

export default {
    name:"CardScreen",
    components:{
        ActionsContainer,
        DescriptionContainer
    },
    props: ['card'],
}
</script>

<style scoped>

</style>
