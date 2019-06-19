<template>
    <div class='button-container'>
        <button v-on:click="$emit('card-pick',card.cardID)"  >{{card.title}} </button>
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

