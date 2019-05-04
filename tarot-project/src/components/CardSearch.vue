<template>
    <div id='cardlist' >
        <h1> Sexy Unique Internet Tarot </h1>
        <SuitButton v-on:change-suit="suitSelect=$event"></SuitButton><br>
        <CardList v-bind:suit="suitSelect" v-on:card-pick="cardPick($event)" v-show="cardPicked === false" />
        
        <div v-show="cardPicked===true">
            <!-- <img src="..\\assets\\pkn.png" width=50 v-on:click="cardPicked=false">  -->
            <br>
            <button v-on:click="cardPicked=false">Go back to card selection</button>

        </div>
        <CardScreen v-bind:card="getCard()" v-show="cardPicked === true" />
    </div>   
</template>

<script>
import {CardInfo} from '..\\assets\\tarot_cards.js';
import CardList from '.\\CardList.vue';
import SuitButton from '.\\SuitButton.vue';
import ListButton from '.\\ListButton.vue';
import CardScreen from '.\\CardScreen.vue';

const Details = {};

export default {
    components:{
        CardList,
        SuitButton,
        ListButton,
        CardScreen
    },
    name: "CardSearch",
    props: [],
    data(){
        return{
            cards: CardInfo,
            suitSelect: 'Major',
            cardPicked: false,
            cardSelect: ""
        }
    },
    methods: {
        changeSuit(newSuit){
            console.log("changeSuit has run");
            this.suitSelect = newSuit;
        },
        cardPick(cardID){
            this.cardPicked = true;
            this.cardSelect = cardID;
        },
        getCard(){
            let pickedCard = this.cards.filter(card=>card.cardID==this.cardSelect);
            console.log(pickedCard); 
            return pickedCard[0];
        }
    } 
}

</script>

<style scoped>

</style>
