import { createRouter, createWebHistory } from "vue-router";

import Home from "@/views/Home.vue";
import LoginSignup from "@/views/LoginSignup.vue";
import Leaderboard from "@/views/Leaderboard.vue";
import PlayerStats from "@/views/PlayerStats.vue";
import Game from "@/views/Game.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes:[
        {
            path: '/',
            name: 'home',
            component: Home,
        },
        {
            path:'/login',
            name:'login-signup',
            component: LoginSignup
        },
        {
            path:'/leaderboard',
            name: 'leaderboard',
            component: Leaderboard,
        },
        {
            path:'/playerstats',
            name: 'playerstats',
            component: PlayerStats,
        },
        {
            path:'/game',
            name: 'game',
            component: Game,
        }
    ]
});

export default router;