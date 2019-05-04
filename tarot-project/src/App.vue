<template>
  <div id="app">
    <CardSearch v-bind:cards = "cardData" />
  </div>
</template>

<script>
import {CardInfo} from '.\\assets\\tarot_cards.js';
import CardSearch from '.\\components\\CardSearch.vue';
import CardList from '.\\components\\CardList.vue';
import SuitButton from '.\\components\\SuitButton.vue';

console.log('hello');
console.log(CardInfo);

// var Cards = JSON.parse(CardInfo);

export default {
  name: 'app',
  components: {
    CardSearch,
    CardList,
    SuitButton
  },
  data(){
      return {
        cardData: CardInfo
      }
    }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

  function newFunction() {
    return JSON.parse(".\\assets\\tarot_cards.js");
  }
