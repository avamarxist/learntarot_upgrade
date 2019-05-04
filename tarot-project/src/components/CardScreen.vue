<template>
    <div>
        <h2> {{card.title}} </h2>
        <p> {{card.description}} </p>
    </div>
</template>

<script>
import {CardInfo} from '..\\assets\\tarot_cards.js';

export default {
    name:"CardScreen",
    props: ['card'],
    data(){
        return{
            cards: CardInfo
        }
    }
}
</script>

<style scoped>

</style>
