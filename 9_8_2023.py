/* 
Braces Valid

Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

const str1 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const expected1 = true;

const str2 = "D(i{a}l[ t]o)n{e";
const expected2 = false;

const str3 = "A(1)s[O (n]0{t) 0}k";
const expected3 = false;

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */
function bracesValid(str) {}

/*****************************************************************************/



function bracesValid(str) {
    var stackP = []; //parenth
    var stackC = []; //brackets
    var stackD = []; //curlies
    for(var i = 0; i < str.length; i++){
        if(str[i] == '('){
            stackP.push(str[i]);
        }
        if(str[i] == '['){
            stackC.push(str[i]);
        }
        if(str[i] == '{'){
            stackD.push(str[i]);
        }
        if(str[i] == ')' && stackP.length > 0){
            stackP.pop()
        }
        else if(str[i] == ')' && stackP.length == 0){
            return false;
        }
        if(str[i] == ']' && stackC.length > 0){
            stackC.pop()
        }
        else if(str[i] == ']' && stackC.length == 0){
            return false;
        }
        if(str[i] == '}' && stackD.length > 0){
            stackD.pop()
        }
        else if(str[i] == '}' && stackD.length == 0){
            return false;
        }
    }
    if(stackP.length > 0 || stackC.length > 0 || stackD.length > 0){
        return false;
    }else{
        return true;
    }
}

    console.log(bracesValid(str5))
function parensValid(str) {
    var stack = [];
    for(var i = 0; i < str.length; i++){
        if(str[i] == '('){
            stack.push(str[i]);
        }
        if(str[i] == ')' && stack.length > 0){
            stack.pop()
        }
        else if(str[i] == ')' && stack.length == 0){
            return false;
        }
    }
    if(stack.length > 0){
        return false;
    }else{
        return true;
    }
}

    console.log(parensValid(str3))