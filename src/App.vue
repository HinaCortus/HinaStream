<template>
  <div id="app">
    <header>
      <h1>Hina Stream</h1>
    </header>
    <main>
      <Input />
      <div class="split">
        <Announcements />
        <Map />
      </div>
    </main>
  </div>
</template>

<script>
import Input from './components/InputView.vue';
import Announcements from './components/AnnouncementsView.vue';
import Map from './components/MapView.vue';

export default {
  components: {
    Input,
    Announcements,
    Map,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

header {
  margin-bottom: 20px;
}

.split {
  display: flex;
  flex-direction: row;
}

.split > * {
  flex: 1;
  padding: 10px;
  border-left: 1px solid #ccc;
}

.split > *:first-child {
  border-left: none;
}

/* Responsive styles */
@media (max-width: 600px) {
  .split {
    flex-direction: column;
  }
}
</style>
