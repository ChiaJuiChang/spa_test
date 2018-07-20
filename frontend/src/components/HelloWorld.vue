<template>
  <div class="videos">
    <ul v-for="car in cars">
      <li>{{ car.name }}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HelloWorld',
  mounted() {
    this.getCar()
    // console.log('test')
  },
  data() {
    return {
      cars: []
    }
  },
  methods: {
    getCar() {
      axios.get('/api/car')
        .then(response => {
          const cars = response.data.fields
          this.cars = cars
          // this.cars = [
          //   { name: '3232' }, 
          //   { name: '2' },
          // ]
        }).catch(error => {
          console.error(error)
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
