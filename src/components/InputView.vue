<template>
  <div>
    <h2>Entrée vocale</h2>
    <button @click="startRecording">Démarrer l'enregistrement</button>
    <button @click="stopRecording">Arrêter l'enregistrement</button>
    <p v-if="recording">Enregistrement en cours...</p>
    <ul>
      <li v-for="(word, index) in words" :key="index">{{ word }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      recognition: null,
      recording: false,
      words: [],
    };
  },
  mounted() {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
      alert('API Web Speech non supportée par ce navigateur.');
      return;
    }

    this.recognition = new SpeechRecognition();
    this.recognition.continuous = true;
    this.recognition.interimResults = false;
    this.recognition.lang = 'fr-FR';

    this.recognition.onstart = () => {
      this.recording = true;
    };

    this.recognition.onresult = (event) => {
      const transcript = Array.from(event.results)
        .map(result => result[0].transcript)
        .join('');
      this.words.push(transcript);
      this.sendWordsToAPI(transcript);
    };

    this.recognition.onerror = (event) => {
      console.error('Speech recognition error', event);
    };

    this.recognition.onend = () => {
      this.recording = false;
    };
  },
  methods: {
    startRecording() {
      if (this.recognition) {
        this.recognition.start();
      }
    },
    stopRecording() {
      if (this.recognition) {
        this.recognition.stop();
      }
    },
    async sendWordsToAPI(words) {
      try {
        const response = await fetch('/api/input', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ words }),
        });
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
      } catch (error) {
        console.error('Error sending words to API:', error);
      }
    },
  },
};
</script>

<style scoped>
button {
  margin-right: 10px;
  padding: 10px;
  font-size: 16px;
}

p {
  color: red;
  font-weight: bold;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  background: #f0f0f0;
  margin: 5px 0;
  padding: 10px;
  border-radius: 5px;
}
</style>
