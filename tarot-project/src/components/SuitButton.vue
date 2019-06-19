<template>
    <div>
        <button v-for="suit in suits" v-bind:key=suit  :style="{ '--angle':rotAngle, '--skewangle':skewAngle }"> {{suit}} </button>

    </div>
</template>

<script>
export default {
    name:'SuitButton',
    data(){
        return { 
            suits:['Major', 'Cups', 'Pentacles', 'Swords', 'Wands'] 
        }
    },
    computed:{
        rotAngle: function(){
            let angle = this.$vnode.key * 360/5;
            console.log(this.count);
            let out = angle.toString() +'deg';
            return out
        },
        skewAngle: function(){
            let angle = 90 - 360/5;
            console.log(this.count);
            let out = angle.toString() +'deg';
            return out
        }
    }
}
</script>

<style scoped>

    button{
        /* width: 50px;
        height: 50px; */
        position:relative;
        /* top:20%;
        left:50%; */
        transform-origin: bottom right;
        /* transform:  translate(100px,200px) skew(var(--skewangle)) rotate(var(--angle)); */
    }

</style>

