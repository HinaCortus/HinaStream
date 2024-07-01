<template>
    <div>
      <h2>Carte</h2>
      <div id="map" ref="map" style="width: 100%; height: 400px;"></div>
    </div>
  </template>
  
  <script>
  import L from 'leaflet';
  import 'leaflet/dist/leaflet.css';
  
  export default {
    data() {
      return {
        map: null,
        defaultCoordinates: {
          lat: 46.603354,
          lng: 1.888334,
        },
        defaultPlaces: [
          {
            name: "Tour Eiffel, Paris",
            lat: 48.8584,
            lng: 2.2945,
            icon: 'https://example.com/icon1.png'
          },
          {
            name: "Mont Saint-Michel, Normandie",
            lat: 48.6361,
            lng: -1.5115,
            icon: 'https://example.com/icon2.png'
          },
          {
            name: "Château de Versailles, Versailles",
            lat: 48.8049,
            lng: 2.1204,
            icon: 'https://example.com/icon3.png'
          },
          {
            name: "Côte d'Azur, Nice",
            lat: 43.7102,
            lng: 7.2620,
            icon: 'https://example.com/icon4.png'
          },
          {
            name: "Cathédrale Notre-Dame de Strasbourg, Strasbourg",
            lat: 48.5800,
            lng: 7.7500,
            icon: 'https://example.com/icon5.png'
          }
        ]
      };
    },
    mounted() {
      this.initializeMap();
    },
    methods: {
      async initializeMap() {
        let coordinates = this.defaultCoordinates;
        let places = this.defaultPlaces;
        try {
          const response = await fetch('/api/map');
          if (response.ok) {
            const data = await response.json();
            if (data.coordinates && data.places) {
              coordinates = data.coordinates;
              places = data.places;
            }
          }
        } catch (error) {
          console.error('Error fetching map data, using default values:', error);
        }
  
        this.map = L.map(this.$refs.map).setView([coordinates.lat, coordinates.lng], 6);
  
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(this.map);
  
        places.forEach(place => {
          const customIcon = L.icon({
            iconUrl: place.icon,
            iconSize: [32, 32], // Customize icon size
            iconAnchor: [16, 32], // Point of the icon which will correspond to marker's location
            popupAnchor: [0, -32] // Point from which the popup should open relative to the iconAnchor
          });
  
          const marker = L.marker([place.lat, place.lng], { icon: customIcon }).addTo(this.map);
          marker.bindPopup(place.name).openPopup();
        });
  
        // Event listener to fix the map issue when clicking
        this.map.on('click', () => {
          setTimeout(() => {
            this.map.invalidateSize();
          }, 0);
        });
  
        // Event listener to fix the map issue when zooming
        this.map.on('zoomend', () => {
          setTimeout(() => {
            this.map.invalidateSize();
          }, 0);
        });
      },
    },
  };
  </script>
  
  <style scoped>
  #map {
    width: 100%;
    height: 400px;
  }
  </style>
  