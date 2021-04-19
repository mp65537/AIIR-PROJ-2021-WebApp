        let hook1=document.querySelector(".check1");
        let hook2=document.querySelector(".check2");
        hook1.addEventListener("change",(e)=>{
            if(e.target.value!=""){
                hook2.disabled=true;
            }
            else{
                hook2.disabled=false;
            }
        });
        hook2.addEventListener("change",(e)=>{
            console.log(e.target.files);
            if(e.target.files.length>0){
                hook1.disabled=true;
            }
            else{
                hook1.disabled=false;
            }
        });