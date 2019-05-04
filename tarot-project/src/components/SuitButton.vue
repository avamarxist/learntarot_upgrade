<template>
    <div>
        <button v-for="suit in suits" v-bind:key=suit v-on:click="$emit('change-suit',suit)"> {{suit}} </button>

    </div>
</template>

<script>
export default {
    name:'SuitButton',
    data(){
        return { 
            suits:['Major', 'Cups', 'Pentacles', 'Swords', 'Wands'] 
        }
    }
}
</script>

<style>

button {
    font-size:25;
}

</style>

