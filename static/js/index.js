// Generated by CoffeeScript 1.10.0
(function() {
  var vm;

  vm = new Vue({
    el: "#app",
    data: {
      mytext: ""
    },
    methods: {
      btn_click: function() {
        var data, obj;
        obj = {
          mytext: this.mytext
        };
        data = myAjax.postSync("/api/parsestr", obj);
        return console.log(data);
      }
    }
  });

}).call(this);

//# sourceMappingURL=index.js.map