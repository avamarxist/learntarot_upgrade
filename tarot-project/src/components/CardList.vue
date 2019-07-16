<template>
    <div id='card-list'>
        <ListButton v-for="(card,index) in filterSuit(cards,suit)" 
                    :key="index"
                    :ckey="index" 
                    :card='card'
                    :count='filterSuit(cards,suit).length'
                    v-on:card-pick="$emit('card-pick',$event)"> 
        </ListButton>
        
    </div>
</template>

<script>
import {CardInfo} from '../assets/tarot_cards.js';
import ListButton from './ListButton.vue';

export default {
    components:{
        ListButton
    },
    name:'CardList',
    props:['suit'],
    data(){
        return{
            cards:CardInfo,
            cardPicked:false
        }
    },
    methods:{
        filterSuit(cards, suit){
            return cards.filter(card => card.suit===suit);
        },
        cardCount(cards){
            return cards.filter(card=>card.suit === suit).length;
        },
    }
}
</script>

<style scoped>
#card-list {
    display:flex;
    flex-direction:row;
    flex-wrap:wrap;
    align-items:stretch;
}


</style>