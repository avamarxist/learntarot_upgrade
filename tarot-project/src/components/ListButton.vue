<template>
    <div class='button-container'>
        <!-- <button v-on:click="$emit('card-pick',card.cardID)"  >{{ imgPath }} </button> -->
        <img :src='imgPath(card)' height="50" width="50" @click="$emit('card-pick',card.cardID)">
        <p font-size='4pt'>{{ card.title }} </p>
    </div>
</template>

<script>
export default {
    name:"ListButton",
    props:['card', 'count'],
    data:function(){
        return {
            curid: this.$vnode.key
        }
    },
    computed:{
        imgSrc: function(){
            let id = this.card.cardID;
            return '../assets/' + id.slice(0,1) + '/' + id.slice(1,id.length) + '.png';
        }
    },
    methods:{
        imgPath(card){
            let id = card.cardID;

            return require('../assets/' + id.slice(0,1) + '/' + id.slice(1,id.length) + '.png');
        }
    }
}
</script>

<style scoped>
    button{
        align-content:center;
        align-items:stretch;
        width:2oopx;
        height:50px;
        display: flex;
        flex-direction: row;
    }
</style>

