<template>
    <div>
        <button v-on:click="$emit('card-pick')"> {{title}} {{cardID}}</button>
    </div>
</template>

<script>
export default {
    name:"ListButton",
    props:['title', 'cardID']
}
</script>

<style scoped>

</style>

