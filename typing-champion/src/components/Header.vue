<script setup>
</script>

<template>
    <div class="header">
        <nav>
            <ul>
                <li><router-link to="/">Home</router-link></li>
                <li><router-link to="/about">About</router-link></li>
                <li><router-link to="/contact">Contact</router-link></li>
            </ul>
        </nav>  
    </div>
    
</template>

<style scoped>
    nav {
        display: flex;
        margin: 0 auto;
        /* padding-right: 100px; */
        /* ^^^^^ This pushes the nav over to the center */
    }

    nav ul {
        display: flex;
        margin: 0 0 0 auto;
        /* list-style-type: none; */
        /* width: 100%; */
        /* padding: 0; */
    }

    nav li {
        display: flex;
        align-items: center;
        padding: 0 20px;
        height: 100%;
        transition: 0.75s;
    }



</style>