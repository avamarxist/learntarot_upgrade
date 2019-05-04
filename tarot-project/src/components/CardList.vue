<template>
    <div id='card-list'>
        <ListButton v-for="card in filterSuit(cards,suit)" 
                    v-bind:key="card.cardID" 
                    v-bind:title='card.title'
                    v-bind:cardID='card.cardID'
                    v-on:card-pick="$emit('card-pick')"> 
        </ListButton>
        
    </div>
</template>

<script>
import {CardInfo} from '..\\assets\\tarot_cards.js';
import ListButton from '.\\ListButton.vue';

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
        }
    }
}
</script>

<style scoped>
#card-list {
    display:flex;
    flex-direction:column;
}
button {
    font-size:25;
}

</style>

