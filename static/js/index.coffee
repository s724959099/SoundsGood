vm=new Vue(
    el:"#app"
    data:{
        mytext:"",
    }
    methods:{
        btn_click:->
            obj={
                mytext:@mytext
            }
            data=myAjax.postSync("/api/parsestr",obj)
            console.log(data)
    }
)