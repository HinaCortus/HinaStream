<template>
  <div>
    <h2>Annonces</h2>
    <div v-for="ad in ads" :key="ad.id" class="ad-block">
      <h3>{{ ad.title }}</h3>
      <p><strong>Prix:</strong> {{ ad.price }} €</p>
      <p><strong>Surface:</strong> {{ ad.surface }} m²</p>
      <p><strong>Adresse:</strong> {{ ad.street }}, {{ ad.city }}, {{ ad.department }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      ads: [
      {
        "id": 1,
        "title": "Appartement T2",
        "price": 500,
        "surface": 45,
        "street": "Rue de la Paix",
        "city": "Paris",
        "department": "75"
      },
      {
        "id": 2,
        "title": "Maison individuelle",
        "price": 1500,
        "surface": 120,
        "street": "Avenue des Champs-Élysées",
        "city": "Paris",
        "department": "75"
      },
    ]
    };
  },
  created() {
    this.fetchAds();
  },
  methods: {
    async fetchAds() {
      try {
        const response = await fetch('/api/ads');
        const data = await response.json();
        this.ads = data.ads;
      } catch (error) {
        console.error('Error fetching ads:', error);
      }
    },
  },
};
</script>

<style scoped>
.ad-block {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 4px;
  background-color: #f9f9f9;
}

.ad-block h3 {
  margin-top: 0;
}

.ad-block p {
  margin: 5px 0;
}
</style>
