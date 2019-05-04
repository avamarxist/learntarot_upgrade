<template>
    <div id='cardlist' >
        <h1> Pick a card </h1>
        <SuitButton v-on:change-suit="suitSelect=$event"></SuitButton>
        <CardList v-bind:suit="suitSelect" v-on:card-pick="cardPicked=true" v-show="cardPicked === false" />
        <img src="..\\assets\\pkn.png" width=50 v-on:click="cardPicked=false" v-show="cardPicked === true"> Go back to card list </img>
    </div>   
</template>

<script>
import {CardInfo} from '..\\assets\\tarot_cards.js';
import CardList from '.\\CardList.vue';
import SuitButton from '.\\SuitButton.vue';
import ListButton from '.\\ListButton.vue';

const Details = {};

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
            suitSelect: 'Major',
            cardPicked: false
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
