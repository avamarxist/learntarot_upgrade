<template>
    <div>
        <p v-on:click="subactToggle=!subactToggle"><b>{{act.act}}</b></p>
        <div v-if="subactToggle === true">
            <li v-for="subaction in act.sub" v-bind:key="subaction.id"> {{subaction}} </li>
        </div>
    </div>
</template>

<script>
export default {
    name:"Actions",
    props:['card','act'],
    data(){
        return{
            subactToggle: false
        }
    }
}
</script>
