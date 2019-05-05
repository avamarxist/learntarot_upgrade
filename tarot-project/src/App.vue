<template>
  <div id="app">
    <CardSearch />
  </div>
</template>

<script>
import {CardInfo} from '.\\assets\\tarot_cards.js';
import CardSearch from '.\\components\\CardSearch.vue';
import CardList from '.\\components\\CardList.vue';
import SuitButton from '.\\components\\SuitButton.vue';
import ListButton from '.\\components\\ListButton.vue';
import CardScreen from '.\\components\\CardScreen.vue';
import ActionsContainer from '.\\components\\ActionsContainer';
import Actions from '.\\components\\Actions';
import DescriptionContainer from '.\\components\\DescriptionContainer';

console.log('hello');
console.log(CardInfo);

// var Cards = JSON.parse(CardInfo);

export default {
  name: 'app',
  components: {
    CardSearch,
    CardList,
    SuitButton,
    ListButton,
    CardScreen,
    ActionsContainer,
    Actions,
    DescriptionContainer
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
