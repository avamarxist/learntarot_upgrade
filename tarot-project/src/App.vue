<template>
  <div id="app">
    <h1>Sexy Unique Internet Tarot</h1>
    <CardList v-bind:suit="lastClicked" v-on:card-pick="cardPick($event)"  />
    <CardScreen v-bind:card="getCard()" v-if="cardPicked === true" />
    <RadialMenu
            style=" background-color: white;"
            :size="15"
            :itemSize="20"
            :radius="20"
            :rotate="90"
            :angle-restriction="360">

            <RadialMenuItem 
                v-for="(item, index) in suits" 
                :key="index" 
                style="background-color: white" 
                @click='function(){handleClick(item)}'>
                <span>{{item}}</span>
            </RadialMenuItem>
        </RadialMenu>
  </div>
</template>

<script>
import {CardInfo} from './assets/tarot_cards.js';
import CardSearch from './components/CardSearch.vue';
import CardList from './components/CardList.vue';
import SuitButton from './components/SuitButton.vue';
import ListButton from './components/ListButton.vue';
import CardScreen from './components/CardScreen.vue';
import ActionsContainer from './components/ActionsContainer';
import Actions from './components/Actions';
import DescriptionContainer from './components/DescriptionContainer';
import RadialMenu from './components/RadialMenu';
import RadialMenuItem from './components/RadialMenuItem'

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
    DescriptionContainer,
    RadialMenu,
    RadialMenuItem
  },

  data(){
    return {
      suits:['Major', 'Cups', 'Pentacles', 'Swords', 'Wands'], 
      lastClicked: 'Please select a suit',
      cards: CardInfo,
      suitSelect: 'Major',
      cardPicked: false,
      cardSelect: ""
    }
  },
  methods: {
    handleClick(item) {
      this.lastClicked = item;
    },
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

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0;
  width: 100vw;
  height: 100vh;
  box-sizing: border-box;
  background-color: rgba(102, 101, 101, 0.3);
  position: absolute;
  top: 0;
  left: 0;
}
</style>