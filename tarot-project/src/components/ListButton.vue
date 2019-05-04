<template>
    <div>
        <button v-on:click="$emit('card-pick',card.cardID)"> {{card.title}} </button>
    </div>
</template>

<script>
export default {
    name:"ListButton",
    props:['card']
}
</script>

<style scoped>

</style>

