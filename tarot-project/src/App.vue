<template>
  <div id="app">
    <h1>Sexy Unique Internet Tarot</h1>   
    <CardScreen v-bind:card="getCard()" v-if="cardPicked === true" />
    <p>{{lastClicked}} </p>
    <RadialMenu class="SuitMenu"
            style=" background-color: white;"
            :size="15"
            :itemSize="20"
            :radius="20"
            :rotate="90"
            :angle-restriction="360"
            v-on:card-list-toggle="function(){this.suitPicked=false;}">

            <RadialMenuItem 
                v-for="(item, index) in suits" 
                :key="index" 
                style="background-color: white" 
                @change-suit='function(){handleClick(item)}'>
                <button>{{item}}</button>
            </RadialMenuItem>
        </RadialMenu>
        <CardList v-bind:suit="lastClicked" v-on:card-pick="cardPick($event)" v-if="cardPicked === false && suitPicked === true" />
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
      suitPicked: false,
      cardPicked: false,
      cardSelect: ""
    }
  },
  methods: {
    handleClick(item) {
      console.log("radial clicked");
      this.lastClicked = item;
      this.suitPicked = true;
      this.changeSuit(item);
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
    },
    listClose(){
        this.suitPicked = false;
    }
  }
}
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display:flex;
  flex-direction:column;
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