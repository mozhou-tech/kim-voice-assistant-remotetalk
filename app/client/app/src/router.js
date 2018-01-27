import Vue from 'vue'
import Router from 'vue-router'

import Navbar from './components/Navbar'
import SubNavbar from './components/SubNavbar'

import Chat from './views/Chat'
import Log from './views/Log'
import Status from './views/Status'
import Login from './views/Login'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      components: {
        main: Login
      }
    },
    {
      path: '/status',
      components: {
        navbar: Navbar,
        subnavbar: SubNavbar,
        main: Status
      }
    }, {
      path: '/chat',
      components: {
        navbar: Navbar,
        subnavbar: SubNavbar,
        main: Chat
      }
    },{
      path: '/log',
      components: {
        navbar: Navbar,
        subnavbar: SubNavbar,
        main: Log
      }
    }
  ]
})
