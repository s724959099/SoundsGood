vm = new Vue(
    el:"#app"
    data:{
        text:null
        type:null
        mytext:null
    }
    methods:{
        submit:->
            if @text!=null and @type!=null
                obj={
                    text:@text
                    type:@type
                }
                data=myAjax.getSync("/api/change/css",obj)
                @mytext=data.link
    }
)

$ ->
    new Clipboard('#copy')