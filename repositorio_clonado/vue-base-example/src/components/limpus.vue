<template>
    <div>
        <label>Marca</label><input v-model="brand">
        <label>Modelo</label><input v-model="model">
        <label>Precio</label><input v-model="price">
        <label>Stock</label><input v-model="stock">
        <button @click="agregarItem()">Agregar</button>
        <table>
            <tr>
                <th>Id</th>
                <th>Marca</th>
                <th>Modelo</th>
                <th>Precio</th>
                <th>stock</th>
            </tr>
            <tr v-for="item in items" :key="item.id">
                <td>{{ item.id }}</td>
                <td>{{ item.brand }}</td>
                <td>{{ item.model }}</td>
                <td>{{ item.price }}</td>
                <td>{{ item.stock }}</td>
            </tr>
        </table>
    </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios'

export default {
    name: 'APITest',
    data: function(){
        return {
            items: [],
            brand: '',
            model: '',
            price: '',
            stock: '',

        }
    },
    methods: {
        cargarDatos (){
            axios.get('http://localhost:8000/products/')
            .then(response => {
                this.items = response.data
                console.log(response.data)
            })
            .catch(error => {
                console.log(error)
            })
        },
        agregarItem(){
            axios.post('http://localhost:8000/products/', {
                model: this.model,
                brand: this.brand,
                stock: this.stock,
                price: this.price
            })
            .then(response => {
                console.log(response)
                this.cargarDatos()
            })
            .catch(error => {
                console.log(error)
            })
        }
    },
    mounted() {
        this.cargarDatos()
    }
}
</script>