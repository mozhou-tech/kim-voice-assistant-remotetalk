import Vue from 'vue'
import Router from 'vue-router'

import Navbar from './components/Navbar'
import SubNavbar from './components/SubNavbar'

import DeviceChat from './views/DeviceChat'
import DeviceLog from './views/DeviceLog'
import DeviceList from './views/DeviceList'
import Device from './views/Device'
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
        redirect:'/device/list',
        components: {
          navbar: Navbar,
          subnavbar: SubNavbar,
          main: Device
        },
        children:[{
          path: 'list',
          component: DeviceList
          }, {
          path: 'chat',
          component: DeviceChat
          }, {
          path: 'log',
          component: DeviceLog
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
