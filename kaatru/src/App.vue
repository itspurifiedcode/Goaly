<template>
  <div class="flex mb-4 relative ">
    <div class="hidden md:block w-20 p-4 fixed h-full bg-white z-10 bg-blue-600 ">
      <LeftLogoBar />
    </div>

    <div class="flex w-full relative bg-white">
      <LeftNavBar />
      <MainWindow />
    </div>
  </div>
</template>

<script>
import LeftNavBar from "./components/LeftNavBar";
import LeftLogoBar from "./components/leftLogoBar";
import MainWindow from "./components/MainWindow.vue";
export default {
  name: "App",
  components: {
    LeftNavBar,
    LeftLogoBar,
    MainWindow,
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap");
#app {
  font-family: "Poppins", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #d7d7d8;
  margin-top: 60px;
}
body {
  font-family: "Poppins", sans-serif;
}
.logo {
  color: #000;
}
</style>
