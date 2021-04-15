<template>

<div class="bg-gray-100">
<!-- card start-->
 <div >
  <div class="p-6 max-w-sm m-4 bg-white rounded-xl shadow-md flex items-center space-x-4 ">
  <div class="flex-shrink-0">
    <img class="h-12 w-12" src="../assets/img/chaticon.svg" alt="ChitChat Logo">
  </div>
  <div>
    <div class="text-2xl font-medium text-black font-bold">{{posts[0].name}}</div>
    <p class="text-gray-400 text-sm">{{posts[0].description}}</p>
    <small>Created: <strong>15-04-2020</strong> Last Change: <strong>15-04-2021</strong> </small>
  </div>
</div>
</div>
 <!-- card start end-->
<!-- card start-->

  <div class="p-6 max-w-sm m-4 bg-white rounded-xl shadow-md flex items-center space-x-4 ">
  <div class="flex-shrink-0">
    <img class="h-12 w-12" src="../assets/img/chaticon green.svg" alt="ChitChat Logo">
  </div>
  <div>
    <div class="text-2xl font-medium text-black font-bold">{{posts[1].name}}</div>
    <p class="text-gray-400 text-sm">{{posts[1].description}}
</p>
    <small>Created: <strong>15-04-2020</strong> Last Change: <strong>15-04-2021</strong> </small>
  </div>
</div>

 <!-- card start end-->

 </div>

</template>


<script>
import axios from 'axios';

export default {
  name:'LeftNavBar',
  data() {
    return {
      posts: [],
      errors: []
    }
  },

  // Fetches posts when the component is created.
  async created() {
    try {
      const response = await axios.get(`/api`)
      this.posts = response.data.goals
    } catch (e) {
      this.errors.push(e)
    }
  }
}
</script>

<style>
.card{
  width: 450px;
  height: 300px;
}
</style>