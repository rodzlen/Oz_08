
window.alert("asd")
window.console.log('첫 번쨰 경고창 실행');
window.alert('그만 하라고');
window.console.log('두 번쨰 경고창 실행');
window.alert('그만 하라고 했지');
window.console.log('세 번쨰 경고창 실행');
/*
명령문은 한 줄에 하나식
세미콜론의 의미'명령문 하나 끝남'
*/
const a = prompt('내용을 입력');
window.alert(a);
// for (let index = 0; index < 10; index++) {
//     alert(a+index);
// }
const b = window.confirm('실행 하시겠습니까?');
console.log(typeof b);
if (b==false) {
    alert(`${b} 를 선택하였습니다.`)
}else{
    alert(`${b}를 선택하였습니다.`)
}