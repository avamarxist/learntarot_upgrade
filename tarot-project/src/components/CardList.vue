<template>
    <div id='card-list'>
        <button v-for="card in filterSuit(cards,suit)" v-bind:key="card.cardID">{{card.title}}</button>

    </div>
</template>

<script>
import {CardInfo} from '..\\assets\\tarot_cards.js';
export default {
    name:'CardList',
    props:['suit'],
    data(){
        return{
            cards:CardInfo
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

