var n=Math.min(6,9,15,-2,92,11)
		alert("最小值 = "+n)
var n=Math.max(6,9,15,-2,92,11)
		alert("最大值 = "+n)
var arr=[6,9,15,-2,92,11]
		alert("元素数量 = "+arr.length)
var arr=[6,9,15,-2,92,11]
function avg(arry){
var sum=0
var len
for(var i=0,len=arry.length;i<len;i++){
sum+=arry[i]
}
var d=sum/len
d=d.toFixed(2)
alert("平均值 = "+d)
}
avg(arr)
		
