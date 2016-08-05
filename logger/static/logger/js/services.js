angular.module('logger.services', ['ngResource'])
  .factory('bmsData', function($resource) {
    return $resource('/api/bmsdata/:pk'); 
  })
  .factory('mcData', function($resource) {
    return $resource('/api/mcdata/:pk'); 
  })
  .factory('generalData', function($resource) {
    return $resource('/api/generaldata/:pk'); 
  })
  .factory('motorData', function($resource) {
    return $resource('/api/motordata/:pk'); 
  })