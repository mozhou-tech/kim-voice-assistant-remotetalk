// Vue.js Filters
// https://vuejs.org/v2/guide/filters.html

import Vue from 'vue'
import moment from 'moment'

let filters = {

  formatNumber (value) {
  	let val = (value / 1);
	return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')
  },
  formatDate(value){
  	 return moment.unix(value/1000).format('YYYY-MM-DD hh:mm')
  },
  shortContent(value){
     if(value.length <= 16){
         return value
     }
  	 return value.substr(0,16)+'...'
  }
};

// Register Filters
Object.keys(filters).forEach(function (filterName) {
  Vue.filter(filterName, filters[filterName])
});