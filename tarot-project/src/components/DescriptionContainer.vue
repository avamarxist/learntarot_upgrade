<template>
    <div>
        <button v-on:click="descToggle=!descToggle"> Extended Description </button>
        <p v-if="descToggle===true" > {{card.description}} </p>
    </div>
</template>

<script>
export default {
    name: "DescriptionContainer",
    props: ['card'],
    data(){
        return{
            descToggle: false
        }
    }
}
</script>

<style scoped>

</style>
