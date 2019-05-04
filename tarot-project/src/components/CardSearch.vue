<template>
    <div id='cardlist'>
        <h1> Pick a card </h1>
        <SuitButton v-on:change-suit="suitSelect=$event"></SuitButton>
        <CardList v-bind:suit="suitSelect" />
    </div>   
</template>

<script>
import {CardInfo} from '..\\assets\\tarot_cards.js';
import CardList from '.\\CardList.vue';
import SuitButton from '.\\SuitButton.vue';
import ListButton from '.\\ListButton.vue';

const Details = {};
console.log('Suit selected: ')
export default {
    components:{
        CardList,
        SuitButton,
        ListButton
    },
    name: "CardSearch",
    props: [],
    data(){
        return{
            cards: CardInfo,
            suitSelect: 'Major'
        }
    },
    methods: {
        changeSuit(newSuit){
            console.log("changeSuit has run");
            this.suitSelect = newSuit;
        }
    } 
}
</script>

<style scoped>

</style>
