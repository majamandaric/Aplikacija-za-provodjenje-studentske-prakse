import Vue from 'vue'
import Router from 'vue-router'
import PrijavaStudent from '@/views/pages/PrijavaStudent'
import PrijavaPoslodavac from '@/views/pages/PrijavaPoslodavac'
import PrijavaProfesor from '@/views/pages/PrijavaProfesor'
import RegistracijaStudent from '@/views/pages/RegistracijaStudent'
import RegistracijaPoslodavac from '@/views/pages/RegistracijaPoslodavac'


Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            name: 'PrijavaStudent',
            path: '/',
            component: PrijavaStudent,
        },

        {
            name: 'PrijavaPoslodavac',
            path: '/loginemployer',
            component: PrijavaPoslodavac,
        },

        {
            name: 'RegistracijaStudent',
            path: '/registerstudent',
            component: RegistracijaStudent,
        },

        {
            name: 'RegistracijaPoslodavac',
            path: '/registeremployer',
            component: RegistracijaPoslodavac,
        },

        {
            name: 'PrijavaProfesor',
            path: '/loginprofesor',
            component: PrijavaProfesor,
        },

        
        
        {
            path: '',
            component: () => import('@/layouts/LayoutPoslodavac'),
            children: [
                // Components
                {
                    name: 'Arhiva',
                    path: '/arhiva',
                    component: () => import('@/views/pages/Arhiva'),
                    
                },

                {
                    name: 'Profile',
                    path: '/profil',
                    component: () => import('@/views/pages/ProfilPoslodavac'),
                },

                {
                    name: 'Dashboard',
                    path: '/naslovnica-poslodavac',
                    component: () => import('@/views/dashboard/NaslovnicaPoslodavac'),
                },

            ]
            
        },

        {
            path: '',
            component: () => import('@/layouts/LayoutStudent'),
            children: [
                // Components
                {
                    name: 'MojOdabir',
                    path: '/moj-odabir',
                    component: () => import('@/views/pages/MojOdabir'),
                    
                },

                {
                    name: 'Profile',
                    path: '/profil-student',
                    component: () => import('@/views/pages/ProfilStudent'),
                },

                {
                    name: 'Dashboard2',
                    path: '/naslovnica-student',
                    component: () => import('@/views/dashboard/NaslovnicaStudent'),
                },

            ]
            
        },

        {
            path: '',
            component: () => import('@/layouts/LayoutProfesor'),
            children: [
                // Components


                {
                    name: 'Dashboard3',
                    path: 'naslovnica-profesor',
                    component: () => import('@/views/dashboard/NaslovnicaProfesor'),
                },

            ]
            
        },

    ],
})