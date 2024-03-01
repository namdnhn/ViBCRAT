<template>
  <div class="w-6/12 mx-auto pb-10 border-2 border-grey">
    <div class="bg-teal-100 w-full">
      <h1
        class="flex justify-center mb-4 text-3xl pt-8 p-10 font-extrabold leading-none tracking-tight text-gray-900 md:text-4xl lg:text-5xl"
      >
        Breast Cancer Risk Assessment Tool
      </h1>
    </div>
    <div class="py-4">
      <router-link to="/info" class="bg-teal-500 hover:bg-teal-700 text-white font-bold py-2 px-4 rounded m-4">
        For American
      </router-link>
      <router-link to="/vietnam" class="bg-teal-500 hover:bg-teal-700 text-white font-bold py-2 px-4 rounded m-4">
        For Vietnamese
      </router-link>
    </div>
    <router-view></router-view>
  </div>
</template>

<script lang="ts" setup>
</script>
