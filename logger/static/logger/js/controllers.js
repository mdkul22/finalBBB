var intervalId = 0;
angular.module('mainApp.controllers',[])
.controller('bmsCtrl', function bmsCtrl($scope,bmsData){
	clearInterval(intervalId);
	var res=[];
	$scope.vh1 = "Battery Quadrant 1";
	$scope.vh2 = "Battery Quadrant 2";
	$scope.vh3 = "Battery Quadrant 3";
	$scope.vh4 = "Battery Quadrant 4";
	$scope.getdata = function(){
		bmsData.get({pk:1},function(data){
			res = dataHandle(data.btq1);
			$("#val1").html(res[res.length-2]);
			res = dataHandle(data.btq2);
			$("#val2").html(res[res.length-2]);
			res = dataHandle(data.btq3);
			$("#val3").html(res[res.length-2]);
			res = dataHandle(data.btq4);
			$("#val4").html(res[res.length-2]);
		});
	};
	intervalId=setInterval($scope.getdata,2000);
	var a=[-1,-1,-1,-1,-1,-1,-1,-1];
		$scope.plot = function(){ 
		bmsData.get({pk:1},function(data){
		var d=[[],[],[],[]];
		if(a[0]!=-1){
				var res = dataHandle(data.btq1);
				for(var i=0; i <100 ; i+=1){
					d[0].push([i,res[i]]);
				}
			}
		if(a[1]!=-1){
				res = dataHandle(data.btq2);
				for(var i=0; i <100 ; i+=1){
					d[1].push([i,res[i]]);
				}}
		if(a[2]!=-1){
				res = dataHandle(data.btq3);
				for(var i=0; i <100 ; i+=1){
					d[2].push([i,res[i]]);
				}}
		if(a[3]!=-1){
				res = dataHandle(data.btq4);
				for(var i=0; i <100 ; i+=1){
					d[3].push([i,res[i]]);
				}}
		$.plot("#platform",d);
	});
	};
	$scope.replot = function(sensid){
		a[sensid-1]*=-1;
		$scope.plot();
	};
})
.controller('mpptCtrl', function mpptCtrl($scope){
	clearInterval(intervalId);
})
.controller('motorCtrl', function motorCtrl($scope,motorData){
	clearInterval(intervalId);
	var res=[];
	$scope.vh1 = "Motor Temp Right";
	$scope.vh2 = "Motor Temp Left";
	$scope.getdata = function(){
		motorData.get({pk:1},function(data){
			res = dataHandle(data.mtr);
			$("#val1").html(res[res.length-2]);
			res = dataHandle(data.mtl);
			$("#val2").html(res[res.length-2]);
		});
	};
	intervalId=setInterval($scope.getdata,2000);
	var a=[-1,-1,-1,-1,-1,-1,-1,-1];
	$scope.plot = function(){ 
		motorData.get({pk:1},function(data){
		var d=[[],[]];
		if(a[0]!=-1){
				var res = dataHandle(data.mtr);
				for(var i=0; i <100 ; i+=1){
					d[0].push([i,res[i]]);
				}
			}
		if(a[1]!=-1){
				res = dataHandle(data.mtl);
				for(var i=0; i <100 ; i+=1){
					d[1].push([i,res[i]]);
				}}
		$.plot("#platform",d);
	});
	};
	$scope.replot = function(sensid){
		a[sensid-1]*=-1;
		$scope.plot();
	};
	
})
.controller('solpanCtrl', function solpanCtrl($scope,generalData){
	clearInterval(intervalId);
	var res=[];
	$scope.vh1 = "Speed Front Left";
	$scope.vh2 = "Speed Front Right";
	$scope.vh3 = "Speed Back Left";
	$scope.vh4 = "Speed Back Right";
	$scope.vh5 = "State of Charge";
	$scope.getdata = function(){
		generalData.get({pk:1},function(data){
			res = dataHandle(data.speedfl);
			$("#val1").html(res[res.length-2]);
			res = dataHandle(data.speedfr);
			$("#val2").html(res[res.length-2]);
			res = dataHandle(data.speedbl);
			$("#val3").html(res[res.length-2]);
			res = dataHandle(data.speedbr);
			$("#val4").html(res[res.length-2]);
			res = dataHandle(data.soc);
			$("#val5").html(res[res.length-2]);
		});
	};
	intervalId=setInterval($scope.getdata,2000);
	var a=[-1,-1,-1,-1,-1,-1,-1,-1];
	$scope.plot = function(){ 
		generalData.get({pk:1},function(data){
		var d=[[],[],[],[],[]];
		if(a[0]!=-1){
				var res = dataHandle(data.speedfl);
				for(var i=0; i <100 ; i+=1){
					d[0].push([i,res[i]]);
				}
			}
		if(a[1]!=-1){
				res = dataHandle(data.speedfr);
				for(var i=0; i <100 ; i+=1){
					d[1].push([i,res[i]]);
				}
			}
		if(a[2]!=-1){
				res = dataHandle(data.speedbl);
				for(var i=0; i <100 ; i+=1){
					d[1].push([i,res[i]]);
				}
			}
		if(a[3]!=-1){
				res = dataHandle(data.speedbr);
				for(var i=0; i <100 ; i+=1){
					d[1].push([i,res[i]]);
				}
			}
		if(a[4]!=-1){
				res = dataHandle(data.soc);
				for(var i=0; i <100 ; i+=1){
					d[1].push([i,res[i]]);
				}
			}
		$.plot("#platform",d);
	});
	};
	$scope.replot = function(sensid){
		a[sensid-1]*=-1;
		$scope.plot();
	};
})
.controller('mcCtrl', function mcCtrl($scope, mcData){
	clearInterval(intervalId);
	var res=[];
	$scope.vh1 = "Motor Controller Temp";
	$scope.vh2 = "MC to Motor Left Current";
	$scope.vh3 = "MC to Motor Right Current";
	$scope.vh4 = "MC to Battery Current";
	$scope.vh5 = "Max Discharge Current";
	$scope.vh6 = "Min Discharge Current";
	$scope.vh7 = "Max Current";	
	$scope.getdata = function(){
		mcData.get({pk:1},function(data){
			res = dataHandle(data.mct);
			$("#val1").html(res[res.length-2]);
			res = dataHandle(data.mc2mlc);
			$("#val2").html(res[res.length-2]);
			res = dataHandle(data.mc2mrc);
			$("#val3").html(res[res.length-2]);
			res = dataHandle(data.mc2bc);
			$("#val4").html(res[res.length-2]);
			res = dataHandle(data.maxdiscC);
			$("#val5").html(res[res.length-2]);
			res = dataHandle(data.mindiscC);
			$("#val6").html(res[res.length-2]);
			res = dataHandle(data.maxc);
			$("#val7").html(res[res.length-2]);
		});
	};
	intervalId=setInterval($scope.getdata,2000);
	var a=[-1,-1,-1,-1,-1,-1,-1,-1];
	$scope.plot = function(){ 
		mcData.get({pk:1},function(data){
		var d=[[],[],[],[],[],[],[]];
		if(a[0]!=-1){
				var res = dataHandle(data.mct);
				for(var i=0; i <100 ; i+=1){
					d[0].push([i,res[i]]);
				}
			}
		if(a[1]!=-1){
				res = dataHandle(data.mc2mlc);
				for(var i=0; i <100 ; i+=1){
					d[1].push([i,res[i]]);
				}
			}
		if(a[2]!=-1){
				res = dataHandle(data.mc2mrc);
				for(var i=0; i <100 ; i+=1){
					d[1].push([i,res[i]]);
				}
			}
		if(a[3]!=-1){
				res = dataHandle(data.mc2bc);
				for(var i=0; i <100 ; i+=1){
					d[1].push([i,res[i]]);
				}
			}
		if(a[4]!=-1){
				res = dataHandle(data.maxdiscC);
				for(var i=0; i <100 ; i+=1){
					d[1].push([i,res[i]]);
				}
			}
		if(a[5]!=-1){
				res = dataHandle(data.mindiscC);
				for(var i=0; i <100 ; i+=1){
					d[1].push([i,res[i]]);
				}
			}
		if(a[6]!=-1){
				res = dataHandle(data.maxc);
				for(var i=0; i <100 ; i+=1){
					d[1].push([i,res[i]]);
				}
			}
		$.plot("#platform",d);
	});
	};
	$scope.replot = function(sensid){
		a[sensid-1]*=-1;
		$scope.plot();
	};
});
function dataHandle(data){
	var res = data.split(",");
   	res[0] = 0;
   	res[res.length-1] = 0;
	return res;
}