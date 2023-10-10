<template>
    <div>
        <h1>¡Bienvenido/a a la calculadora virtual!</h1>
        <p>Ingrese el primer número</p>
        <input v-model="num1"/>
        <p>Ingrese el segundo número</p>
        <input v-model="num2"/>
        <p>Seleccione la operación</p>
        <select v-model="operacion">
          <option value="suma">Suma</option>
          <option value="resta">Resta</option>
          <option value="multiplicacion">Multiplicación</option>
          <option value="división">División</option>
        </select>
        <button v-on:click="calcular()">Calcular</button>
        <div>
          <div v-if="!num1_valid" class="mensaje error">El valor 1 es inválido</div>
          <div v-else-if="!num2_valid" class="mensaje error">El valor 2 es inválido</div>
          <div v-else class="mensaje resultado">El resultado es: {{ resultado }}</div>
        </div>
    </div>
</template>

<style scoped>
.mensaje{
  text-align: center;
  border-radius: 10px;
  margin: 10px 0;
  padding: 10px;
}
.error{
  border: 1px solid red;
  background-color: lightcoral;
  color: red;
}
.resultado{
  border: 1px solid green;
  background-color: lightgreen;
  color: green;
}
</style>

<script>
export default {
  name: 'Calculadora',
  data: function () {
    return {
      num1: 0,
      num2: 0,
      resultado: undefined,
      num1_valid: false,
      num2_valid: false,
      operacion: ''
    }
  },
  methods: {
    calcular: function () {
      var num1Parsed = parseFloat(this.num1)
      var num2Parsed = parseFloat(this.num2)
      this.num1_valid = !isNaN(num1Parsed)
      this.num2_valid = !isNaN(num2Parsed)

      if (this.num1_valid && this.num2_valid) {
        if (this.operacion === 'suma') {
          this.resultado = num1Parsed + num2Parsed
        } else if (this.operacion === 'resta') {
          this.resultado = num1Parsed - num2Parsed
        } else if (this.operacion === 'multiplicacion') {
          this.resultado = num1Parsed * num2Parsed
        } else {
          this.resultado = num1Parsed / num2Parsed
        }
      }
    }
  }
}
</script>
