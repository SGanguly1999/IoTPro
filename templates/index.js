function start_acc() {
        console.log("Starting accelerometer execution");
       var ourRequest=new XMLHttpRequest();
ourRequest.open('GET','/start_acc',true);
ourRequest.send()
    }
    function stop_acc() {
        console.log("Stopping Accelerometer Execution");
       var ourRequest=new XMLHttpRequest();
ourRequest.open('GET','/stop_acc',true);
ourRequest.send()
    }