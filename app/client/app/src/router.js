import Vue from 'vue'
import Router from 'vue-router'

import Navbar from './components/Navbar'
import SubNavbar from './components/SubNavbar'

import Chat from './views/Chat'
import Log from './views/Log'
import Status from './views/Device'
import Login from './views/Login'
import About from './views/About'

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
      path: '/device',
      components: {
        navbar: Navbar,
        subnavbar: SubNavbar,
        main: Status
      },
        children:[{
          path: 'chat',
          components: {
            navbar: Navbar,
            subnavbar: SubNavbar,
            main: Chat
            }
          }, {
          path: 'log',
          components: {
            navbar: Navbar,
            subnavbar: SubNavbar,
            main: Log
          }
        }]
    },
      {
      path: '/about',
      components: {
        navbar: Navbar,
        subnavbar: SubNavbar,
        main: About
      }
    }
  ]
})
