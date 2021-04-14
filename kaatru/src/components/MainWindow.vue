<template>
 
<div class="p-8  my-10 flex-auto">
   <h1 class="font-bold text-5xl">Design</h1> 
   <ul class="flex gap-20 mt-8 border-b-2 border-grey-200">
       <li class="font-bold mx-3 px-5 border-b-4 border-blue-500">Todo</li>
       <li class="font-medium mx-3 px-5">Notes</li>
       <li class="font-medium mx-3 px-5">Links</li>
       <li class="font-medium mx-3 px-5">Files</li>
   </ul>

    <ul class="p-10">
        <li class=" font-medium py-3 text-grey-500"><span class="flex"> <svg class="w-4 h-4 my-auto mx-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>Project Planning</span> </li>
        <li class=" font-medium py-3 text-grey-500"><span class="flex"> <svg class="w-4 h-4 my-auto mx-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>Today Page</span> </li>
    </ul>

</div>

</template>

<script>
export default {
    name:'MainWindow'
}
</script>